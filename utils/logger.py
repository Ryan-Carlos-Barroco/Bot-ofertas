import logging 
import sys 

def configurar_logger (nome: str) -> logging.Logger:
        logger = logging.getLogger(nome)
        logger.setLevel (logging.INFO)

        if not logger.handlers:
                formato = logging.Formatter(
                        "%(asctime)s | %(levelname)s | %(name)s | %(message)s "
                )

                handler_console = logging.StreamHandler (sys.stdout)
                handler_console.setFormatter(formato)
                logger.addHandler (handler_console)

                handler_arquivo = logging.FileHandler("logs/app.log", encoding="utf-8")
                handler_arquivo.setFormatter(formato)
                logger.addHandler(handler_arquivo)

        return logger 