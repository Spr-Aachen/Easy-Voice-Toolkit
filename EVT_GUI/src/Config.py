import sys
from pathlib import Path
from QEasyWidgets import QFunctions as QFunc

##############################################################################################################################

# Set current version
CurrentVersion = "v1.2.1"

# Set info for update url
RepoOwner = 'Spr-Aachen'
RepoName = 'Easy-Voice-Toolkit'
FileName = 'EVT_windows_x64'
FileFormat = 'zip'

##############################################################################################################################

# Check whether python file is compiled
_, IsFileCompiled = QFunc.GetFileInfo()

# Get current directory
CurrentDir = QFunc.GetBaseDir(__file__ if IsFileCompiled == False else sys.executable)

# Set path to store log
LogPath = QFunc.NormPath(Path(CurrentDir).joinpath('log.txt'))

# Set directory to load static dependencies
ResourceDir = CurrentDir if QFunc.GetBaseDir(SearchMEIPASS = True) is None else QFunc.GetBaseDir(SearchMEIPASS = True)

##############################################################################################################################