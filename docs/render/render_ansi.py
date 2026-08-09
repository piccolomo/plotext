"""Render ANSI terminal output to a PNG, painting block glyphs as exact rectangles."""
import re
import sys
import unicodedata
from PIL import Image, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]

font_size = 20
font_regular = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', font_size)
font_bold = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', font_size)
font_wide = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', font_size)

# The columns a character covers on a terminal: two for the east asian wide ones, one for the rest
def get_columns(character):
    return 2 if unicodedata.east_asian_width(character) in ("W", "F") else 1

cell_width = int(font_regular.getlength('M'))
ascent, descent = font_regular.getmetrics()
cell_height = ascent + descent

default_fg = (0, 0, 0)
default_bg = (255, 255, 255)

# Fractions of the cell painted by each block glyph, as a list of (left, top, right, bottom) rectangles
blocks = {
    '█': [(0, 0, 1, 1)],
    '▀': [(0, 0, 1, 0.5)], '▄': [(0, 0.5, 1, 1)],
    '▌': [(0, 0, 0.5, 1)], '▐': [(0.5, 0, 1, 1)],
    '▘': [(0, 0, 0.5, 0.5)], '▝': [(0.5, 0, 1, 0.5)],
    '▖': [(0, 0.5, 0.5, 1)], '▗': [(0.5, 0.5, 1, 1)],
}
for i, ch in enumerate('▁▂▃▄▅▆▇█'):
    blocks.setdefault(ch, [(0, 1 - (i + 1) / 8, 1, 1)])
for i, ch in enumerate('▏▎▍▌▋▊▉█'):
    blocks.setdefault(ch, [(0, 0, (i + 1) / 8, 1)])

# Sextants (the fhd marker): a 2 x 3 grid of sub-cells, one bit each, laid out from U+1FB00 skipping the four patterns that already have a character (empty, left half, right half, full)
sextant_pieces = [(0, 0), (0.5, 0), (0, 1 / 3), (0.5, 1 / 3), (0, 2 / 3), (0.5, 2 / 3)]
codepoint = 0x1FB00
for pattern in range(1, 63):
    if pattern in (0b010101, 0b101010):
        continue
    rectangles = [(l, t, l + 0.5, t + 1 / 3) for bit, (l, t) in enumerate(sextant_pieces) if pattern >> bit & 1]
    blocks.setdefault(chr(codepoint), rectangles)
    codepoint += 1

# Braille (the braille marker): a 2 x 4 grid of dots, one bit each from U+2800; only the raised dots are painted, as filled circles
braille_dots = [(0, 0), (0, 0.25), (0, 0.5), (0.5, 0), (0.5, 0.25), (0.5, 0.5), (0, 0.75), (0.5, 0.75)]


# Standard 256-color palette
def color_256(n):
    if n < 16:
        base = [(23,20,33),(192,28,40),(38,162,105),(162,115,76),(18,72,139),(163,71,186),(42,161,179),(208,207,204),
                (94,92,100),(246,97,81),(51,218,122),(233,173,12),(42,123,222),(192,97,203),(51,199,222),(255,255,255)]
        return base[n]
    if n < 232:
        n -= 16
        steps = [0, 95, 135, 175, 215, 255]
        return (steps[n // 36], steps[n // 6 % 6], steps[n % 6])
    gray = 8 + (n - 232) * 10
    return (gray, gray, gray)

# Parse the ANSI text into a grid of (character, fg, bg, bold) cells
def parse(text):
    rows, row = [], []
    fg, bg, bold = None, None, False
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == '\x1b':
            match = re.match(r'\x1b\[([0-9;]*)m', text[i:])
            if match:
                parts = [int(p) for p in match.group(1).split(';') if p != ''] or [0]
                j = 0
                while j < len(parts):
                    p = parts[j]
                    if p == 0: fg, bg, bold = None, None, False
                    elif p == 1: bold = True
                    elif p == 22: bold = False
                    elif 30 <= p <= 37: fg = color_256(p - 30)
                    elif p == 39: fg = None
                    elif 40 <= p <= 47: bg = color_256(p - 40)
                    elif p == 49: bg = None
                    elif 90 <= p <= 97: fg = color_256(p - 90 + 8)
                    elif 100 <= p <= 107: bg = color_256(p - 100 + 8)
                    elif p in (38, 48):
                        target = 'fg' if p == 38 else 'bg'
                        if parts[j + 1] == 5:
                            value = color_256(parts[j + 2]); j += 2
                        else:
                            value = tuple(parts[j + 2 : j + 5]); j += 4
                        fg, bg = (value, bg) if target == 'fg' else (fg, value)
                    j += 1
                i += match.end()
                continue
            i += 1
            continue
        if ch == '\n':
            rows.append(row); row = []
        elif ch != '\r':
            row.append((ch, fg, bg, bold))
        i += 1
    if row: rows.append(row)
    return rows

rows = parse(open(src).read())
while rows and not rows[-1]:   # trailing newlines are not content rows
    rows.pop()

# Drop the trailing blank cells each padded line carries, so the image hugs its content
def trim(row):
    while row and row[-1][0] == ' ' and row[-1][2] is None:
        row = row[:-1]
    return row

rows = [trim(row) for row in rows]
width = max(sum(get_columns(cell[0]) for cell in row) for row in rows)
im = Image.new('RGB', (width * cell_width, len(rows) * cell_height), default_bg)
draw = ImageDraw.Draw(im)

for y, row in enumerate(rows):
    column = 0
    for ch, fg, bg, bold in row:
        columns = get_columns(ch)
        x0, y0 = column * cell_width, y * cell_height
        column += columns
        fg = fg or default_fg
        bg = bg or default_bg
        if bg != default_bg:
            draw.rectangle([x0, y0, x0 + columns * cell_width - 1, y0 + cell_height - 1], fill = bg)
        if ch in blocks:
            for l, t, r, b in blocks[ch]:
                draw.rectangle([x0 + l * cell_width, y0 + t * cell_height,
                                x0 + r * cell_width, y0 + b * cell_height], fill = fg)
        elif '\u2800' <= ch <= '\u28ff':
            pattern = ord(ch) - 0x2800
            for bit, (l, t) in enumerate(braille_dots):
                if pattern >> bit & 1:
                    pad_x, pad_y = cell_width * 0.08, cell_height * 0.04
                    draw.ellipse([x0 + l * cell_width + pad_x, y0 + t * cell_height + pad_y,
                                  x0 + (l + 0.5) * cell_width - 1 - pad_x, y0 + (t + 0.25) * cell_height - 1 - pad_y], fill = fg)
        elif ch != ' ':
            font = font_wide if columns == 2 else (font_bold if bold else font_regular)
            draw.text((x0, y0), ch, font = font, fill = fg)

im.save(dst, optimize = True)
print(dst, im.size)
