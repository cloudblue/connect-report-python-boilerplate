# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#

import os

from {{ cookiecutter.package_name }}.report import {{cookiecutter.project_name|title|replace(" ", "")}}


def test_get_start_row():
    report = {{cookiecutter.project_name|title|replace(" ", "")}}()
    assert report.get_start_row() == 2


def test_get_start_col():
    report = {{cookiecutter.project_name|title|replace(" ", "")}}()
    assert report.get_start_col() == 1


def test_get_template_file():
    report = {{cookiecutter.project_name|title|replace(" ", "")}}()
    template_file = report.get_template_file()
    assert template_file is not None
    assert isinstance(template_file, str)
    assert template_file.startswith(os.sep) is False
    assert template_file.lower().endswith('.xlsx') is True
    assert report.get_template_file() == 'templates/template.xlsx'


def test_get_progress_value_max():
    report = {{cookiecutter.project_name|title|replace(" ", "")}}()
    assert report.get_progress_value_max() == 100