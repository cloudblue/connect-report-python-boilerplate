# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#


class {{cookiecutter.project_slug|title}}:
    def get_start_row(self):
        """
        [summary]

        :return: [description]
        :rtype: [type]
        """
        return 2
    
    def get_start_col(self):
        """
        [summary]

        :return: [description]
        :rtype: [type]
        """
        return 1
        
    def get_template_file(self):
        """
        [summary]

        :return: [description]
        :rtype: [type]
        """
        return 'templates/template.xlsx'

    def get_progress_value_max(self):
        """
        [summary]

        :return: [description]
        :rtype: [type]
        """
        return 100

    def get_dataset(self, client, parameters, progress_callback):
        """
        [summary]

        :param client: [description]
        :type client: [type]
        :param parameters: [description]
        :type parameters: [type]
        :param progress_callback: [description]
        :type progress_callback: [type]
        """
        pass