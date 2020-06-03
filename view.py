import controller

event = {}

event['simulation'] = True
event['user'] = ''
event['senha'] = ''
event['ip'] = ''


def terminal_start():
    return controller.terminal_start(event['ip'], event['user'], event['senha'], simulation=event['simulation'])

# def telnet_ip(ip, user, senha):
def telnet_ip():
        while True:
            ip = input('IP para acesso : ')
            
            controller.telnet_ip(ip, event['user'], event['senha'])
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
    while True:
        event['ip'] = input('IP do Server : ')
        event['user'] = input('User : ')
        event['senha'] = input('Senha : ')
        
        if terminal_start():
            controller.terminal_take_over()
            break
            
    
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






