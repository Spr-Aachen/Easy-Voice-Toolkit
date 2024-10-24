import os
import sys
import platform
import shutil
import argparse
from pathlib import Path
from typing import Optional
from PySide6.QtCore import Qt, QObject, QThread, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QSizePolicy, QWidget, QMessageBox, QPushButton, QProgressBar, QLabel
from QEasyWidgets import QFunctions as QFunc
from QEasyWidgets.Windows import MessageBoxBase

from Functions import FunctionSignals, Function_SetMethodExecutor, Function_UpdateChecker
from Config import *

##############################################################################################################################

# Parse path settings
parser = argparse.ArgumentParser()
parser.add_argument("--config",    help = "path to config",    default = Path(CurrentDir).joinpath('Config', 'Config.ini'))
args = parser.parse_args()

ConfigPath = args.config

# Set DownloadDir&ExtractDir
DownloadDir = CurrentDir
ExtractDir = QFunc.NormPath(Path(CurrentDir).joinpath('Temp'))

# Set up client config
Config = QFunc.ManageConfig(ConfigPath)

# Set path of executer
try:
    ExecuterName = str(Config.getValue('Info', 'ExecuterName'))
    ExecuterPath = QFunc.NormPath(Path(CurrentDir).joinpath(ExecuterName))
except:
    BootExecuter = False
else:
    BootExecuter = True

##############################################################################################################################

def RebootIfFailed():
    if platform.system() == 'Windows':
        ScriptName = 'Booter.bat'
    if platform.system() == 'Linux':
        ScriptName = 'Booter.sh'
    if ScriptName:
        QFunc.BootWithScript(
            ProgramPath = ExecuterPath,
            DelayTime = 0,
            ScriptPath = Path(QFunc.NormPath(CurrentDir)).joinpath(ScriptName)
        )


def RebootIfSucceeded():
    if platform.system() == 'Windows':
        QFunc.RunScript(
            CommandList = [
                '@echo off',
                'echo Ready to move files and reboot',
                #f'taskkill /pid {os.getpid()} /f /t',
                'timeout /t 2 /nobreak',
                'echo Moving files...',
                f'robocopy "{ExtractDir}" "{CurrentDir}" /E /MOVE /R:3 /W:1 /NP',
                f'start "Programm Running" "{ExecuterPath}"',
                'del "%~f0"'
            ],
            ScriptPath = QFunc.NormPath(Path(CurrentDir).joinpath('Updater.bat'))
        )
    if platform.system() == 'Linux':
        QFunc.RunScript(
            CommandList = [
                'echo Ready to move files and reboot',
                #f'kill -9 {os.getpid()}',
                'sleep 2',
                'echo Moving files...',
                f'rsync -a --delete "{ExtractDir}" "{CurrentDir}"',
                f'./{ExecuterName}', #f'nohup ./{ExecuterName} &',
                'rm -rf Updater.sh'
            ],
            ScriptPath = QFunc.NormPath(Path(CurrentDir).joinpath('Updater.sh'))
        )


def UpdateDownloader(
    DownloadURL: str = ...,
    DownloadDir: str = ...,
    Name: str = ...,
    ExtractDir: str = ...,
    TargetDir: str = ...,
    #ExecuterPath: str = ...
):
    try:
        # Download
        FunctionSignals.Signal_UpdateMessage.emit("正在下载文件...\nDownloading files...")
        FileInfo = QFunc.DownloadFile(
            DownloadURL = DownloadURL,
            DownloadDir = DownloadDir,
            FileName = Name,
            FileFormat = 'zip',
            SHA_Expected = None
        )
    except Exception as e:
        #FunctionSignals.Signal_UpdateMessage.emit("文件下载失败！\nFailed to download files!")
        FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "文件下载失败！\nFailed to download files!")
    else:
        # Unpack
        FunctionSignals.Signal_UpdateMessage.emit("正在解压文件...\nUnpacking files...")
        ExtractDir = QFunc.NormPath(Path(TargetDir).joinpath('Temp')) if ExtractDir == TargetDir else ExtractDir
        shutil.unpack_archive(
            filename = FileInfo[1],
            extract_dir = ExtractDir
        )
        os.remove(FileInfo[1])
        # Cover old files (About to finish)
        FunctionSignals.Signal_UpdateMessage.emit("即将重启客户端...\nRebooting client...")
        '''
        CleanDirectory(
            Directory = TargetDir,
            WhiteList = [os.path.basename(ExtractDir), '__pycache__', '.git'].extend(FoldersToKeep)
        )
        shutil.copytree(ExtractDir, TargetDir, dirs_exist_ok = True)
        shutil.rmtree(ExtractDir)
        '''
        FunctionSignals.Signal_IsUpdateSucceeded.emit(True, "")


