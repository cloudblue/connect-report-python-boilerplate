# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#

import os

from {{ cookiecutter.package_name }}.{{ cookiecutter.project_slug }} import {{cookiecutter.project_name|title|replace(" ", "")}}


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

def test_get_dataset(progress, client_factory, response_factory):
    """
    Test dataset generation.
    To mock http calls, you must create the list of responses
    for each client call.

    Ex:
    ```

    responses = []
    # create a response for a count call
    
    responses.append(response_factory(count=100))

    # create response for a collection

    responses.append(response_factory(value=[
        {
            'id': 'OBJ-001',
            ....
        },
        {
            'id': 'OBJ-002',
            ....
        },        
    ]))

    # create a response that raises an Exception

    responses.append(response_factory(exception=Exception('my_exception')))

    # create a response that returns a http 404

    responses.append(response_factory(status=404))

    # create a response and pass an RQL query to check that it match

    responses.append(response_factory(
        query='in(status,(approved,rejected))',
        value=[],
    ))

    # create a client instance

    client = client_factory(responses)

    :param progress: MagicMock to use as progress_callback
    :type mocker: MagicMock
    :param client_factory: Function that returns an instance of ConnectClient
    :type client_factory: func
    :param response_factory: Function that creates ConnectClient reponses.
    :type response_factory: func
    """
    pass