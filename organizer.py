import os, sys
from os.path import expanduser

#os.mkdir(home+"/Test",mode=0o777)

class Directories:

    def __init__(self):
        self.user_desktop = expanduser("~/Desktop")
        print(self.user_desktop)
        self.all_directories = ['/Documents',
                '/Pictures',
                '/Code',
                '/Music',
                '/Videos']

    def create_directories(self):
        for directory in self.all_directories:
            os.mkdir(self.user_desktop+directory, mode=0o777)
            print("\nDirectories successfully added to your desktop.")

    # For now, this is for testing purposes: quickly remove dirs so we don't have to manually do it every time.
    def remove_directories(self):
        for directory in self.all_directories:
            os.rmdir(self.user_desktop+directory)

class Program:

    def getcmd(self,cmdlist):
        cmd = input("Press 1 to create directories, or 2 to remove previous directories: (Warning, you may lose data in these folders)")
        if cmd in cmdlist:
            return cmd

def main():
    cmdlist = ['1','2']
    command = Program()
    command.getcmd(cmdlist)
    cmd = command.getcmd(cmdlist)

    main_program = Directories()

    if cmd == '1':
        main_program.create_directories()
    if cmd == '2':
        main_program.remove_directories()
            

if __name__ == "__main__":
    main()
    