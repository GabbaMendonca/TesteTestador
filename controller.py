from command import Command
from settings import Settings


s = Settings()

c = Command()

c.set_user('gabba')
c.set_senha('123')
c.set_ip('10.10.10.10')

c.terminal_start()

c.terminal_start(False)

c.select_router_alcatel()

print(c.terminal_print())
c.command.telnet()
print(c.terminal_print())
c.command.version()
print(c.terminal_print())

