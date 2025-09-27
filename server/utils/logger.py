import sys
from pathlib import Path
from PyEasyUtils import loggerManager

#############################################################################################################

currentDir = Path(sys.argv[0]).parent.as_posix()

logDir = Path(currentDir).joinpath('logs').as_posix()

logger = loggerManager()

infoLogger = logger.createLogger(
    name = "info",
    level = "INFO",
    outputPath = Path(logDir).joinpath("server.log"),
)

errorLogger = logger.createLogger(
    name = "error",
    level = "ERROR",
    outputPath = Path(logDir).joinpath("server.log"),
)

#############################################################################################################