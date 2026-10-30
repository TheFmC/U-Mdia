# FMC Media — Updates

Public installers for Windows and Android TV. Source code and personal backups stay in the owner's private repositories.

| Platform | Channel | Downloads |
| --- | --- | --- |
| Windows 10/11 x64 | [channels/windows.json](channels/windows.json) | Tags pc-vX.Y.Z; EXE installers |
| Android TV | [channels/android-tv.json](channels/android-tv.json) | Tags vX.Y.Z; signed APKs |
| Mobile | Planned | A separate channel will be added when the app is available |

Windows: Settings → About → **Check for updates**. Startup also offers newer Windows versions. Download & install verifies SHA-256 and size before opening the installer; the user completes installation.

Existing TV versions use GitHub's [latest release](https://github.com/TheFmC/U-Mdia/releases/latest). Keep Android TV marked latest and publish Windows releases with `--latest=false` until TV migrates to its own channel. Never offer EXE to TV or APK to Windows.

## Publishing

Publish the release asset first, then update its channel JSON on main. Windows requires platform, a numeric three-part version, pc-v tag, exact asset URL, size, sha256 and plain-text notes. Preserve earlier releases for recovery. Future mobile must have a separate channel and matching artifact.

Do not upload personal state, provider credentials, signing keys or service environment files here.
