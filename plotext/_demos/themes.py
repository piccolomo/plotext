# The themes demo: a grid of mini plots, one per theme.

# Display available color themes as a grid of mini plots, one cell per theme
def themes():
    from math import sqrt, ceil
    from plotext._kernel.api import figure
    from plotext._settings.themes import themes as theme_registry
    from plotext._methods.sequence import sin

    names = list(theme_registry)
    rows = int(sqrt(len(names)))
    cols = ceil(len(names) / rows)
    y1, y2 = sin(periods = 1), sin(periods = 1.5)

    figure.clear()
    figure.subplots(rows, cols)
    for index, name in enumerate(names):
        sub = figure.subplot(index // cols + 1, index % cols + 1)
        sub.theme(name)
        sub.title(name)
        sub.draw(sub.signal(y1).label("sin"))
        sub.draw(sub.signal(y2).lines().label("-sin"))
    figure.show()
    figure.clear()
