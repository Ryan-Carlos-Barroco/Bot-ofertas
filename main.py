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

from repositories.oferta_repository import OfertaRepository

repository = OfertaRepository()

oferta_teste = Oferta(
    nome="Fone Bluetooth JBL",
    preco=99.90,
    link="https://exemplo.com/oferta-teste-1",
)

if not repository.existe_link(oferta_teste.link):
    repository.salvar(oferta_teste)
    logger.info("Oferta de teste salva com sucesso")
else:
    logger.info("Oferta de teste ja existia, nao foi duplicada")

todas = repository.listar_todas()
logger.info(f"Total de ofertas no banco: {len(todas)}")