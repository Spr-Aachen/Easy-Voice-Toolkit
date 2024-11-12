import sys
from pathlib import Path
from QEasyWidgets import QFunctions as QFunc

##############################################################################################################################

# Set current version
currentVersion = "v1.2.1"

# Set info for update url
repoOwner = 'Spr-Aachen'
repoName = 'Easy-Voice-Toolkit'
fileName = 'EVT_windows_x64'
fileFormat = 'zip'

##############################################################################################################################

# Check whether python file is compiled
_, isFileCompiled = QFunc.getFileInfo()

# Get current directory
currentDir = QFunc.getBaseDir(__file__ if isFileCompiled == False else sys.executable)

# Set path to store log
logPath = QFunc.normPath(Path(currentDir).joinpath('log.txt'))

# Set directory to load static dependencies
resourceDir = currentDir if QFunc.getBaseDir(searchMEIPASS = True) is None else QFunc.getBaseDir(searchMEIPASS = True)

##############################################################################################################################