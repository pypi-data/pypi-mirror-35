import logging

class Logger:
    """
    日志工具类
    参数:
        filename: 日志文件路径
        level: 日志级别
        fmt：日期格式
        datefmt: 时间格式
    """

    def __init__(self, filename, level=logging.INFO,fmt="%(asctime)s %(levelname)s %(filename)s %(lineno)d: %(message)s",datefmt="%Y-%m-%d %H:%M:%S"):
        self._logger = logging.getLogger()
        self._logger.setLevel(level)
        fh = logging.FileHandler(filename)
        fh.setLevel(level)
        ft = logging.Formatter(fmt, datefmt)
        fh.setFormatter(ft)
        self._logger.addHandler(fh)

    @property
    def logger(self):
        return self._logger