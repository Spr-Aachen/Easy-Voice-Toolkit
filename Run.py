# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from subprocess import Popen

##############################################################################################################################

# Get current directory
CurrentDir = Path(sys.argv[0]).parent.as_posix()


isCompiled = False


def run(
    CoreDir: str = ...,
    ManifestPath: str = ...,
    RequirementsPath: str = ...,
    DependencyDir: str = ...,
    ModelDir: str = ...,
    OutputDir: str = ...,
    ProfileDir: str = ...
):
    resourceDir = Path(sys._MEIPASS).as_posix() if getattr(sys, 'frozen', None) else CurrentDir
    frontendDir = Path(f'{resourceDir}{os.sep}{"EVT_GUI" if not isCompiled else "EVT"}').as_posix()
    frontendFile = Path(f'{frontendDir}{os.sep}{f"src{os.sep}Main.py" if not isCompiled else "Main.exe"}').as_posix()
    frontendCommand = f'{'python' if not isCompiled else ''} "{frontendFile}" --core "{CoreDir}" --manifest "{ManifestPath}" --requirements "{RequirementsPath}" --dependencies "{DependencyDir}" --models "{ModelDir}" --output "{OutputDir}" --profile "{ProfileDir}"'
    Popen(frontendCommand.strip(), shell = True)

##############################################################################################################################

if __name__ == "__main__":
    run(
        CoreDir = Path(CurrentDir).joinpath('EVT_Core').as_posix(),
        ManifestPath = Path(CurrentDir).joinpath('manifest.json').as_posix(),
        RequirementsPath = Path(CurrentDir).joinpath('requirements.txt').as_posix(),
        DependencyDir = Path(CurrentDir).as_posix(),
        ModelDir = Path(CurrentDir).joinpath('Models').as_posix(),
        OutputDir = Path(CurrentDir).as_posix(),
        ProfileDir = Path(CurrentDir).as_posix()
    )

##############################################################################################################################