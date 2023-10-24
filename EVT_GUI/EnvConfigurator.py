import os
#import sys
import platform
import shutil
import pynvml
#import subprocess
#import pkg_resources
#from packaging import version
from PySide6.QtCore import QObject, Signal

from .QSimpleWidgets.Utils import *

##############################################################################################################################

# Where to store custom signals
class CustomSignals_EnvConfigurator(QObject):
    '''
    Set up signals for configurator functions
    '''
    Signal_FFmpegDetected = Signal()
    Signal_FFmpegUndetected = Signal()
    Signal_FFmpegInstalled = Signal()
    Signal_FFmpegInstallFailed = Signal()
    '''
    Signal_GCCDetected = Signal()
    Signal_GCCUndetected = Signal()
    Signal_GCCInstalled = Signal()
    Signal_GCCInstallFailed = Signal()

    Signal_CMakeDetected = Signal()
    Signal_CMakeUndetected = Signal()
    Signal_CMakeInstalled = Signal()
    Signal_CMakeInstallFailed = Signal()
    '''
    Signal_PythonDetected = Signal()
    Signal_PythonUndetected = Signal()
    Signal_PythonInstalled = Signal()
    Signal_PythonInstallFailed = Signal()

    Signal_PyReqsDetected = Signal()
    Signal_PyReqsUndetected = Signal()
    Signal_PyReqsInstalled = Signal()
    Signal_PyReqsInstallFailed = Signal()

    Signal_PytorchDetected = Signal()
    Signal_PytorchUndetected = Signal()
    Signal_PytorchInstalled = Signal()
    Signal_PytorchInstallFailed = Signal()


EnvConfiguratorSignals = CustomSignals_EnvConfigurator()

##############################################################################################################################

class FFmpeg_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()
        
    def Check_FFmpeg(self):
        try:
            FFmpegVersion, _, _ = RunCMD([['ffmpeg', '-version']], DecodeResult = True)
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
            Dir_Install = f"{os.getenv('SystemDrive')}/FFmpeg"
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            DownloadFile(URL, Dir_Download, File_Name, File_Format, None) #RunCMD([f'powershell.exe -Command (New-Object System.Net.WebClient).DownloadFile("{URL}", "{Path_Download}")'])
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            MoveFiles(os.path.dirname(GetPath(Dir_Install, 'bin')), Dir_Install)
            SetEnvVar('PATH', Path_Binary, 'User') #RunCMD([f'setx /M PATH "%PATH%;{Path_Binary}"'])
            os.remove(Path_Download) #RunCMD([f'powershell.exe -Command Remove-Item -Force -Path "{Path_Download}"'])
        
        if platform.system() == 'Linux':
            RunCMD(['sudo apt-get update', 'sudo apt-get install ffmpeg'])

    def Execute_FFmpeg_Installation(self):
        Result = self.Check_FFmpeg()
        if Result == False:
            EnvConfiguratorSignals.Signal_FFmpegUndetected.emit()
            print("Installing FFmpeg. Please wait...")
            try:
                self.Install_FFmpeg()
                EnvConfiguratorSignals.Signal_FFmpegInstalled.emit()
            except:
                EnvConfiguratorSignals.Signal_FFmpegInstallFailed.emit()
        else:
            EnvConfiguratorSignals.Signal_FFmpegDetected.emit()
            print(f"FFmpeg detected. Version: {Result}")
    
    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_FFmpeg_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()

