# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.

import os
import shutil
from pathlib import Path

pkg_name = '{{ cookiecutter.package_slug }}'
report_slug = '{{ cookiecutter.initial_report_slug }}'


def selected_render():
    if '{{ cookiecutter.initial_report_renderer }}' == 'xlsx':
        template_dir = f'{pkg_name}/{report_slug}/templates/xlsx'
        os.makedirs(template_dir)
        Path(f'{template_dir}/template.xlsx').touch()

    elif '{{ cookiecutter.initial_report_renderer }}' == 'pdf':
        template_dir = f'{pkg_name}/{report_slug}/templates/pdf'
        os.makedirs(template_dir)
        Path(f'{template_dir}/template.css').touch()
        Path(f'{template_dir}/template.html.j2').touch()

    elif '{{ cookiecutter.initial_report_renderer }}' == 'jinja2':
        template_dir = f'{pkg_name}/{report_slug}/templates/j2'
        os.makedirs(template_dir)
        open(f'{template_dir}/template.ext.j2', 'w').write(
            'Please rename this file with a proper extension file.\n',
        )

def remove_github_actions():
    shutil.rmtree('.github')

def main():    
    if '{{ cookiecutter.use_github_actions }}'.lower() == 'n':
        remove_github_actions()

    selected_render()

    print('Done! Your report project is ready to go!')

if __name__ == '__main__':
    main()