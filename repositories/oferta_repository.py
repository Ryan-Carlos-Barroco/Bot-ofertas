from database.connection import SessionLocal
from models.oferta import Oferta

class OfertaRepository: 
        def salvar (self, oferta: Oferta) -> None:
                with SessionLocal() as sessao:
                        sessao.add(oferta)
                        sessao.commit()

        def existe_link(self, link: str) -> bool:
                with SessionLocal() as sessao:
                        resultado = sessao.query(Oferta).filter(Oferta.link == link).first()
                        return resultado is not None

        def listar_todas(self) -> list[Oferta]:
                with SessionLocal() as sessao:
                        return sessao.query(Oferta).all()

          