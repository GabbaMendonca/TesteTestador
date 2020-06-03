import pexpect

class Terminal():    
    def start(self, ip_servidor, username, password):
        self.console = pexpect.spawn('ssh ' + str(ip_servidor))
        try:
            index = self.console.expect(['Login :', 'autorizados.', 'Connection timed out'], 
            timeout=30)

            if index == 0:
                self.console.sendline(str(username))
            elif index == 1:
                print("Terminal inicializado com sucesso !")
                return True
            elif index == 2:
                print("Verifique se o IP esta correto !!!")
                return False

            self.console.expect('Senha :', timeout=5)
            self.console.sendline(str(password))

            index = self.console.expect(['-01>', '!'], timeout=10)

            if index == 0:
                print("Terminal inicializado com sucesso !")
                return True
            elif index == 1:
                print("Senha ou usuario incorretos !!!")
                return False

        except pexpect.EOF:
            print("EOF - TERMINAL : Ops! Algo errado nao esta certo !")
            return False

        except pexpect.TIMEOUT:
            print("TIMEOUT - TERMINAL : Ops! Algo errado nao esta certo ! O terminal parou de responder ...")
            return False

        except Exception as e:
            print(e)
            return False


    def start_simulation(self, ip_servidor, username, password):
        self.console = pexpect.spawn("python router_de_testes/router_testes.py")
        try:
            self.console.sendline('ssh ' + ip_servidor)
            index = self.console.expect(['Login :', '-01>', '!'], timeout=5) # TODO : Pendente verificar erro do ip do server estiver errado

            if index == 0:
                self.console.sendline(username)
            elif index == 1:
                print("Terminal SIMULADO - OK")
                return True
            elif index == 2:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tVerifique se o IP esta correto ... ")
                return False

            self.console.expect('Senha :', timeout=5)
            self.console.sendline(password)

            index = self.console.expect(['01>', '!'], timeout=5) # TODO : Pendente verificar erro quando logiun e senha nao bater

            if index == 0:
                print("Terminal SIMULADO - OK")
                return True
            elif index == 1:
                print("\n*** Epa! Nao conseguimos acessar ***")
                print("\tSenha ou usuario incorretos ... ")
                return False

        except pexpect.EOF:
            print("EOF - TERMINAL : Ops! Algo errado nao esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT - TERMINAL : Ops! Algo errado nao esta certo !")

        except Exception:
            print("Ops! O caminho esta incorreto !")
        
    def stop(self):
        print('[Terminal sim] Stopping ...')
        print('[Terminal sim] DOWM ...')
            
            
    def take_over(self):
        try:
            print("\n *** Terminal em modo interativo *** \n\n Digite ESC para sair do modo interativo \n")
            self.console.interact(escape_character=chr(27))
            # print("\n *** Terminal em modo interativo *** \n\n Digite ( _ -> underline ) para sair do modo interativo \n")
            # self.console.interact(escape_character=chr(95))

        except pexpect.EOF:
            print("EOF : Ops! Algo errado não esta certo !")

        except pexpect.TIMEOUT:
            print("TIMEOUT : Ops! Algo errado não esta certo !")
