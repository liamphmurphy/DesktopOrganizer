import os, sys
from os.path import expanduser

#os.mkdir(home+"/Test",mode=0o777)

class Directories:

    def __init__(self):
        self.user_desktop = expanduser("~/Desktop")
        self.all_directories = ['/Documents',
                '/Pictures',
                '/Code',
                '/Music',
                '/Videos']

    def create_directories(self):
        for directory in self.all_directories:
            os.mkdir(self.user_desktop+directory, mode=0o777)

    # For now, this is for testing purposes: quickly remove dirs so we don't have to manually do it every time.
    def remove_directories(self):
        for directory in self.all_directories:
            os.rmdir(self.user_desktop+directory)
