import os

# ruleid: os-command-injection
os.system(user_input)

# ruleid: os-command-injection
os.popen(user_input)

# ruleid: os-command-injection
os.popen2(user_input)

# ruleid: os-command-injection
os.popen3(user_input)

# ruleid: os-command-injection
os.popen4(user_input)

# ok: os-command-injection
os.system("ls")

# ok: os-command-injection
os.popen("ls")

# ok: os-command-injection
os.popen2("ls")

# ok: os-command-injection
os.popen3("ls")

# ok: os-command-injection
os.popen4("ls")

import os as f
# ruleid: os-command-injection
f.system(user_input)

from os import system as g
# ruleid: os-command-injection
g(user_input)
