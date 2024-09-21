from plotext._system import platform
import ctypes as c
import sys, os

folder = os.path.dirname(os.path.realpath(__file__))
matrix_file_name = 'kernel.dll' if platform == 'windows' else 'kernel.so'
matrix_file = os.path.join(folder, 'cpp', matrix_file_name)
kernel = c.CDLL(matrix_file)

class Clink:
	def add(self, name, surname = None):
		name = (name + '_' + surname) if surname is not None else name
		cfunction = getattr(kernel, name)
		globals()[name] = cfunction
		setattr(self, 'last', cfunction)
		return self

	def input(self, *args):
		setattr(self.last, 'argtypes', list(args))
		return self

	def output(self, output):
		setattr(self.last, 'restype', output)
		return self


void = c.c_void_p
size = c.c_size_t; integer = c.c_int
float = c.c_float; p_float = c.POINTER(float);
bool = c.c_bool
wstring = c.c_wchar_p
string = c.c_char_p
wchar = c.c_wchar
cstring = c.POINTER(wchar)

link = Clink()

link.add('pixel', 'new').input().output(void)
link.add('pixel', 'delete').input().output(void)
link.add('pixel', 'set_fullground_integer').input(void, size).output(void)
link.add('pixel', 'set_fullground_rgb').input(void, size, size, size).output(void)
link.add('pixel', 'set_fullground_code').input(void, string).output(void)
link.add('pixel', 'set_background_integer').input(void, size).output(void)
link.add('pixel', 'set_background_rgb').input(void, size, size, size).output(void)
link.add('pixel', 'set_background_code').input(void, string).output(void)
link.add('pixel', 'set_style_code').input(void, string).output(void)
link.add('pixel', 'log').input(void).output(void)
link.add('pixel', 'copy').input(void).output(void)

link.add('matrix', 'new').input(size, size).output(void)
link.add('matrix', 'clear').input(void).output(void)
link.add('matrix', 'delete').input().output(void)
link.add('matrix', 'get_width').input(void).output(size)
link.add('matrix', 'get_height').input(void).output(size)
link.add('matrix', 'vstack').input(void, void, bool).output(void)
link.add('matrix', 'hstack').input(void, void, bool).output(void)
link.add('matrix', 'get_wstring').input(void, bool).output(cstring)
link.add('wstring', 'delete').input(wstring).output(void)
link.add('matrix', 'part').input(void, size, size, size, size).output(void)
link.add('matrix', 'is_empty').input(void, size, size, size, size).output(bool)
link.add('matrix', 'show').input(void, bool).output(void)
link.add('matrix', 'copy').input(void).output(void)
link.add('matrix', 'insert').input(void, size, size, void, integer, integer, bool).output(bool)
link.add('matrix', 'insert_aligned').input(void, size, size, void, integer, bool, bool).output(bool)
link.add('matrix', 'insert_dynamically').input(void, size, size, wstring).output(integer)
link.add('matrix', 'insert_wstring').input(void, size, size, wstring).output(void)
link.add('matrix', 'set_char').input(void, size, size, wchar).output(void)

link.add('colorize', 'new').input(wstring, void).output(void)
link.add('colorize', 'get_length').input(void).output(size)
link.add('colorize', 'get_wstring').input(void, bool).output(cstring)
link.add('colorize', 'get_matrix').input(void).output(cstring)
link.add('colorize', 'get_pixel').input(void).output(void)
link.add('colorize', 'set_pixel').input(void).output(void)
link.add('colorize', 'part').input(void, size, size).output(void)
link.add('colorize', 'show').input(void, bool).output(void)
link.add('colorize', 'copy').input(void).output(void)
link.add('colorize', 'copy_from').input(void, void).output(void)
link.add('colorize', 'equals').input(void, void).output(bool)

link.add('canvas', 'new').input(size, size).output(void)
link.add('canvas', 'delete').input().output(void)
link.add('canvas', 'show').input(void).output(void)
link.add('canvas', 'set_xlim').input(void, float, float).output(void)
link.add('canvas', 'set_ylim').input(void, float, float).output(void)
link.add('canvas', 'set_fillx_level').input(void, float).output(void)
link.add('canvas', 'set_filly_level').input(void, float).output(void)
link.add('canvas', 'draw').input(void, void).output(void)

link.add('points', 'new').input(size).output(void)
link.add('points', 'delete').input().output(void)
link.add('points', 'add_normal').input(void, float, float, wchar, void, bool, bool, bool).output(void)
link.add('points', 'add_hd').input(void, float, float, size, void, bool, bool, bool).output(void)
link.add('points', 'log').input(void, bool).output(void)


# link.add('fullground', 'new').input().output(void)
# link.add('fullground', 'set_rgb').input(void, size, size, size).output(void)
# link.add('fullground', 'set_code').input(void, string).output(void)

