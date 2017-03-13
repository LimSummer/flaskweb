#encoding:utf
import logging,os
from logging.handlers import TimedRotatingFileHandler  
#print os.path.realpath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

logger = logging.getLogger('timerotating')
formatter = logging.Formatter(fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
filename = os.path.join(LOG_DIR, 'myapp')
#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

handler = TimedRotatingFileHandler(filename,when='h',interval=1,backupCount=0)
handler.suffix = "%Y%m%d%H.log"
handler.setFormatter(formatter) 
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
#################################################################################################
logger.info('log module loaded.')