# FMC Media — Updates

Public installers for Windows and Android. Source repositories and personal backups remain private. Corresponding Online Sources component source archives and notices are attached to their releases and bundled with the apps.

| Platform | Channel | Downloads |
| --- | --- | --- |
| Windows 10/11 x64 | [channels/windows.json](channels/windows.json) | [PC 0.3.29](https://github.com/TheFmC/U-Mdia/releases/tag/pc-v0.3.29) · EXE installer |
| Android phones | [channels/android-mobile.json](channels/android-mobile.json) | [Mobile 1.0.31](https://github.com/TheFmC/U-Mdia/releases/tag/v1.0.31) · signed APK |
| Android TV | [channels/android-tv.json](channels/android-tv.json) | Legacy TV channel metadata; the current shared Android app also retains its supported TV interface |

## Latest changes

**PC 0.3.29:** Online Sources with 40 provider definitions, per-work playback checks, actual quality selection including 4K/1080p/720p when supplied, and audio-preserving HLS/DASH selection. See the [full release notes](https://github.com/TheFmC/U-Mdia/releases/tag/pc-v0.3.29).

**Mobile 1.0.31:** on-device Online Sources, quality selection, multiple-episode downloads with subtitles, full-season pack search and the check/download action, and poster → season → episode download browsing. See the [full release notes](https://github.com/TheFmC/U-Mdia/releases/tag/v1.0.31).

Windows: Settings → About → **Check for updates**. Downloads are verified by SHA-256 and size before opening the installer.

Current Android versions check GitHub's [latest release](https://github.com/TheFmC/U-Mdia/releases/latest). The Android APK release stays marked latest; Windows releases use `--latest=false`. The mobile channel metadata is published separately for clients that consume it. The Android APK supports Android 8.0+ on arm64-v8a, armeabi-v7a and x86_64 and preserves the same Android signing identity.

## Publishing

Publish and verify release assets before updating channel JSON on main. Windows uses pc-vX.Y.Z tags; Android uses vX.Y.Z. Channel metadata includes the exact asset URL, byte size and SHA-256. Keep earlier releases available for recovery. Never offer an EXE to Android or an APK to Windows.

Do not upload personal state, provider credentials, signing keys or service environment files here. Source availability and quality vary by title, episode and provider; green checks report a bounded playback test, not a guarantee of future availability.
