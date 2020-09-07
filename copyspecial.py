#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """Manuel Velasco,
        Gabby,
        'https://stackoverflow.com/questions/24705679/misunderstanding-of-python-os-path-abspath'
        """

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    list_dir = []
    for item in os.listdir(dirname):
        if re.findall(r'__(\w+)__', item):
            list_dir.append(os.path.abspath(os.path.join(dirname, item)))

    return list_dir


def copy_to(path_list, dest_dir):
    """ copying file given directory, creating the directory if necessary"""

    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for item in path_list:
        shutil.copy(item, dest_dir)


def zip_to(path_list, dest_zip):
    """ using list zip and extent Use the subprocess library to launch zip """
    list_zip = ['zip', '-j', dest_zip]
    list_zip.extend(path_list)
    subprocess.run(list_zip)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    special_list = get_special_paths(ns.fromdir)
    print('\n'.join(special_list))

    # copy_list = copy_to(ns.tozip)
    if ns.todir is not None:
        copy_to(special_list, ns.todir)

    if ns.tozip is not None:
        zip_to(special_list, ns.tozip)
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python copyspecial.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
