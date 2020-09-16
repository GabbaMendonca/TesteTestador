from settings import Settings

def _novo_server():
    return input('IP do Server : ')

def _novo_login():
    user = input('Usuario : ')
    senha = input('Senha : ')
    return user, senha

def carregar_dados():

    settings = Settings()
    print('Data Antes : ', settings.data)

    if False == settings.load():
        ip = _novo_server()
        settings.server.update('1', ip)

        user, senha = _novo_login()
        settings.login.update(user, senha)

        if not settings.save():
            return 'Não salvou !'
            
    print('Data Depois : ', settings.data)