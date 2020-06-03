import pickle  # modulo pickle
from time import sleep

def _save_dictionary(dictionary: dict, name_file: str):
    try:
        # abrir o arquivo para gravação - o "b" significa que o arquivo é binário
        file_ = open(name_file + '.txt', 'wb')
    except:
        return False
    else:
        # Grava uma stream do objeto "dic" para o arquivo.
        pickle.dump(dictionary, file_)
        file_.close()  # fechar o arquivo
        return True


def _get_dictionary(name: str):
    try:
        # abrir o arquivo para leitura - o "b" significa que o arquivo é binário
        file_ = open(name + '.txt', 'rb')
    except:
        return False
    else:
        # Ler a stream a partir do arquivo e reconstroi o objeto original.
        dic = pickle.load(file_)
        file_.close()  # fechar o arquivo
        return dic  # retorna o conteúdo do dicionário


def _add_update_dictionary(dictionary: dict, key: str, value: str):
    dictionary[key] = value


def _delete_dictionary(dictionary: dict, key: str):
    try:
        del dictionary[key]
        return True
    except:
        return False


def new(name: str):
    dic = _get_dictionary(name)

    if dic:
        return False
    
    dic = {}
    return _save_dictionary(dic, name)


def update(name: str, key: str, value: str):
    dic = _get_dictionary(name)

    if dic == False :
        return False

    _add_update_dictionary(dic, key, value)
    return _save_dictionary(dic, name)


def get(name: str):
    return _get_dictionary(name)


def delete(name: str, key: str):
    dic = _get_dictionary(name)

    if not dic:
        return False

    if _delete_dictionary(dic, key):
        _save_dictionary(dic, name)
        return True

    return False

# ==============================================

class Login():
    def new_login(self, user, password):
        
        if False != get('login'):
            return update('login', user, password)
        
        if new('login'):
            sleep(1)
            return update('login', user, password)
        
    def get_login(self):
        return get('login')

    def update_login(self, user, password): 
        return update('login', user, password)
        
    def deletar_login(self, user):
        return delete('login', user)

class Server():
    def new_server(self, name_server, ip_server):
        
        if False != get('server'):
            return update('server', name_server, ip_server)
        
        if new('server'):
            sleep(1)
            return update('server', name_server, ip_server)
        
    def get_server(self):
        return get('server')

    def update_server(self, name_server, ip_server): 
        return update('server', name_server, ip_server)
        
    def deletar_server(self, name_server):
        return delete('server', name_server)