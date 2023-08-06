"""
a Wrapper that simplifies usage of logging


Example usage:
    import simple_logs
    logs = simple_logs.log_handling("ModuleName","filename.log")
    logs.debug("Debug Message")

Copyright 2018 Arttu Mahlakaarto
https://github.com/amahlaka
"""


import datetime
import logging


class log_handling:
    logger = ""

    def __init__(self, loggerName, fileName):
        self.logger = logging.getLogger(loggerName)
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(fileName)
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)
