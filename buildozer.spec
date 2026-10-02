[app]

title = Maze
package.name = maze
package.domain = org.maze

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
source.exclude_dirs = bin,.buildozer,__pycache__

version = 1.0.0

requirements = python3,kivy,pillow

orientation = portrait
fullscreen = 1

android.permissions = 

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

android.logcat_filters = *:S python:D

[buildozer]

log_level = 2
warn_on_root = 1
