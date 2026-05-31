[app]

title = 服装厂管理
package.name = clothingfactory
package.domain = org.example

version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

orientation = portrait

fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

requirements = python3,kivy==2.2.1

android.ndk = 25b
android.api = 33
android.buildtools = 33.0.0

log_level = 2

warn_on_root = 1

[buildozer]

build_dir = ./build
bin_dir = ./bin
