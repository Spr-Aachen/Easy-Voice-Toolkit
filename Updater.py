import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import Optional
from PySide6.QtCore import Qt, QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QPushButton, QProgressBar, QLabel

from EVT_GUI.Functions import Function_AnimateProgressBar
from EVT_GUI.QSimpleWidgets.Utils import CheckUpdate, DownloadFile, CleanDirectory, NormPath, TaskAccelerating, Booter, GetFileInfo, GetBaseDir, ManageConfig

##############################################################################################################################

_, IsFileCompiled = GetFileInfo()


TargetDir = GetBaseDir(__file__ if IsFileCompiled == False else sys.executable)
#os.chdir(TargetDir)


ConfigPath = NormPath(Path(TargetDir).joinpath(Path('Config', 'Config.ini')))
Config = ManageConfig(ConfigPath)


CurrentVersion = str(Config.GetValue('Info', 'CurrentVersion'))
ExecuterName = str(Config.GetValue('Info', 'ExecuterName'))
DownloadDir = TargetDir
ExtractDir = NormPath(Path(TargetDir).joinpath(Path('Temp')))
ExecuterPath = NormPath(Path(TargetDir).joinpath(Path(ExecuterName)))

##############################################################################################################################

# Where to store custom signals
class CustomSignals_Updater(QObject):
    '''
    Set up signals for updater
    '''
    Signal_ExecuteTask = Signal(tuple)

    Signal_Message = Signal(str)

    Signal_RebootAfterFinished = Signal(bool)

    Signal_Finished = Signal()


UpdaterSignals = CustomSignals_Updater()


def Updater(
    CurrentVersion: str = ...,
    IsFileCompiled: bool = ...,
    DownloadDir: str = ...,
    Name: str = ...,
    Format: str = 'zip',
    ExtractDir: str = ...,
    TargetDir: str = ...,
    ExecuterPath: str = ...
):
    '''
    '''
    try:
        IsUpdateNeeded, URL, SHA = CheckUpdate(
            RepoOwner = 'Spr-Aachen',
            RepoName = 'Easy-Voice-Toolkit',
            FileName = 'EVT',
            FileFormat = 'zip',
            Version_Current = CurrentVersion
        )

    except:
        UpdaterSignals.Signal_Message.emit("Failed to check for update")
        UpdaterSignals.Signal_RebootAfterFinished.emit(True)

    else:
        if IsUpdateNeeded:
            print("Start updating!")
            # Download
            try:
                FileInfo = DownloadFile(
                    URL = URL,
                    DownloadDir = DownloadDir,
                    FileName = Name,
                    FileFormat = Format,
                    SHA_Expected = SHA
                )
            except:
                pass
            UpdaterSignals.Signal_Message.emit("Downloading finished!")
            # Unpack
            ExtractDir = NormPath(Path(TargetDir).joinpath(Path('Temp'))) if ExtractDir == TargetDir else ExtractDir
            shutil.unpack_archive(
                filename = FileInfo[1],
                extract_dir = ExtractDir,
                format = Format
            )
            UpdaterSignals.Signal_Message.emit("File unpacked!")
            # Clean and move (Finish)
            if IsFileCompiled:
                DelayTime: int = 3
                BatFilePath = NormPath(Path(TargetDir).joinpath(Path('Updater.bat')))
                with open(BatFilePath, 'w') as BatFile:
                    CommandList = [
                        '@echo off',
                        f'ping 127.0.0.1 -n {DelayTime + 1} > nul',
                        f'set "folder_path={TargetDir}"',
                        f'set "specific_folder={ExtractDir}"',
                        'echo Cleaning old files...',
                        '''
                        for /R "%folder_path%" %%F in (*) do (
                            if /I not "%%~dpF"=="%specific_folder%\" (
                                del "%%F" /Q
                            )
                        )
                        ''',
                        'echo Moving new files...',
                        'move "%specific_folder%\*.*" "%folder_path%\"',
                        f'start "Programm Running" "{ExecuterPath}"',
                        'del "%~f0"'
                    ]
                    Commands = "\n".joinpath(CommandList)
                    BatFile.write(Commands)
                subprocess.Popen([BatFilePath], creationflags = subprocess.CREATE_NEW_CONSOLE).communicate()
            else:
                CleanDirectory(
                    Directory = TargetDir,
                    WhiteList = [os.path.basename(ExtractDir), '__pycache__', '.git']
                )
                shutil.copytree(ExtractDir, TargetDir, dirs_exist_ok = True)
                shutil.rmtree(ExtractDir)
                Booter(True, IsFileCompiled, TargetDir, ExecuterPath)
            UpdaterSignals.Signal_Message.emit("Successfully updated!")
            UpdaterSignals.Signal_RebootAfterFinished.emit(False)
        else:
            UpdaterSignals.Signal_Message.emit("Already up to date!")
            UpdaterSignals.Signal_RebootAfterFinished.emit(True)

    finally:
        UpdaterSignals.Signal_Finished.emit()


