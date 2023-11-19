import ctypes as c
from plotext._system import platform
import os

folder = os.path.dirname(os.path.realpath(__file__))
matrix_file_name = '_kernel.dll' if platform == 'windows' else '_kernel.so'
matrix_file = os.path.join(folder, matrix_file_name)
kernel = c.CDLL(matrix_file)

pixel_create = kernel.pixel_create
pixel_create.argtypes = []
pixel_create.restype = c.c_void_p

pixel_set_marker = kernel.pixel_set_marker
pixel_set_marker.argtypes = [c.c_void_p, c.c_wchar]
pixel_set_marker.restype = c.c_void_p

pixel_set_fullground = kernel.pixel_set_fullground
pixel_set_fullground.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_int, c.c_int]
pixel_set_fullground.restype = c.c_void_p

pixel_set_background = kernel.pixel_set_background
pixel_set_background.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_int, c.c_int]
pixel_set_background.restype = c.c_void_p

pixel_set_style = kernel.pixel_set_style
pixel_set_style.argtypes = [c.c_void_p, c.c_int]
pixel_set_style.restype = c.c_void_p

pixel_log = kernel.pixel_log
pixel_log.argtypes = [c.c_void_p]
pixel_log.restype = c.c_void_p

pixel_show = kernel.pixel_show
pixel_show.argtypes = [c.c_void_p]
pixel_show.restype = c.c_void_p

pixel_destroy = kernel.pixel_destroy
pixel_destroy.argtypes = [c.c_void_p]
pixel_destroy.restype = c.c_void_p


string_create = kernel.string_create
string_create.argtypes = [c.c_int]
string_create.restype = c.c_void_p

string_destroy = kernel.string_destroy
string_destroy.argtypes = [c.c_void_p]
string_destroy.restype = c.c_void_p


matrix_create = kernel.matrix_create
matrix_create.argtypes = [c.c_int, c.c_int, c.c_void_p]
matrix_create.restype = c.c_void_p

matrix_show = kernel.matrix_show
matrix_show.argtypes = [c.c_void_p]
matrix_show.restype = c.c_void_p

matrix_insert_h = kernel.matrix_insert_h
matrix_insert_h.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_wchar_p, c.c_void_p]
matrix_insert_h.restype = c.c_void_p

matrix_insert_d = kernel.matrix_insert_d
matrix_insert_d.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_wchar_p, c.c_void_p]
matrix_insert_d.restype = c.c_bool

matrix_insert_v = kernel.matrix_insert_v
matrix_insert_v.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_wchar_p, c.c_void_p]
matrix_insert_v.restype = c.c_void_p

matrix_insert_m = kernel.matrix_insert_m
matrix_insert_m.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_void_p]
matrix_insert_m.restype = c.c_void_p

matrix_check = kernel.matrix_check
matrix_check.argtypes = [c.c_void_p, c.c_int, c.c_int, c.c_int]
matrix_check.restype = c.c_bool

matrix_get_string = kernel.matrix_get_string
matrix_get_string.argtypes = [c.c_void_p, c.c_bool]
matrix_get_string.restype = c.POINTER(c.c_wchar_p)

string_free_memory = kernel.string_free_memory
string_free_memory.argtypes = [c.POINTER(c.c_wchar_p)]
string_free_memory.restype = c.c_void_p

matrix_destroy = kernel.matrix_destroy
matrix_destroy.argtypes = [c.c_void_p]
matrix_destroy.restype = c.c_void_p

matrix_copy = kernel.matrix_copy
matrix_copy.argtypes = [c.c_void_p]
matrix_copy.restype = c.c_void_p

matrix_rows = kernel.matrix_rows
matrix_rows.argtypes = [c.c_void_p]
matrix_rows.restype = c.c_int

matrix_cols = kernel.matrix_cols
matrix_cols.argtypes = [c.c_void_p]
matrix_cols.restype = c.c_int



markers_create = kernel.markers_create
markers_create.argtypes = []
markers_create.restype = c.c_void_p

markers_add = kernel.markers_add
markers_add.argtypes = [c.c_void_p, c.POINTER(c.c_bool), c.c_int, c.c_wchar]
markers_add.restype = c.c_void_p

markers_sum = kernel.markers_sum
markers_sum.argtypes = [c.c_void_p, c.c_wchar, c.c_wchar]
markers_sum.restype = c.c_wchar

markers_in = kernel.markers_in
markers_in.argtypes = [c.c_void_p, c.c_wchar_p]
markers_in.restype = c.c_bool

markers_log = kernel.markers_log
markers_log.argtypes = [c.c_void_p]
markers_log.restype = c.c_void_p

markers_destroy = kernel.markers_destroy
markers_destroy.argtypes = [c.c_void_p]
markers_destroy.restype = c.c_void_p
