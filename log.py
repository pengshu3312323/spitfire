import logging
import logging.handlers

import settings


logger = logging.getLogger('spitfire')
logger.setLevel(logging.DEBUG)

logging.basicConfig(datefmt=settings.LOG_DATE_FORMAT)

handler = logging.handlers.RotatingFileHandler(
    settings.LOG_FILE_NAME,
    maxBytes=1024 * 1024,
    backupCount=5
    )
handler.setFormatter(logging.Formatter(settings.LOG_FORMAT))

logger.addHandler(handler)
