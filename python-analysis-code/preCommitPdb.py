#!/usr/bin/python
"""
Git hook to catch pdb issues before committing.

How it works?
copy file to '/usr/share/git-core/templates/hooks/' then,
it will automatically copy to .git/hooks whenever new repository is cloned.

How to use this hook independently?
just rename file name to pre-commit and make it executable
"""

__author__ = 'Darshan RK Gowda'

import subprocess
import re
import os
from sys import exit


def get_staged_files():
    """
    get all staged files for next commit
    """
    proc23 = subprocess.Popen('pwd', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print proc23.communicate()[0]
    proc = subprocess.Popen(('git', 'status', '--porcelain'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    staged_files = [matched_group[1] for matched_group in re.findall(r'^([AM]|MM)\s+(.*\.py)', out, re.MULTILINE)]
    return staged_files


def check_for_pdb_violations():
    """
    validates staged file's for pdb used, if used
    generates report
    """
    staged_files = get_staged_files()
    pdb_report = ""

    for each_staged_files in staged_files:
            proc1 = subprocess.Popen(
                ('grep', '-Hn', 'pdb', os.path.abspath(each_staged_files)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pdb_report += proc1.communicate()[0]

    if pdb_report:
        print '\033[95m' + "***** Commit failed due to pdb usage in staged files *****\n" + '\033[0m'
        print pdb_report
        exit(1)

if __name__ == '__main__':
    check_for_pdb_violations()
