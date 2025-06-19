# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2025 CloudBlue. All Rights Reserved.


project_slug = '{{ cookiecutter.project_slug }}'
if hasattr(project_slug, 'isidentifier'):
    assert (
        project_slug.isidentifier()
    ), '`{}` project slug is not a valid Python identifier.'.format(project_slug)

assert (
    project_slug == project_slug.lower()
), '`{}` project slug should be all lowercase'.format(project_slug)


package_slug = '{{ cookiecutter.package_slug }}'
if hasattr(package_slug, 'isidentifier'):
    assert (
        package_slug.isidentifier()
    ), '`{}` package slug is not a valid Python identifier.'.format(package_slug)

assert (
    package_slug == package_slug.lower()
), '`{}` package slug should be all lowercase'.format(package_slug)


initial_report_slug = '{{ cookiecutter.initial_report_slug }}'
if hasattr(initial_report_slug, 'isidentifier'):
    assert (
        initial_report_slug.isidentifier()
    ), '`{}` report slug is not a valid Python identifier.'.format(initial_report_slug)

assert (
    initial_report_slug == initial_report_slug.lower()
), '`{}` report slug should be all lowercase'.format(initial_report_slug)