# link.add('background', 'new').input().output(void)
# link.add('background', 'set_rgb').input(void, size, size, size).output(void)
# link.add('background', 'set_code').input(void, string).output(void)

# link.add('style', 'new').input().output(void)
# link.add('style', 'set_code').input(void, string).output(void)

# pixel_create = kernel.pixel_create
# pixel_create.argtypes = []
# pixel_create.restype = c.c_void_p

# pixel_destroy = kernel.pixel_destroy
# pixel_destroy.argtypes = [c.c_void_p]
# pixel_destroy.restype = c.c_void_p

# pixel_set_marker = kernel.pixel_set_marker
# pixel_set_marker.argtypes = [c.c_void_p, c.c_wchar]
# pixel_set_marker.restype = c.c_void_p

# pixel_set_fullground = kernel.pixel_set_fullground
# pixel_set_fullground.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
# pixel_set_fullground.restype = c.c_void_p

# pixel_set_background = kernel.pixel_set_background
# pixel_set_background.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
# pixel_set_background.restype = c.c_void_p

# pixel_set_style = kernel.pixel_set_style
# pixel_set_style.argtypes = [c.c_void_p, c.c_size_t]
# pixel_set_style.restype = c.c_void_p

# pixel_clear = kernel.pixel_clear
# pixel_clear.argtypes = [c.c_void_p]
# pixel_clear.restype = c.c_void_p

# pixel_log = kernel.pixel_log
# pixel_log.argtypes = [c.c_void_p]
# pixel_log.restype = c.c_void_p

# pixel_get_string = kernel.pixel_get_string
# pixel_get_string.argtypes = [c.c_void_p]
# pixel_get_string.restype = c.POINTER(c.c_wchar_p)

# pixel_assign = kernel.pixel_assign
# pixel_assign.argtypes = [c.c_void_p, c.c_void_p]
# pixel_assign.restype = c.c_void_p

# pixel_get_fullground = kernel.pixel_get_fullground
# pixel_get_fullground.argtypes = [c.c_void_p, c.c_size_t]
# pixel_get_fullground.restype = c.c_size_t

# pixel_get_background = kernel.pixel_get_background
# pixel_get_background.argtypes = [c.c_void_p, c.c_size_t]
# pixel_get_background.restype = c.c_size_t

# pixel_get_style = kernel.pixel_get_style
# pixel_get_style.argtypes = [c.c_void_p, c.c_size_t]
# pixel_get_style.restype = c.c_size_t


# matrix_create = kernel.matrix_create
# matrix_create.argtypes = [c.c_size_t, c.c_size_t, c.c_void_p]
# matrix_create.restype = c.c_void_p

# matrix_destroy = kernel.matrix_destroy
# matrix_destroy.argtypes = [c.c_void_p]
# matrix_destroy.restype = c.c_void_p

# matrix_insert_pixel = kernel.matrix_insert_pixel
# matrix_insert_pixel.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
# matrix_insert_pixel.restype = c.c_void_p

# matrix_insert_string = kernel.matrix_insert_string
# matrix_insert_string.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_wchar_p, c.c_void_p]
# matrix_insert_string.restype = c.c_void_p

# matrix_insert_matrix = kernel.matrix_insert_matrix
# matrix_insert_matrix.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
# matrix_insert_matrix.restype = c.c_void_p

# matrix_insert_aligned = kernel.matrix_insert_aligned
# matrix_insert_aligned.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p, c.c_size_t, c.c_size_t, c.c_bool]
# matrix_insert_aligned.restype = c.c_bool

# matrix_insert_dynamic = kernel.matrix_insert_dynamic
# matrix_insert_dynamic.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
# matrix_insert_dynamic.restype = c.c_bool

# matrix_fill = kernel.matrix_fill
# matrix_fill.argtypes = [c.c_void_p, c.c_void_p]
# matrix_fill.restype = c.c_void_p

# matrix_fill_color = kernel.matrix_fill_color
# matrix_fill_color.argtypes = [c.c_void_p, c.c_void_p]
# matrix_fill_color.restype = c.c_void_p

# matrix_clear = kernel.matrix_clear
# matrix_clear.argtypes = [c.c_void_p]
# matrix_clear.restype = c.c_void_p

# matrix_resize = kernel.matrix_resize
# matrix_resize.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_void_p]
# matrix_resize.restype = c.c_void_p

# matrix_hstack = kernel.matrix_hstack
# matrix_hstack.argtypes = [c.c_void_p, c.c_void_p]
# matrix_hstack.restype = c.c_void_p

# matrix_vstack = kernel.matrix_vstack
# matrix_vstack.argtypes = [c.c_void_p, c.c_void_p]
# matrix_vstack.restype = c.c_void_p

# matrix_transpose = kernel.matrix_transpose
# matrix_transpose.argtypes = [c.c_void_p]
# matrix_transpose.restype = c.c_void_p

