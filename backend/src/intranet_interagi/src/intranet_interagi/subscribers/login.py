from intranet_interagi import logger
from plone import api


def login_handler(event):
    """Cria objeto Pessoa se esse não existir."""
    portal = api.portal.get()
    user = event.object
    username = user.getUserName()
    nome = user.getProperty("fullname")
    email = user.getProperty("email")
    pasta_time = portal["time"]
    area_ti = portal["ti"]
    predio = "sede"
    with api.env.adopt_roles(["Manager"]):
        # Buscar por objeto Pessoa com o mesmo id do username
        brains = api.content.find(portal_type="Pessoa", getId=username)
    # Cria objeto Pessoa
    # Dar permissão de Owner no objeto Pessoa para o usuário
