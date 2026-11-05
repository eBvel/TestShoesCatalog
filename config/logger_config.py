import logging
import logging.config
from logging import Logger

CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "class": "logging.Formatter",
            "format": "[%(asctime)s] #%(levelname)-9s %(module)s:%(lineno)-3d - MESSAGE: %(message)s",
            "datefmt": "%Y-%m-%d - %H:%M:%S",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "custom",
            "stream": "ext://sys.stdout",
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "custom",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "tests": {
            "level": "INFO",
            "propagate": False,
            "handlers": ["stderr", "stdout"],
        },
        "utils": {
            "level": "INFO",
            "propagate": False,
            "handlers": ["stderr", "stdout"],
        },
    },
}

logging.config.dictConfig(CONFIG)


def get_logger(name: str) -> Logger:
    return logging.getLogger(name)
