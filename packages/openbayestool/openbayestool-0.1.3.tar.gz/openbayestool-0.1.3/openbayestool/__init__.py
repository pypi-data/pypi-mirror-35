# -*- coding: utf-8 -*-

from openbayestool.version import VERSION as __version__

import openbayestool.tracker

log_param = openbayestool.tracker.log_param
log_metric = openbayestool.tracker.log_metric
get_callback_url = openbayestool.tracker.get_callback_url
set_callback_url = openbayestool.tracker.set_callback_url


__all__ = [
    'log_param',
    'log_metric',
    'get_callback_url',
    'set_callback_url'
]