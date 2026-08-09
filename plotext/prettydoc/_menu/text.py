# Text: measuring and wrapping colored text, so that a docstring fits a column without its colors bleeding outside it.

import re

from plotext._constants.text import new_line

# The sequence closing every color, so that what follows is left uncolored.
end_of_colors = '\x1b[0m'

# Matches one color sequence, used to measure and wrap colored text by its visible characters alone.
color_sequence = re.compile('\x1b\\[[0-9;]*m')


# Number of characters the text takes on screen, color sequences excluded.
def get_visible_length(text):
    return len(color_sequence.sub('', text))


# Split a colored line into its words and the single spaces between them, each given as a list of pairs, one per character: the color sequences sitting right before it, and the character itself.
def get_words(line):
    words, word, codes, index = [], [], '', 0
    while index < len(line):
        match = color_sequence.match(line, index)
        if match:
            codes += match.group()
            index = match.end()
            continue
        character = line[index]
        if character == ' ':
            if word:
                words.append(word)
            words.append([(codes, character)])
            word = []
        else:
            word.append((codes, character))
        codes = ''
        index += 1
    if word:
        words.append(word)
    return words


# The colors in use after reading some color sequences: the closing one empties them, any other adds to them.
def update_colors(colors, codes):
    for sequence in color_sequence.findall(codes):
        colors = '' if sequence == end_of_colors else colors + sequence
    return colors


# Cut one colored line into lines no wider than the given width, breaking at a space when there is one; the colors in use carry to the next line, and each line closes them at its end, so that no color escapes it.
def wrap_colored_line(line, width):
    lines, current, length, colors, starting_colors = [], '', 0, '', ''
    for word in get_words(line):
        if length > 0 and length + len(word) > width:
            lines.append(starting_colors + current + end_of_colors)
            current, length, starting_colors = '', 0, colors
            if word[0][1] == ' ':
                colors = update_colors(colors, word[0][0])
                starting_colors = colors
                continue
        for codes, character in word:
            if length == width:
                lines.append(starting_colors + current + end_of_colors)
                current, length, starting_colors = '', 0, colors
            colors = update_colors(colors, codes)
            current += codes + character
            length += 1
    if current or not lines:
        lines.append(starting_colors + current + end_of_colors)
    return lines


# Cut a whole docstring into lines no wider than the given width, its empty lines kept as they are.
def wrap_docstring(docstring, width):
    lines = []
    for line in docstring.split(new_line):
        lines += wrap_colored_line(line, width)
    return lines


# Paint a background effect under an already colored cell, re-applied after each color reset, so that it covers the whole cell.
def add_background(cell, background):
    return background + cell.replace(end_of_colors, end_of_colors + background) + end_of_colors
