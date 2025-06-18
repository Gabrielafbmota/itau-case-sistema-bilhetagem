import logging


def get_logger(name: str = __name__):
    """Return a configured logger using the provided name."""
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
