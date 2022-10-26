import logging
from datetime import datetime


def Logger(logLevel):
    loggerName = "Logger"

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
        filename=f"logs_{datetime.today().strftime('%m-%d_%H-%M')}.log", mode="w"
    )

    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s: %(message)s", datefmt="%m/%d %I:%M:%S %p"
    )

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
