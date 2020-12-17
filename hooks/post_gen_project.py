# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.

import os
import shutil
import string


def remove_license():
        os.remove('LICENSE')

def remove_github_actions():
    shutil.rmtree('.github')

def main():
    if '{{ cookiecutter.license }}' == 'Other, not Open-source':
        remove_license()
    
    if '{{ cookiecutter.use_github_actions }}'.lower() == 'n':
        remove_github_actions()


    print('Done! Your report project is ready to go!')

if __name__ == '__main__':
    main()