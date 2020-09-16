class ViewSettings:
    @staticmethod
    def novo_server():
        return input('IP do Server : ')

    @staticmethod
    def novo_login():
        user = input('Usuario : ')
        senha = input('Senha : ')
        return user, senha