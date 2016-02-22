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

try:
    # to be in compatible with jiva buildout python
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


class ReportGenerator():
    """
    ReportGenerator class can be used to generate basic report with its class attributes
    """
    def __init__(self):
        self.report_header = """<html>
        <head>
            <title>Select Tag Report</title>
            <style type="text/css">body {
                font-family: Arial, sans-serif;
                margin: 20px 20px 20px 30px;
                }

                .repo {
                font-weight: bold;
                }

                .tableHeader {
                font-weight: bold;
                }

                .file {
                text-align: left;
                }

                .num {
                text-align: center;
                }

                .pattern {
                font-weight: bold;
                text-align: center;
                color: #990000;
                background-color: #FFAAAA;
                }

                table {
                border: 2px solid gray;
                border-collapse: collapse;

                -moz-box-shadow: 3px 3px 4px #AAA;
                -webkit-box-shadow: 3px 3px 4px #AAA;
                box-shadow: 3px 3px 4px #AAA;
                }

                td, th {
                border: 1px solid #D3D3D3;
                padding: 4px 15px 4px 15px;
                margin: 20px 15px 20px 15px;
                }

                th {
                text-shadow: 2px 2px 2px white;
                }

                th {
                border-bottom: 1px solid gray;
                background-color: #DDDDFF;
                }
            </style>
        </head>
        <body>
        <body>
        <div>
            <h2>Select Tag Scan Report</h2>
            <table>
                <tbody>
                <tr class="tableHeader">
                    <th>Module</th>
                    <th>File Name</th>
                    <th>Count Of Select Identified</th>
                    <th>Patterns Found</th>
                </tr>
        """

        self.report_footer = """</tbody>
            </table>
        </div>
        </body>
        </html>"""

        self.report_repo_heading_header = """
        <tr>
                    <td class="repo">{0}</td>
                    <td class="file">{1}</td>
                    <td class="num">{2}</td>
                    <td class="pattern">{3}</td>
                </tr>
        """

        self.report_repo_value_header = """
        <tr>
                    <td></td>
                    <td class="file">{1}</td>
                    <td class="num">{2}</td>
                    <td class="pattern">{3}</td>
                </tr>
        """


def check_any_dir_exist(html_occurence):
    """checks if a path is a dir, then expands it to files level(only one level)"""
    html_container = []
    for each_path in html_occurence:
        if os.path.isdir(each_path):
            html_container.extend([os.path.join(each_path, each) for each in os.listdir(each_path)])
        else:
            html_container.append(each_path)
    return html_container


def get_files_with_select_tag():
    """scans for htmls under components and generates report"""
    components = sys.argv[1:] if sys.argv[1:] else glob.glob('*')
    report_body = ""
    report_gen = ReportGenerator()
    for each_repo in components:
        component_flag = True
        try:
            html_list = check_any_dir_exist(glob.glob('./{0}/*/*/ui/src/*/partials/*'.format(each_repo)))
            for each_html in html_list:
                soup = BeautifulSoup(open(each_html).read())
                select_group = soup.findAll('select')
                if select_group:
                    select_group = ['<p>'+str(each_select)+'</p>' for each_select in select_group]
                    if component_flag:
                        report_body += report_gen.report_repo_heading_header.format(each_repo, each_html,
                                                                                    len(select_group),
                                                                                    ''.join(select_group).replace(
                                                                                        '<select', 'select'))
                    else:
                        report_body += report_gen.report_repo_value_header.format(each_repo, each_html,
                                                                                  len(select_group),
                                                                                  ''.join(select_group).replace(
                                                                                      '<select', 'select'))
                    component_flag = False

        except Exception as e:
            print e, each_repo

    with open("report.html", "w") as f:
        f.write(report_gen.report_header + report_body + report_gen.report_footer)

if __name__ == "__main__":
    get_files_with_select_tag()
