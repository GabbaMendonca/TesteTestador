from settings import Settings
from view import ViewSettings as view

def carregar_dados():
    """
    Carregar os dados.

    Da o comando load da classe Settings.
    Se retornar False, pede os dados de server, login e senha.
    """
    
    settings = Settings()

    if False == settings.load():

        ip = view.novo_server()
        settings.server.update('1', ip)

        user, senha = view.novo_login()
        settings.login.update(user, senha)

        if not settings.save():
            return False

    return settings.data