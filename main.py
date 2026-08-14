from config.settings import settings
from utils.logger import configurar_logger
from database.connection import criar_tabelas
from models.oferta import Oferta

logger = configurar_logger("main")

logger.info("Bot inciado com sucesso")
logger.warning("Isso é so um teste de aviso")
logger.error("isso é so um teste de erro")

criar_tabelas()
logger.info("Tabelas criadas com sucesso")