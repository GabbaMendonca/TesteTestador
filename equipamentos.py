from abc import abstractmethod, ABC

class RouterBase(ABC):
    
    @abstractmethod
    def login(self, *args, **kargs):
        pass
    
    @abstractmethod
    def logout(self, *args, **kargs):
        pass
    
    @abstractmethod
    def telnet(self, *args, **kargs):
        pass
    
    @abstractmethod
    def version(self, *args, **kargs):
        pass
    
    @abstractmethod
    def bgp(self, *args, **kargs):
        pass
    
    @abstractmethod
    def interface(self, *args, **kargs):
        pass
    
    @abstractmethod
    def arp(self, *args, **kargs):
        pass
    
    

# ----- *** -----

class RouterAlcatel(RouterBase):
    def __init__(self, terminal):
        self._terminal = terminal
    
    def login(self, *args, **kargs):
        print('[Router Alcatel] Logando ...')
        self._terminal.console = 'logado no Alactel ...'
        print('[Router Alcatel] Logado ...')
    
    def logout(self, *args, **kargs):
        print('[Router Alcatel] Deslogado ...')
        self._terminal.console = 'Deslogado no Alactel ...'
        print('[Router Alcatel] Deslogado ...')
    
    def telnet(self, *args, **kargs):
        print('[Router Alcatel] Logando ...')
        self._terminal.console = 'logado no Alactel ...'
        print('[Router Alcatel] Logado ...')
    
    def version(self, *args, **kargs):
        print('[Router Alactel] Version ...')
        self._terminal.console = 'version 2.0 ...'
    
    def bgp(self, *args, **kargs):
        print('[Router Alactel] BPG ...')
        self._terminal.console = 'BPG UP ...'
    
    def interface(self, *args, **kargs):
        print('[Router Alactel] interface ...')
        self._terminal.console = 'interface UP ...'
    
    def arp(self, *args, **kargs):
        print('[Router Alactel] arp ...')
        self._terminal.console = 'arp UP ...'


class RouterCisco(RouterBase):
    def __init__(self, terminal):
        self._terminal = terminal
        
    def login(self, *args, **kargs):
        print('[Router Cisco] Logando ...')
        self._terminal.console = 'logado no Cisco ...'
        print('[Router Cisco] Logado ...')
    
    def logout(self, *args, **kargs):
        print('[Router Cisco] Deslogando ...')
        self._terminal.console = 'Deslogado no Cisco ...'
        print('[Router Cisco] Deslogado ...')
    
    def telnet(self, *args, **kargs):
        print('[Router Cisco] Logando ...')
        self._terminal.console = 'logado no Cisco ...'
        print('[Router Cisco] Logado ...')
    
    def version(self, *args, **kargs):
        print('[Router Cisco] Version ...')
        self._terminal.console = 'version 2.0 ...'
    
    def bgp(self, *args, **kargs):
        print('[Router Cisco] BPG ...')
        self._terminal.console = 'BPG UP ...'
    
    def interface(self, *args, **kargs):
        print('[Router Cisco] interface ...')
        self._terminal.console = 'interface UP ...'
    
    def arp(self, *args, **kargs):
        print('[Router Cisco] arp ...')
        self._terminal.console = 'arp UP ...'

        
# ----- *** -----
        
        
        
        
        




# def _telnet(self):
#     self.terminal.child.sendline("telnet {0}".format(self.ip))

#     # Digita a senha TACACS
#     self.terminal.child.expect(':', timeout=self.timeout)  # Espera Username
#     self.terminal.child.sendline(self.user)

#     self.terminal.child.expect(':', timeout=self.timeout)  # Espera Senha
#     self.terminal.child.sendline(self.senha)

#     index = self.terminal.child.expect(['>', 'failed'], timeout=self.timeout)

#     if index == 0:
#         # Entra em modo privilegiado
#         self.terminal.child.sendline("ena")
#         self.terminal.child.sendline(self.senha)
#         index = self.terminal.child.expect(['#', '>'], timeout=self.timeout)
#         if index == 0:
#             print("Router Alcatel : Modo Privilegiado UP")
#         if index == 1:
#             print("Router Alcatel : Modo Privilegiado DOWN")
#         return True
#     if index == 1:
#         return False


class ServerAlcatel:
    ...
class ServerCisco:
    ...