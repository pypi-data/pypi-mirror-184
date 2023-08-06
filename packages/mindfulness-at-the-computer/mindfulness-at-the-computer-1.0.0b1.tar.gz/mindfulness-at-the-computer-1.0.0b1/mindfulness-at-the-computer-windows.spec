# -*- mode: python -*-

block_cipher = None

####################################
# PLEASE NOTE: The path for the Qt binaries have been hard-coded
####################################

import os
# import matc.constants  # -is this risky? could be a relative path or it could look among the packages
cwd_str = os.getcwd()
# 'C:\\TordPython\\mindfulness-at-the-computer-master'

a = Analysis(
    ['matc/__main__.py'],
    pathex=[cwd_str],
    binaries=[],
    datas=[('.\\README.md', '.'), ('.\\LICENSE.txt', '.'), ('.\\matc\\matc.qss', '.\\matc'), ('matc/version.txt', './matc')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

# Adding the res and icons directories
# Please note that when adding individual files this is done above - inside "Analysis"
res_dir_str = "matc\\res"
a.datas += Tree(res_dir_str, prefix=res_dir_str)
# -documentation: https://pythonhosted.org/PyInstaller/advanced-topics.html#the-tree-class

# win_icon_path_str = '.\\' + icons_dir_str + '\\icon.ico'
# under "exe =": icon=win_icon_path_str,

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="mindfulness-at-the-computer",
    debug=False,
    strip=False,
    upx=True,
    console=False
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="mindfulness-at-the-computer"
)
