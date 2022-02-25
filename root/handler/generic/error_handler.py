#!/usr/bin/env python3

# region
from io import TextIOWrapper
from telegram import Update
from telegram.ext import CallbackContext
from root.constant.telegram import DEFAULT_CONTEXT_ARGS, LOG_CHANNEL
import root.util.logger as logger
from telegram.error import BadRequest

# endregion


def handle_error(update: Update, context: CallbackContext):
    """Send the log files to the desired Telegram chat"""
    exception: Exception = context.error
    exception_type: str = (
        exception.__class__.__name__ if exception else "UnknownException"
    )
    log_file: TextIOWrapper = open("log/server.log", "r")
    exception_message = "Exception of type {} while processing the update".format(
        exception_type
    )
    logger.error(exception_message)
    try:
        context.bot.send_document(
            LOG_CHANNEL, log_file, caption=exception_message, **DEFAULT_CONTEXT_ARGS
        )
    except BadRequest:
        logger.error("Unable to send log files to chat {}".format(LOG_CHANNEL))
    finally:
        log_file.close()
