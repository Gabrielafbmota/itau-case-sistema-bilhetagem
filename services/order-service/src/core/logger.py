import logging


def get_logger(name="user-service"):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
