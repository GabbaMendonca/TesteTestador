from dictionary import Dictionary

from time import sleep

class _Server():
    """
    Manipula as confugurações do para acesso do server.
    """
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
    """
    Manipula as confugurações do para acesso do login.
    """
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
    """
    Habilita ou desabilita a simulação do router.
    """
    def __init__(self, data):
        self.data = data

    def true(self):
        self.data['simulation'] = True
    
    def false(self):
        self.data['simulation'] = False


class Settings():
    """
    Manipula do dados de configuração que
    posteriormente serão gravados no dicionario.
    """
    def __init__(self):
        self.data = {}
        self.NAME_DIC = 'settings'
        self.server = _Server(self.data)
        self.login = _Login(self.data)
        self.simulation = _Simulation(self.data)


    def save(self):
        """
        Salva os dados do dicionario em um arquivo .txt
        
        :return: True ou False
        """
        dic = Dictionary()
        return dic.save( self.data, self.NAME_DIC )
    
    def load(self):
        """
        Carrega os dados do .txt 

        :return: True ou False
        """
        dic = Dictionary()
        if False == dic.get( self.NAME_DIC ):
            return False
        else:
            self.data = dic.get( self.NAME_DIC )
            return True