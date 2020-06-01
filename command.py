from terminal import Terminal
from router import RouterAlcatel, RouterCisco
from server import ServerAlcatel, ServerCisco

from time import sleep

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
        self.timeout = 5
        if modulesExtern:
            self.modules = modulesExtern
        else:
            self.modules = modules()
                
    def terminal_start(self, ip, user, pwd, simulation):    
        self.terminal = self.modules['Terminal']()
        
        if simulation:
            self.terminal.start_simulation(ip, user, pwd)
        else:
            self.terminal.start(ip, user, pwd)
    
    def terminal_stop(self):
        self.terminal.stop()
        
    def terminal_take_over(self):
        self.terminal.take_over()
    
    def terminal_print(self):
        return f'Executando : "{self.terminal.console}"' 
    
    
    def telnet_ip(self, ip, user, senha):
        self.terminal.console.sendline("telnet {0}".format(ip))
        
        # Digita a senha TACACS
        self.terminal.console.expect(':', timeout=self.timeout)  # Espera Username
        self.terminal.console.sendline(user)

        self.terminal.console.expect(':', timeout=self.timeout)  # Espera Senha
        self.terminal.console.sendline(senha)

        index = self.terminal.console.expect(['>', 'failed'], timeout=self.timeout)

        if index == 0:
            # Entra em modo privilegiado
            self.terminal.console.sendline("ena")
            self.terminal.console.sendline(senha)
            index = self.terminal.console.expect(['#', '>'], timeout=self.timeout)
            if index == 0:
                print("Router Alcatel : Modo Privilegiado UP")
            if index == 1:
                print("Router Alcatel : Modo Privilegiado DOWN")
            return True
        if index == 1:
            print('Falha ao fazer login !!!')
    
    def telnet_ip_logout(self):
        self.terminal.console.sendline("logout")
    
    '''
    sh ver | i power | up
    sh ip bg su | i :
    sh int | i Last clearing 
    sh int | i CRC
    sh ip int br
    sh arp
    sh int su
    '''
    
    def teste(self):
        self.terminal.console.sendline("sh ver | i power | up")
        sleep(1)
        self.terminal.console.sendline("sh ip bg su | i :")
        sleep(1)
        self.terminal.console.sendline("sh int | i Last clearing")
        sleep(1)
        self.terminal.console.sendline("sh int | i CRC")
        sleep(1)
        self.terminal.console.sendline("sh ip int br")
        sleep(1)
        self.terminal.console.sendline("sh arp")
        sleep(1)
        self.terminal.console.sendline("sh int su")
        sleep(1)
        print(str(self.terminal.console.before + self.terminal.console.after))
    
    def select_server_alcatel(self):
        self.command = self.modules['ServerAlcatel'](self.terminal)
        print('[Command] selecionado server alcatel')
    
    def select_server_cisco(self):
        self.command = self.modules['ServerCisco'](self.terminal)
        print('[Command] selecionado server cisco')
    
    def select_router_alcatel(self):
        self.command = self.modules['RouterAlcatel'](self.terminal)
        print('[Command] selecionado router alcatel')
    
    def select_router_cisco(self):
        self.command = self.modules['RouterCisco'](self.terminal)
        print('[Command] selecionado router cisco')
        


    def set_timeout(self, timeout):
        self.timeout = timeout