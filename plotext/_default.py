from plotext._system import platform


class default_terminal():
    width = 211 * 2 // 3
    height = 53 * 2 // 3
    size = width, height
    prompt_height = 3

    
class default_master():
    limit_width = True
    limit_height = True
    interactive = False


class default_subplot():
    size_direction = 1

    
class default_settings():
    ticks_color = "black"
    axes_color = "white"
    canvas_color = 'white'

    marks_style = 'normal'
    marks_styles = ['normal', 'rounded', 'doubled', 'dotted']

    frame = True
    xfrequency = 5
    yfrequency = 7

    xdirection = 1
    ydirection = 1

    scales = ['linear', 'log']
    scale = 'linear'

    scales = ['linear', 'log']
    scale = scales[0]

        
class default_signal():
    marker = 'x'
    color = 'blue+'
    style = None
    fills = [False, True, 'internal']
    fill = fills[0] # same for x and y
    xsides = ["lower", "upper"] # the two possibilities, the first is default
    ysides = ["left", "right"] # the two possibilities, the first is default
    xside = xsides[0]
    yside = ysides[0]
    lines = False

    
class default_datetime_converter():
    form = '%d/%m/%Y'
    time0 = '01/01/1900'
    zone = 'utc'

        
default_terminal = default_terminal()
default_master = default_master()
default_subplot = default_subplot()
default_settings = default_settings()
default_signal = default_signal()
default_datetime_converter = default_datetime_converter()




