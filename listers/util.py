_avl_listers = { }

def register(name, classobj):
    _avl_listers[name] = classobj

def get_available_lister_names():
    return sorted(_avl_listers, key=lambda k: _avl_listers[k].PRIORITY)

def get_lister(name):
    return _avl_listers[name]

def restrict_width(command, args):
    lines = []

    line = [command]
    line_len = len(command)

    for arg in args:
        if line_len + len(arg) + 1 < 80:
            line.append(arg)
            line_len += len(arg) + 1
        else:
            lines.append(' '.join(line))
            line_len = len(arg) + 1
            line = [arg]

    return ' \\\n'.join(lines) + '\n\n'
