import sys
from pathlib import Path
from QEasyWidgets import QFunctions as QFunc

##############################################################################################################################

# Set current version
CurrentVersion = "v1.1.6"

##############################################################################################################################

# Check whether python file is compiled
_, IsFileCompiled = QFunc.GetFileInfo()

# Get current directory
CurrentDir = QFunc.GetBaseDir(__file__ if IsFileCompiled == False else sys.executable)

# Set path to store log
LogPath = QFunc.NormPath(Path(CurrentDir).joinpath('log.txt'))

# Set directory to store static dependencies
ResourceDir = CurrentDir if QFunc.GetBaseDir(SearchMEIPASS = True) is None else QFunc.GetBaseDir(SearchMEIPASS = True)

# Set directory to store models (and relevant config)
ModelsDir = QFunc.NormPath(Path(CurrentDir).joinpath('Models'))

# Set directory to store client config
ConfigDir = QFunc.NormPath(Path(CurrentDir).joinpath('Config'))

# Set path of client config
ConfigPath = QFunc.NormPath(Path(ConfigDir).joinpath('Config.ini'))

##############################################################################################################################

TargetDir = CurrentDir

DownloadDir = TargetDir

ExtractDir = QFunc.NormPath(Path(TargetDir).joinpath('Temp'))

##############################################################################################################################