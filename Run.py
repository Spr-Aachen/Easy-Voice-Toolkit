# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from subprocess import Popen

##############################################################################################################################

# Get current directory
CurrentDir = sys.path[0]


def run(
    CoreDir: str = ...,
    ManifestPath: str = ...,
    RequirementsPath: str = ...,
    DependencyDir: str = ...,
    ModelDir: str = ...,
    OutputDir: str = ...
):
    FrontendDir = Path(f'{CurrentDir}{os.sep}EVT_GUI').as_posix()
    FrontendFileStem = Path(f'{FrontendDir}{os.sep}src{os.sep}main').as_posix()
    if Path(f'{FrontendFileStem}.py').exists():
        Popen(
            f'python "{FrontendFileStem}.py" --core "{CoreDir}" --manifest "{ManifestPath}" --requirements "{RequirementsPath}" --dependencies "{DependencyDir}" --models "{ModelDir}" --output "{OutputDir}"',
            shell = True
        )
    if Path(f'{FrontendFileStem}.exe').exists():
        Popen(
            f'"{FrontendFileStem}.exe"'
        )

##############################################################################################################################

if __name__ == "__main__":
    run(
        CoreDir = Path(CurrentDir).joinpath('EVT_Core').as_posix(),
        ManifestPath = Path(CurrentDir).joinpath('manifest.json').as_posix(),
        RequirementsPath = Path(CurrentDir).joinpath('requirements.txt').as_posix(),
        DependencyDir = Path(CurrentDir).as_posix(),
        ModelDir = Path(CurrentDir).joinpath('Models').as_posix(),
        OutputDir = Path(CurrentDir).as_posix()
    )

##############################################################################################################################