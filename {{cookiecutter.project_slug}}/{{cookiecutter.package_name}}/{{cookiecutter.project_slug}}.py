# -*- coding: utf-8 -*-
#
# Copyright (c) {% now 'utc', '%Y' %}, {{ cookiecutter.author }}
# All rights reserved.
#
from cnct import R

class {{cookiecutter.project_name|title|replace(" ", "")}}:
    def get_start_row(self):
        """
        Return the index (1-based) of the row
        where the report should start to be populated.

        :return: Start row of the report.
        :rtype: int
        """
        return 2
    
    def get_start_col(self):
        """
        Return the index (1-based) of the column
        where the report should start to be populated.

        :return: Start row of the report.
        :rtype: int
        """
        return 1
    
    def get_template_file(self):
        """
        Return the path to the Excel template file
        relative to the root of the project.

        :return: Path to the Excel template file.
        :rtype: str
        """
        return 'templates/template.xlsx'

    def get_dataset(self, client, parameters, progress_callback):
        """
        Extracts data from Connect using the ConnectClient instance
        and input parameters provided as arguments, applies
        required transformations (if any) and returns an iterator of rows
        that will be used to fill the Excel file.
        Each element returned by the iterator must be an iterator over
        the columns value.

        :param client: An instance of the CloudBlue Connect
                       client.
        :type client: cnct.ConnectClient
        :param parameters: Input parameters used to calculate the
                           resulting dataset.
        :type parameters: dict
        :param progress_callback: A function that accepts t
                                  argument of type int that must
                                  be invoked to notify the progress
                                  of the report generation.
        :type progress_callback: func
        """
        pass