# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['spider.py', 'GUI.py', 'random_search.py', '/Users/lynch0114/Documents/Code/python/FanhaoSearcher'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('kato_megumi.gif', '/Users/lynch0114/Documents/Code/python/FanhaoSearcher/kato_megumi.gif', 'Data')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='番号搜索器',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , 
          manifest='akespec',
          icon='/Users/lynch0114/Documents/Code/python/FanhaoSearcher/kato_megumi.gif')
