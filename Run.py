# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from subprocess import Popen

##############################################################################################################################

# Get current directory
CurrentDir = sys.path[0]


def run(
    DependencyDir: str = ...,
    ModelDir: str = ...,
    CoreDir: str = ...,
    ManifestPath: str = ...,
    RequirementsPath: str = ...,
    OutputDir: str = ...
):
    FrontendDir = Path(f'{CurrentDir}{os.sep}EVT_GUI').as_posix()
    FrontendFile = Path(f'{FrontendDir}{os.sep}Main.py').as_posix()
    Popen(
        f'python "{FrontendFile}" --dependencies "{DependencyDir}" --models "{ModelDir}" --core "{CoreDir}" --manifest "{ManifestPath}" --requirements "{RequirementsPath}" --output "{OutputDir}"',
        shell = True
    )

##############################################################################################################################

if __name__ == "__main__":
    run(
        DependencyDir = Path(CurrentDir).as_posix(),
        ModelDir = Path(CurrentDir).joinpath('Models').as_posix(),
        CoreDir = Path(CurrentDir).joinpath('EVT_Core').as_posix(),
        ManifestPath = Path(CurrentDir).joinpath('manifest.json').as_posix(),
        RequirementsPath = Path(CurrentDir).joinpath('requirements.txt').as_posix(),
        OutputDir = Path(CurrentDir).as_posix()
    )

##############################################################################################################################