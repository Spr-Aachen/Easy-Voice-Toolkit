import os
import re
import platform
import shutil
import pynvml
import PyEasyUtils as EasyUtils
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

    def execute(self):
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

    def execute(self):
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

    def terminate(self):
        self.stopEvent.set()


class Python_Installer:
    '''
    '''
    def __init__(self):
        super().__init__()

        self.stopEvent = Event()

    def _checkPython(self):
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

    def execute(self, Version_Download: str):
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

    def execute(self, filePath: str):
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

    def execute(self, Version: Optional[str] = None, Reinstall: bool = False):
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

    def terminate(self):
        self.stopEvent.set()

##############################################################################################################################