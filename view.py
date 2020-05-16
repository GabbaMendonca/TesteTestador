import controller

event = {}

event['simulation'] = False
event['user'] = 'gabba'
event['senha'] = '123'
event['ip'] = '10.10.10.10'

def c():
    print('Sou a func c')

def b():
    print('Sou a func b')
    print('Camando func c')
    c()

def a():    
    opc = input('Opc : ')

    func = com['menu_inicial'][opc]
    func()

    opc = input('Opc : ')

    func = com['menu_inicial'][opc]
    func()


com = {
    'menu_inicial': {
        '1': controller.terminal_start(event['user'], event['senha'], event['ip'], False),
        '2': controller.select_router_alcatel,
        '3': controller.router_alcatel_telnet,
        '4': controller.router_alcatel_version,
        '5': b,
    }
}

a()










