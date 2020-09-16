import unittest

from dictionary import Dictionary
from settings import Settings

class MyTest(unittest.TestCase):

    def test_dictionary(self):
        
        d = Dictionary()
        self.assertTrue( d.save({} , 'teste_dic') )
        self.assertEqual( d.get('teste_dic'), {})

    
    def test_settings_save(self):

        s = Settings()
        s.NAME_DIC = 'teste_settings'
        self.assertTrue( s.save() )
        
        d = Dictionary()
        self.assertEqual( d.get('teste_settings'), {} )

        s.data = {'teste':'123'}
        s.save()
        self.assertEqual( d.get('teste_settings'), {'teste':'123'} )
        self.assertTrue( s.load() )
        self.assertEqual( s.data, {'teste':'123'} )

        
    def test_settings_server(self):
        
        s = Settings()
        s.server.update('1','0.0.0.0')
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0'}} )
        s.server.update('2','0.0.0.1')
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0', '2':'0.0.0.1' }} )
        
        s.NAME_DIC = 'teste_settings'
        s.save()

        d = Dictionary()
        self.assertEqual( d.get('teste_settings'), {'server':{ '1':'0.0.0.0', '2':'0.0.0.1' }} )

        s.server.update('2','0.0.1.1')
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0', '2':'0.0.1.1' }} )
        
        s.save()
        self.assertEqual( d.get('teste_settings'), {'server':{ '1':'0.0.0.0', '2':'0.0.1.1' }} )

        self.assertFalse(s.server.delete('0'))
        self.assertTrue(s.server.delete('2'))
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0'}} )

        s.save()
        self.assertEqual( d.get('teste_settings'), {'server':{ '1':'0.0.0.0'}} )
        

    def test_settings_login(self):

        s = Settings()
        s.login.update('usuario','senha')
        self.assertEqual( s.data, {'login':{'usuario':'senha'}} )
        s.login.update('user','pass')
        self.assertEqual( s.data, {'login':{'usuario':'senha','user':'pass'}} )
        s.login.update('user','minha_senha')
        self.assertEqual( s.data, {'login':{'usuario':'senha','user':'minha_senha'}} )
        self.assertFalse(s.login.delete('teste'))
        self.assertTrue(s.login.delete('user'))
        self.assertEqual( s.data, {'login':{'usuario':'senha'}} )
        

        s.NAME_DIC = 'teste_settings'
        s.save()
        d = Dictionary()
        self.assertEqual( d.get('teste_settings'), {'login':{'usuario':'senha' }} )

    def test_settings_simulation(self):
        
        s = Settings()
        s.simulation.true()
        self.assertEqual( s.data, {'simulation':True} )
        s.simulation.false()
        self.assertEqual( s.data, {'simulation':False} )

    def test_settings(self):
        
        s = Settings()
        s.server.update('1','0.0.0.0')
        s.login.update('usuario','senha')
        s.simulation.true()
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0'}, 'login':{'usuario':'senha'}, 'simulation':True} )

        s.NAME_DIC = 'teste_settings'
        s.save()
        d = Dictionary()
        self.assertEqual( d.get('teste_settings'), {'server':{ '1':'0.0.0.0'}, 'login':{'usuario':'senha'}, 'simulation':True} )
        s.load()
        self.assertEqual( s.data, {'server':{ '1':'0.0.0.0'}, 'login':{'usuario':'senha'}, 'simulation':True} )
        
        s.NAME_DIC = 'abc'
        self.assertFalse(s.load())

if __name__ == '__main__':
    unittest.main()
