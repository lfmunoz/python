import logging
import logging.config
import test

LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s - %(levelname)-8s - %(module)s] %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s - %(levelname)-8s - %(module)s] %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'test': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

logging.config.dictConfig(LOGGING_DICT)
logger = logging.getLogger('main')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


test.test()