class Execute_Update_Checking(QObject):
    '''
    '''
    finished = Signal()

    def __init__(self):
        super().__init__()

    def Execute_Updater(self):
        Updater(
            CurrentVersion = CurrentVersion,
            IsFileCompiled = IsFileCompiled,
            DownloadDir = DownloadDir,
            Name = f"Easy Voice Toolkit {Config.GetValue('Info', 'CurrentVersion')}",
            Format = 'zip',
            ExtractDir = ExtractDir,
            TargetDir = TargetDir,
            ExecuterPath = ExecuterPath
        )

    def Execute(self, Params: tuple):
        TaskAccelerating(
            TargetList = [self.Execute_Updater],
            ArgsList = [Params],
            TypeList = ['MultiThreading']
        )

        self.finished.emit()


# Show GUI
class Widget_Updater(QWidget):
    '''
    '''
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.Layout = QVBoxLayout()
        self.setLayout(self.Layout)
        #self.Layout.setAlignment(Qt.AlignCenter)

        self.Label = QLabel()
        self.Label.setVisible(True)
        self.Label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.Label.setText('正在检查更新，请稍候')
        #self.Label.setStyleSheet("text-align: center;")
        self.Layout.addWidget(self.Label)

        self.ExecuteButton = QPushButton()
        self.ExecuteButton.setVisible(False)
        self.ExecuteButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.ExecuteButton.setText('执行')
        #self.ExecuteButton.setStyleSheet("text-align: center;")
        self.Layout.addWidget(self.ExecuteButton)

        self.ProgressBar = QProgressBar()
        self.ProgressBar.setVisible(True)
        self.ProgressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        #self.ProgressBar.setText('执行')
        #self.ProgressBar.setStyleSheet("text-align: center;")
        self.Layout.addWidget(self.ProgressBar)

        UpdaterSignals.Signal_Message.connect(self.Label.setText)
        UpdaterSignals.Signal_RebootAfterFinished.connect(lambda: Config.EditConfig('Updater', 'Status', 'Executed')) #UpdaterSignals.Signal_Finished.connect(lambda: Config.EditConfig('Updater', 'Status', 'Executed'), Qt.QueuedConnection)
        UpdaterSignals.Signal_RebootAfterFinished.connect(lambda Reboot: Booter(TargetDir, ExecuterPath, IsFileCompiled) if Reboot else None)
        UpdaterSignals.Signal_Finished.connect(lambda: self.close(), Qt.QueuedConnection)

    def Function_ExecuteMethod(self,
        ExecuteButton: QPushButton,
        ProgressBar: Optional[QProgressBar] = None,
        Method: object = ...,
        Params: Optional[tuple] = ()
    ):
        '''
        Function to execute outer class methods (through button)
        '''
        ClassName =  str(Method.__qualname__).split('.')[0]
        MethodName = str(Method.__qualname__).split('.')[1]

        ClassInstance = globals()[ClassName]()
        WorkerThread = QThread()

        ClassInstance.moveToThread(WorkerThread)
        ClassInstance.finished.connect(WorkerThread.quit)

        def ExecuteMethod():
            '''
            Update the attributes for outer class methods and wait to execute with multithreading
            '''
            Args = Params

            QFunctionsSignals = CustomSignals_Updater()
            QFunctionsSignals.Signal_ExecuteTask.connect(getattr(ClassInstance, MethodName))

            WorkerThread.started.connect(lambda: Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = True)) if ProgressBar else None
            WorkerThread.finished.connect(lambda: Function_AnimateProgressBar(ProgressBar = ProgressBar, IsTaskAlive = False)) if ProgressBar else None
            WorkerThread.start()

            QFunctionsSignals.Signal_ExecuteTask.emit(Args)

        ExecuteButton.clicked.connect(ExecuteMethod)
        ExecuteButton.setText("Execute 执行") if ExecuteButton.text() == "" else None

    def Main(self):
        self.Function_ExecuteMethod(
            ExecuteButton = self.ExecuteButton,
            ProgressBar = self.ProgressBar,
            Method = Execute_Update_Checking.Execute,
            Params = ()
        )
        self.ExecuteButton.click()

        self.show()

##############################################################################################################################

if __name__ == "__main__":
    App = QApplication(sys.argv) #App = QApplication([])

    UpdaterWidget = Widget_Updater()
    UpdaterWidget.Main() #UpdaterWidget.show()

    sys.exit(App.exec()) #App.exec()

##############################################################################################################################