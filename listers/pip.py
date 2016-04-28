import os, subprocess
from subprocess import PIPE
import listers

from .util import register as register, restrict_width
from .package import PackageLister


class PipLister(PackageLister):
    PIP_INSTALL = 'sudo pip install '
    CMD_PIP_LIST = ['pip', 'list']

    def run(self):
        proc_pip_list = subprocess.Popen(self.CMD_PIP_LIST, stdout=PIPE)

        pip_list = proc_pip_list.communicate()[0].split('\n')
        self.pkg_list = [x.split(' ')[0] for x in pip_list if x[:8] != 'Warning:']

        return True

    def get_install_sh(self, pkg_list):
        return restrict_width(self.PIP_INSTALL, pkg_list)

register('pip',PipLister)
