import os
import re
import sys
import platform
import shutil
import pynvml
#import pkg_resources
import PyEasyUtils as EasyUtils
from packaging import version
from pathlib import Path
from threading import Event
from typing import Optional
from PySide6.QtCore import QObject, Signal, Slot

##############################################################################################################################

# Where to store custom signals
class CustomSignals_EnvConfigurator(QObject):
    '''
    Set up signals for configurator functions
    '''
    Signal_Aria2Status = Signal(str)
    Signal_Aria2Detected = Signal()
    Signal_Aria2Undetected = Signal()
    Signal_Aria2Installed = Signal()
    Signal_Aria2InstallFailed = Signal(Exception)

    Signal_FFmpegStatus = Signal(str)
    Signal_FFmpegDetected = Signal()
    Signal_FFmpegUndetected = Signal()
    Signal_FFmpegInstalled = Signal()
    Signal_FFmpegInstallFailed = Signal(Exception)
    '''
    Signal_GCCStatus = Signal(str)
    Signal_GCCDetected = Signal()
    Signal_GCCUndetected = Signal()
    Signal_GCCInstalled = Signal()
    Signal_GCCInstallFailed = Signal(Exception)

    Signal_CMakeStatus = Signal(str)
    Signal_CMakeDetected = Signal()
    Signal_CMakeUndetected = Signal()
    Signal_CMakeInstalled = Signal()
    Signal_CMakeInstallFailed = Signal(Exception)
    '''
    Signal_PythonStatus = Signal(str)
    Signal_PythonDetected = Signal()
    Signal_PythonUndetected = Signal()
    Signal_PythonInstalled = Signal()
    Signal_PythonInstallFailed = Signal(Exception)

    Signal_PyReqsStatus = Signal(str)
    Signal_PyReqsDetected = Signal()
    Signal_PyReqsUndetected = Signal()
    Signal_PyReqsInstalled = Signal()
    Signal_PyReqsInstallFailed = Signal(Exception)

    Signal_PytorchStatus = Signal(str)
    Signal_PytorchDetected = Signal()
    Signal_PytorchUndetected = Signal()
    Signal_PytorchInstalled = Signal()
    Signal_PytorchInstallFailed = Signal(Exception)


EnvConfiguratorSignals = CustomSignals_EnvConfigurator()


class Aria2_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def Check_Aria2(self):
        try:
            Aria2Version = str(EasyUtils.runCMD([['aria2c', '-v']], decodeResult = True)[0])
            return Aria2Version
        except OSError:
            return False

    def Install_Aria2(self):
        if platform.system() == 'Windows':
            URL = "https://github.com/aria2/aria2/releases/download/release-1.37.0/aria2-1.37.0-win-64bit-build1.zip"
            Dir_Download = './'
            File_Name = 'Aria2'
            File_Format = 'zip'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            Dir_Install = Path(f"{os.getenv('SystemDrive')}/Aria2").__str__()
            if self.stopEvent.isSet():
                return
            EasyUtils.downloadFile(URL, Dir_Download, File_Name, File_Format, None)
            if self.stopEvent.isSet():
                return
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            if self.stopEvent.isSet():
                return
            EasyUtils.moveFiles(os.path.dirname(EasyUtils.getPaths(Dir_Install, 'aria2c.exe')[0]), Dir_Install)
            if self.stopEvent.isSet():
                return
            EasyUtils.setEnvVar('PATH', Dir_Install, 'User')
            if self.stopEvent.isSet():
                return
            os.remove(Path_Download)

        if platform.system() == 'Linux':
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(['sudo apt-get update', 'sudo apt-get install aria2'])

    def Execute_Aria2_Installation(self):
        Result = self.Check_Aria2()
        if Result == False:
            EnvConfiguratorSignals.Signal_Aria2Undetected.emit()
            EnvConfiguratorSignals.Signal_Aria2Status.emit("Installing Aria2. Please wait...")
            try:
                self.Install_Aria2()
                EnvConfiguratorSignals.Signal_Aria2Installed.emit()
                EnvConfiguratorSignals.Signal_Aria2Status.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_Aria2InstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_Aria2Status.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_Aria2Detected.emit()
            EnvConfiguratorSignals.Signal_Aria2Status.emit(f"Aria2 detected. Version: {Result}")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_Aria2_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()

