# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
from subprocess import Popen

##############################################################################################################################

# Get current directory
currentDir = Path(sys.argv[0]).parent.as_posix()


def run(
    dependencyDir: str = ...,
    modelDir: str = ...,
    outputDir: str = ...,
    profileDir: str = ...,
):
    serverFile = Path(currentDir).joinpath('server', 'app', 'main.py').as_posix()
    clientFile = Path(currentDir).joinpath('client', 'src', 'main.py').as_posix()
    clientCommand = f'python "{clientFile}" --server "{serverFile}" --dependencies "{dependencyDir}" --models "{modelDir}" --output "{outputDir}" --profile "{profileDir}"'
    Popen(clientCommand.strip(), shell = True)

##############################################################################################################################

if __name__ == "__main__":
    run(
        dependencyDir = Path(currentDir).as_posix(),
        modelDir = Path(currentDir).joinpath('Models').as_posix(),
        outputDir = Path(currentDir).as_posix(),
        profileDir = Path(currentDir).as_posix()
    )

##############################################################################################################################