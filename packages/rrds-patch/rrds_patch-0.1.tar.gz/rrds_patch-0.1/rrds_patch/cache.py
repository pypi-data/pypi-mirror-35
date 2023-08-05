import os,cPickle

global Dir, cache

Dir = os.getcwd()
if "\\" in Dir:
    cache = Dir+"\\rigo.cache"
else:
    cache = Dir+"/rigo.cache"

def read_cache():
    p = open(cache,"rb+")
    data = cPickle.loads(p.read())
    p.close()
    return data

def update_cache(update):
    p = open(cache,"wb+")
    p.write(cPickle.dumps(update))
    p.close()

try:
    read_cache()
except:
    update_cache({})
