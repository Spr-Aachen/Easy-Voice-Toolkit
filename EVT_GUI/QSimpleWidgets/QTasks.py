import sys
import psutil
import pynvml
from PySide6.QtCore import QObject, QThread, QMutex, Signal, Slot#, QTimer, QEventLoop

##############################################################################################################################

# Handle the consol's output
class ConsolOutputHandler(QThread):
    '''
    Intercept the output of the consol and send to the UI
    '''
    Signal_ConsoleInfo = Signal(str)

    def __init__(self):
        super().__init__()

        self.Mutex = QMutex()

    def run(self):
        '''
        Function to redirect stdout & stderr to the childthread
        '''
        sys.stdout = self
        sys.stderr = self

    def write(self,
        Info: object
    ):
        '''
        Function to override the default write functions of sys.stdout & sys.stderr
        '''
        self.Mutex.lock()

        self.Signal_ConsoleInfo.emit(str(Info))

        self.Mutex.unlock()

        '''
        EventLoop = QEventLoop()
        QTimer.singleShot(123, EventLoop.quit)
        EventLoop.exec()
        '''

    def flush(self):
        '''
        Function to override the default flush functions of sys.stdout & sys.stderr
        '''
        pass


# Monitor the cpu&gpu's usage
class MonitorUsage(QThread):
    '''
    Get the usage of CPU and GPU and send to the UI
    '''
    Signal_UsageInfo = Signal(str, str)

    def __init__(self):
        super().__init__()

        pynvml.nvmlInit()

    def run(self):
        while True:
            Usage_CPU_Percent = psutil.cpu_percent(interval = 1.)
            Usage_CPU = f"{Usage_CPU_Percent}%"

            #Usage_RAM_Percent = psutil.virtual_memory().percent
            #Usage_RAM = f"{Usage_RAM_Percent}%"

            Usage_GPU_Percent = 0
            for Index in range(pynvml.nvmlDeviceGetCount()):
                Usage_GPU_Percent_Single = pynvml.nvmlDeviceGetUtilizationRates(pynvml.nvmlDeviceGetHandleByIndex(Index)).gpu
                Usage_GPU_Percent += Usage_GPU_Percent_Single #Usage_GPU_Percent = Usage_GPU_Percent_Single if Usage_GPU_Percent < Usage_GPU_Percent_Single else Usage_GPU_Percent
            Usage_GPU = f"{Usage_GPU_Percent / pynvml.nvmlDeviceGetCount()}%" #Usage_GPU = f"{Usage_GPU_Percent}%"

            self.Signal_UsageInfo.emit(Usage_CPU, Usage_GPU)

            self.msleep(1000)


# Monitor the file's content
class MonitorFile(QThread):
    '''
    Get the content of file and send to the UI
    '''
    Signal_FileContent = Signal(str)

    def __init__(self, FilePath):
        super().__init__()

        self.FilePath = FilePath

    def run(self):
        while True:
            with open(self.FilePath, 'r') as File:
                FileContent = File.read()

            self.Signal_FileContent.emit(FileContent)

            self.msleep(100)

##############################################################################################################################