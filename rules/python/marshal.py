import marshal

# ruleid: marshal
marshal.dump(s)

# ruleid: marshal
marshal.dumps(s)

# ruleid: marshal
marshal.load(s)

# ruleid: marshal
marshal.loads(s)

import marshal as f
# ruleid: marshal
f.load(s)

from marshal import dump as g
# ruleid: marshal
g(s)
