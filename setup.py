import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os", "vlc", "pygame"], "include_files": "LAX.png"}
build_mac_options = {"include_resources": "LAX.png", "iconfile": "flyLAX.ico"}
# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "lax",
    version = "0.1",
    description = "ATC LAX",
    options = {"build_exe": build_exe_options, "bdist_mac": build_mac_options},
    executables = [Executable("lax.py", base=base, icon="flyLAX.ico")]
)