# matrix_height = kernel.matrix_height
# matrix_height.argtypes = [c.c_void_p]
# matrix_height.restype = c.c_size_t

# matrix_width = kernel.matrix_width
# matrix_width.argtypes = [c.c_void_p]
# matrix_width.restype = c.c_size_t

# matrix_part = kernel.matrix_part
# matrix_part.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t, c.c_size_t, c.c_size_t]
# matrix_part.restype = c.c_void_p

# matrix_get_pixel = kernel.matrix_get_pixel
# matrix_get_pixel.argtypes = [c.c_void_p, c.c_size_t, c.c_size_t]
# matrix_get_pixel.restype = c.c_void_p


# matrix_get_string = kernel.matrix_get_string
# matrix_get_string.argtypes = [c.c_void_p, c.c_bool]
# matrix_get_string.restype = c.POINTER(c.c_wchar_p)

# string_free_memory = kernel.string_free_memory
# string_free_memory.argtypes = [c.POINTER(c.c_wchar_p)]
# string_free_memory.restype = c.c_void_p

# matrix_show = kernel.matrix_show
# matrix_show.argtypes = [c.c_void_p]
# matrix_show.restype = c.c_void_p

# matrix_get_marker = kernel.matrix_get_marker
# matrix_get_marker.argtypes = [c.c_void_p, c.c_wchar]
# matrix_get_marker.restype = c.c_void_p


# matrix_copy = kernel.matrix_copy
# matrix_copy.argtypes = [c.c_void_p]
# matrix_copy.restype = c.c_void_p

# matrix_assign = kernel.matrix_assign
# matrix_assign.argtypes = [c.c_void_p, c.c_void_p]
# matrix_assign.restype = c.c_void_p

# matrix_equal = kernel.matrix_equal
# matrix_equal.argtypes = [c.c_void_p, c.c_void_p]
# matrix_equal.restype = c.c_bool

# marker_create = kernel.marker_create
# marker_create.argtypes = [c.c_size_t, c.c_size_t]
# marker_create.restype = c.c_void_p

# marker_destroy = kernel.marker_destroy
# marker_destroy.argtypes = []
# marker_destroy.restype = c.c_void_p

# marker_add = kernel.marker_add
# marker_add.argtypes = [c.c_void_p, c.POINTER(c.c_bool), c.c_size_t,  c.c_wchar]
# marker_add.restype = c.c_void_p

# marker_show = kernel.marker_show
# marker_show.argtypes = [c.c_void_p]
# marker_show.restype = c.c_void_p

# marker_get_marker = kernel.marker_get_marker
# marker_get_marker.argtypes = [c.c_void_p, c.POINTER(c.c_bool), c.c_size_t]
# marker_get_marker.restype = c.c_wchar

# marker_get_fill_marker = kernel.marker_get_fill_marker
# marker_get_fill_marker.argtypes = [c.c_void_p, c.c_wchar, c.c_size_t, c.c_size_t]
# marker_get_fill_marker.restype = c.c_wchar

# marker_sum_markers = kernel.marker_sum_markers
# marker_sum_markers.argtypes = [c.c_void_p, c.c_wchar, c.c_wchar]
# marker_sum_markers.restype = c.c_wchar

# colorize_create = kernel.colorize_create
# colorize_create.argtypes = [c.c_void_p, c.c_wchar_p]
# colorize_create.restype = c.c_void_p

# colorize_destroy = kernel.colorize_destroy
# colorize_destroy.argtypes = [c.c_void_p]
# colorize_destroy.restype = c.c_void_p

# colorize_get_string = kernel.colorize_get_string
# colorize_get_string.argtypes = [c.c_void_p, c.c_bool]
# colorize_get_string.restype = c.POINTER(c.c_wchar_p)

# colorize_get_matrix = kernel.colorize_get_matrix
# colorize_get_matrix.argtypes = [c.c_void_p]
# colorize_get_matrix.restype = c.c_void_p

# colorize_get_pixel = kernel.colorize_get_pixel
# colorize_get_pixel.argtypes = [c.c_void_p]
# colorize_get_pixel.restype = c.c_void_p

# colorize_copy = kernel.colorize_copy
# colorize_copy.argtypes = [c.c_void_p]
# colorize_copy.restype = c.c_void_p

# colorize_new = kernel.colorize_new
# colorize_new.argtypes = [c.c_void_p, c.c_wchar_p]
# colorize_new.restype = c.c_void_p

# colorize_fill = kernel.colorize_fill
# colorize_fill.argtypes = [c.c_void_p, c.c_void_p]
# colorize_fill.restype = c.c_void_p

# colorize_assign = kernel.colorize_assign
# colorize_assign.argtypes = [c.c_void_p, c.c_void_p]
# colorize_assign.restype = c.c_void_p

