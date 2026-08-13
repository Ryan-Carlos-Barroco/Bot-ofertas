from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///database/bot.db"

engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def criar_tabelas() -> None: 
        Base.metadata.create_all(bind=engine)
        


