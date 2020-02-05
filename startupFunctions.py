#####################################################
#                 startupFuntions.py                #
#     made by Iván Montalvo & Santiago Buitrago     #
#                                                   #
# The idea behind this definitions is to initialize #
# and clean the folders that we need for the        #
# programm execution                                #
#                                                   #
#####################################################


import os
import shutil


def remove_contents(path):
    # Given a path, it'll clean the folder.
    # This will keep the process clean and
    # won't overwrite files.
    for c in os.listdir(path):
        full_path = os.path.join(path, c)
        if os.path.isfile(full_path):
            os.remove(full_path)
        else:
            shutil.rmtree(full_path)


def createFolder(path):
    # Given a path, it'll create the given
    # folders.
    try:
        os.mkdir(path)
    except OSError:
        print("Can't make folder or already created.")


def startFolders():
    # Whole creation of basic folders that
    # will be needed for the process and
    # analysis.
    createFolder('Lines')
    createFolder('Word')
    createFolder('Rotation')
    createFolder('Section')
    createFolder('Character')


def removeInnerFolders(path):
    # Here we remove the subfolders
    # inside a given folder.
    for folder in os.listdir(path):
        contents = len(os.listdir(path + folder))
        if contents == 0:
            os.rmdir(path + folder)

## END
