#! /usr/bin/env python3
import os


def walkFolder(folder_root, name_delete):
    print('Traversing folder is %s and deleting %s' % (folder_root, name_delete))

    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(folder_root):
        to_delete = os.path.join(root, name_delete)
        
        deleted = False
        if os.path.isfile(to_delete):
            os.remove(to_delete)
            deleted = True
        elif os.path.isdir(to_delete):
            os.removedirs(to_delete)
            deleted = True

        if deleted:
            print('Deleted %s' % to_delete)



if __name__ == '__main__':
    name_delete = input('Which folder(s) name to delete: ')
    folder = os.getcwd()
    walkFolder(folder, name_delete)