class Execute_Update_Checking(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self):
        Function_UpdateChecker(
            RepoOwner = RepoOwner,
            RepoName = RepoName,
            FileName = FileName,
            FileFormat = FileFormat,
            CurrentVersion = CurrentVersion
        )

        self.finished.emit()


class Execute_Update_Downloading(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute(self, DownloadURL):
        UpdateDownloader(
            DownloadURL = DownloadURL,
            DownloadDir = DownloadDir,
            Name = "EVT Update",
            ExtractDir = ExtractDir,
            TargetDir = CurrentDir
        )

        self.finished.emit()


# Show GUI
class Widget_Updater(QWidget):
    '''
    '''
    def __init__(self):
        super().__init__(
            parent = None,
            f = Qt.Widget #| Qt.FramelessWindowHint
        )

        self.setMaximumSize(246, 123)
        self.setGeometry(
            QApplication.primaryScreen().size().width() // 2 - self.width() // 2,
            QApplication.primaryScreen().size().height() // 2 - self.height() // 2,
            self.width(),
            self.height()
        )

        self.setWindowIcon(QIcon(QFunc.NormPath(Path(ResourceDir).joinpath('assets/images/Logo.ico'))))

        self.Label = QLabel()
        self.Label.setVisible(True)
        self.Label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.Label.setStyleSheet("text-align: center; font-size: 11.1px;")
        self.Label.clear()

        self.ProgressBar = QProgressBar()
        self.ProgressBar.setVisible(True)
        self.ProgressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.ProgressBar.setStyleSheet("text-align: center;")

        self.SkipButton = QPushButton()
        self.SkipButton.setVisible(True)
        self.SkipButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.SkipButton.setStyleSheet("text-align: center;")

        self.Layout = QVBoxLayout(self)
        self.Layout.setAlignment(Qt.AlignCenter)
        self.Layout.setContentsMargins(21, 12, 21, 12)
        self.Layout.setSpacing(12)
        self.Layout.addWidget(self.Label)
        self.Layout.addWidget(self.ProgressBar)
        self.Layout.addWidget(self.SkipButton)

    def Main(self):
        self.DownloadURL = str()
        def UpdateDownloadURL(DownloadURL):
            self.DownloadURL = DownloadURL

        FunctionSignals.Signal_UpdateMessage.connect(
            lambda Message: QFunc.Function_SetText(
                self.Label,
                QFunc.SetRichText(Message, 'center', 9, 420, 0.3, 12)
            )
        )
        FunctionSignals.Signal_ReadyToUpdate.connect(
            lambda DownloadURL: (
                UpdateDownloadURL(DownloadURL),
                MessageBoxBase.pop(
                    MessageType = QMessageBox.Question,
                    WindowTitle = 'Ask',
                    Text = '检测到可用的新版本，是否更新？\nNew version available, wanna update?',
                    Buttons = QMessageBox.Yes|QMessageBox.No,
                    ButtonEvents = {
                        QMessageBox.Yes: lambda: Function_SetMethodExecutor(self,
                            ProgressBar = self.ProgressBar,
                            Method = Execute_Update_Downloading.Execute,
                            Params = (self.DownloadURL)
                        ),
                        QMessageBox.No: lambda: FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "已取消下载更新！\nDownload canceled!")
                    }
                )
            ) if eval(Config.getValue('Updater', 'Asked', 'False')) is False else (
                Function_SetMethodExecutor(self,
                    ProgressBar = self.ProgressBar,
                    Method = Execute_Update_Downloading.Execute,
                    Params = (self.DownloadURL)
                ),
                Config.editConfig('Updater', 'Asked', 'False')
            )
        )
        FunctionSignals.Signal_IsUpdateSucceeded.connect(
            lambda Succeeded, Info: (
                MessageBoxBase.pop(
                    MessageType = QMessageBox.Warning,
                    WindowTitle = 'Warning',
                    Text = Info
                ) if not Succeeded and len(Info) > 0 else None,
                (RebootIfSucceeded() if Succeeded else RebootIfFailed()) if BootExecuter else None,
                QApplication.instance().exit()
            )
        )

        Function_SetMethodExecutor(self,
            ProgressBar = self.ProgressBar,
            Method = Execute_Update_Checking.Execute,
            Params = ()
        )

        self.SkipButton.setText("跳过")
        self.SkipButton.clicked.connect(
            lambda: FunctionSignals.Signal_IsUpdateSucceeded.emit(False, "")
        )

        self.show()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv) #App = QApplication([])

    UpdaterWidget = Widget_Updater()
    UpdaterWidget.Main() #UpdaterWidget.show()

    sys.exit(App.exec()) #App.exec()

##############################################################################################################################