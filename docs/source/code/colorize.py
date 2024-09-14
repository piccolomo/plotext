import plotext as plt

lines = '\n' * 2

plt.colorize("black on white, bold", "black",  "white", "bold").print(end = lines)

plt.colorize("red on green+, italic", "red",  "green+" , "italic").print(end = lines)

plt.colorize("yellow on blue+, flash", "yellow", "blue+",  "flash").print(end = lines)

plt.colorize("magenta on gray+, underlined", "magenta", "gray+" , "underline").print(end = lines)

plt.colorize("integer color codes", 201, 158).print(end = lines)

plt.colorize("RGB color codes", (16, 100, 200), (200, 100, 100)).print()