import sys
import os
import re


def create_notes_path(path_file):
    path_list = re.split('\.', path_file)
    path_list[0] = path_list[0] + '_transcript'
    path_notes = '.'.join(path_list)
    return path_notes
    
def create_notes(path_file, path_notes):
    if os.path.isfile(path_file) and not os.path.exists(path_notes):
        f1 = open(path_file, mode='r')
        f2 = open(path_notes, mode='w')

        for line in f1.readlines():
            f2.write(line)

        f1.close()
        f2.close()
    else:
        print("A problem occured!")


def replace_chapter():


filepath = sys.argv[1] 
notespath = create_notes_path(filepath)
create_notes(filepath, notespath)
