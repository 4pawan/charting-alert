import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def complete(message):
    logger.warning(f"✅ {message}")

def info(message):
    logger.info(f"{message}")

def success(message):
    logger.info(f"🟢 {message}")

def warning(message):
    logger.warning(f"⚠️ {message}")

def error(message):
    logger.error(f"❌ {message}")

def critical(message):
    logger.critical(f"🚨 {message}")

def processing(message):
    logger.warning(f"🔄 {message}")
