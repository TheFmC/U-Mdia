"""Publish the highest stable Windows release into its channel after asset upload."""
import base64
import json
import os
import re
import subprocess
import sys
import tempfile

repo = os.environ.get('GH_REPO', 'TheFmC/U-Mdia')
if repo != 'TheFmC/U-Mdia': raise RuntimeError('Unexpected update repository')
def api(path, *args):
    return json.loads(subprocess.check_output(['gh', 'api', path, *args], text=True, stderr=subprocess.PIPE))

pages = api(f'repos/{repo}/releases', '--paginate', '--slurp')
choices = []
for release in (item for page in pages for item in page):
    match = re.fullmatch(r'pc-v(\d+)\.(\d+)\.(\d+)', release['tag_name'])
    if match and not release['draft'] and not release['prerelease']:
        choices.append((tuple(map(int, match.groups())), release))
if not choices: raise RuntimeError('No published stable Windows release')
release = max(choices, key=lambda row: row[0])[1]
version = release['tag_name'][4:]
name = f'FMC-Media-PC-{version}-setup.exe'
asset = next((a for a in release['assets'] if a['name'] == name and a['state'] == 'uploaded'), None)
if not asset: raise RuntimeError('Windows installer asset is missing')
digest = asset.get('digest') or ''
if not re.fullmatch(r'sha256:[0-9a-fA-F]{64}', digest): raise RuntimeError('GitHub asset checksum is not available')
expected = f'https://github.com/{repo}/releases/download/{release["tag_name"]}/{name}'
if asset['browser_download_url'] != expected or not 0 < asset['size'] <= 1024**3:
    raise RuntimeError('Unexpected Windows installer URL or size')
manifest = {'platform': 'windows-x86_64', 'version': version, 'tag': release['tag_name'],
            'url': expected, 'sha256': digest[7:].lower(), 'size': asset['size'],
            'notes': (release.get('body') or '').strip()[:16000]}
content = (json.dumps(manifest, ensure_ascii=False, indent=2)+'\n').encode()
if '--dry-run' in sys.argv:
    print(content.decode())
else:
    path = f'repos/{repo}/contents/channels/windows.json'
    try:
        old = api(path)
    except subprocess.CalledProcessError as error:
        if 'HTTP 404' not in (error.stderr or ''): raise
        old = None
    if old and base64.b64decode(old['content']) == content:
        print('Windows channel already matches the latest release')
        sys.exit(0)
    payload = {'message': f'Publish Windows {version} update channel', 'branch': 'main',
               'content': base64.b64encode(content).decode()}
    if old: payload['sha'] = old['sha']
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as file:
        json.dump(payload, file)
        filename = file.name
    try:
        api(path, '--method', 'PUT', '--input', filename)
        print(f'Windows channel published: {version}')
    finally:
        os.unlink(filename)
