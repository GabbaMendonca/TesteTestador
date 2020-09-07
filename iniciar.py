from settings import Settings

LOGIN = 0
SERVER = 1
SIMULATION = 2

def carregar_dados():

    settings = Settings()

    # ----- CARREGANDO/REGISTARNDO SERVER -----    
    
    server = settings.server.get_server()

    if not server:
        ip = input('IP do Server : ')
        settings.server.new_server('1', ip)
        server = settings.server.get_server()
        
    # ----- CARREGANDO/REGISTARNDO LOGIN -----

    login = settings.login.get_login()

    if not login:
        user = input('Usuario : ')
        senha = input('Senha : ')
        settings.login.new_login(user, senha)
        login = settings.login.get_login()

    # ----- CARREGANDO STATUS SIMULAÇÃO -----

    simulation = settings.simulation.get_status()

    return login, server, simulation



