from joblib import Memory

cachedir = './cache'

memory = Memory(cachedir, verbose=0)

@memory.cache
def model():
    pass

