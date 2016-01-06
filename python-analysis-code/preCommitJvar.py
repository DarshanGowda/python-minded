#!/usr/bin/python
"""
Git hook to catch jvar on select issues before committing.

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


def get_staged_files():
    """
    get all staged files for next commit
    """
    proc = subprocess.Popen(('git', 'status', '--porcelain'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    staged_files = [matched_group[1] for matched_group in re.findall(r'^([AM]|MM)\s+(.*\.html)', out, re.MULTILINE)]
    return staged_files


def is_select_need_tobe_jvar(staged_files):
    """
    validates staged file's for pdb used, if used
    generates report
    """
    j_var_report = ""
    for each_staged_files in staged_files:
            print each_staged_files
            proc1 = subprocess.Popen(
                ('pcregrep', '-M', '<select.*(\n|.)*?</select>', os.path.abspath(each_staged_files)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            j_var_report += proc1.communicate()[0]

    if j_var_report:
        print '\033[95m' + "***** warnings staged files contains non-jvar select statements *****\n" + '\033[0m'
        print j_var_report

    return
if __name__ == '__main__':
    is_select_need_tobe_jvar(get_staged_files())
