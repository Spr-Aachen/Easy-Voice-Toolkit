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
from PySide6.QtCore import QObject, Signal

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


class Aria2_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def _checkAria2(self):
        try:
            Aria2Version = str(EasyUtils.runCMD([['aria2c', '-v']], decodeResult = True)[0])
            return Aria2Version
        except OSError:
            return False

    def _installAria2(self):
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

    def executeAria2Installation(self):
        result = self._checkAria2()
        if result == False:
            EnvConfiguratorSignals.Signal_Aria2Undetected.emit()
            EnvConfiguratorSignals.Signal_Aria2Status.emit("Installing Aria2. Please wait...")
            try:
                self._installAria2()
                EnvConfiguratorSignals.Signal_Aria2Installed.emit()
                EnvConfiguratorSignals.Signal_Aria2Status.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_Aria2InstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_Aria2Status.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_Aria2Detected.emit()
            EnvConfiguratorSignals.Signal_Aria2Status.emit(f"Aria2 detected. Version: {result}")

    def execute(self):
        self.executeAria2Installation()

    def terminate(self):
        self.stopEvent.set()


class FFmpeg_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def _checkFFmpeg(self):
        try:
            FFmpegVersion = str(EasyUtils.runCMD([['ffmpeg', '-version']], decodeResult = True)[0])
            return FFmpegVersion
        except OSError:
            return False

    def _installFFmpeg(self):
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

    def executeFFmpegInstallation(self):
        result = self._checkFFmpeg()
        if result == False:
            EnvConfiguratorSignals.Signal_FFmpegUndetected.emit()
            EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Installing FFmpeg. Please wait...")
            try:
                self._installFFmpeg()
                EnvConfiguratorSignals.Signal_FFmpegInstalled.emit()
                EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_FFmpegInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_FFmpegStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
            EnvConfiguratorSignals.Signal_FFmpegStatus.emit(f"FFmpeg detected. Version: {result}")

    def execute(self):
        self.executeFFmpegInstallation()

    def terminate(self):
        self.stopEvent.set()

"""
class GCC_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()
        
    def _checkGCC(self):
        try:
            GCCVersion = str(EasyUtils.runCMD([['gcc', '--version']], decodeResult = True)[0])
            return GCCVersion
        except OSError:
            return False

    def _installGCC(self):
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

    def executeGCCInstallation(self):
        result = self._checkGCC()
        if result == False:
            EnvConfiguratorSignals.Signal_GCCUndetected.emit()
            EnvConfiguratorSignals.Signal_GCCStatus.emit("Installing GCC. Please wait...")
            try:
                self._installGCC()
                EnvConfiguratorSignals.Signal_GCCInstalled.emit()
                EnvConfiguratorSignals.Signal_GCCStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_GCCInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_GCCStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_GCCDetected.emit()
            EnvConfiguratorSignals.Signal_GCCStatus.emit(f"GCC detected. Version: {result}")

    def execute(self):
        self.executeGCCInstallation()

    def terminate(self):
        self.stopEvent.set()


class CMake_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()
        
    def _checkCMake(self):
        try:
            CMakeVersion = str(EasyUtils.runCMD([['cmake', '--version']], decodeResult = True)[0])
            return CMakeVersion
        except OSError:
            return False

    def installCMake(self):
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

    def executeCMakeInstallation(self):
        PathList = os.environ['PATH'].split(os.pathsep)
        for index, Path in enumerate(PathList):
            if 'mingw' in Path.lower() and 'bin' in Path.lower():
                self.MinGW_Bin_Path = Path
                break
            elif index == len(PathList) - 1:
                self.MinGW_Bin_Path = Path(f"{os.getenv('SystemDrive')}/MinGW/bin").__str__()
        #shutil.copy2(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'), os.path.join(self.MinGW_Bin_Path, 'make.exe')) if not os.path.isfile(os.path.join(self.MinGW_Bin_Path, 'make.exe')) else None

        result = self._checkCMake()
        if result == False:
            EnvConfiguratorSignals.Signal_CMakeUndetected.emit()
            EnvConfiguratorSignals.Signal_CMakeStatus.emit("Installing CMake. Please wait...")
            try:
                self.installCMake()
                EnvConfiguratorSignals.Signal_CMakeInstalled.emit()
                EnvConfiguratorSignals.Signal_CMakeStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_CMakeInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_CMakeStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_CMakeDetected.emit()
            EnvConfiguratorSignals.Signal_CMakeStatus.emit(f"CMake detected. Version: {result}")

        EasyUtils.runCMD(['set CMAKE_MAKE_PROGRAM={}'.format(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'))])
        EasyUtils.runCMD(['set CC={}'.format(os.path.join(self.MinGW_Bin_Path, 'gcc.exe'))])
        EasyUtils.runCMD(['set CXX={}'.format(os.path.join(self.MinGW_Bin_Path, 'g++.exe'))])

    def execute(self):
        self.executeCMakeInstallation()

    def terminate(self):
        self.stopEvent.set()
"""

