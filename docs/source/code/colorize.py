import plotext as plt

plt.colorize("black on white, bold", ("black", "white", "bold")).print()
print()

plt.colorize("red on green+, italic", ("red", "green+", "italic")).print()
print()

plt.colorize("yellow on blue+, flash", ("yellow", "blue+", "flash")).print()
print()

plt.colorize("magenta on gray+, underlined", ("magenta", "gray+", "underline")).print()
print()

plt.colorize("integer color codes", (201, 158)).print()
print()

plt.colorize("RGB color codes", ((16, 100, 200), (200, 100, 100))).print()
