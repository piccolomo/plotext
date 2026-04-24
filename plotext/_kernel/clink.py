# Registration of all C kernel bindings: declares input and output types for every exported function

from plotext._kernel.tools import clink

# =========================
# Core
# =========================

clink.add('rescale').input("float", "float", "float", "size", "float").output("float")

clink.add('wstring', 'delete').input("wstring").output("void")
clink.add('get', 'color', 'name').input("size").output("string")

clink.add('fast', 'print').input("void").output("void")


# =========================
# Pixel
# =========================

clink.add('pixel', 'new').input().output("void")
clink.add('pixel', 'delete').input("void").output("void")
clink.add('pixel', 'clear').input("void").output("void")

clink.add('pixel', 'set', 'fullground', 'integer').input("void", "size").output("void")
clink.add('pixel', 'set', 'fullground', 'rgb').input("void", "size", "size", "size").output("void")
clink.add('pixel', 'set', 'fullground', 'code').input("void", "string").output("void")

clink.add('pixel', 'set', 'background', 'integer').input("void", "size").output("void")
clink.add('pixel', 'set', 'background', 'rgb').input("void", "size", "size", "size").output("void")
clink.add('pixel', 'set', 'background', 'code').input("void", "string").output("void")

clink.add('pixel', 'set', 'style', 'code').input("void", "string").output("void")

clink.add('pixel', 'get', 'wstring').input("void").output("wchar pointer")

clink.add('pixel', 'log').input("void").output("void")
clink.add('pixel', 'copy').input("void").output("void")

clink.add('pixel', 'no', 'background').input("void").output("bool")

clink.add('pixel', 'copy', 'background').input("void", "void").output("void")
clink.add('pixel', 'copy', 'pixel').input("void", "void").output("void")

clink.add('pixel', 'fix', 'background').input("void", "void").output("void")
clink.add('pixel', 'fix').input("void", "void").output("void")


# =========================
# Colorize
# =========================

clink.add('colorize', 'new').input("wstring", "void").output("void")
clink.add('colorize', 'delete').input("void").output("void")

clink.add('colorize', 'get', 'length').input("void").output("size")
clink.add('colorize', 'get', 'wstring').input("void", "bool").output("wchar pointer")
clink.add('colorize', 'get', 'matrix').input("void").output("void")
clink.add('colorize', 'get', 'pixel').input("void").output("void")

clink.add('colorize', 'set', 'pixel').input("void").output("void")

clink.add('colorize', 'part').input("void", "size", "size").output("void")
clink.add('colorize', 'print').input("void", "bool", "bool").output("void")

clink.add('colorize', 'copy').input("void").output("void")
clink.add('colorize', 'copy', 'from').input("void", "void").output("void")

clink.add('colorize', 'equals').input("void", "void").output("bool")

clink.add('colorize', 'no', 'background').input("void").output("bool")

clink.add('colorize', 'copy', 'background').input("void", "void").output("void")
clink.add('colorize', 'fix', 'background').input("void", "void").output("void")


# =========================
# Matrix
# =========================

clink.add('matrix', 'new').input("size", "size").output("void")
clink.add('matrix', 'clear').input("void").output("void")
clink.add('matrix', 'delete').input("void")

clink.add('matrix', 'get', 'width').input("void").output("size")
clink.add('matrix', 'get', 'height').input("void").output("size")

clink.add('matrix', 'vstack').input("void", "void", "bool").output("void")
clink.add('matrix', 'hstack').input("void", "void", "bool").output("void")

clink.add('matrix', 'get', 'wstring').input("void", "bool").output("wchar pointer")

clink.add('matrix', 'part').input("void", "size", "size", "size", "size").output("void")
clink.add('matrix', 'is', 'empty').input("void", "size", "size", "size", "size").output("bool")

clink.add('matrix', 'print').input("void", "bool", "bool").output("void")
clink.add('matrix', 'copy').input("void").output("void")

clink.add('matrix', 'insert', 'matrix').input("void", "size", "size", "void").output("void")
clink.add('matrix', 'insert', 'matrix', 'aligned').input("void", "size", "size", "void", "integer", "integer").output("void")

clink.add('matrix', 'insert', 'colorized', 'aligned').input("void", "size", "size", "void", "integer", "bool").output("bool")
clink.add('matrix', 'insert', 'colorized', 'dynamically').input("void", "size", "size", "void").output("integer")

clink.add('matrix', 'insert', 'wstring').input("void", "size", "size", "wstring").output("void")
clink.add('matrix', 'set', 'wcharacter').input("void", "size", "size", "wchar").output("void")

clink.add('matrix', 'set', 'pixel').input("void", "size", "size", "void").output("void")


# =========================
# Marker
# =========================

clink.add('marker', 'new', 'normal').input("wchar", "void").output("void")
clink.add('marker', 'new', 'hd').input("size", "void").output("void")
clink.add('marker', 'new', 'code').input("string", "void").output("void")

clink.add('marker', 'delete').input().output("void")
clink.add('marker', 'copy').input("void").output("void")

clink.add('marker', 'get', 'wstring').input("void").output("wchar pointer")
clink.add('marker', 'get', 'model').input("void").output("wchar pointer")
clink.add('marker', 'get', 'pixel').input("void").output("void")

clink.add('marker', 'fix').input("void", "void").output("void")


