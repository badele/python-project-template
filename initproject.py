#!/usr/bin/env python
# -*- coding: utf-8 -*-

__authors__ = 'Bruno Adelé <bruno@adele.im>'
__copyright__ = 'Copyright (C) 2013 Bruno Adelé'
__description__ = """A python template project """
__license__ = 'GPLv3'
__version__ = '1.0.0'

import os
import sys
import fileinput

PROJECT = {
    'PROJECTNAME': "",
    'COPYRIGHTDATE': "",
    'FIRSTRELEASE': "",
    'DESCRIPTION': "",
    'LICENSE': "",
    'VERSION': "",
    'AUTHOR': "",
    'EMAIL': "",
    'USERNAME': "",
}


def replaceVars(path, extensions):
    filelist = [os.path.join(dirpath, f)
                for dirpath, dirnames, files in os.walk(path)
                for f in files if f.endswith(extensions)]

    for fname in filelist:
        if not fname.endswith('initproject.py'):
            print (fname)
            for line in fileinput.FileInput(fname, inplace=1):
                for prj in PROJECT:
                    line = line.replace("{{%s}}" % prj, PROJECT[prj])
                sys.stdout.write(line)


if __name__ == '__main__':

    # Check if all vars is filled
    error = False
    for prj in PROJECT:
        if not PROJECT[prj]:
            print ("Please fill %s" % prj)
            error = True

    # Vars not filled
    if error:
        sys.exit(1)

    # Get this script directory
    path = os.path.dirname(os.path.realpath(__file__))

    # Replace all vars
    replaceVars(
        path,
        (
            '.txt',
            '.in',
            '.py',
            '.rc',
            '.rst',
            'Makefile',
        )
    )

    # Rename files
    os.rename(
        "%s/README_project.rst" % path,
        "%s/README.rst" % path
    )

    os.rename(
        "%s/project/project.py" % path,
        "%s/project/%s.py" % (path, PROJECT['PROJECTNAME'])
    )

    os.rename(
        "%s/project" % path,
        "%s/%s" % (path, PROJECT['PROJECTNAME'])
    )