class FFmpeg_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def Check_FFmpeg(self):
        try:
            FFmpegVersion = str(EasyUtils.runCMD([['ffmpeg', '-version']], decodeResult = True)[0])
            return FFmpegVersion
        except OSError:
            return False

    def Install_FFmpeg(self):
        if platform.system() == 'Windows':
            URL = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip"
            Dir_Download = './'
            File_Name = 'FFmpeg'
            File_Format = 'zip'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            Dir_Install = Path(f"{os.getenv('SystemDrive')}/FFmpeg").__str__()
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            if self.stopEvent.isSet():
                return
            EasyUtils.downloadFile(URL, Dir_Download, File_Name, File_Format, None)
            if self.stopEvent.isSet():
                return
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            if self.stopEvent.isSet():
                return
            EasyUtils.moveFiles(os.path.dirname(EasyUtils.getPaths(Dir_Install, 'bin')[0]), Dir_Install)
            if self.stopEvent.isSet():
                return
            EasyUtils.setEnvVar('PATH', Path_Binary, 'User')
            if self.stopEvent.isSet():
                return
            os.remove(Path_Download)

        if platform.system() == 'Linux':
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(['sudo apt-get update', 'sudo apt-get install ffmpeg'])

    def Execute_FFmpeg_Installation(self):
        Result = self.Check_FFmpeg()
        if Result == False:
            EnvConfiguratorSignals.Signal_FFmpegUndetected.emit()
            EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Installing FFmpeg. Please wait...")
            try:
                self.Install_FFmpeg()
                EnvConfiguratorSignals.Signal_FFmpegInstalled.emit()
                EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_FFmpegInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
            EnvConfiguratorSignals.Signal_FFmpegStatus.emit(f"FFmpeg detected. Version: {Result}")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_FFmpeg_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()

