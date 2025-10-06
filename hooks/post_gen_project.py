# -*- coding: utf-8 -*-

# This file is part of the CloudBlue Connect Report Python Boilerplate.
# Copyright (c) 2025 CloudBlue. All Rights Reserved.

import os
import shutil
from pathlib import Path

import openpyxl


def create_renderer_templates():
    pkg_slug = '{{ cookiecutter.package_slug }}'
    report_slug = '{{ cookiecutter.initial_report_slug }}'

    # XLSX
    xlsx_template_dir = f'{pkg_slug}/{report_slug}/templates/xlsx'
    os.makedirs(xlsx_template_dir)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Data"
    wb.save(f'{xlsx_template_dir}/template.xlsx')

    # PDF
    pdf_template_dir = f'{pkg_slug}/{report_slug}/templates/pdf'
    os.makedirs(pdf_template_dir)
    Path(f'{pdf_template_dir}/template.css').touch()
    Path(f'{pdf_template_dir}/template.html.j2').touch()

    # JINJA2
    jinja2_template_dir = f'{pkg_slug}/{report_slug}/templates/xml'
    os.makedirs(jinja2_template_dir)
    open(f'{jinja2_template_dir}/template.xml.j2', 'w').write(
        'Please rename this file with a proper extension file.\n',
    )

def remove_github_actions():
    shutil.rmtree('.github')

def main():    
    if '{{ cookiecutter.use_github_actions }}'.lower() == 'n':
        remove_github_actions()

    create_renderer_templates()

    print('Done! Your report project is ready to go!')

if __name__ == '__main__':
    main()
