from terminal import Terminal
from router import RouterAlcatel, RouterCisco
from server import ServerAlcatel, ServerCisco

def modules():
    modules = {}

    modules['Terminal'] = Terminal
    modules['RouterAlcatel'] = RouterAlcatel
    modules['RouterCisco'] = RouterCisco
    modules['ServerAlcatel'] = ServerAlcatel
    modules['ServerCisco'] = ServerCisco
    
    return modules



class Command():    
    def __init__(self, modulesExtern: dict = {}):
        if modulesExtern:
            self.modules = modulesExtern
        else:
            self.modules = modules()
                
    def terminal_start(self, simulation=True):    
        self.terminal = self.modules['Terminal']()
        
        if simulation:
            self.terminal.start_simulation(self.ip, self.user, self.pwd)
        else:
            self.terminal.start(self.ip, self.user, self.pwd)
    
    def terminal_stop(self):
        self.terminal.stop()
        
    def terminal_take_over(self):
        self.terminal.take_over()
    
    def terminal_print(self):
        return f'Executando : "{self.terminal.console}"' 
    
    
        
    def select_server_alcatel(self):
        self.command = self.modules['ServerAlcatel'](self.terminal)
        print('[command] selecionado server alcatel')
    
    def select_server_cisco(self):
        self.command = self.modules['ServerCisco'](self.terminal)
        print('[command] selecionado server cisco')
    
    def select_router_alcatel(self):
        self.command = self.modules['RouterAlcatel'](self.terminal)
        print('[command] selecionado router alcatel')
    
    def select_router_cisco(self):
        self.command = self.modules['RouterCisco'](self.terminal)
        print('[command] selecionado router cisco')
    
    
    
    def set_user(self, user):
        self.user = user
    
    def set_senha(self, pwd):
        self.pwd = pwd        
    
    def set_ip(self, ip):
        self.ip = ip        

    def set_timeout(self, timeout):
        self.timeout = timeout