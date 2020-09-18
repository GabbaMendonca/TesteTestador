class ViewSettings:
    @staticmethod
    def novo_server():
        return input('IP do Server : ')

    @staticmethod
    def novo_login():
        user = input('Usuario : ')
        senha = input('Senha : ')
        return user, senha
    
    @staticmethod
    def simulation():
        return input(
    '''            
    (1) >>> Habilitar
    (2) >>> Desabilidatar
        
    (0) <<< Voltar
    
    '''
        )