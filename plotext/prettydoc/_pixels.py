from plotext._pixel import pixel


# Default pixel configurations for docstring components
default_pixels = {
    "title": pixel(foreground = 'green+', style = 'bold'),
    "alias": pixel(style = 'italic'),
    "doc": pixel(style = 'default'),

    "parameters.label": pixel(foreground = 'cyan+', style = 'default'),
    "parameter.name": pixel(foreground = 'cyan+', style = 'default'),

    "parameter.type.label": pixel(foreground = 'orange+', style = 'dim'),
    "parameter.type": pixel(foreground = 'default', style = 'italic'),

    "parameter.default.label": pixel(foreground = 'orange+', style = 'dim'),
    "parameter.default": pixel(foreground = 'default', style = 'italic'),

    "parameter.doc": pixel(foreground = 'default', style = 'default'),

    "output.name": pixel(foreground = 'default', style = 'bold'),
    "output.type.label": pixel(foreground = 'orange+', style = 'dim'),
    "output.type": pixel(foreground = 'default', style = 'italic'),
    "output.doc": pixel(foreground = 'default', style = 'italic')
}
