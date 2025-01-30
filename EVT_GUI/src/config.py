import sys
from pathlib import Path
from PyEasyUtils import getFileInfo, getBaseDir, normPath

##############################################################################################################################

# Set current version
currentVersion = "v1.2.4"

# Set info for update url
repoOwner = 'Spr-Aachen'
repoName = 'Easy-Voice-Toolkit'
fileName = 'EVT_windows_x64'
fileFormat = 'zip'

##############################################################################################################################

# Check whether python file is compiled
_, isFileCompiled = getFileInfo()

# Get current directory
currentDir = getBaseDir(sys.argv[0])

# Set path to store log
logPath = normPath(Path(currentDir).joinpath('log.txt'))

# Set directory to load static dependencies
resourceDir = currentDir if getBaseDir(searchMEIPASS = True) is None else getBaseDir(searchMEIPASS = True)

##############################################################################################################################