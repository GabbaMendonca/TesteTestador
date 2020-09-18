from dictionary import Dictionary
from time import sleep

class _Server():
    """
    Manipula as confugurações do para acesso do server.
    """
    def __init__(self, data):
        self._data = data

    def update(self, name_server: str, ip_server: str):
        """
        Cria ou atualiza um server.
        """
        if 'server' in self._data:
            self._data['server'][name_server] = ip_server
        else:
            self._data['server'] = {name_server:ip_server}

    def delete(self, name_server : str):
        """
        Deleta um server.
        """
        try:
            del self._data['server'][name_server]
            return True
        except:
            return False

class _Login():
    """
    Manipula as confugurações do para acesso do login.
    """
    def __init__(self, data):
        self._data = data

    def update(self, user: str, password: str):
        """
        Cria ou atualiza um login.
        """
        if 'login' in self._data:
            self._data['login'][user] = password
        else:
            self._data['login'] = {user:password}

    def delete(self, user : str):
        """
        Deleta um login.
        """
        try:
            del self._data['login'][user]
            return True
        except:
            return False

class _Simulation():
    """
    Habilita ou desabilita a simulação do router.
    """
    def __init__(self, data):
        self._data = data

    def true(self):
        self._data['simulation'] = True
    
    def false(self):
        self._data['simulation'] = False


class Settings():
    """
    Manipula do dados de configuração que
    posteriormente serão gravados no dicionario.
    """
    def __init__(self):
        self._data = {}
        self.NAME_DIC = 'settings'
        self.server = _Server(self._data)
        self.login = _Login(self._data)
        self.simulation = _Simulation(self._data)


    def save(self):
        """
        Salva os dados do dicionario em um arquivo .txt
        
        :return: True ou False
        """
        dic = Dictionary()
        return dic.save( self._data, self.NAME_DIC )
    
    def load(self):
        """
        Carrega os dados do .txt 

        :return: True ou False
        """
        dic = Dictionary()
        if False == dic.get( self.NAME_DIC ):
            return False
        else:
            self._data = dic.get( self.NAME_DIC )
            return True

    def set(self, dictiorary : dict):
        """
        Carrega um dicionario externo para manipulação.

        :parm: Recebe um dicionario.
        """
        self._data = dictiorary
    
    def get(self):
        """
        :return: Retorna um dicionario com os dados carregados.
        """
        return self._data

