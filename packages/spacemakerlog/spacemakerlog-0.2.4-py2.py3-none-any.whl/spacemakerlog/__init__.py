import os
import log
import logging

log.set_level(os.getenv('LOG_LEVEL', 'debug'))
log.set_format(os.getenv('LOG_FORMAT', 'json'))

botologger = logging.getLogger('boto')

for logger_name in logging.getLogger().manager.loggerDict.keys():
    logging.getLogger(logger_name).setLevel(logging.WARNING)
