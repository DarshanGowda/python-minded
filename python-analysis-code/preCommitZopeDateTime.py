#!/usr/bin/python
"""
Git hook to catch zopeDateTime imports before committing.

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
    staged_files = [matched_group[1] for matched_group in re.findall(r'^([AM]|MM)\s+(.*\.py)', out, re.MULTILINE)]
    return staged_files


def is_zope_datetime_used(staged_files):
    """
    validates staged file's for Zope DateTime, if used
    generates report
    """
    zope_datetime_report = ""

    for each_staged_files in staged_files:
            proc1 = subprocess.Popen(
                ('grep', '-Hn', 'DateTime', os.path.abspath(each_staged_files)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            zope_datetime_report += proc1.communicate()[0]

    if zope_datetime_report:
        print '\033[95m' + "***** Zope Datetime related imports used in staged files *****\n" + '\033[0m'
        print zope_datetime_report

    return

if __name__ == '__main__':
    is_zope_datetime_used(get_staged_files())
