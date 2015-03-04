import logging

logger0 = logging.getLogger(__name__)


def test():
    print "2. TEST.PY"
    logger0.debug('1 debug message')
    logger0.info('info message')
    logger0.warn('warn message')
    logger0.error('error message')
    logger0.critical('critical message')
