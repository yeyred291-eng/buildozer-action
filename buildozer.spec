[app]
title = MyRemind
package.name = myremind
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.12,kivy==2.3.0,kivymd==1.1.1,plyer

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 24
android.ndk_api = 24

[buildozer]
log_level = 2
warn_on_root = 0
