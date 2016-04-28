class PackageLister():
    DEFAULT_ENABLE = False
    pkg_list = []

    def get_pkg_list(self):
        return self.pkg_list

    def get_install_sh(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

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

    return ' \\\n'.join(lines)
