from datetime import datetime 
from sqlalchemy import Column, Integer, String, Float, DateTime

from database.connection import Base 

class Oferta(Base):
        __tablename__ = "ofertas"

        id = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String(255), nullable=False)
        preco = Column(Float, nullable=False)
        link = Column(String(500), nullable=False, unique=True)
        coletado_em = Column(DateTime, default=datetime.utcnow)
