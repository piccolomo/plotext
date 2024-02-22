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

pixel_destroy = kernel.pixel_destroy
pixel_destroy.argtypes = [c.c_void_p]
pixel_destroy.restype = c.c_void_p

pixel_set_marker = kernel.pixel_set_marker
pixel_set_marker.argtypes = [c.c_void_p, c.c_wchar]
pixel_set_marker.restype = c.c_void_p

pixel_set_fullground = kernel.pixel_set_fullground
pixel_set_fullground.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
pixel_set_fullground.restype = c.c_void_p

pixel_set_background = kernel.pixel_set_background
pixel_set_background.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
pixel_set_background.restype = c.c_void_p

pixel_set_style = kernel.pixel_set_style
pixel_set_style.argtypes = [c.c_void_p, c.c_size_t]
pixel_set_style.restype = c.c_void_p

pixel_log = kernel.pixel_log
pixel_log.argtypes = [c.c_void_p]
pixel_log.restype = c.c_void_p

pixel_get_string = kernel.pixel_get_string
pixel_get_string.argtypes = [c.c_void_p]
pixel_get_string.restype = c.POINTER(c.c_wchar_p)

pixel_assign = kernel.pixel_assign
pixel_assign.argtypes = [c.c_void_p, c.c_void_p]
pixel_assign.restype = c.c_void_p


matrix_create = kernel.matrix_create
matrix_create.argtypes = [c.c_size_t, c.c_size_t, c.c_void_p]
matrix_create.restype = c.c_void_p

matrix_destroy = kernel.matrix_destroy
matrix_destroy.argtypes = [c.c_void_p]
matrix_destroy.restype = c.c_void_p

matrix_insert_pixel = kernel.matrix_insert_pixel
matrix_insert_pixel.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
matrix_insert_pixel.restype = c.c_void_p

matrix_insert_string = kernel.matrix_insert_string
matrix_insert_string.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_wchar_p, c.c_void_p]
matrix_insert_string.restype = c.c_void_p

matrix_insert_matrix = kernel.matrix_insert_matrix
matrix_insert_matrix.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
matrix_insert_matrix.restype = c.c_void_p

matrix_insert_aligned = kernel.matrix_insert_aligned
matrix_insert_aligned.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p, c.c_size_t, c.c_size_t, c.c_bool]
matrix_insert_aligned.restype = c.c_bool

matrix_insert_dynamic = kernel.matrix_insert_dynamic
matrix_insert_dynamic.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
matrix_insert_dynamic.restype = c.c_bool

matrix_fill = kernel.matrix_fill
matrix_fill.argtypes = [c.c_void_p, c.c_void_p]
matrix_fill.restype = c.c_void_p

matrix_fill_color = kernel.matrix_fill_color
matrix_fill_color.argtypes = [c.c_void_p, c.c_void_p]
matrix_fill_color.restype = c.c_void_p

matrix_clear = kernel.matrix_clear
matrix_clear.argtypes = [c.c_void_p]
matrix_clear.restype = c.c_void_p

matrix_resize = kernel.matrix_resize
matrix_resize.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
matrix_resize.restype = c.c_void_p

matrix_hstack = kernel.matrix_hstack
matrix_hstack.argtypes = [c.c_void_p, c.c_void_p]
matrix_hstack.restype = c.c_void_p

matrix_vstack = kernel.matrix_vstack
matrix_vstack.argtypes = [c.c_void_p, c.c_void_p]
matrix_vstack.restype = c.c_void_p

matrix_transpose = kernel.matrix_transpose
matrix_transpose.argtypes = [c.c_void_p]
matrix_transpose.restype = c.c_void_p

matrix_height = kernel.matrix_height
matrix_height.argtypes = [c.c_void_p]
matrix_height.restype = c.c_size_t

matrix_width = kernel.matrix_width
matrix_width.argtypes = [c.c_void_p]
matrix_width.restype = c.c_size_t

matrix_part = kernel.matrix_part
matrix_part.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
matrix_part.restype = c.c_void_p

matrix_get_pixel = kernel.matrix_get_pixel
matrix_get_pixel.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t]
matrix_get_pixel.restype = c.c_void_p


matrix_get_string = kernel.matrix_get_string
matrix_get_string.argtypes = [c.c_void_p, c.c_bool]
matrix_get_string.restype = c.POINTER(c.c_wchar_p)

string_free_memory = kernel.string_free_memory
string_free_memory.argtypes = [c.POINTER(c.c_wchar_p)]
string_free_memory.restype = c.c_void_p

matrix_show = kernel.matrix_show
matrix_show.argtypes = [c.c_void_p]
matrix_show.restype = c.c_void_p

matrix_copy = kernel.matrix_copy
matrix_copy.argtypes = [c.c_void_p]
matrix_copy.restype = c.c_void_p

matrix_assign = kernel.matrix_assign
matrix_assign.argtypes = [c.c_void_p, c.c_void_p]
matrix_assign.restype = c.c_void_p
