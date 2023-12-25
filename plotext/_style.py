style_codes = ["bold", "dim", "italic", "underline", "double-underline", "strike", "inverted", "flash"]

def styles_to_integers(styles = None):
    integers = []
    styles = styles.split() if styles is not None else []
    for style in styles:
        if style in style_codes:
            index = style_codes.index(style)
            integers.append(index)
    return integers
