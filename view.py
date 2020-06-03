import controller
from settings import Server, Login

data = {}
keys = {}

data['simulation'] = True
data['user'] = ''
data['senha'] = ''
data['ip'] = ''


def terminal_start(num_key_login, num_key_server):
    ip = data['server'][keys['server'][0]]
    user = keys['login'][0]
    senha = data['login'][user]
    
    return controller.terminal_start(ip, user, senha, simulation=data['simulation'])

# def telnet_ip(ip, user, senha):
def telnet_ip():
        while True:
            ip = input('IP para acesso : ')
            
            controller.telnet_ip(ip, data['user'], data['senha'])
            print('Rodando testes, aguarde ...')
            controller.testes()
            controller.terminal_take_over()
            
            while True:
                opc = input(
    '''
    
    (9) >>> Voltar ao Terminal
    (0) >>> Logout
    
    '''
                )
            
                if opc == '9':
                    controller.terminal_take_over()
                if opc == '0':
                    controller.telnet_ip_logout()
                    return
            
            
        
def iniciar():
    
    # ----- CARREGANDO/REGISTARNDO SERVER -----    
    
    server = Server()
    data['server'] = server.get_server()
    
    if not data['server']:
        ip = input('IP do Server : ')
        server.new_server('1', ip)
        data['server'] = server.get_server()
        

    # ----- CARREGANDO/REGISTARNDO LOGIN -----

    login = Login()
    data['login'] = login.get_login()

    if not data['login']:
        user = input('User : ')
        senha = input('Senha : ')
        login.new_login(user, senha)
        data['login'] = login.get_login()
        
    keys['server'] = list(data['server'])
    keys['login'] = list(data['login'])
            
    if terminal_start(0,0):
        controller.terminal_take_over()
    else:
        raise('Problemas ao fazer login')
            
    
    while True:
        opc = input(
    '''
            
    (1) >>> Telnet no IP
    (9) >>> Voltar ao Terminal
    (0) <<< Sair
    
    '''
        )
        
        if opc == '1':
            telnet_ip()
        if opc == '9':
            controller.terminal_take_over()
        if opc == '0':
            exit()


          

iniciar()






