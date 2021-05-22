import random

# ruleid: random
random.random()

# ruleid: random
random.randbytes()

# ok: random
r = random.SystemRandom()

# ok: random
r.randbytes()

# ruleid: random
r = random.Random()

# ruleid: random
r.randbytes()
