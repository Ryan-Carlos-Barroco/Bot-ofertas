from config.settings import settings 
from utils.logger import configurar_logger

logger = configurar_logger("main")

logger.info("Bot inciado com sucesso")
logger.warning("Isso é so um teste de aviso")
logger.error("isso é so um teste de erro")


