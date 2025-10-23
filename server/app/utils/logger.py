from pathlib import Path
from PyEasyUtils import loggerManager, getBaseDir, getCurrentPath

#############################################################################################################

currentDir = getBaseDir(getCurrentPath())

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