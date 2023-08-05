from __future__ import print_function

import os
import sys

if __name__ == "__main__":
    print(sys.version_info)
    for line in open('data.txt'):
        print(line, end='')
