from settings import Settings
from view import ViewSettings as view

def iniciar():
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

        settings.simulation.true()

        if not settings.save():
            return False

    return settings.get()

def simulation():
    settings = Settings()

    print(settings._data)
    settings.load()
    print(settings._data)

    while True:
        opc = view.simulation()

        if opc == '1':
            settings.simulation.true()
            break
        if opc == '2':
            settings.simulation.false()
            break
        if opc == '0':
            return

    print(settings._data)
    settings.save()
    return settings.get()