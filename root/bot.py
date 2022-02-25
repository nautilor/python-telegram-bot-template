#!/usr/bin/env python3

# region
from telegram.ext import Updater, Dispatcher, CommandHandler
from root.constant.command import START
from root.constant.telegram import GROUP_CHAT, PRIVATE_CHAT, TELEGRAM_TOKEN
from root.handler.generic.error_handler import handle_error
from root.handler.group.start_handler import handle_group_start
from root.handler.private.start_handler import handle_private_start

# endregion


def initialize():
    """Initialize the bot and start listening for incoming updates"""
    updater: Updater = Updater(TELEGRAM_TOKEN)
    dispatcher: Dispatcher = updater.dispatcher
    add_handler(dispatcher)
    updater.start_polling(drop_pending_updates=True)


def add_handler(dispatcher: Dispatcher):
    """Add the handlers for the updates to receive"""
    dispatcher.add_error_handler(handle_error)
    dispatcher.add_handler(CommandHandler(START, handle_private_start, PRIVATE_CHAT))
    dispatcher.add_handler(CommandHandler(START, handle_group_start, GROUP_CHAT))