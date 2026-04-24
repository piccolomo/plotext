# Default pixel configurations for every docstring component (title, alias, parameters, output)

from plotext._primitives.pixel import pixel


# Map from component name to its default pixel (colors and style)
default_pixels = {
    "title":                  pixel(foreground = 'green+',  style = 'bold'),
    "alias":                  pixel(                        style = 'italic'),
    "doc":                    pixel(                        style = 'default'),

    "parameters.label":       pixel(foreground = 'cyan+',   style = 'default'),
    "parameter.name":         pixel(foreground = 'cyan+',   style = 'default'),

    "parameter.type.label":   pixel(foreground = 'orange+', style = 'dim'),
    "parameter.type":         pixel(foreground = 'default', style = 'italic'),

    "parameter.default.label": pixel(foreground = 'orange+', style = 'dim'),
    "parameter.default":      pixel(foreground = 'default', style = 'italic'),

    "parameter.doc":          pixel(foreground = 'default', style = 'default'),

    "output.name":            pixel(foreground = 'default', style = 'bold'),
    "output.type.label":      pixel(foreground = 'orange+', style = 'dim'),
    "output.type":            pixel(foreground = 'default', style = 'italic'),
    "output.doc":             pixel(foreground = 'default', style = 'italic'),
}
