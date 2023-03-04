import os
import shutil

path= 'G:\\My Drive\\My Documents\\Misc\\test.txt'

try:
    os.remove(path)
    #os.rmdir(path) for folder deletion
    #sutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission :P")
except OSError:
    print("Can't delete using that function")
else:
    print(path+" was deleted")