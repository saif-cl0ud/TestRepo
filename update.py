#!/bin/env python

import sys
import os
from subprocess import check_output


def tags():
    return [i.lstrip(' *') for i in check_output(["git", "branch"]).split('\n') if i!='']


def main():
    branch_id = sys.argv[1]

    # Only ref/heads are being processed
    if branch_id.startswith('refs/heads/'):
        if not branch_id.lstrip('refs/heads/') in tags():
            exit(1)

if __name__ == '__main__':
    main()