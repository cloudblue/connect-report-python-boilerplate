# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#

from {{cookiecutter.package_name}}.{{cookiecutter.initial_report_slug}}.entrypoint import generate


def test_{{cookiecutter.initial_report_slug}}(progress, client_factory, response_factory):
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

    # create a response and pass an RQL query, ordering and select
    # to check that it match

    responses.append(response_factory(
        query='in(status,(approved,rejected))',
        ordering=['-created'],
        select=['asset'],
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
