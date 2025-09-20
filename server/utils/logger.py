import sys
from loguru import logger
from pathlib import Path
from typing import Optional

#############################################################################################################

_loggers_initialized = False


def createLogger(
    name: str,
    level: str = "INFO",
    format: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    outputPath: Optional[str] = None,
    rotation: str = "10 MB",
):
    global _loggers_initialized

    if not _loggers_initialized:
        logger.remove()
        _loggers_initialized = True

    logger.add(
        sys.stderr,
        format = format,
        level = level,
    )

    if outputPath:
        dir = Path(outputPath).parent
        dir.mkdir(parents = True) if not dir.exists() else None

        logger.add(
            Path(outputPath).as_posix(),
            level = level,
            format = format,
            backtrace = True,
            diagnose = True,
            enqueue = True,
            rotation = rotation,
        )

    return logger.bind(name = name)

#############################################################################################################

currentDir = Path(sys.argv[0]).parent.as_posix()

logDir = Path(currentDir).joinpath('logs').as_posix()

infoLogger = createLogger(
    name = "router",
    level = "INFO",
    outputPath = Path(logDir).joinpath("server.log"),
)

errorLogger = createLogger(
    name = "error",
    level = "ERROR",
    outputPath = Path(logDir).joinpath("server.log"),
)

#############################################################################################################