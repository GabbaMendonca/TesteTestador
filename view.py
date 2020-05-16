import controller

event = {}

event['simulation'] = False
event['user'] = 'gabba'
event['senha'] = '123'
event['ip'] = '10.10.10.10'

def c():
    print('Sou a func c')

def terminal_start():
    controller.terminal_start(event['user'], event['senha'], event['ip'], False)

def select_router_alcatel():
    controller.select_router_alcatel()
    
def router_alcatel_telnet():
    controller.router_alcatel_telnet()
    
def router_alcatel_version():
    controller.router_alcatel_version()
    

def a():    
    while True:
        try:
            opc = input('Opc : ')

            func = com['menu inicial'][opc]
            func()
        except KeyError:
            print('Este não tem ...')




com = {
    'menu inicial': {
        '0': exit,
        '1': terminal_start,
        '2': select_router_alcatel,
        '3': router_alcatel_telnet,
        '4': router_alcatel_version,
        '5': c,
    }
}

def iniciar():
    event['user'] = input('User : ')
    event['senha'] = input('Senha : ')
    event['ip'] = input('IP : ')
    a()

iniciar()






