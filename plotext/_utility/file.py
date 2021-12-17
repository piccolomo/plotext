from plotext._utility.data import transpose as _transpose
import inspect as _inspect
import sys as _sys
import os as _os

def parent_folder(path, level = 1): # it return the parent folder of the path or file given; if level is higher then 1 the process is iterated 
    if level <= 0:
        return path
    if level == 1:
        return _os.path.abspath(_os.path.join(path, _os.pardir))
    else:
        return parent_folder(parent_folder(path, level - 1))

def script_folder(): # the folder of the script executed
    return parent_folder(_inspect.getfile(_sys._getframe(1)))

def _correct_path(path):
    if _os.path.dirname(path) == '':
        path = _os.path.join(_os.path.expanduser("~"),_os.path.basename(path))
    elif path == "~":
        path = _os.path.expanduser("~")
    return path

def join_paths(*args): # it join a list of string in a proper file path; if the first argument is ~ it is turnded into the used home folder path 
    args = list(args)
    args[0] = _correct_path(args[0]) if args[0] == "~" else args[0]
    return _os.path.abspath(_os.path.join(*args))

def save_text(path, text):
    path = _correct_path(path)
    with open(path , "w+") as file:
        file.write(text)
    print("data saved as " + path)

def read_data(path, delimiter = None, columns = None, header = None): # it turns a text file into data lists
    delimiter = " " if delimiter is None else delimiter
    header = True if header is None else header
    begin = int(not header)
    file = open(path, "r")
    lines = file.readlines()[begin:]
    file.close()
    data = []
    for x in lines:
        row = x.split(delimiter)
        cols = row if columns is None else columns
        row = [float(row[c].replace('\n', '')) for c in cols]
        data.append(row)
    data = _transpose(data)
    return data

def write_data(path, matrix, delimiter = None, columns = None):# it turns a matrix into a text file 
    delimiter = " " if delimiter is None else delimiter
    cols = list(range(len(matrix[0]))) if columns is None else columns
    text = ""
    for row in matrix:
        row = [row[i] for i in cols]
        row = list(map(str, row))
        text += delimiter.join(row) + '\n'
    save_text(path, text)
