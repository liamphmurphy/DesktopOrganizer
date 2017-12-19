import os, sys, shutil
from os.path import expanduser, splitext
import settings
from collections import defaultdict

#print(settings.file_extensions.items())
#for directory, extensions in settings.file_extensions.items():
#    print(directory, extensions)

class Directories:

    def create_directories(user_desktop, files):
        #path_extensions = defaultdict(list)
        for directory, extensions in settings.file_extensions.items():
            print(directory)
            directory_path = user_desktop+"/"+directory
            os.mkdir(directory_path, mode=0o777)
            print("\nDirectories successfully added to your desktop.")


        for file in files:
            file_path = directory_path + "/" + file
            print(files)
            print(file_path)
            shutil.move(user_desktop + "/" + file, directory_path)

            
    # For now, this is for testing purposes: quickly remove dirs so we don't have to manually do it every time.
    def remove_directories(user_desktop):
        for directory in settings.file_extensions.keys():
            try:
                os.rmdir(user_desktop+"/"+directory)
            except:
                pass

def main():
    main_program = Directories()
    user_desktop = expanduser("~/Desktop")
    files = [f for f in os.listdir(user_desktop) if os.path.isfile(os.path.join(user_desktop, f))]
    Directories.create_directories(user_desktop,files)

if __name__ == "__main__":
    main()
    