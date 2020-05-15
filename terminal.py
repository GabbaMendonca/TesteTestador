class Terminal():    
    def start(self, ip_servidor, username, password):
        print('[Terminal] startando ...')
        self.console = 'Aguardando ...'
        print(f'[Terminal] IP servidor : {ip_servidor}')
        print(f'[Terminal] Username    : {username}')
        print(f'[Terminal] Password    : {password}')
        
        print('[Terminal] UP ...')


    def start_simulation(self, ip_servidor, username, password):
        print('[Terminal sim] startando ...')
        self.console = 'Aguardando ...'
        print(f'[Terminal sim] IP servidor : {ip_servidor}')
        print(f'[Terminal sim] Username    : {username}')
        print(f'[Terminal sim] Password    : {password}')
        
        print('[Terminal sim] UP ...')
        
    def stop(self):
        print('[Terminal sim] Stopping ...')
        print('[Terminal sim] DOWM ...')
            
            
    def take_over(self):
        print('[Terminal sim] voce assumiu o terminal ...')
        print('[Terminal sim] aperte "q" para sair...')
        
        while True:    
            entrada = input('Escreva <<< ')
            
            if entrada == 'q':
                break
            print(entrada)