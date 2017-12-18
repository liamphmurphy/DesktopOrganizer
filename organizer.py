import os, sys, shutil
from os.path import expanduser, splitext
from collections import defaultdict
import settings

#os.mkdir(home+"/Test",mode=0o777)

class Directories:

    def create_directories(user_desktop):
        #settings.file_extensions.items() = defaultdict(list)
        for folder, extensions in settings.file_extensions.items():
            os.mkdir(user_desktop+"/"+folder, mode=0o777)
            print("\nDirectories successfully added to your desktop.")
        for folder, extensions in settings.file_extensions.items():
            os.chdir(user_desktop)
            extensions = str(extensions)
            file_path = (folder+"/"+extensions)
            shutil.move(extensions, file_path)
            

    # For now, this is for testing purposes: quickly remove dirs so we don't have to manually do it every time.
    def remove_directories(user_desktop):
        for folder, extensions in settings.file_extensions.items():
            os.rmdir(user_desktop+"/"+folder)

def main():
    main_program = Directories()
    user_desktop = expanduser("~/Desktop")
    Directories.create_directories(user_desktop)

if __name__ == "__main__":
    main()
    