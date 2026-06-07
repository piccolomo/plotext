# Structural converter: walks a matplotlib Figure (subplot grid, axes, lines, scatters, patches) and rebuilds it onto plt.figure as native plotext signals. Improvements over the old plotext 5.x adapter: cleaner subplot detection via rowspan/colspan, uses the OO API directly (no separate monitor abstraction), gracefully skips empty/no-color cases. matplotlib is imported lazily so plotext doesn't carry it as a hard dependency.


def matplotlib(mpl_fig):
    from matplotlib.colors import to_rgb as _to_rgb
    from plotext._kernel.api import figure
    from plotext._primitives.pixel import pixel
    from plotext._primitives.marker import marker

    mpl_fig.canvas.draw()
    fig = figure
    fig.clear()
    if not mpl_fig.axes:
        return fig

    rows, cols = mpl_fig.axes[0].get_subplotspec().get_gridspec().get_geometry()
    if (rows, cols) != (1, 1):
        fig.subplots(rows, cols)
    rgb = lambda c: tuple(round(255 * x) for x in _to_rgb(c))   # accepts any mpl colour spec (name, hex, tuple)
    fig.canvas_pixel(pixel(background = rgb(mpl_fig.patch.get_facecolor())))

    for ax in mpl_fig.axes:
        spec = ax.get_subplotspec()
        sub = fig.subplot(spec.rowspan.start + 1, spec.colspan.start + 1) if (rows, cols) != (1, 1) else fig

        if ax.get_title():  sub.title(ax.get_title())
        if ax.get_xlabel(): sub.label(ax.get_xlabel(), axis = 'x')
        if ax.get_ylabel(): sub.label(ax.get_ylabel(), axis = 'y')
        sub.canvas_pixel(pixel(background = rgb(ax.get_facecolor())))

        for line in ax.get_lines():
            label = line.get_label()
            label = None if not label or label.startswith('_') else label
            x, y = line.get_data()
            m = marker(pixel = pixel(foreground = rgb(line.get_color())))
            sig = sub.signal(list(x), list(y), marker = m).lines(True)
            if label: sig.label(label)
            sub.draw(sig)

        for coll in ax.collections:
            offsets = coll.get_offsets()
            if len(offsets) == 0:
                continue
            label = coll.get_label()
            label = None if not label or label.startswith('_') else label
            xs, ys = zip(*offsets)
            facecolors = coll.get_facecolors()
            m = marker('x', pixel = pixel(foreground = rgb(facecolors[0]))) if len(facecolors) else 'x'
            sig = sub.signal(list(xs), list(ys), marker = m)
            if label: sig.label(label)
            sub.draw(sig)

        for patch in ax.patches:
            bbox, color = patch.get_bbox(), rgb(patch.get_facecolor())
            m = marker(pixel = pixel(foreground = color))
            sub.draw(sub.rectangle((bbox.x0, bbox.x1), (bbox.y0, bbox.y1),
                                    marker = m, fill = patch.get_fill()))

    return fig
