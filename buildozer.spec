[app]
title = Orman Barkod Kayıt
package.name = ormanbarkod
package.domain = org.poyraz
source.dir = .
source.include_exts = py,kv,png,jpg,atlas,json
version = 1.0.0
requirements = python3,kivy,openpyxl
orientation = portrait
fullscreen = 0
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
