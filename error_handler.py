import logging
import os

class ErrorHandler:
    def __init__(self, log_file='logs/activity.log'):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(filename=self.log_file, level=logging.ERROR)

    def log_error(self, message):
        logging.error(message)

    def log_info(self, message):
        logging.info(message)

