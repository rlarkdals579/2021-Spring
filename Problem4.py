# Name : Kangmin Kim
# NetID KangKim
# SBUID : 111329652

import re

class FS_Item:
    def __init__(self, __name):
        self.name = __name


class Folder(FS_Item):

    def __init__(self, __name):
        self.items = []
        self.name = __name

    def add_item(self, item):
        self.items.append(item)


class File(FS_Item):
    def __init__(self, __name, __size):
        self.size = __size
        self.name = __name


def load_fs(ls_output):

    root_folder = Folder('.')

    with open(ls_output, 'r') as file:

        while True:

            # folder name
            folder_name = file.readline()
            if not folder_name:
                break
            else:

                # find corresponding folder
                current_folder = root_folder
                hierarchy = (folder_name[:-2].split('/'))[1:]

                for name in hierarchy:
                    for item in current_folder.items:
                        if type(item) is Folder and item.name == name:
                            current_folder = item

            # total number of files
            total_files = file.readline()

            # read items one by one
            while True:
                line = file.readline()

                # exit on blank line
                if len(line) < 10:
                    break

                # get file info
                pattern = re.compile("([-d])(([-r][-w][-x]){3})(( +[^ ]+){3}) +([0-9]+)(( +[^ ]+){3} )(.+)")
                match = pattern.search(line)
                directory_flag = match.group(1)
                file_size = int(match.group(6))
                file_name = match.group(9)

                if directory_flag == '-':
                    file_obj = File(file_name, file_size)
                else:
                    file_obj = Folder(file_name)

                current_folder.add_item(file_obj)

    return root_folder

def print_fs(fs_object, depth): # funcition that can visualize the result of the sample file in console part

    print(depth * '\t' + f"Folder {fs_object.name}")
    depth += 1

    for obj in fs_object.items:
        if type(obj) is File:
            print(depth * '\t' + f"File {obj.name}")
        if type(obj) is Folder:
            print_fs(obj, depth)

obj = load_fs("p4_case02.txt") # match the txt file name that located in the same file
print_fs(obj, 0)