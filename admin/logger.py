import logging
from colorama import Fore, Style, init

init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt, datefmt=None):
        super().__init__(fmt, datefmt)
        self.FORMATS = {
            logging.DEBUG: Fore.BLUE + fmt + Style.RESET_ALL,
            logging.INFO: Fore.GREEN + fmt + Style.RESET_ALL,
            logging.WARNING: Fore.YELLOW + fmt + Style.RESET_ALL,
            logging.ERROR: Fore.RED + fmt + Style.RESET_ALL,
            logging.CRITICAL: Fore.MAGENTA + fmt + Style.RESET_ALL,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class AppLogger:
    _logger = None

    @staticmethod
    def _initialize(name="app_logger"):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            formatter_str = "%(asctime)s - %(levelname)s - %(message)s"
            console_handler.setFormatter(ColoredFormatter(formatter_str))
            logger.addHandler(console_handler)

        # Set Jetty logging level to CRITICAL to suppress lower-level messages
        logging.getLogger('org.eclipse.jetty').setLevel(logging.CRITICAL)

        return logger

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            cls._logger = cls._initialize()
        return cls._logger

    @staticmethod
    def debug(message):
        AppLogger.get_logger().debug(message)

    @staticmethod
    def info(message):
        AppLogger.get_logger().info(message)

    @staticmethod
    def warning(message):
        AppLogger.get_logger().warning(message)

    @staticmethod
    def error(message):
        AppLogger.get_logger().error(message)

    @staticmethod
    def critical(message):
        AppLogger.get_logger().critical(message)

logger = AppLogger

# Example of use
if __name__ == '__main__':
    logger = AppLogger.get_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.critical("This is a critical message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")