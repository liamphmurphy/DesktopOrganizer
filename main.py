from organizer import Directories

def getcmd(cmdlist):
    cmd = input("Enter your choice: ")
    if cmd in cmdlist:
        return cmd

print("Would you like to create or remove previously made directories?")
print("\n1: Create directories\n2: Remove Directories")

cmdlist = ['1','2']
cmd = getcmd(cmdlist)

if cmd == '1':
    User = Directories()

if cmd == '2':
    User = Directories.main()