"""
class GCC_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()
        
    def Check_GCC(self):
        try:
            GCCVersion = str(EasyUtils.runCMD([['gcc', '--version']], decodeResult = True)[0])
            return GCCVersion
        except OSError:
            return False

    def Install_GCC(self):
        if platform.system() == 'Windows':
            URL = "https://github.com/Spr-Aachen/EVT-Resources/raw/main/Environment%20Dependency/GCC/MinGW.zip"
            Dir_Download = './'
            File_Name = 'MinGW'
            File_Format = 'zip'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            Dir_Install = Path(f"{os.getenv('SystemDrive')}/MinGW").__str__()
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            if self.stopEvent.isSet():
                return
            EasyUtils.downloadFile(URL, Dir_Download, File_Name, File_Format, None)
            if self.stopEvent.isSet():
                return
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            if self.stopEvent.isSet():
                return
            EasyUtils.moveFiles(os.path.dirname(EasyUtils.getPaths(Dir_Install, 'bin')[0]), Dir_Install)
            if self.stopEvent.isSet():
                return
            EasyUtils.setEnvVar('PATH', Path_Binary, 'User')
            if self.stopEvent.isSet():
                return
            os.remove(Path_Download)

        if platform.system() == 'Linux':
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(['sudo apt-get update', 'sudo apt-get install build-essential'])

    def Execute_GCC_Installation(self):
        Result = self.Check_GCC()
        if Result == False:
            EnvConfiguratorSignals.Signal_GCCUndetected.emit()
            EnvConfiguratorSignals.Signal_GCCStatus.emit("Installing GCC. Please wait...")
            try:
                self.Install_GCC()
                EnvConfiguratorSignals.Signal_GCCInstalled.emit()
                EnvConfiguratorSignals.Signal_GCCStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_GCCInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_GCCStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_GCCDetected.emit()
            EnvConfiguratorSignals.Signal_GCCStatus.emit(f"GCC detected. Version: {Result}")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_GCC_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()


class CMake_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()
        
    def Check_CMake(self):
        try:
            CMakeVersion = str(EasyUtils.runCMD([['cmake', '--version']], decodeResult = True)[0])
            return CMakeVersion
        except OSError:
            return False

    def Install_CMake(self):
        if platform.system() == 'Windows':
            URL = "https://github.com/Kitware/CMake/releases/download/v3.27.0/cmake-3.27.0-windows-x86_64.zip"
            Dir_Download = './'
            File_Name = 'CMake'
            File_Format = 'zip'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            Dir_Install = Path(f"{os.getenv('SystemDrive')}/CMake").__str__()
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            if self.stopEvent.isSet():
                return
            EasyUtils.downloadFile(URL, Dir_Download, File_Name, File_Format, None)
            if self.stopEvent.isSet():
                return
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            if self.stopEvent.isSet():
                return
            EasyUtils.moveFiles(os.path.dirname(EasyUtils.getPaths(Dir_Install, 'bin')[0]), Dir_Install)
            if self.stopEvent.isSet():
                return
            EasyUtils.setEnvVar('PATH', Path_Binary, 'User')
            if self.stopEvent.isSet():
                return
            os.remove(Path_Download)

        if platform.system() == 'Linux':
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(['sudo apt-get update', 'sudo apt-get install build-essential'])

    def Execute_CMake_Installation(self):
        PathList = os.environ['PATH'].split(os.pathsep)
        for Index, Path in enumerate(PathList):
            if 'mingw' in Path.lower() and 'bin' in Path.lower():
                self.MinGW_Bin_Path = Path
                break
            elif Index == len(PathList) - 1:
                self.MinGW_Bin_Path = Path(f"{os.getenv('SystemDrive')}/MinGW/bin").__str__()
        #shutil.copy2(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'), os.path.join(self.MinGW_Bin_Path, 'make.exe')) if not os.path.isfile(os.path.join(self.MinGW_Bin_Path, 'make.exe')) else None

        Result = self.Check_CMake()
        if Result == False:
            EnvConfiguratorSignals.Signal_CMakeUndetected.emit()
            EnvConfiguratorSignals.Signal_CMakeStatus.emit("Installing CMake. Please wait...")
            try:
                self.Install_CMake()
                EnvConfiguratorSignals.Signal_CMakeInstalled.emit()
                EnvConfiguratorSignals.Signal_CMakeStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_CMakeInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_CMakeStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_CMakeDetected.emit()
            EnvConfiguratorSignals.Signal_CMakeStatus.emit(f"CMake detected. Version: {Result}")

        EasyUtils.runCMD(['set CMAKE_MAKE_PROGRAM={}'.format(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'))])
        EasyUtils.runCMD(['set CC={}'.format(os.path.join(self.MinGW_Bin_Path, 'gcc.exe'))])
        EasyUtils.runCMD(['set CXX={}'.format(os.path.join(self.MinGW_Bin_Path, 'g++.exe'))])

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_CMake_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()
"""

class Python_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def Check_Python(self):
        '''
        try:
            Version_Current = "%d.%d.%d" % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
            if sys.version_info.major == 3 and sys.version_info.minor >= 8:
                return Version_Current
            else:
                return False
        except ImportError:
            return False
        '''
        try:
            PythonVersion = str(EasyUtils.runCMD([['python', '--version']], decodeResult = True)[0])
            if PythonVersion.split('.')[0] == 'Python 3' and int(PythonVersion.split('.')[1]) >= 8:
                return PythonVersion
            else:
                return False
        except OSError:
            return False

    def Install_Python(self, Version_Download: str):
        if platform.system() == 'Windows':
            URL = "https://www.python.org/ftp/python/{0}/python-{0}.exe".format(Version_Download)
            Dir_Download = './'
            File_Name = 'python'
            File_Format = 'exe'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            if self.stopEvent.isSet():
                return
            EasyUtils.downloadFile(URL, Dir_Download, File_Name, File_Format, None)
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD([f'{Path_Download} /quiet InstallAllUsers=1 PrependPath=1'])
            if self.stopEvent.isSet():
                return
            os.remove(Path_Download)

        if platform.system() == 'Linux':
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(['sudo apt-get update', 'sudo apt-get install -y python3'])

    def Execute_Python_Installation(self, Version_Download: str):
        Result = self.Check_Python()
        if Result == False:
            EnvConfiguratorSignals.Signal_PythonUndetected.emit()
            EnvConfiguratorSignals.Signal_PythonStatus.emit("Installing Python. Please wait...")
            try:
                self.Install_Python(Version_Download)
                EnvConfiguratorSignals.Signal_PythonInstalled.emit()
                EnvConfiguratorSignals.Signal_PythonStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_PythonInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_PythonStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_PythonDetected.emit()
            EnvConfiguratorSignals.Signal_PythonStatus.emit(f"Python detected. Version: {Result}")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_Python_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()


