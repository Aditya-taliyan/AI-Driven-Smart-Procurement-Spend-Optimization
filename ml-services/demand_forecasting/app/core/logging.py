import logging
import sys
from pathlib import Path
from loguru import logger
from app.core.config import settings


class InterceptHandler(logging.Handler):
    """Intercept standard logging and redirect to Loguru."""
    
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging():
    """Setup logging configuration."""
    # Remove default handlers
    logger.remove()
    
    # Add console handler
    logger.add(
        sys.stdout,
        format=settings.LOG_FORMAT,
        level=settings.LOG_LEVEL,
        colorize=True
    )
    
    # Add file handler for errors
    logger.add(
        Path("logs/error.log"),
        format=settings.LOG_FORMAT,
        level="ERROR",
        rotation="10 MB",
        retention="30 days"
    )
    
    # Add file handler for all logs
    logger.add(
        Path("logs/app.log"),
        format=settings.LOG_FORMAT,
        level=settings.LOG_LEVEL,
        rotation="10 MB",
        retention="30 days"
    )
    
    # Intercept standard logging
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
