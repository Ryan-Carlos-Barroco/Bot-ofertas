import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    bot_oferta: str


def carregar_configuracoes() -> Settings:
    return Settings(
        bot_oferta=os.getenv("NOME_DO_BOT", "BotSemNome")
    )


settings = carregar_configuracoes()