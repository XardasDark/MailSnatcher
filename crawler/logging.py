"""
logging.py

This module configures the global logging for the MailSnatcher project using
a JSON formatter. It sets up a console (stdout) handler and applies the
default log level from the project's configuration. 

The configuration ensures that all log messages throughout the project are
output in JSON format, which is useful for structured logging, debugging,
and later integration with log management systems.

Usage:
    Simply import this module in your entry point or other modules to
    activate the JSON logging configuration:

        import crawler.logging

Notes:
    - The root logger is configured, so all module loggers inherit this setup.
    - Log messages containing dictionaries should use the `extra` parameter
      to be properly serialized by the JSON formatter.
"""

import logging.config
import crawler.config as config

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%d.%m.%Y - %I:%M:%S",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "json",
        }
    },
    "loggers": {"": {"handlers": ["stdout"], "level": config.DEFAULT_LOG_LEVEL}},
}


logging.config.dictConfig(LOGGING)
