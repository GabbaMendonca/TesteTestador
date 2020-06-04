import controller
from settings import Server, Login

data = {}
keys = {}

data['simulation'] = True
data['login_select'] = 'oi369932'
data['server_select'] = '1'



def terminal_start(num_key_login, num_key_server):
    ip = data['server'][keys['server'][0]]
    user = keys['login'][0]
    senha = data['login'][user]
    
    return controller.terminal_start(ip, user, senha, simulation=data['simulation'])

# def telnet_ip(ip, user, senha):
def telnet_ip():
    while True:
        ip = input('IP para acesso : ')
        
        controller.telnet_ip(ip, data['login_select'], data['senha'][data['login_select']])
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
            
            
def carregar_dados():
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


def server():
    while True:
        opc = input(
    '''
            
    (1) >>> Mostar/Selecionar Server
    (2) >>> Editar Server 
    (3) >>> Criar Server 
    (4) >>> Deletar Server
    
    (0) <<< Voltar
    
    '''
        )
        
        if opc == '1':
            
            print(data['server'])
                
            name_server = input('Escreva o nome do server que deseja selecionar \nou "q" para sair : ')
            
            if name_server == 'q':
                return
                
            if name_server in keys['server']:
                data['server_select'] = name_server
                print('server selecionado : {}'.format(data['server_select']))
            else:
                print('server errado ou não exite !!!')
            
        if opc == '2':
            
            print(data['server'])
            
            name_server = input('Escreva o nome do server que deseja modificar : ')
            ip_server = input('Qual o novo ip do server ? : ')
            
            server = Server()
            if server.update_server(name_server, ip_server):
                data['server'] = server.get_server()
                print(data['server'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
            
        if opc == '3':
            
            print(data['server'])
            
            name_server = input('Escreva o nome do server que deseja adicionar : ')
            ip_server = input('Qual o ip do server ? : ')
            
            server = Server()
            if server.update_server(name_server, ip_server):
                data['server'] = server.get_server()
                print(data['server'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
                
        if opc == '4':
            
            print(data['server'])
            
            name_server = input('Escreva o nome do server que deseja deletar : ')
            
            server = Server()
            if server.deletar_server(name_server):
                data['server'] = server.get_server()
                print(data['server'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
            
        if opc == '0':
            return

def login():
    while True:
        opc = input(
    '''
            
    (1) >>> Mostar/Selecionar Login
    (2) >>> Editar Login 
    (3) >>> Criar Login 
    (4) >>> Deletar Login 
    
    (0) <<< Voltar
    
    '''
        )
        
        if opc == '1':
            
            # print(data['login'])
            print(keys['login'])
            
            name_user = input('Escreva o nome do user que deseja selecionar \nou "q" para sair : ')
            
            if name_user == 'q':
                return
                
            if name_user in keys['login']:
                data['login_select'] = name_user
                print('user selecionado : {}'.format(data['login_select']))
            else:
                print('user errado ou não exite !!!')
            
            
        if opc == '2':
            
            print(data['login'])
            
            name_user = input('Escreva o nome do user que deseja modificar : ')
            senha_user = input('Qual o nova senha do user ? : ')
            
            login = Login()
            if login.update_login(name_user, senha_user):
                data['login'] = login.get_login()
                print(data['login'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
                
        if opc == '3':
            
            print(data['login'])
            
            name_user = input('Escreva o nome do user que deseja inserir : ')
            senha_user = input('Qual a senha do user ? : ')
            
            login = Login()
            if login.update_login(name_user, senha_user):
                data['login'] = login.get_login()
                print(data['login'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
                
        if opc == '4':
            
            print(data['login'])
            
            name_user = input('Escreva o nome do user que deseja deletar : ')
            
            login = Login()
            if login.deletar_login(name_user):
                data['login'] = login.get_login()
                print(data['login'])
                
                print('Modificado com sucesso !!!')
            else:
                print('Erro ao modificar !!!')
            
        if opc == '0':
            return

def simulacao():
    print('Simulação : {}'.format(data['simulation']))
    while True:
        opc = input(
    '''            
    (1) >>> Habilitar
    (2) >>> Desabilidatar
        
    (0) <<< Voltar
    
    '''
        )
        
        if opc == '1':
            data['simulation'] = True
            print('Simulação : {}'.format(data['simulation']))
        if opc == '2':
            data['simulation'] = False
            print('Simulação : {}'.format(data['simulation']))
        if opc == '0':
            return
    
    

def configuracoes():
    while True:
        opc = input(
    '''
            
    (1) >>> Server ->  {0}
    (2) >>> Login  ->  {1}
    
    (3) >>> Simulação ->  {2}
    
    (0) <<< Voltar
    
    '''.format(data['server'][data['server_select']], data['login_select'], data['simulation'])
        )
        
        if opc == '1':
            server()
        if opc == '2':
            login()
        if opc == '3':
            simulacao()
        if opc == '0':
            return
            

def tela_inicial():
    while True:
        opc = input(
    '''
            
    (1) >>> Iniciar
    (9) >>> Configurações
    (0) <<< Sair
    
    '''
        )
        
        if opc == '1':
            return
        if opc == '9':
            configuracoes()
        if opc == '0':
            exit()
        
def iniciar():
    
    carregar_dados()
    tela_inicial()
    if terminal_start(data['login_select'], data['server_select']):
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
            return


          

iniciar()






