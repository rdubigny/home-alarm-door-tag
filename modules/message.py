import socket

from modules import logger
import config


class Message:
    def __init__(self):
        self.HOST = config.control_center_ip
        self.PORT = config.control_center_port

    def send(self, message):
        logger.logger.info(message.upper() + '!')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.HOST, self.PORT))
        s.sendall(bytes(message, 'UTF-8'))
        logger.logger.info('MESSAGE SENT!')
        s.close()
