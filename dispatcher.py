class generic:
    def __init__(self, default):
        self.funcs = []
        self.default = default

    def when(self, pred):
        def add(func):
            self.funcs.append( (pred, func) )
            return func
        return add

    def __call__(self, *args, **kwargs):
        for pred, func in self.funcs:
            try:
                match = pred(*args, **kwargs)
            except Exception:
                match = False
            if match:
                return func(*args, **kwargs)
        return self.default(*args, **kwargs)
    
    
    
@generic
def paul(evento):
    print(f'{evento}')


@paul.when(lambda evento: evento['cor'] == 'amarelo')
def amarelo(evento):
    print(evento)


@paul.when(lambda evento: evento == 'amarelo')
def amarelo2(evento):
    print(evento)

@paul.when(lambda evento: evento == 'verde')
def verde(evento):
    print(evento)


# @paul.when(lambda evento: 'amarelo' in evento['msg'])
# def amarelo(evento):
#     print(evento)
    
    
"""
Exemplo de dispatcher da live do Eduardo.
Passa um dicionario para o paul e ele seleciona
e passa o evento para a função.

python -i dispatcher.py

paul({'cor' : 'amarelo'})
{'cor': 'amarelo'}

Mesmo exemplo porem com uma string.

python -i dispatcher.py

paul({'cor' : 'amarelo'})
{'cor': 'amarelo'}

paul('amarelo')
amarelo
 
paul('verde')
verde

"""