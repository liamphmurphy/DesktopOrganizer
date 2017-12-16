import os, sys
from os.path import expanduser

#os.mkdir(home+"/Test",mode=0o777)

class Directories:
    def create_directories():
        all_directories = ['/Documents',
                '/Pictures',
                '/Code',
                '/Music',
                '/Videos']
        for directory in all_directories:
            user_desktop = expanduser("~/Desktop")
            os.mkdir(user_desktop+directory, mode=0o777)
