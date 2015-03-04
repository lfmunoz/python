import logging

logger0 = logging.getLogger(__name__)


print "1. TEST.PY"

def test():
    print "2. TEST.PY"
    logger0.debug('debug message')
    logger0.info('info message')
    logger0.warn('warn message')
    logger0.error('error message')
    logger0.critical('critical message')
