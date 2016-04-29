import os, subprocess
from subprocess import PIPE
import listers

from .util import register as register, restrict_width
from .package import PackageLister


class NpmLister(PackageLister):
    PRIORITY = 1
    NPM_INSTALL = 'sudo npm install '
    CMD_NPM_LIST = ['npm', '-g', 'list', '--depth=0', '-parseable']

    def run(self):
        proc_npm_list = subprocess.Popen(self.CMD_NPM_LIST, stdout=PIPE)

        npm_list = proc_npm_list.communicate()[0].split('\n')
        self.pkg_list = [x.split('/')[-1] for x in npm_list[1:]]

        return True

    def get_install_sh(self, pkg_list):
        return restrict_width(self.NPM_INSTALL, pkg_list)

register('npm',NpmLister)
