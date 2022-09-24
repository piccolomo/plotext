from plotext._utility import colorize, transpose, try_float
import inspect, sys, os

def script_folder(): # the folder of the script executed
    return parent_folder(inspect.getfile(sys._getframe(1)))

def parent_folder(path, level = 1): # it return the parent folder of the path or file given; if level is higher then 1 the process is iterated 
    if level <= 0:
        return path
    elif level == 1:
        return os.path.abspath(os.path.join(path, os.pardir))
    else:
        return parent_folder(parent_folder(path, level - 1))

def join_paths(*args): # it join a list of string in a proper file path; if the first argument is ~ it is turnded into the used home folder path 
    args = list(args)
    args[0] = _correct_path(args[0]) if args[0] == "~" else args[0]
    return os.path.abspath(os.path.join(*args))

def save_text(text, path): # it saves some text to the path selected
    path = correct_path(path)
    with open(path , "w+") as file:
        file.write(text)
    print(colorize("text saved", "green", "bold") + " as " + colorize(path, style = "dim"))

def read_data(path, delimiter = None, columns = None, header = None): # it turns a text file into data lists
    header = True if header is None else header
    file = open(path, "r")
    begin = int(not header)
    lines = file.readlines()[begin:]
    file.close()
    return read_lines(lines, delimiter, columns)

def write_data(data, path, delimiter = None, columns = None): # it turns a matrix into a text file 
    delimiter = " " if delimiter is None else delimiter
    cols = len(data[0])
    cols = range(1, cols + 1) if columns is None else columns
    text = ""
    for row in data:
        row = [row[i - 1] for i in cols]
        row = list(map(str, row))
        text += delimiter.join(row) + '\n'
    save_text(text, path)

def download(url, path): # it download the url (image, video, gif etc) to path
    from urllib.request import urlretrieve
    path = correct_path(path)
    urlretrieve(url, path)
    print('url saved in:', path)
    return path

def delete_file(path): # remove the file if it exists
    if is_file(path):
        os.remove(path)
        print("file removed:", path)

###############################################
#############    Utilities    #################
###############################################

def correct_path(path):
    folder, base = os.path.dirname(path), os.path.basename(path)
    folder = os.path.expanduser("~") if folder in ['', '~'] else folder
    path = os.path.join(folder, base)
    return path

def read_lines(lines, delimiter = None, columns = None): # it turns a text file into data lists
    delimiter = " " if delimiter is None else delimiter
    data = []
    for x in lines:
        row = x.split(delimiter)
        cols = range(1, len(row) + 1) if columns is None else columns
        row = [try_float(row[col - 1].replace('\n', '')) for col in cols]
        data.append(row)
    data = transpose(data)
    return data

def is_file(path): # returns True if path exists
    res = os.path.isfile(path)
    if not res:
        print("this path is not a file:", path)
    return res

