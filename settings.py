from dictionary import new, update, delete, get

from time import sleep

class _Login():
    def new_login(self, user : str, password : str):
        "Cria um novo login"
        settings = get('settings')    

        if False != settings:
            if 'login' in settings:
                settings['login'][user] = password
                return update('settings', 'login', settings['login'])
            else:
                settings['login'] = {user : password}
                return update('settings', 'login', settings['login'])
        
        if new('settings'):
            sleep(1)
            login = {}
            login[user] = password
            return update('settings', 'login', login)
        
    def get_login(self):
        "Retorna um dict com todos os logins e senha"
        settings = get('settings')

        if 'login' in settings:
            return settings['login']
        else: 
            return False

    def update_login(self, user, password): 
        "Atualiza um login"
        settings = get('settings')
        
        if False != settings:
            settings['login'][user] = password
            return update('settings', 'login', settings['login'])
        
    def deletar_login(self, user):
        "Deleta um login"
        settings = get('settings')
        
        if False != settings:
            try:
                del settings['login'][user]
                return update('settings', 'login', settings['login'])
            except:
                return False

class _Server():
    def new_server(self, name_server: str, ip_server: str):
        "Cria um novo server"
        settings = get('settings')
        
        if False != settings:
            if 'server' in settings:
                settings['server'][name_server] = ip_server
                return update('settings', 'server', settings['server'])
            else:
                settings['server'] = {name_server : ip_server}
                return update('settings', 'server', settings['server'])
            
        
        if new('settings'):            
            sleep(1)
            server = {}
            server[name_server] = ip_server
            return update('settings', 'server', server)
         
    def get_server(self):
        "Retorna todos os servers"
        settings = get('settings')

        if 'server' in settings:
            return settings['server']
        else:
            return False

    def update_server(self, name_server : str, ip_server : str):
        "Atualiza um server"
        settings = get('settings')
        
        if False != settings:
            settings['server'][name_server] = ip_server
            return update('settings', 'server', settings['server'])

        
    def deletar_server(self, name_server : str):
        "Deleta um server"
        settings = get('settings')
        
        if False != settings:
            try:
                del settings['server'][name_server]
                return update('settings', 'server', settings['server'])
            except:
                return False
        

class _Simulation():
    def get_status(self):

        settings = get('settings')

        if 'simulation' in settings:
            return settings['simulation']
        else:
            return update('settings', 'simulation', True)
    
    def true(self):
        return update('settings', 'simulation', True)
    
    def false(self):
        return update('settings', 'simulation', False)

class Settings():
    def __init__(self):
        self.server = _Server()
        self.login = _Login()
        self.simulation = _Simulation()

    