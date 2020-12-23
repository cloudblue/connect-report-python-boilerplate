# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.


project_slug = '{{ cookiecutter.project_slug }}'
if hasattr(project_slug, 'isidentifier'):
    assert (
        project_slug.isidentifier()
    ), '`{}` project slug is not a valid Python identifier.'.format(project_slug)

assert (
    project_slug == project_slug.lower()
), '`{}` project slug should be all lowercase'.format(project_slug)
