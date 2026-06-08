[app]
title = MyRemind
package.name = myremind
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Wir nehmen eine stabile Kivy-Kombination ohne feste Python-Sperre
requirements = python3,kivy==2.3.0,kivymd==1.1.1,plyer,materialyoucolor

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Hier zwingen wir Buildozer auf stabilere Versionen für GitHub-Server:
android.api = 33
android.ndk = 25b
android.sdk_build_tools_version = 33.0.0
android.minapi = 24
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
