_avl_listers = { }

def register(name, classobj):
    _avl_listers[name] = classobj

def get_available_lister_names():
    return _avl_listers.keys()

def get_lister(name):
    return _avl_listers[name]
