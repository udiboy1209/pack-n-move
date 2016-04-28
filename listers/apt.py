import os, subprocess
from subprocess import PIPE
import listers

from .util import register as register, restrict_width
from .package import PackageLister


class AptLister(PackageLister):
    APT_INSTALL = 'sudo apt-get install '
    CMD_APT_LIST = ['apt-mark', 'showmanual']
    CMD_INIT_PKG_LIST = ['gzip', '-dc', '/var/log/installer/initial-status.gz']

    def run(self):
        proc_apt_list = subprocess.Popen(self.CMD_APT_LIST, stdout=PIPE)
        proc_init_pkg_list = subprocess.Popen(self.CMD_INIT_PKG_LIST, stdout=PIPE)

        apt_list = proc_apt_list.communicate()[0].split('\n')
        init_pkg_list = proc_init_pkg_list.communicate()[0].split('\n')
        init_pkg_list = [x[9:] for x in init_pkg_list if x[:7] == 'Package']

        self.pkg_list = [x for x in apt_list if x not in init_pkg_list]

        return True

    def get_install_sh(self, pkg_list):
        return restrict_width("sudo apt-get install", pkg_list)

register('apt',AptLister)
