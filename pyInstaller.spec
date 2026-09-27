# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all

# ==================================初始设置===================================

version = "1.3.5"

# 运行文件
file_main = ["./client/src/main.py"]
file_updater = ["./client/src/updater.py"]
file_server = ["./server/app/main.py"]

# 程序名字
exeName_main = 'main'
exeName_updater = 'updater'
exeName_server = 'server'

# 给 exe 加图标，如果有图标文件的话
icon_main = ["./client/src/assets/images/Logo.ico"]
icon_updater = []
icon_server = []

# 要额外复制的文件夹与对应放置路径
folders2dst = {
    "./client/src/assets/docs": "./assets/docs",
    "./client/src/assets/images/others": "./assets/images/others",
    "./server/app/modules": "./modules",
}

# 要额外复制的文件
files2dst = {
    "./client/src/assets/images/Logo.ico": "./assets/images/",
    "./server/manifest.json": "./",
    "./requirements.txt": "./",
}

# 要额外复制的模块
hiddenimports = []

# 要额外复制的dll
modules = []

# internal目录名（相对路径），使用'.'会令exe生成在internal目录内
internalDir_main = version
internalDir_updater = '.'
internalDir_server = '.'

# 输出路径（dist文件夹内）
outputDir_main = './把%s移进来覆盖'%version
outputDir_updater = './%s'%version
outputDir_server = './%s（删除括号）'%version

# ============================添加要额外复制的内容===============================

# 空列表，用于准备要复制的数据
datas = []

# 文件夹
for src, dst in folders2dst.items():
    datas.append((src, dst))

# 文件
for src, dst in files2dst.items():
    datas.append((src, dst))

# dll
binaries = []
for module in modules:
    tmp_ret = collect_all(module)
    binaries += tmp_ret[1]

# ==========================新建 Analysis 变量============================

a = Analysis(
    file_main,
    pathex=[],
    binaries=binaries,
    datas=datas,                 # 额外文件
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['IPython'],        # 排除不需要的包
    noarchive=False,
)

b = Analysis(
    file_updater,
    pathex=[],
    binaries=binaries,
    datas=[],				     # 留空,由第一个处理就行
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['IPython'],        # 排除不需要的包
    noarchive=False,
)

c = Analysis(
    file_server,
    pathex=[],
    binaries=binaries,
    datas=[],				     # 留空,由第一个处理就行
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['IPython'],        # 排除不需要的包
    noarchive=False,
)

#============================重定向 py 文件===============================

# 可选地保留 a 要打包的依赖
private_module = []
pure = a.pure.copy(); a.pure.clear()
for name, src, type in pure:
    condition = [name == m or name.startswith(m + '.') for m in private_module]
    if condition and any(condition):
        ...
    else:
        a.pure.append((name, src, type))    # 把需要保留打包的 py 文件重新添加回 pure

# 可选地保留 b 要打包的依赖
private_module = []
pure = b.pure.copy(); b.pure.clear()
for name, src, type in pure:
    condition = [name == m or name.startswith(m + '.') for m in private_module]
    if condition and any(condition):
        ...
    else:
        b.pure.append((name, src, type))    # 把需要保留打包的 py 文件重新添加回 pure

# 可选地保留 c 要打包的依赖
private_module = []
pure = c.pure.copy(); c.pure.clear()
for name, src, type in pure:
    condition = [name == m or name.startswith(m + '.') for m in private_module]
    if condition and any(condition):
        ...
    else:
        c.pure.append((name, src, type))    # 把需要保留打包的 py 文件重新添加回 pure

# ==============================生成 exe===============================

pyzA = PYZ(a.pure)
pyzB = PYZ(b.pure)
pyzC = PYZ(c.pure)

exeA = EXE(
    pyzA,
    a.scripts,
    [],
    exclude_binaries=True,
    name=exeName_main,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                         # 运行时弹出终端窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_main,
    contents_directory=internalDir_main,
)

exeB = EXE(
    pyzB,
    b.scripts,
    [],
    exclude_binaries=True,
    name=exeName_updater,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                         # 运行时弹出终端窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_updater,
    contents_directory=internalDir_updater,
)

exeC = EXE(
    pyzC,
    c.scripts,
    [],
    exclude_binaries=True,
    name=exeName_server,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                         # 运行时弹出终端窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_server,
    contents_directory=internalDir_server,
)

# =============用 coll 把 exe 和其所属的文件收集到目标文件夹======================

collA = COLLECT(
    exeA,                           # .exe
    a.binaries,                     # 二进制文件（实际上已被清空了）
    a.datas,                        # 依赖文件和自定义复制文件

    strip=False,
    upx=True,
    upx_exclude=[],
    name=outputDir_main,
)

collB = COLLECT(
    exeB,                           # .exe
    b.binaries,                     # 二进制文件（实际上已被清空了）
    b.datas,                        # 依赖文件

    strip=False,
    upx=True,
    upx_exclude=[],
    name=outputDir_updater,
)

collC = COLLECT(
    exeC,                           # .exe
    c.binaries,                     # 二进制文件（实际上已被清空了）
    c.datas,                        # 依赖文件

    strip=False,
    upx=True,
    upx_exclude=[],
    name=outputDir_server,
)