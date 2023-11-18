import settings
import logging
from dramatiq.middleware import CurrentMessage


def getLogger(name):

    return TaskLogger(name)


class TaskLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        if settings.ENABLE_DEBUG:
            self.logger.setLevel(logging.DEBUG)

    def debug(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.debug(msg,  *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.info(msg,  *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.warning(msg,  *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.warn(msg,  *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.error(msg,  *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        self.logger.exception(msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        message_id = self.get_msg_id()
        msg = f'{message_id} - {msg}'
        self.logger.critical(msg,  *args, **kwargs)

    @staticmethod
    def get_msg_id():
        curr_msg = CurrentMessage.get_current_message()
        if curr_msg:
            message_id = curr_msg.message_id
        else:
            message_id = ''
        return message_id
