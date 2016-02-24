__author__ = 'rdarshan'

import subprocess
import re
import os


def get_staged_files():
    """
    get all staged files for next commit
    """
    proc = subprocess.Popen(('git', 'status', '--porcelain'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    staged_files = [matched_group[1] for matched_group in re.findall(r'^([AM]|MM)\s+(.*\.js)', out, re.MULTILINE)]
    return staged_files

def scan_for_jshint_errors(staged_files):
    """
    validates staged js file's for jshint errors
    """
    jshint_report = ""
    for each_staged_files in staged_files:
            proc1 = subprocess.Popen(
                ('jshint', os.path.abspath(each_staged_files)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            jshint_report += proc1.communicate()[0]

    if jshint_report:
        print '\033[95m' + "***** warnings staged files contains jshint errors *****\n" + '\033[0m'
        print jshint_report

if __name__ == '__main__':
    scan_for_jshint_errors(get_staged_files())