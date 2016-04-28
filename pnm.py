#!/usr/bin/env python

from os import getcwd
import argparse
from datetime import date

from listers import *
from listers.util import *

CWD = getcwd()

SEPARATOR_COMMENT = "##################\n"
HEADER_COMMENT = "Pack and Move Install script generated on {date:s}\n"
LISTER_COMMENT = "Lister: {name:s}. List of packages included:\n"

def column_format(pkg_list):
    col_width = max(len(word) for word in pkg_list) + 2
    rows = []

    for i in range((len(pkg_list)-1)/3 + 1):
        rows.append("".join(word.ljust(col_width) for word in pkg_list[i*3:i*3+3]) + "\n")

    return rows

def print_comment_block(f, *largs):
    f.write(SEPARATOR_COMMENT)
    for arg in largs:
        f.write("# "+ arg)
    f.write(SEPARATOR_COMMENT)
    f.write('\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("outfile", help="path to output file")

    args = parser.parse_args()

    with open(CWD + '/' + args.outfile, 'w') as outfile:
        avl_listers = get_available_lister_names()

        print_comment_block(outfile, HEADER_COMMENT.format(date=str(date.today())))

        for ls in avl_listers:
            ls_instance = get_lister(ls)()
            ls_instance.run()

            pkg_list = ls_instance.get_pkg_list()
            pkg_list_comment = column_format(pkg_list)
            pkg_install_str = ls_instance.get_install_sh(pkg_list)

            print_comment_block(outfile, LISTER_COMMENT.format(name=ls), *pkg_list_comment)

            outfile.write(ls_instance.get_install_sh(pkg_list))

if __name__ == '__main__':
    main()
