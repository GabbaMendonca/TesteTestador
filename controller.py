from command import Command


c = Command()

def terminal_start(ip, user, senha, simulation=True):
    return c.terminal_start(ip, user, senha, simulation)

def terminal_stop():
    return c.terminal_stop()

def terminal_take_over():
    c.terminal_take_over()

def testes():
    c.teste()
    
def telnet_ip_logout():
    c.telnet_ip_logout()


def telnet_ip(ip, user, senha):
    c.telnet_ip(ip, user, senha)
        
def select_router_alcatel():
    c.select_router_alcatel()

def router_alcatel_telnet():
    c.command.telnet()
    
def router_alcatel_version():
    c.command.version()

# print(c.terminal_print())

