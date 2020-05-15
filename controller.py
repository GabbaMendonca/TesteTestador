from command import Command
from dispatcher import generic


c = Command()

@generic
def dispatcher(event):
    print(f'Não encontrei o comando {event}')


@dispatcher.when(lambda event: 'terminal_start' == event['command'])
def terminal_start(event):
    if event['simulation']:
        c.terminal_start(event['user'], event['senha'], event['ip'])
    else:
        c.terminal_start(event['user'], event['senha'], event['ip'], False)
        

@dispatcher.when(lambda event: 'select_router_alcatel' == event['command'])
def select_router_alcatel(event):
    c.select_router_alcatel()


@dispatcher.when(lambda event: 'ra_telnet' == event['command'])
def router_alcatel_telnet(event):
    c.command.telnet()

    
@dispatcher.when(lambda event: 'ra_version' == event['command'])
def router_alcatel_version(event):
    c.command.version()

# print(c.terminal_print())

eventStart = {}

eventStart['command'] = 'terminal_start'
eventStart['simulation'] = False
eventStart['user'] = 'gabba'
eventStart['senha'] = '123'
eventStart['ip'] = '10.10.10.10'

dispatcher(eventStart)

event = {}

event['command'] = 'select_router_alcatel'
dispatcher(event)
event['command'] = 'ra_telnet'
dispatcher(event)
event['command'] = 'ra_version'
dispatcher(event)