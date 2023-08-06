import logging


APPLICATION_LOG_NAME = 'SHORTEST-API-CLIENT'
LOG_LEVEL = 'INFO'
DEFAULT_FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(message)s')

root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(DEFAULT_FORMATTER)
root_logger.addHandler(stream_handler)


def getLogger(short_name=None):
    name = _get_qualified_name(short_name)
    logger = logging.getLogger(name)
    return logger


def _get_qualified_name(name):
    if name:
        return '%s.%s' % (APPLICATION_LOG_NAME, name)
    else:
        return APPLICATION_LOG_NAME
