#!/usr/bin/env python3

# region
from os import environ
from telegram.ext.filters import Filters
from telegram.parsemode import ParseMode

# endregion

TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN", "MISSING_TOKEN")

LOG_CHANNEL = environ.get("LOG_CHANNEL", "MISSING_LOG_CHANNEL")

PRIVATE_CHAT = Filters.private

GROUP_CHAT = Filters.group

DEFAULT_CONTEXT_ARGS: dict = {
    "parse_mode": ParseMode.HTML,
    "disable_web_page_preview": True,
}
