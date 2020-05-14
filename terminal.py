class Terminal():    
    def start(self, ip_servidor, username, password):
        print('[terminal] startando ...')
        self.console = 'Aguardando ...'
        print(f'[terminal] IP servidor : {ip_servidor}')
        print(f'[terminal] Username    : {username}')
        print(f'[terminal] Password    : {password}')
        
        print('[terminal] UP ...')


    def start_simulation(self, ip_servidor, username, password):
        print('[terminal sim] startando ...')
        self.console = 'Aguardando ...'
        print(f'[terminal sim] IP servidor : {ip_servidor}')
        print(f'[terminal sim] Username    : {username}')
        print(f'[terminal sim] Password    : {password}')
        
        print('[terminal sim] UP ...')
        
    def stop(self):
        print('[terminal sim] Stopping ...')
        print('[terminal sim] DOWM ...')
            
            
    def take_over(self):
        print('[terminal sim] voce assumiu o terminal ...')
        print('[terminal sim] aperte "q" para sair...')
        
        while True:    
            entrada = input('Escreva <<< ')
            
            if entrada == 'q':
                break
            print(entrada)