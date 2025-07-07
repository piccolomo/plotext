from plotext._cimport import pixel_class


# Default pixel configurations for docstring components
default_pixels = {
    "title": pixel_class(foreground = 'green+', style = 'bold'),
    "alias": pixel_class(style = 'italic'),
    "doc": pixel_class(style = 'default'),

    "parameters.label": pixel_class(foreground = 'cyan+', style = 'default'),
    "parameter.name": pixel_class(foreground = 'cyan+', style = 'default'),

    "parameter.type.label": pixel_class(foreground = 'orange+', style = 'dim'),
    "parameter.type": pixel_class(foreground = 'default', style = 'default'),

    "parameter.default.label": pixel_class(foreground = 'orange+', style = 'dim'),
    "parameter.default": pixel_class(foreground = 'default', style = 'default'),

    "parameter.doc": pixel_class(foreground = 'default', style = 'italic'),

    "output.name": pixel_class(foreground = 'default', style = 'bold'),
    "output.type.label": pixel_class(foreground = 'orange+', style = 'dim'),
    "output.type": pixel_class(foreground = 'default', style = 'default'),
    "output.doc": pixel_class(foreground = 'default', style = 'italic')
}
