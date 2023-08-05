# -*- coding:utf-8 -*-
import logging
import weakref

from .output import get_output_obj_list, OUTPUT_STDOUT, OUTPUT_FILE, OUTPUT_ROTATE_FILE


_REE_LOGGERS = weakref.WeakValueDictionary()


def get_logger(name=None, outputs=[OUTPUT_STDOUT], level=logging.INFO):
    if not name:
        name = "root"
    logger = _REE_LOGGERS.get(name)
    if not logger:
        logger = _init_logger(name, outputs, level)
        _REE_LOGGERS[name] = logger

    return logger


def _init_logger(name, outputs, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    [logger.removeHandler(handler) for handler in logger.handlers]
    [logger.addHandler(output_obj.handler) for output_obj in get_output_obj_list(outputs)]
    return logger
