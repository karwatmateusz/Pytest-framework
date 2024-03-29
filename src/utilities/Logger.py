import logging
import inspect
from datetime import datetime


def Logger(logLevel):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logLevel)

    fileHandler = logging.FileHandler(
        filename=f"logs/logs__{datetime.today().strftime('%m-%d_%H-%M')}.log",
        mode="a",
    )

    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
