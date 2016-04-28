class PackageLister():
    DEFAULT_ENABLE = False
    pkg_list = []

    def get_pkg_list(self):
        return self.pkg_list

    def get_install_sh(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
