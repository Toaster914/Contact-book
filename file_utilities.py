'''
Implements simplified versoins of readlines(), and writelines() functions.
'''

import os

def read_lines(file_path):
    '''
    Return a list of all the entries in the file with the new line
    char auto removed. If the file does not exist, a blank list is returned.
    Also, all numaric values will be converted to the appropriate type.
    '''

    entries = []
    if os.path.exists(file_path):
        file = open(file_path, "r")
        for entry in file:
            entry = entry.strip()
            if entry.isnumeric():
                entries.append(int(entry))
            elif is_float(entry):
                entries.append(float(entry))
            else:
                entries.append(entry)
        file.close()
    return entries

def write_lines(entries, file_path, mode="w"):
    '''
    Writes all entries in the list to a file such that each entry
    is on a sperate line. Mode can only be "w" or "a"
    '''

    file = open(file_path, mode)
    for entry in entries:
        file.write(str(entry) + "\n")
    file.close()

def is_float(value):
    '''
    Checks if a string is a float.
    '''

    try:
        float(value)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    file_path = "test.txt"

    #TESTING strings
    write_lines(["a", "b", "c", "d"], file_path)
    print(read_lines(file_path))

    #TESTING integers
    write_lines([1, 2, 3, 4], file_path)
    print(read_lines(file_path))

    #TESTING Floats
    write_lines([1.1, 2.2, 3.3, 4.4], file_path)
    print(read_lines(file_path))

    os.remove(file_path)
