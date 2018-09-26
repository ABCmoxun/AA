
import logging
import sys

#创建日志实例对象
logger=logging.getLogger('name1')
#定制日志格式
formatter=logging.Formatter('%(asctime)s%(levelname)\
            s%(message)s')

#日志的输出方式:文本日志，终端日志
file_handler=logging.FileHandler('日志保存名路径文件')
#绑定日志输出格式
file_handler.setFormatter(formatter)

console_handler=logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

#日志的级别，比它高的输出
logger.setLevel(logging.DEBUG)

#上升日志错误
logger.critical('重大错误')


#把文件日志和终端日志添加到日志处理器中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#当不在使用这个日志handler时，记得remove
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)
