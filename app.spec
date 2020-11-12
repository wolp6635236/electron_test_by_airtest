# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import sys
from os import path
site_packages = next(p for p in sys.path if 'site-packages' in p)
block_cipher = None

a = Analysis(['app.py'],
             pathex=['E:\\IdeaWorkSpace\\electron_test'],
             binaries=[('lib/chromedriver.exe', 'lib/'), ('airtest_script', 'airtest_script/'), ('lib/adb.exe', 'lib/'), ('lib/airtest.exe', 'lib/')],
             datas=[(path.join(site_packages,"airtest"),
                    "airtest")],
             hiddenimports=['airtest'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='快采伴侣',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
