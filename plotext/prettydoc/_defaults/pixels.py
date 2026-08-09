# Default pixel configurations for every docstring component (title, alias, parameters, output)

from plotext._primitives.pixel import pixel
from plotext._settings.defaults import doc_pixels


# Map from component name to its default pixel (colors and style)
default_pixels = {
    "title":                  doc_pixels["title"],
    "header":                 doc_pixels["header"],
    "section":                pixel(foreground = 'blue+',   style = 'bold'),
    "alias":                  pixel(                        style = 'italic'),
    "doc":                    pixel(                        style = 'default'),
    "attribute":              pixel(                        style = 'italic dim'),

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
