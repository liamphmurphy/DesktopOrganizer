from organizer import Directories
from os.path import expanduser

user_desktop= expanduser("~/Desktop")
Directories.remove_directories(user_desktop)