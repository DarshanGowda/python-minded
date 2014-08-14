import subprocess
import re
import os

CONFIG = {"Analysis_tool1": "pep8",
          "Analysis_tool2": "pyflakes"}


def get_staged_files():
    """
    get all staged files for next commit
    """
    proc = subprocess.Popen(('git', 'status', '--porcelain'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, _ = proc.communicate()
    staged_files = re.findall(r'^[AM]\s+(.*\.py)', out, re.MULTILINE)
    return staged_files


def validate_with_analysis_tools():
    """
    validates staged file with analysis tool and
    generates report
    """
    pep_generated_report = ''
    pyflakes_generated_report = ''
    staged_files = get_staged_files()
    for each_staged_files in staged_files:
        proc1 = subprocess.Popen([CONFIG['Analysis_tool1'], os.path.abspath(each_staged_files)], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
        proc2 = subprocess.Popen([CONFIG['Analysis_tool2'], os.path.abspath(each_staged_files)], stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        pep_report, _ = proc1.communicate()
        pyflakes_report, _ = proc2.communicate()
        pep_generated_report += pep_report
        pyflakes_generated_report += pyflakes_report

    if pep_generated_report or pyflakes_generated_report:
        print "*"*20+"pep8 report start"+"*"*20+"\n"
        print pep_generated_report
        print "*"*20+"pep8 report end"+"*"*20+"\n"

        print "*"*20+"pyflakes report start"+"*"*20+"\n"
        print pyflakes_generated_report
        print "*"*20+"pyflakes report end"+"*"*20+"\n"
        exit(1)

if __name__ == '__main__':
    validate_with_analysis_tools()