class Python_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def _checkPython(self):
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

    def _installPython(self, Version_Download: str):
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

    def executePythonInstallation(self, Version_Download: str):
        result = self._checkPython()
        if result == False:
            EnvConfiguratorSignals.Signal_PythonUndetected.emit()
            EnvConfiguratorSignals.Signal_PythonStatus.emit("Installing Python. Please wait...")
            try:
                self._installPython(Version_Download)
                EnvConfiguratorSignals.Signal_PythonInstalled.emit()
                EnvConfiguratorSignals.Signal_PythonStatus.emit("Successfully installed!")
            except Exception as e:
                EnvConfiguratorSignals.Signal_PythonInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_PythonStatus.emit("Installation failed:(")
        else:
            EnvConfiguratorSignals.Signal_PythonDetected.emit()
            EnvConfiguratorSignals.Signal_PythonStatus.emit(f"Python detected. Version: {result}")

    def execute(self, version: str):
        self.executePythonInstallation(version)

    def terminate(self):
        self.stopEvent.set()


class PyReqs_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

        self.emitFlag = True

    def _checkPyReq(self, packageName: str, packageVersionReqs: str, systemReqs: str):
        '''
        try:
            Version_Current = pkg_resources.get_distribution(package).version #exec("import {0}".format(package))
            Location_Current = pkg_resources.get_distribution(package).location
            return Version_Current#, Location_Current
        except pkg_resources.DistributionNotFound: #except ModuleNotFoundError:
            return False
        '''
        try:
            packageInfos = str(EasyUtils.runCMD([['pip', 'show', packageName]], decodeResult = True)[0])
            if packageInfos != 'None':
                currentVersion = None
                for packageInfo in packageInfos.splitlines():
                    if packageInfo.startswith('Version:'):
                        currentVersion = packageInfo[len('Version:'):].strip()
                        continue
                currentVersion = packageInfos if currentVersion is None else currentVersion
                return currentVersion if EasyUtils.isVersionSatisfied(currentVersion, packageVersionReqs) or not EasyUtils.isSystemSatisfied(systemReqs) else False
            else:
                return False if EasyUtils.isSystemSatisfied(systemReqs) else None
        except OSError:
            return False

    def _installPyReq(self, package: str):
        mirrorList = ['https://pypi.org/simple', 'https://pypi.tuna.tsinghua.edu.cn/simple']
        for mirror in mirrorList:
            if self.stopEvent.isSet():
                return
            _, _, ReturnCode = EasyUtils.runCMD([f'pip3 install {package} --index-url {mirror}'])
            if ReturnCode == 0:
                break

    def executePyReqsInstallation(self, filePath: str):
        missingRequirementList = []
        with open(filePath, 'r') as f:
            requirements = f.read().splitlines() #requirements = f.readlines()
        for index, requirement in enumerate(requirements):
            if not (requirement.startswith('#') or requirement.strip() == ''):
                splitRequirement = re.split(';', requirement, 1)
                package = splitRequirement[0]
                systemReqs = splitRequirement[1] if len(splitRequirement) == 2 else None
                splitPackage = re.split('!|=|>|<', package, 1)
                packageName = splitPackage[0]
                packageVersionReqs = package[len(packageName):] if len(splitPackage) == 2 else None
                result = self._checkPyReq(packageName, packageVersionReqs, systemReqs)
                if result == False:
                    if self.emitFlag == True:
                        EnvConfiguratorSignals.Signal_PyReqsUndetected.emit()
                        self.emitFlag = False
                    missingRequirementList.append(package)
                else:
                    EnvConfiguratorSignals.Signal_PyReqsDetected.emit() if index + 1 == len(requirements) and missingRequirementList == [] else None
                    EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"{packageName} detected. Version: {result}") if result is not None else None
            else:
                continue
        for index, missingRequirement in enumerate(missingRequirementList):
            EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"Installing {missingRequirement}. Please wait...")
            try:
                self._installPyReq(missingRequirement)
                EnvConfiguratorSignals.Signal_PyReqsInstalled.emit() if index + 1 == len(missingRequirementList) else None
                EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"{missingRequirement} is successfully installed!") if index + 1 == len(missingRequirementList) else None
            except Exception as e:
                EnvConfiguratorSignals.Signal_PyReqsInstallFailed.emit(e)
                EnvConfiguratorSignals.Signal_PyReqsStatus.emit(f"{missingRequirement} installation failed:(")

    def execute(self, filePath: str):
        self.executePyReqsInstallation(filePath)

    def terminate(self):
        self.stopEvent.set()