"""
class GCC_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()
        
    def Check_GCC(self):
        try:
            GCCVersion, _, _ = RunCMD([['gcc', '--version']], DecodeResult = True)
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
            Dir_Install = f"{os.getenv('SystemDrive')}/MinGW"
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            DownloadFile(URL, Dir_Download, File_Name, File_Format, None) #RunCMD([f'powershell.exe -Command (New-Object System.Net.WebClient).DownloadFile("{URL}", "{Path_Download}")'])
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            MoveFiles(os.path.dirname(GetPath(Dir_Install, 'bin')), Dir_Install)
            SetEnvVar('PATH', Path_Binary, 'User') #RunCMD([f'setx /M PATH "%PATH%;{Path_Binary}"'])
            os.remove(Path_Download) #RunCMD([f'powershell.exe -Command Remove-Item -Force -Path "{Path_Download}"'])
        
        if platform.system() == 'Linux':
            RunCMD(['sudo apt-get update', 'sudo apt-get install build-essential'])

    def Execute_GCC_Installation(self):
        Result = self.Check_GCC()
        if Result == False:
            EnvConfiguratorSignals.Signal_GCCUndetected.emit()
            print("Installing GCC. Please wait...")
            try:
                self.Install_GCC()
                EnvConfiguratorSignals.Signal_GCCInstalled.emit()
            except:
                EnvConfiguratorSignals.Signal_GCCInstallFailed.emit()
        else:
            EnvConfiguratorSignals.Signal_GCCDetected.emit()
            print(f"GCC detected. Version: {Result}")
    
    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_GCC_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


class CMake_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Check_CMake(self):
        try:
            CMakeVersion, _, _ = RunCMD([['cmake', '--version']], DecodeResult = True)
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
            Dir_Install = f"{os.getenv('SystemDrive')}/CMake"
            Path_Binary = os.path.normpath(os.path.join(Dir_Install, 'bin'))
            DownloadFile(URL, Dir_Download, File_Name, File_Format, None) #RunCMD([f'powershell.exe -Command (New-Object System.Net.WebClient).DownloadFile("{URL}", "{Path_Download}")'])
            shutil.unpack_archive(Path_Download, Dir_Install, Path_Download.rsplit('.', 1)[-1])
            MoveFiles(os.path.dirname(GetPath(Dir_Install, 'bin')), Dir_Install)
            SetEnvVar('PATH', Path_Binary, 'User') #RunCMD([f'setx /M PATH "%PATH%;{Path_Binary}"'])
            os.remove(Path_Download) #RunCMD([f'powershell.exe -Command Remove-Item -Force -Path "{Path_Download}"'])
        
        if platform.system() == 'Linux':
            RunCMD(['sudo apt-get update', 'sudo apt-get install build-essential'])

    def Execute_CMake_Installation(self):
        PathList = os.environ['PATH'].split(os.pathsep)
        for Index, Path in enumerate(PathList):
            if 'mingw' in Path.lower() and 'bin' in Path.lower():
                self.MinGW_Bin_Path = Path
                break
            elif Index == len(PathList) - 1:
                self.MinGW_Bin_Path = f"{os.getenv('SystemDrive')}/MinGW/bin"
        #shutil.copy2(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'), os.path.join(self.MinGW_Bin_Path, 'make.exe')) if not os.path.isfile(os.path.join(self.MinGW_Bin_Path, 'make.exe')) else None

        Result = self.Check_CMake()
        if Result == False:
            EnvConfiguratorSignals.Signal_CMakeUndetected.emit()
            print("Installing CMake. Please wait...")
            try:
                self.Install_CMake()
                EnvConfiguratorSignals.Signal_CMakeInstalled.emit()
            except:
                EnvConfiguratorSignals.Signal_CMakeInstallFailed.emit()
        else:
            EnvConfiguratorSignals.Signal_CMakeDetected.emit()
            print(f"CMake detected. Version: {Result}")

        RunCMD(['set CMAKE_MAKE_PROGRAM={}'.format(os.path.join(self.MinGW_Bin_Path, 'mingw32-make.exe'))])
        RunCMD(['set CC={}'.format(os.path.join(self.MinGW_Bin_Path, 'gcc.exe'))])
        RunCMD(['set CXX={}'.format(os.path.join(self.MinGW_Bin_Path, 'g++.exe'))])

    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_CMake_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()
"""

class Python_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

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
            PythonVersion, _, _ = RunCMD([['python', '--version']], DecodeResult = True)
            if PythonVersion.split('.')[0] == 'Python 3' and int(PythonVersion.split('.')[1]) >= 8:
                return PythonVersion
            else:
                return False
        except OSError:
            return False

    def Install_Python(self, Version_Download: str):
        if platform.system() == 'Windows':
            URL = "https://www.python.org/ftp/python/{0}/python-{0}-amd64.exe".format(Version_Download)
            Dir_Download = './'
            File_Name = 'python'
            File_Format = 'exe'
            Path_Download = os.path.join(Dir_Download, f"{File_Name}.{File_Format}")
            DownloadFile(URL, Dir_Download, File_Name, File_Format, None) #RunCMD([f'powershell.exe -Command (New-Object System.Net.WebClient).DownloadFile("{URL}", "{Path_Download}")'])
            RunCMD([f'{Path_Download} /quiet InstallAllUsers=1 PrependPath=1'])
            os.remove(Path_Download) #RunCMD([f'powershell.exe -Command Remove-Item -Force -Path "{Path_Download}"'])
            
        if platform.system() == 'Linux':
            RunCMD(['sudo apt-get update', 'sudo apt-get install -y python3'])

    def Execute_Python_Installation(self, Version_Download: str):
        Result = self.Check_Python()
        if Result == False:
            EnvConfiguratorSignals.Signal_PythonUndetected.emit()
            print("Installing Python. Please wait...")
            try:
                self.Install_Python(Version_Download)
                EnvConfiguratorSignals.Signal_PythonInstalled.emit()
            except:
                EnvConfiguratorSignals.Signal_PythonInstallFailed.emit()
        else:
            EnvConfiguratorSignals.Signal_PythonDetected.emit()
            print(f"Python detected. Version: {Result}")
    
    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_Python_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


