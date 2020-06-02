import controller

event = {}

event['simulation'] = True
event['user'] = ''
event['senha'] = ''
event['ip'] = ''


def terminal_start():
    controller.terminal_start(event['ip'], event['user'], event['senha'], simulation=event['simulation'])
    
def telnet_ip(ip, user, senha):
    controller.telnet_ip(ip, user, senha)
    
def iniciar():
    event['ip'] = input('IP do Server : ')
    event['user'] = input('User : ')
    event['senha'] = input('Senha : ')
    
    terminal_start()
    
    while True:
        ip = input('IP para acesso : ')
        
        telnet_ip(ip, event['user'], event['senha'])
        print('Rodando testes, aguarde ...')
        controller.testes()
        controller.terminal_take_over()
        #controller.telnet_ip_logout()
        
        while True:
            opc = input('Deseja testar outro IP [s/n]: ')
            
            if opc == 's':
                break
            if opc == 'n':
                exit()
                

iniciar()






