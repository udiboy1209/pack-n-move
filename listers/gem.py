import os, subprocess
from subprocess import PIPE
import listers

from .util import register as register, restrict_width
from .package import PackageLister


class GemLister(PackageLister):
    PRIORITY = 1
    GEM_INSTALL = 'sudo gem install '
    CMD_GEM_LIST = ['gem', 'query']

    def run(self):
        proc_gem_list = subprocess.Popen(self.CMD_GEM_LIST, stdout=PIPE)

        gem_list = proc_gem_list.communicate()[0].split('\n')
        self.pkg_list = [x.split(' ')[0] for x in gem_list]

        return True

    def get_install_sh(self, pkg_list):
        return restrict_width(self.GEM_INSTALL, pkg_list)

register('gem',GemLister)
