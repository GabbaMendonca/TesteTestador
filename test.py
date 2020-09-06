import unittest

from settings import Settings
from dictionary import get
from iniciar import carregar_dados

class MyTest(unittest.TestCase):

    def test_carregar_dados(self):
        s = Settings()
        s.server.new_server('server_teste','10.10.10.10')
        s.login.new_login('meu_usuario','minha_senha')
        dados = carregar_dados()

        self.assertEqual(dados , ({'meu_usuario':'minha_senha'}, {'server_teste':'10.10.10.10'}, True))
        print(' Tupla retornada com os dados ususario e senha : ', dados)

    def test_settings_server(self):
        s = Settings()
        self.assertEqual(s.server.new_server('teste','0.0.0.0'), True)
        
        server = s.server.get_server()
        self.assertEqual(server['teste'], '0.0.0.0')
        
        server = s.server.update_server('teste','1.1.1.1')
        server = s.server.get_server()
        self.assertEqual(server['teste'], '1.1.1.1')

        server = s.server.deletar_server('teste')
        server = s.server.get_server()
        if 'teste' in server:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

        print(' Valor atual no dict server : ', server)


    def test_settings_login(self):
        s = Settings()
        self.assertEqual(s.login.new_login('usuario','senha'), True)
        
        login = s.login.get_login()
        self.assertEqual(login['usuario'], 'senha')

        login = s.login.update_login('usuario','password')
        login = s.login.get_login()
        self.assertEqual(login['usuario'], 'password')

        login = s.login.deletar_login('usuario')
        login = s.login.get_login()
        if 'usuario' in login:
            self.assertTrue(False)
        else:
            self.assertTrue(True)
        
        print(' Valor atual no dict login : ', login)

    
    def test_alterar_simulacao(self):
        
        s = Settings()
        self.assertTrue(s.simulation.get_status())
        self.assertTrue(s.simulation.false())
        self.assertFalse(s.simulation.get_status())
        self.assertTrue(s.simulation.true())
        self.assertTrue(s.simulation.get_status())

    print('''
    Status atual do dicionario:  
    
    {}
    '''.format(get('settings')))

if __name__ == '__main__':
    unittest.main()
