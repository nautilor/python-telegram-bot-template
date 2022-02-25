#!/usr/bin/env python3

# region
from telegram import Update
from telegram.ext import CallbackContext
from constant.exception import NOT_IMPLEMENTED

# endregion


def handle_group_start(update: Update, context: CallbackContext):
    """Handle the command '/start' on groups"""
    raise NOT_IMPLEMENTED