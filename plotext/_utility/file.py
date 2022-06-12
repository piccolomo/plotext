from plotext._utility import transpose, try_float, colorize, positive_color, negative_color, info_style
import inspect, sys, os, re, linecache


def format_strings(string1, string2, color = positive_color):
    print(colorize(string1, color, "bold") + " " + colorize(string2, style = info_style))

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

def save_text(text, path, log = True): # it saves some text to the path selected
    path = correct_path(path)
    with open(path , "w+") as file:
        file.write(text)
    format_strings("text saved in", path) if log else None

def read_data(path, delimiter = None, columns = None, header = None): # it turns a text file into data lists
    path = correct_path(path)
    header = True if header is None else header
    file = open(path, "r")
    begin = int(not header)
    text = file.readlines()[begin:]
    file.close()
    return read_lines(text, delimiter, columns)

def write_data(data, path, delimiter = None, columns = None, log = True): # it turns a matrix into a text file 
    delimiter = " " if delimiter is None else delimiter
    cols = len(data[0])
    cols = range(1, cols + 1) if columns is None else columns
    text = ""
    for row in data:
        row = [row[i - 1] for i in cols]
        row = list(map(str, row))
        text += delimiter.join(row) + '\n'
    save_text(text, path, log = log)

def download(url, path, log = True): # it download the url (image, video, gif etc) to path
    from urllib.request import urlretrieve
    path = correct_path(path)
    urlretrieve(url, path)
    format_strings('url saved in', path) if log else None
    return path

def delete_file(path, log = True): # remove the file if it exists
    path = correct_path(path)
    if is_file(path):
        os.remove(path)
        format_strings("file removed:", path) if log else None

###############################################
#############    Utilities    #################
###############################################

def correct_path(path):
    folder, base = os.path.dirname(path), os.path.basename(path)
    folder = os.path.expanduser("~") if folder in ['', '~'] else folder
    path = os.path.join(folder, base)
    return path

def is_file(path, log = True): # returns True if path exists
    res = os.path.isfile(path)
    format_strings("not a file:", path, negative_color) if not res and log else None
    return res

def no_char_duplicates(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def read_lines(text, delimiter = None, columns = None):
    delimiter = " " if delimiter is None else delimiter
    data = []
    columns = len(no_char_duplicates(text[0], delimiter).split(delimiter)) if columns is None else columns
    for i in range(len(text)):
        row = text[i]
        row = no_char_duplicates(row, delimiter)
        row = row.split(delimiter)
        row = [el.replace('\n', '') for el in row]
        cols = len(row)
        row = [row[col].replace('\n', '') if col in range(cols) else '' for col in range(columns)]
        row = [try_float(el) for el in row]
        data.append(row)
    return data