# =========================
# Point / Points
# =========================

clink.add('point', 'filled', 'new').input("float", "float", "void").output("void")
clink.add('point', 'filled', 'get', 'marker').input("void").output("void")
clink.add('point', 'filled', 'delete').input().output("void")
clink.add('point', 'filled', 'get', 'wstring').input("void", "bool").output("wchar pointer")
clink.add('point', 'filled', 'get', 'col').input("void").output("size")
clink.add('point', 'filled', 'get', 'row').input("void").output("size")
clink.add('point', 'filled', 'get', 'x').input("void").output("float")
clink.add('point', 'filled', 'get', 'y').input("void").output("float")
clink.add('point', 'filled', 'get', 'code').input("void").output("size")

clink.add('points', 'new').input("size").output("void")
clink.add('points', 'delete').input("void").output("void")
clink.add('points', 'clear').input("void").output("void")

clink.add('points', 'append', 'point').input("void", "void").output("void")
clink.add('points', 'append', 'points').input("void", "void").output("void")

clink.add('points', 'get', 'point').input("void", "size").output("void")
clink.add('points', 'get', 'length').input("void").output("size")

clink.add('points', 'add', 'offset').input("void", "size", "size").output("void")
clink.add('points', 'select', 'in', 'matrix').input("void", "size", "size").output("void")

clink.add('matrix', 'insert', 'points').input("void", "void").output("void")
clink.add('matrix', 'fill', 'pixel').input("void", "void").output("void")

clink.add('points', 'fix', 'background').input("void", "void").output("void")
clink.add('points', 'squash').input("void", "void").output("void")
clink.add('points', 'log').input("void").output("void")
clink.add('points', 'copy').input("void").output("void")

clink.add('points', 'map', 'new').input("size", "size").output("void")
clink.add('points', 'map', 'delete').input("void").output("void")
clink.add('points', 'map', 'log').input("void").output("void")
clink.add('points', 'map', 'clear').input("void").output("void")
clink.add('points', 'map', 'get', 'length').input("void").output("size")


# =========================
# Point (single)
# =========================

clink.add('point', 'new', 'marker').input("float", "float", "void").output("void")
clink.add('point', 'delete').input("void").output("void")

clink.add('point', 'get', 'x').input("void").output("float")
clink.add('point', 'get', 'y').input("void").output("float")
clink.add('point', 'get', 'wstring').input("void").output("wchar pointer")

clink.add('point', 'log').input("void").output("void")


# =========================
# Signal
# =========================

clink.add('signal', 'new').input("size").output("void")
clink.add('signal', 'delete').input("void")

clink.add('signal', 'copy').input("void").output("void")
clink.add('signal', 'clear').input("void").output("void")

clink.add('signal', 'get', 'xside').input("void").output("bool")
clink.add('signal', 'get', 'yside').input("void").output("bool")
clink.add('signal', 'get', 'label').input("void").output("wchar pointer")
clink.add('signal', 'get', 'marker').input("void").output("void")

clink.add('signal', 'get', 'fill', 'method').input("void").output("bool")
clink.add('signal', 'get', 'line', 'method').input("void").output("bool")

clink.add('signal', 'set', 'xside').input("void", "bool").output("void")
clink.add('signal', 'set', 'yside').input("void", "bool").output("void")
clink.add('signal', 'set', 'label').input("void", "wstring").output("void")
clink.add('signal', 'set', 'marker').input("void", "void").output("void")

clink.add('signal', 'set', 'fill', 'method').input("void", "bool").output("void")
clink.add('signal', 'set', 'line', 'method').input("void", "bool").output("void")

clink.add('signal', 'append', 'point').input("void", "float", "float", "void").output("void")
clink.add('signal', 'append').input("void", "void").output("void")

clink.add('signal', 'set', 'point').input("void", "size", "float", "float", "void").output("void")
clink.add('signal', 'set', 'fill', 'point').input("void", "size", "float", "float", "void").output("void")

clink.add('signal', 'get', 'point').input("void", "size").output("void")
clink.add('signal', 'get', 'fill', 'point').input("void", "size").output("void")

clink.add('signal', 'log', 'x').input("void").output("void")
clink.add('signal', 'log', 'y').input("void").output("void")

clink.add('signal', 'rescale', 'x').input("void", "float", "float", "size", "float").output("float")
clink.add('signal', 'rescale', 'y').input("void", "float", "float", "size", "float").output("float")

clink.add('signal', 'add', 'offset').input("void", "size", "size").output("void")
clink.add('signal', 'select', 'in', 'matrix').input("void", "size", "size").output("void")

clink.add('signal', 'get', 'xmin').input("void", "float", "float").output("float")
clink.add('signal', 'get', 'xmax').input("void", "float", "float").output("float")
clink.add('signal', 'get', 'ymin').input("void", "float", "float").output("float")
clink.add('signal', 'get', 'ymax').input("void", "float", "float").output("float")

clink.add('signal', 'assign').input("void", "void").output("void")
clink.add('signal', 'fix', 'background').input("void", "void").output("void")

clink.add('signal', 'plot').input("void").output("void")
clink.add('signal', 'get', 'wstring').input("void", "bool").output("wchar pointer")
clink.add('signal', 'get', 'length').input("void").output("size")
clink.add('signal', 'get', 'points').input("void").output("void")