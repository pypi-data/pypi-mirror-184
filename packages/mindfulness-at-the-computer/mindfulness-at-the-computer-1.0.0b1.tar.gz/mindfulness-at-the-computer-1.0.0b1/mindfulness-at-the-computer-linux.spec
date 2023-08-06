# -*- mode: python -*-

block_cipher = None

import os
# import matc.constants

cwd_str = os.getcwd()

a = Analysis(
    ['matc/__main__.py'],
    pathex=[cwd_str],
    binaries=[],
    datas=[('README.md', '.'), ('LICENSE.txt', '.'), ('matc/matc.qss', './matc'), ('matc/version.txt', './matc')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher
)

# Adding the res directory
# Please note that adding individual files this is done above - inside "Analysis" -> "datas"
res_dir_str = "matc/res"
a.datas += Tree('./' + res_dir_str, prefix=res_dir_str)
# -documentation: https://pythonhosted.org/PyInstaller/advanced-topics.html#the-tree-class

# Removing unneeded files
# https://stackoverflow.com/questions/57466637/how-to-exclude-unnecessary-qt-so-files-when-packaging-an-application
# Without removing files we have 412 files
a.binaries = a.binaries - TOC([
  ('libgio-2.0.so.0', None, None),
  ('libgtk-3.so.0', None, None),
  ('libQt53DAnimation.so.5', None, None), ('libQt63DAnimation.so.6', None, None),
  ('libQt53DCore.so.5', None, None), ('libQt63DCore.so.6', None, None),
  ('libQt5Quick.so.5', None, None), ('libQt6Quick.so.6', None, None)
])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="mindfulness-at-the-computer",
    debug=False,
    strip=False,
    upx=True,
    console=True
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
