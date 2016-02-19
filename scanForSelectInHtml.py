__author__ = 'rdarshan'

"""
usage: python scanForSelectInHtml.py jiva.prvportal (scans single repo)
       python scanForSelectInHtml.py jiva.prvportal jiva.mbrportal (scans multiple repo)
       python scanForSelectInHtml.py (scans src/* )
output:
        search for select tag under given repo's, and list in report
"""
import glob
import os
import sys
import report_config
from bs4 import BeautifulSoup


def check_any_dir_exist(html_occurence):
    html_container = []
    for each_path in html_occurence:
        if os.path.isdir(each_path):
            html_container.extend([os.path.join(each_path, each) for each in os.listdir(each_path)])
        else:
            html_container.append(each_path)
    return html_container


def get_files_with_select_tag():
    components = sys.argv[1:] if sys.argv[1:] else glob.glob('*')
    report_body = ""
    for each_repo in components:
        component_flag = True
        try:
            html_list = check_any_dir_exist(glob.glob('./{0}/*/*/ui/src/*/partials/*'.format(each_repo)))
            for each_html in html_list:
                soup = BeautifulSoup(open(each_html).read(), 'html.parser')
                select_group = soup.findAll('select')
                if select_group:
                    select_group = ['<p>'+str(each_select)+'</p>' for each_select in select_group]
                    if component_flag:
                        report_body += report_config.report_repo_heading_header.format(each_repo, each_html,
                                                                                       len(select_group),
                                                                                       ''.join(map(str,
                                                                                                   select_group)).replace(
                                                                                           '<select', 'select'))
                    else:
                        report_body += report_config.report_repo_value_header.format(each_repo, each_html,
                                                                                     len(select_group),
                                                                                     ''.join(map(str,
                                                                                                 select_group)).replace(
                                                                                         '<select', 'select'))
                    component_flag = False

        except Exception as e:
            print e, each_repo

    with open("report.html", "w") as f:
        f.write(report_config.report_header + report_body + report_config.report_footer)

if __name__ == "__main__":
    get_files_with_select_tag()
