from pathlib import Path
from PyEasyUtils import loggerLevel, loggerManager, getBaseDir, getCurrentPath

#############################################################################################################

currentDir = getBaseDir(getCurrentPath())

logDir = Path(currentDir).joinpath('logs').as_posix()

logger = loggerManager()

infoLogger = logger.createLogger(
    name = "info",
    level = loggerLevel.INFO,
    outputPath = Path(logDir).joinpath("server.log"),
)

errorLogger = logger.createLogger(
    name = "error",
    level = loggerLevel.ERROR,
    outputPath = Path(logDir).joinpath("server.log"),
)

#############################################################################################################