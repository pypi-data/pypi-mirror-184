import logging
from .datetime_utils import common_date_time_formats


log_level_types = list(logging._nameToLevel.keys())


class LogConfigDc:
    complex = {
        'format': '[%(levelname)s] - [%(asctime)s] [%(pathname)s:%(lineno)d:%(funcName)s] - %(message)s',
        "datefmt": common_date_time_formats.s_dt,
        "level": logging.DEBUG,
    }

    simple = {
        'format': '[%(levelname)s] %(message)s',
        "datefmt": common_date_time_formats.s_dt,
        "level": logging.DEBUG,
    }

    usual = {
        'format': '[%(levelname)s] - [%(asctime)s] [%(filename)s:%(lineno)d] - %(message)s',
        "datefmt": common_date_time_formats.s_dt,
        "level": logging.DEBUG,
    }


log_config_dc = LogConfigDc()


log = logging.getLogger('bdtime')


def show_all_loggers():
    for name in logging.Logger.manager.loggerDict.keys():
        logger = logging.getLogger(name)
        print('name: [%s], logger: [%s]'%(name, logger))


if __name__ == '__main__':
    log = logging.getLogger("dqn")
    logging.basicConfig(**log_config_dc.usual)
    log.setLevel(logging.INFO)
    show_all_loggers()
