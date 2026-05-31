[app]

title = 服装厂管理
package.name = clothingfactory
package.domain = org.example

version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

orientation = portrait

fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE

requirements = python3,kivy

android.ndk = 25b

log_level = 2

warn_on_root = 1

[buildozer]

build_dir = ./build
bin_dir = ./bin
