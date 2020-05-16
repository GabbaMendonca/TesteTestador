from command import Command


c = Command()

def terminal_start(user, senha, ip, simulation=True):
    c.terminal_start(user, senha, ip, simulation)
        
def select_router_alcatel():
    c.select_router_alcatel()

def router_alcatel_telnet():
    c.command.telnet()
    
def router_alcatel_version():
    c.command.version()

# print(c.terminal_print())

