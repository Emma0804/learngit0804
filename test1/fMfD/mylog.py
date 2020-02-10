import logging
import logging.config
CONF_LOG = "D:/Study/Code/test1/fMfD/static/config/config.ini"
logging.config.fileConfig(CONF_LOG);  # 采用配置文件
logger_error = logging.getLogger('errorlogger')