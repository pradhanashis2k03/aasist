"""
AASIST
Copyright (c) 2021-present NAVER Corp.
MIT license
"""

import os

if __name__ == "__main__":
    cmd = "curl -o /content/gdrive/MyDrive/hoho/LA.zip -# https://datashare.ed.ac.uk/bitstream/handle/10283/3336/LA.zip\?sequence\=3\&isAllowed\=y"
    os.system(cmd)
    cmd = "unzip /content/gdrive/MyDrive/hoho/LA.zip"
    os.system(cmd)
