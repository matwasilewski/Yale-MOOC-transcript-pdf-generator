import sys
import os
import re


def create_notes_path(path_file):
    """Creates path to out
    PARAMETER: Path to in
    RETURNS: Path to output"""

    path_list = re.split('\.', path_file)
    path_list[0] = path_list[0] + '_transcript'
    path_notes = path_list[0] + '.tex'

    return path_notes
    

def prompt_user(path_notes):
    """Asks user to specify if they want to override file"""
    while True:
        user_choice = input(path_notes + \
        ' exists! Do you want to override it? y/n\n').lower()
        if user_choice == 'y':
            return True 
        elif user_choice == 'n':
            return False    

def create_notes(path_file, path_notes, title):
    """Main function"""

    # regex specifying what to look for
    regex = re.compile(r'(Chapter \d+\. )(.*)(\[\d\d:\d\d:\d\d])')
    
    # checks existance / nonexistance of in/out files
    if os.path.isfile(path_file):
        if (os.path.exists(path_notes) and prompt_user(path_notes)) \
        or not os.path.exists(path_notes):
            file_object_1 = open(path_file, mode='r')
            file_object_2 = open(path_notes, mode='w')
                
            # writes header at the beginning of a file
            write_header(title, file_object_2)
                
            # for every line in input file
            for line in file_object_1.readlines():
                # run function write_line, an extended writer checking if there's
                # a match and modifying line accordingly
                write_line(file_object_2, line, regex)

                # write tail at the end of a file
            write_tail(file_object_2)

            # close files
            file_object_1.close()
            file_object_2.close()
            print("Notes file written!")
        else:
            print("The output file does exist and was not overwritten")
    else:
        print("The input file does not exist!")

def write_line(file_object, line, regex):
    """Extended line writer, checking if a match is produced. Assumes that
    only second and third (index 1 and 2) groups are interesting, if regex was
    to be changed this group should be too
    RETURNS: None"""

    match_object = re.search(regex, line)
    
    # If match != None
    if match_object:
        output = r'\section{\large ' + match_object.group(1) + match_object.group(2) + '}\n'
    else:
        output = line
        
    file_object.write(output)

def write_header(title, file_object):
    """Write hardcoded header
    PARAMETERS: file object
    RETURN: None"""

    message = 'The lectures are available at https://oyc.yale.edu/english/engl-300. Those PDFs were generated using Yale\'s transcript, by Mateusz Wasilewski github.com//santiagonasar\n Code used to enerate them is available at ' 

    a = "\documentclass[12pt]{article}\n\\setcounter{secnumdepth}{0}\n\n\\begin{document}\n\n\\title{\n Introduction to Theory of Literature\\\ \n\\begin{large}" + title
    a = a + "\\end{large} }\n\n\\maketitle\n\n{\\large \\tableofcontents}\n\n"
    a = a + message + '\\pagebreak\n'

    file_object.write(a)

def write_tail(file_object):
    """Write hardcoded tail.
    PARAMETERS: file object
    RETURNS: None"""

    a = '\\end{document}'
    file_object.write(a)


def notesmaker(in_path, title):
    out_path = create_notes_path(in_path)
    create_notes(in_path, out_path, title)

filepath = sys.argv[1] 
title = sys.argv[2]

notesmaker(filepath, title)
