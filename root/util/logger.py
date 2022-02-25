#!/usr/bin/env python3

# region
import logging
import configparser
from logging.handlers import RotatingFileHandler

# endregion

CONFIG = configparser.ConfigParser()
CONFIG.read("logger.conf")
FORMAT = "%(asctime)-15s %(levelname)s:%(funcName)-8s %(message)s"
FILE = "log/server.log"
LEVEL = logging.INFO
logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    handlers=[RotatingFileHandler("server.log", maxBytes=10000000, backupCount=10)],
)


def info(message: str):
    """Log a message of at level INFO"""
    logging.info(message)


def error(message: str):
    """Log a message of at level ERROR"""
    logging.error(message)


def warn(message: str):
    """Log a message of at level WARNING"""
    logging.warning(message)


def debug(message: str):
    """Log a message of at level DEBUG"""
    logging.debug(message)


def log(level: int, message: str):
    """Log with a specific loggin level"""
    logging.log(level, message)