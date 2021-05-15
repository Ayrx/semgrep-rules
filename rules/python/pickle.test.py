import pickle, _pickle, cPickle, dill, shelve

# ruleid: pickle-pickle
pickle.dump(s)

# ruleid: pickle-pickle
pickle.dumps(s)

# ruleid: pickle-pickle
pickle.load(s)

# ruleid: pickle-pickle
pickle.loads(s)

import pickle as f
# ruleid: pickle-pickle
f.load(s)

from pickle import dump as g
# ruleid: pickle-pickle
g(s)

# ruleid: pickle-pickle
_pickle.dump(s)

# ruleid: pickle-pickle
_pickle.dumps(s)

# ruleid: pickle-pickle
_pickle.load(s)

# ruleid: pickle-pickle
_pickle.loads(s)

import _pickle as f
# ruleid: pickle-pickle
f.load(s)

from _pickle import dump as g
# ruleid: pickle-pickle
g(s)

# ruleid: pickle-pickle
cPickle.dump(s)

# ruleid: pickle-pickle
cPickle.dumps(s)

# ruleid: pickle-pickle
cPickle.load(s)

# ruleid: pickle-pickle
cPickle.loads(s)

import cPickle as f
# ruleid: pickle-pickle
f.load(s)

from cPickle import dump as g
# ruleid: pickle-pickle
g(s)

# ruleid: pickle-dill
dill.dump(s)

# ruleid: pickle-dill
dill.dumps(s)

# ruleid: pickle-dill
dill.load(s)

# ruleid: pickle-dill
dill.loads(s)

import dill as f
# ruleid: pickle-dill
f.load(s)

from dill import dump as g
# ruleid: pickle-dill
g(s)

# ruleid: pickle-shelve
shelve.open(s)

import shelve as f
# ruleid: pickle-shelve
f.open(s)

from shelve import open as g
# ruleid: pickle-shelve
g(s)