class PyReqs_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

        self.EmitFlag = True

    def Check_PyReq(self, PackageName: str, PackageVersionReqs: str, SystemReqs: str):
        '''
        try:
            Version_Current = pkg_resources.get_distribution(Package).version #exec("import {0}".format(Package))
            Location_Current = pkg_resources.get_distribution(Package).location
            return Version_Current#, Location_Current
        except pkg_resources.DistributionNotFound: #except ModuleNotFoundError:
            return False
        '''
        try:
            PackageInfos = str(EasyUtils.runCMD([['pip', 'show', PackageName]], decodeResult = True)[0])
            if PackageInfos != 'None':
                CurrentVersion = None
                for PackageInfo in PackageInfos.splitlines():
                    if PackageInfo.startswith('Version:'):
                        CurrentVersion = PackageInfo[len('Version:'):].strip()
                        continue
                CurrentVersion = PackageInfos if CurrentVersion is None else CurrentVersion
                return CurrentVersion if EasyUtils.isVersionSatisfied(CurrentVersion, PackageVersionReqs) or not EasyUtils.isSystemSatisfied(SystemReqs) else False
            else:
                return False
        except OSError:
            return False

    def Install_PyReq(self, Package: str):
        MirrorList = ['https://pypi.org/simple', 'https://pypi.tuna.tsinghua.edu.cn/simple']
        for Mirror in MirrorList:
            if self.stopEvent.isSet():
                return
            _, _, ReturnCode = EasyUtils.runCMD([f'pip3 install {Package} --index-url {Mirror}'])
            if ReturnCode == 0:
                break

    def Execute_PyReqs_Installation(self, FilePath: str):
        MissingRequirementList = []
        with open(FilePath, 'r') as f:
            Requirements = f.read().splitlines() #Requirements = f.readlines()
        for Index, Requirement in enumerate(Requirements):
            if not (Requirement.startswith('#') or Requirement.strip() == ''):
                SplitRequirement = re.split(';', Requirement, 1)
                Package = SplitRequirement[0]
                SystemReqs = SplitRequirement[1] if len(SplitRequirement) == 2 else None
                SplitPackage = re.split('=|>|<', Package, 1)
                PackageName = SplitPackage[0]
                PackageVersionReqs = Package[len(PackageName):] if len(SplitPackage) == 2 else None
                Result = self.Check_PyReq(PackageName, PackageVersionReqs, SystemReqs)
                if Result == False:
                    if self.EmitFlag == True:
                        EnvConfiguratorSignals.Signal_PyReqsUndetected.emit()
                        self.EmitFlag = False
                    MissingRequirementList.append(Package)
                else:
                    EnvConfiguratorSignals.Signal_PyReqsDetected.emit() if Index + 1 == len(Requirements) and MissingRequirementList == [] else None
                    EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"{PackageName} detected. Version: {Result}")
            else:
                continue
        for Index, MissingRequirement in enumerate(MissingRequirementList):
            EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"Installing {MissingRequirement}. Please wait...")
            try:
                self.Install_PyReq(MissingRequirement)
                EnvConfiguratorSignals.Signal_PyReqsInstalled.emit() if Index + 1 == len(MissingRequirementList) else None
                EnvConfiguratorSignals.Signal_PyReqsStatus.emit("Successfully installed!") if Index + 1 == len(MissingRequirementList) else None
            except Exception as e:
                EnvConfiguratorSignals.Signal_PyReqsInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_PyReqsStatus.emit("Installation failed:(")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_PyReqs_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()


