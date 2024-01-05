# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/victo/Documents/projetos/Automação Whatssap/app.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/victo/Documents/projetos/Automação Whatssap/assets', 'assets/'), ('C:/Users/victo/Documents/projetos/Automação Whatssap/utils', 'utils/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\victo\\Downloads\\sparta.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
