# Bot de Ofertas

Bot em Python para monitoramento de promoções e publicação automática de ofertas de afiliados, respeitando as regras e os meios oficiais das plataformas envolvidas.

## Sobre o projeto

Projeto de estudo prático de Python e arquitetura de software, com o objetivo futuro de também gerar renda através de publicação de ofertas em canais de afiliados.

## Funcionalidades planejadas

- Monitoramento de produtos e promoções
- Coleta automática de dados
- Filtro de boas ofertas
- Geração/uso de links de afiliado pelos meios oficiais
- Publicação automática em canais (WhatsApp, futuramente Telegram)
- Prevenção de duplicações
- Histórico de ofertas publicadas
- Execução contínua

## Arquitetura

Projeto organizado em camadas, com responsabilidades separadas:

    config/         # configurações do sistema (.env)
    models/         # entidades do domínio (ex: Oferta)
    repositories/   # acesso e persistência de dados
    services/       # regras de negócio (ex: filtro de boas ofertas)
    scrapers/       # coleta de dados nas plataformas
    publishers/     # publicação nos canais
    database/       # conexão e configuração do banco
    utils/          # funções auxiliares (ex: logging)
    tests/          # testes automatizados

## Stack

- **Python 3.14**
- **SQLAlchemy** (ORM) + **SQLite** (banco de dados)
- **python-dotenv** (configuração via variáveis de ambiente)

## Status

🚧 Em desenvolvimento — projeto de aprendizado incremental.

- [x] Estrutura do projeto
- [x] Ambiente virtual
- [x] Git
- [x] Configuração via `.env`
- [x] Logging
- [x] Conexão com banco de dados
- [ ] Modelos
- [ ] Camada de acesso a dados
- [ ] Coleta de dados
- [ ] Filtros
- [ ] Histórico
- [ ] Publicação
- [ ] Agendamento
- [ ] Testes
- [ ] Empacotamento
- [ ] Deploy

## Como rodar

```bash
git clone <url-do-repositorio>
cd bot_afiliados
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com as variáveis necessárias (veja `config/settings.py`).