class Pytorch_Installer(QObject):
    '''
    '''
    started = Signal()
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

        self.EmitFlag = True

    def Check_Pytorch(self, Package: str):
        '''
        try:
            Version_Current = version.parse(pkg_resources.get_distribution(Package).version) #exec("import {0}".format(Package))
            if Package == 'torch':
                return Version_Current if Version_Current.major >= 2 or (Version_Current.major == 1 and Version_Current.minor >= 13) else False
            else:
                return Version_Current
        except pkg_resources.DistributionNotFound: #except ModuleNotFoundError:
            return False
        '''
        try:
            PackageInfos = str(EasyUtils.runCMD([['pip', 'show', Package]], decodeResult = True)[0])
            if PackageInfos != 'None':
                return PackageInfos
            else:
                return False
        except OSError:
            return False

    def Install_Pytorch(self, Package: str, Reinstall: bool):
        DisplayCommand = 'cmd /c start cmd /k ' if platform.system() == 'Windows' else 'x-terminal-emulator -e '
        if Package in ('torch', 'torchvision', 'torchaudio'):
            if self.stopEvent.isSet():
                return
            try:
                pynvml.nvmlInit()
            except:
                raise Exception("Failed to get NVIDIA GPUs' info.")
            CudaList = [117, 118, 121]
            CudaVersion = min(CudaList, key = lambda Cuda: abs(Cuda - pynvml.nvmlSystemGetCudaDriverVersion()//100))
            MirrorList = [f'https://download.pytorch.org/whl/cu{CudaVersion}', '']
            for Mirror in MirrorList:
                if self.stopEvent.isSet():
                    return
                Result = EasyUtils.runCMD([
                    DisplayCommand if Reinstall else '' + f'pip3 install {Package} --index-url {Mirror}' + '--force-reinstall' if Reinstall else ''
                ])
                if Result.returncode == 0:
                    break
        else:
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(
                [DisplayCommand if Reinstall else '' + f'pip3 uninstall {Package} -y'] if Reinstall else [] +
                [DisplayCommand if Reinstall else '' + f'pip3 install {Package} -y']
            )

    def Execute_Pytorch_Installation(self, Version: Optional[str] = None, Reinstall: bool = False):
        PackageList = ['torch', 'torchvision', 'torchaudio', 'pytorch-lightning']
        VersionDict = {
            '2.0.1': {'torch': '2.0.1', 'torchvision': '0.15.2', 'torchaudio': '2.0.2', 'pytorch-lightning': '2.1'},
            '2.2.2': {'torch': '2.2.2', 'torchvision': '0.17.2', 'torchaudio': '2.2.2', 'pytorch-lightning': '2.2'}
        }.get(Version)
        for Index, Package in enumerate(PackageList if VersionDict is None else [f'{Package}=={VersionDict[Package]}' for Package in PackageList]):
            Result = self.Check_Pytorch(Package)
            if Result == False:
                if self.EmitFlag == True:
                    EnvConfiguratorSignals.Signal_PytorchUndetected.emit()
                    self.EmitFlag = False
                EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"Installing {Package}. Please wait...")
                try:
                    self.Install_Pytorch(Package, Reinstall = False)
                    EnvConfiguratorSignals.Signal_PytorchInstalled.emit() if Index + 1 == len(PackageList) else None
                    EnvConfiguratorSignals.Signal_PytorchStatus.emit("Successfully installed!") if Index + 1 == len(PackageList) else None
                except Exception as e:
                    EnvConfiguratorSignals.Signal_PytorchInstallFailed.emit(e)
                    EnvConfiguratorSignals.Signal_PytorchStatus.emit("Installation failed:(")
            else:
                self.Install_Pytorch(Package, Reinstall) if Reinstall else None
                EnvConfiguratorSignals.Signal_PytorchDetected.emit() if Index + 1 == len(PackageList) else None
                EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"{Package} detected. Version: {Result}")

    @Slot(tuple)
    def Execute(self, Params: tuple):
        self.started.emit()

        self.Execute_Pytorch_Installation(*Params)

        self.finished.emit()

    def Terminate(self):
        self.stopEvent.set()

##############################################################################################################################