class Pytorch_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

        self.emitFlag = True

    def _checkPytorch(self, package: str):
        '''
        try:
            Version_Current = version.parse(pkg_resources.get_distribution(package).version) #exec("import {0}".format(package))
            if package == 'torch':
                return Version_Current if Version_Current.major >= 2 or (Version_Current.major == 1 and Version_Current.minor >= 13) else False
            else:
                return Version_Current
        except pkg_resources.DistributionNotFound: #except ModuleNotFoundError:
            return False
        '''
        try:
            packageInfos = str(EasyUtils.runCMD([['pip', 'show', package]], decodeResult = True)[0])
            if packageInfos != 'None':
                return packageInfos
            else:
                return False
        except OSError:
            return False

    def _installPytorch(self, package: str, Reinstall: bool):
        DisplayCommand = 'cmd /c start cmd /k ' if platform.system() == 'Windows' else 'x-terminal-emulator -e '
        if package in ('torch', 'torchvision', 'torchaudio'):
            if self.stopEvent.isSet():
                return
            try:
                pynvml.nvmlInit()
            except:
                raise Exception("Failed to get NVIDIA GPUs' info.")
            CudaList = [117, 118, 121]
            CudaVersion = min(CudaList, key = lambda Cuda: abs(Cuda - pynvml.nvmlSystemGetCudaDriverVersion()//100))
            mirrorList = [f'https://download.pytorch.org/whl/cu{CudaVersion}', '']
            for mirror in mirrorList:
                if self.stopEvent.isSet():
                    return
                result = EasyUtils.runCMD([
                    DisplayCommand if Reinstall else '' + f'pip3 install {package} --index-url {mirror}' + '--force-reinstall' if Reinstall else ''
                ])
                if result.returncode == 0:
                    break
        else:
            if self.stopEvent.isSet():
                return
            EasyUtils.runCMD(
                [DisplayCommand if Reinstall else '' + f'pip3 uninstall {package} -y'] if Reinstall else [] +
                [DisplayCommand if Reinstall else '' + f'pip3 install {package} -y']
            )

    def executePytorchInstallation(self, Version: Optional[str] = None, Reinstall: bool = False):
        PackageList = ['torch', 'torchvision', 'torchaudio', 'pytorch-lightning']
        VersionDict = {
            '2.0.1': {'torch': '2.0.1', 'torchvision': '0.15.2', 'torchaudio': '2.0.2', 'pytorch-lightning': '2.1'},
            '2.2.2': {'torch': '2.2.2', 'torchvision': '0.17.2', 'torchaudio': '2.2.2', 'pytorch-lightning': '2.2'}
        }.get(Version)
        for index, package in enumerate(PackageList if VersionDict is None else [f'{package}=={VersionDict[package]}' for package in PackageList]):
            result = self._checkPytorch(package)
            if result == False:
                if self.emitFlag == True:
                    EnvConfiguratorSignals.Signal_PytorchUndetected.emit()
                    self.emitFlag = False
                EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"Installing {package}. Please wait...")
                try:
                    self._installPytorch(package, Reinstall = False)
                    EnvConfiguratorSignals.Signal_PytorchInstalled.emit() if index + 1 == len(PackageList) else None
                    EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"{package} is successfully installed!") if index + 1 == len(PackageList) else None
                except Exception as e:
                    EnvConfiguratorSignals.Signal_PytorchInstallFailed.emit(e)
                    EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"{package} installation failed:(")
            else:
                self._installPytorch(package, Reinstall) if Reinstall else None
                EnvConfiguratorSignals.Signal_PytorchDetected.emit() if index + 1 == len(PackageList) else None
                EnvConfiguratorSignals.Signal_PytorchStatus.emit(f"{package} detected. Version: {result}")

    def execute(self, version: Optional[str] = None, reinstall: bool = False):
        self.executePytorchInstallation(version, reinstall)

    def terminate(self):
        self.stopEvent.set()

##############################################################################################################################