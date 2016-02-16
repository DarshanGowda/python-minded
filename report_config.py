__author__ = 'rdarshan'

report_header = """<html>
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

report_footer = """</tbody>
    </table>
</div>
</body>
</html>"""


report_repo_heading_header = """
<tr>
            <td class="repo">{0}</td>
            <td class="file">{1}</td>
            <td class="num">{2}</td>
            <td class="pattern">{3}</td>
        </tr>
"""
report_repo_value_header = """
<tr>
            <td></td>
            <td class="file">{1}</td>
            <td class="num">{2}</td>
            <td class="pattern">{3}</td>
        </tr>
"""
