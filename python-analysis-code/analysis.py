import subprocess
import re
import os

CONFIG = {"Analysis_tool": "pep8"}


def get_staged_files():
    """
    get all staged files for next commit
    """
    proc = subprocess.Popen(('git', 'status', '--porcelain'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    staged_files = re.findall(r'^M{1,2}\s+(.*\.py)', out, re.MULTILINE)
    return staged_files


def validate_with_analysis_tools():
    """
    validates staged file with analysis tool and
    generates report
    """
    generated_report = ''
    staged_files = get_staged_files()
    for each_staged_files in staged_files:
        proc = subprocess.Popen([CONFIG['Analysis_tool'], os.path.abspath(each_staged_files)], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        report, _ = proc.communicate()
        generated_report += report

    if generated_report:
        print generated_report
        exit(1)

if __name__ == '__main__':
    validate_with_analysis_tools()