class PyReqs_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.EmitFlag = True

    def Check_PyReq(self, Package: str):
        '''
        try:
            Version_Current = pkg_resources.get_distribution(Package).version #exec("import {0}".format(Package))
            Location_Current = pkg_resources.get_distribution(Package).location
            return Version_Current#, Location_Current
        except pkg_resources.DistributionNotFound: #except ModuleNotFoundError:
            return False
        '''
        try:
            PackageInfo, _, _ = RunCMD([['pip', 'show', Package]], DecodeResult = True)
            if 'not found' not in PackageInfo:
                return PackageInfo
            else:
                return False
        except OSError:
            return False

    def Install_PyReq(self, Package: str):
        MirrorList = ['https://pypi.org/simple/', 'https://pypi.tuna.tsinghua.edu.cn/simple']
        for Mirror in MirrorList:
            '''
            Ask = "This script requires {0}. Do you want to install {0}? [y/n]".format(Package)
            Inquiry = input(Ask)
            while Inquiry not in ("y", "n"):
                Inquiry = input(Ask)
            if Inquiry == "y":
                os.system("pip3 install {0} --index-url {1}".format(Package, Mirror))
            else:
                exit(-1)
            '''
            _, _, ReturnCode = RunCMD([f'pip3 install {Package} --index-url {Mirror}'])
            if ReturnCode == 0:
                break

    def Execute_PyReqs_Installation(self, FilePath: str):
        with open(FilePath, 'r') as f:
            Requirements = f.read().splitlines() #Requirements = f.readlines()
        for Requirement in Requirements:
            if not (Requirement.startswith('#') or Requirement.strip() == ''):
                Package = Requirement.strip()
                Result = self.Check_PyReq(Package)
                if Result == False:
                    if self.EmitFlag == True:
                        EnvConfiguratorSignals.Signal_PyReqsUndetected.emit()
                        self.EmitFlag == False
                    print(f"Installing {Package}. Please wait...")
                    try:
                        self.Install_PyReq(Package)
                        EnvConfiguratorSignals.Signal_PyReqsInstalled.emit()
                    except:
                        EnvConfiguratorSignals.Signal_PyReqsInstallFailed.emit()
                else:
                    EnvConfiguratorSignals.Signal_PyReqsDetected.emit()
                    print(f"{Package} detected. Version: {Result}")
            else:
                continue
    
    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_PyReqs_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


class Pytorch_Installer(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

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
            PackageInfo, _, _ = RunCMD(['pip', 'show', Package], DecodeResult = True)
            if 'not found' not in PackageInfo:
                return PackageInfo
            else:
                return False
        except OSError:
            return False

    def Install_Pytorch(self, Package: str):
        pynvml.nvmlInit()
        CudaVersion = pynvml.nvmlDeviceGetCudaComputeCapability(pynvml.nvmlDeviceGetHandleByIndex(0))[1]
        MirrorList = [f'https://download.pytorch.org/whl/cu{CudaVersion}', '']
        for Mirror in MirrorList:
            Result = RunCMD([f'pip3 install {Package} --index-url {Mirror}'])
            if Result.returncode == 0:
                break

    def Execute_Pytorch_Installation(self):
        PackageList = ['torch', 'torchvision', 'torchaudio']
        for Package in PackageList:
            Result = self.Check_Pytorch(Package)
            if Result == False:
                if self.EmitFlag == True:
                    EnvConfiguratorSignals.Signal_PytorchUndetected.emit()
                    self.EmitFlag == False
                print(f"Installing {Package}. Please wait...")
                try:
                    self.Install_Pytorch(Package)
                    EnvConfiguratorSignals.Signal_PytorchInstalled.emit()
                except:
                    EnvConfiguratorSignals.Signal_PytorchInstallFailed.emit()
            else:
                EnvConfiguratorSignals.Signal_PytorchDetected.emit()
                print(f"{Package} detected. Version: {Result}")
    
    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_Pytorch_Installation],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()

##############################################################################################################################