from dictionary import Dictionary

from time import sleep

class _Server():
    def __init__(self, data):
        self.data = data

    def update(self, name_server: str, ip_server: str):
        if 'server' in self.data:
            self.data['server'][name_server] = ip_server
        else:
            self.data['server'] = {name_server:ip_server}

    def delete(self, name_server : str):
        try:
            del self.data['server'][name_server]
            return True
        except:
            return False

class _Login():
    def __init__(self, data):
        self.data = data

    def update(self, user: str, password: str):
        if 'login' in self.data:
            self.data['login'][user] = password
        else:
            self.data['login'] = {user:password}

    def delete(self, user : str):
        try:
            del self.data['login'][user]
            return True
        except:
            return False

class _Simulation():
    def __init__(self, data):
        self.data = data

    def true(self):
        self.data['simulation'] = True
    
    def false(self):
        self.data['simulation'] = False


class Settings():
    def __init__(self):
        self.data = {}
        self.NAME_DIC = 'settings'
        self.server = _Server(self.data)
        self.login = _Login(self.data)
        self.simulation = _Simulation(self.data)


    def save(self):
        dic = Dictionary()
        return dic.save( self.data, self.NAME_DIC )
    
    def load(self):
        dic = Dictionary()
        self.data = dic.get( self.NAME_DIC )
        if self.data == False:
            return False
        else:
            return True







    