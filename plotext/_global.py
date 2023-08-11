# This file contains some plotext functions which are only available to the top main level and not to sub figures (which are written in _figure.py and _monitor.py). These are functions which requires some coding and would be too long to be added directly in _core.py

from plotext._utility import marker_codes, hd_symbols, sin
from plotext._figure import _figure_class
from plotext._utility import themes as _themes
import plotext._utility as ut
from time import time, sleep
from math import sqrt, ceil
import datetime as dt

figure = _figure_class() # the main figure at top level

##############################################
#######     Simple  Bar Functions    ########
##############################################

def simple_bar(*args, width = None, marker = None, color = None, title = None):
    x, y = ut.set_data(*args)
    marker = ut.correct_marker(marker)

    color_ok = ut.is_color(color) or (isinstance(color, list) and len(color) == len(x))
    color = [color] if color_ok else None

    simple_stacked_bar(x, [y], width = width, marker = marker, colors = color, title = title)

def simple_stacked_bar(*args, width = None, marker = None, colors = None, title = None, labels = None):
    x, y, Y, width = ut.bar_data(*args, width = width)
    marker = ut.correct_marker(marker)
    
    bars = len(Y); stacked_bars = len(Y[0])

    colors_ok1 = isinstance(colors, list) and isinstance(colors[0], list) and ut.matrix_size(colors) == [bars, stacked_bars]
    colors_ok2 = isinstance(colors, list) and len(colors) == stacked_bars
    colors = ut.transpose(colors) if colors_ok1 else [colors] * bars if colors_ok2 else [ut.color_sequence[:stacked_bars]] * bars

    title = ut.get_title(title, width)
    bars = [ut.single_bar(x[i], Y[i], y[i], marker, colors[i]) for i in range(bars)]
    labels = ut.get_simple_labels(marker, labels, colors[0], width)
    figure.monitor.matrix.canvas = title + '\n'.join(bars) + labels 
    figure.monitor.fast_plot = True

def simple_multiple_bar(*args, width = None, marker = None, colors = None, title = None, labels = None):
    x, y, Y, width = ut.bar_data(*args, width = width, mode='multiple')
    bars = len(Y); multiple_bars = len(Y[0]); lx = len(x[0])
    marker = ut.correct_marker(marker)

    colors_ok = isinstance(colors, list) and len(colors) == multiple_bars
    colors = colors if colors_ok else ut.color_sequence[:multiple_bars]

    out = ut.get_title(title, width)
    for i in range(bars):
        xn = [x[i] if j == (multiple_bars - 1) // 2 else ut.space * lx for j in range(multiple_bars)]
        new = [ut.single_bar(xn[j], [Y[i][j]], y[j][i], marker, [colors[j]]) for j in range(multiple_bars)]
        out += '\n'.join(new)
        out += '\n\n' if i != bars - 1 else ''
    labels = ut.get_simple_labels(marker, labels, colors, width)
    figure.monitor.matrix.canvas = out + labels
    figure.monitor.fast_plot = True

##############################################
#############     Play GIF    ################
##############################################

def play_gif(path):
    from PIL import Image, ImageSequence
    path = ut.correct_path(path)
    if not ut.is_file(path):
        return
    im = Image.open(path)
    index = 1
    for image in ImageSequence.Iterator(im):
        load_time = time()
        figure.clt()
        image = image.convert('RGB')
        figure.monitor._draw_image(image, fast = True)
        figure.show()
        load_time = time() - load_time
        frame_time = image.info['duration'] / 10 ** 3
        if load_time < frame_time:
            sleep(frame_time - load_time)
                
##############################################
##########     Video Functions    ############
##############################################

def play_video(path, from_youtube = False):
    path = ut.correct_path(path)
    if not ut.is_file(path):
        return
    _play_video(path, from_youtube)

def play_youtube(url):
    import pafy
    video = pafy.new(url)
    best = video.getbest()
    _play_video(best.url, from_youtube = True)

def get_youtube(url, path, log):
    import pafy
    video = pafy.new(url)
    best = video.getbest(preftype = "mp4")
    path = "youtube-video.mp4" if path is None else path
    path = ut.correct_path(path)
    best.download(filepath = path, quiet = not log)
    print(ut.format_strings('YouTube video downloaded as', path)) if log else None

def _play_video(path, from_youtube = False):
    import cv2
    from ffpyplayer.player import MediaPlayer
    from PIL import Image
    cap = cv2.VideoCapture(path)
    player = MediaPlayer(path)#, paused = True, loglevel = 'quiet');
    fr = 0;
    while fr == 0:
        fr = cap.get(cv2.CAP_PROP_FPS)
    frame_time = 1 / fr 
    #to_list = lambda frame: [[tuple(int(el) for el in tup) for tup in row] for row in frame]
    pt = lambda time: '{time:05.1f}  '.format(time=round(10 ** 3 * time, 1))
    real_time = video_time = 0
    while True:
        load_time = time()
        check_video, frame = cap.read();
        audio, check_audio = player.get_frame(show = False)
        load_time = time() - load_time
        if not check_video:
            break
        if load_time >= frame_time:
            continue
        real_time += load_time
        video_time += frame_time
        show_time = 0
        shown = False
        if video_time >= real_time:
            shown = True
            show_time = time()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if from_youtube else frame
            #frame = to_list(frame)
            image = Image.fromarray(frame)
            figure.clt()
            figure.monitor._draw_image(image, fast = True)
            figure.show()
            show_time = time() - show_time
        sleep_time = 0
        if real_time < video_time:
            sleep_time = time()
            sleep(video_time - real_time)
            sleep_time = time() - sleep_time
        total_time = load_time + show_time + sleep_time
        real_time += show_time + sleep_time
        #print('load: ' + pt(load_time), 'show: ' + pt(show_time), 'sleep: ' + pt(sleep_time), 'total: ' + pt(total_time), 'frame: ' + pt(frame_time), 'real: ' + pt(real_time), 'video: ' + pt(video_time), 'r/v:', round(real_time / video_time, 3)) if shown else None
    player.close_player()
    cap.release()
    cv2.destroyAllWindows()
    figure.clf()

##############################################
############     Utilities     ###############
##############################################

test_data_url = "https://raw.githubusercontent.com/piccolomo/plotext/master/data/data.txt"
test_bar_data_url = "https://raw.githubusercontent.com/piccolomo/plotext/master/data/bar_data.txt"
test_image_url  = "https://raw.githubusercontent.com/piccolomo/plotext/master/data/cat.jpg"
test_gif_url    = "https://raw.githubusercontent.com/piccolomo/plotext/master/data/homer.gif"
test_video_url  = "https://raw.githubusercontent.com/piccolomo/plotext/master/data/moonwalk.mp4"
test_youtube_url = 'https://www.youtube.com/watch?v=ZNAvVVc4b3E&t=75s'

##############################################
#########     Matplotlib Backend    ##########
##############################################

def from_matplotlib(fig, marker = None):
    fig.canvas.draw()
    slots = (rows, cols) = fig.axes[0].get_subplotspec().get_gridspec().get_geometry()
    figure.clf(); #clt()
    figure.subplots(*slots)
    round10 = lambda data: [round(el, 10) for el in data]
    to_rgb = lambda rgb_norm: tuple([round(255 * el) for el in rgb_norm[:3]])
    figure.axes_color(to_rgb(fig.patch.get_facecolor()))
    for sub in fig.axes[:]:
        p = sub.get_subplotspec().get_geometry()[2]
        row = int((p - 0) / cols + 1)
        col = p + 1 - (row - 1) * cols
        monitor = figure.subplot(row, col)
        monitor.xlabel(sub.get_xlabel())
        monitor.ylabel(sub.get_ylabel())
        monitor.title(sub.get_title())
        monitor.xscale(sub.get_xscale())
        monitor.yscale(sub.get_yscale())
        monitor.xticks(round10(sub.get_xticks()))
        monitor.yticks(round10(sub.get_yticks()))
        monitor.canvas_color(to_rgb(sub.get_facecolor()))
        for point in sub.collections:
            label = point.get_label()
            label = label if label[0] != '_' else ''
            #point.set_offset_position('data')
            x, y = ut.transpose(point.get_offsets())
            color = [ut.to_rgb(point.to_rgba(el)) for el in point.get_facecolors()[0]]
            # can't find the right point colors
            monitor.scatter(x, y, label = label, marker = marker)
        for line in sub.get_lines():
            label = line.get_label()
            label = label if label[0] != '_' else ''
            x, y = line.get_data()
            monitor.plot(x, y, marker = marker, color = line.get_c(), label = label)
        for b in sub.patches:
            label = b.get_label()
            label = label if label[0] != '_' else ''
            color = b.get_facecolor()
            color = ut.to_rgb(color)
            box = b.get_bbox()
            x0, y0, x1, y1 = box.x0, box.y0, box.x1, box.y1
            x = [x0, x0, x1, x1, x0]
            y = [y0, y1, y1, y0, y0]
            fill = b.get_fill()
            fillx = fill if y0 == 0 else False
            filly = fill if x0 == 0 else False
            monitor.plot(x, y, fillx = fillx, filly = filly, marker = marker, color = color, label = label)
        monitor.xlim(*sub.get_xlim())
        monitor.ylim(*sub.get_ylim())

##############################################
#######     Presentation Functions    ########
##############################################
        
def markers():
    markers = list(hd_symbols.keys())[::-1] + list(marker_codes.keys())
    l = len(markers)
    rows = int(sqrt(l))
    cols = ceil(l / rows)
    y = ut.sin(1)
    figure.clf(); figure.theme('pro'); figure.xfrequency(0); figure.yfrequency(0); figure.frame(1)
    figure.subplots(rows, cols)
    figure.frame(0)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                subplot = figure.subplot(row, col)
                figure.frame(1)
                default = ' [default]' if markers[i] == 'hd' else ''
                subplot.title(markers[i] + default)
                subplot.scatter(y, marker = markers[i])
                subplot.ticks_style('bold')
                #figure.ticks_color(figure._utility.title_color)
    figure.show()
    figure.clf()

def colors():
    print(ut.colorize("String Color Codes", style = 'bold'))
    bg = "default"
    c = ut.no_duplicates([el.replace('+', '') for el in ut.colors if el not in ['default', 'black', 'white']])
    cp = [ut.colorize(ut.pad_string(el + '+', 10), el + '+', background = bg) for el in c]
    c = [ut.colorize(ut.pad_string(el, 10), el, background = bg) for el in c]
    c = [' ' + c[i]  + cp[i] for i in range(len(c))]
    c = '\n'.join(c)
    print(' ' + ut.colorize(ut.pad_string('default', 20), background = bg))
    print(' ' + ut.colorize(ut.pad_string('black', 10), 'black', background = 'gray') + ut.colorize(ut.pad_string('white', 10), 'white', background = bg))
    print(c)
    print()
    #print(colorize("\n\nInteger Color Codes:", style = ''))
    c = ut.colorize("Integer Color Codes", style = 'bold', show = False) + '\n'
    for row in range(16):
        cr = ' '
        for col in range(16):
            i = row * 16 + col
            cr += ut.colorize(ut.pad_string(i, 5), i)
        c += cr + '\n'
    print(c)
    c = '\n'
    rgb = (100, 200, 85)
    rgb_string = '(' + ', '.join([str(el) for el in rgb]) + ')'
    print(ut.colorize("RGB Tuples like:", style = "bold"), ut.colorize(rgb_string, rgb, "bold"))

def styles():
    from plotext._utility import styles, colorize, title_color
    c = [colorize(el, style = el) for el in styles]
    c = '\n'.join(c)
    print(c)
    mul = 'bold italic dim'
    print('\n' + colorize('multiple styles are accepted, ', title_color) + 'eg: ' + colorize(mul, style = mul))

def themes():
    themes = list(_themes.keys())[::]
    l = len(themes)
    rows = int(sqrt(l))
    cols = ceil(l / rows)
    y1 = ut.sin(periods = 1)
    y2 = ut.sin(periods = 1, phase = -1)
    figure.clf()
    figure.subplots(rows, cols)
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            i = (row - 1) * cols + col - 1
            if i < l:
                subplot = figure.subplot(row, col)
                subplot.theme(themes[i])
                subplot.title(themes[i])
                subplot.scatter(y1); subplot.plot(y2)
    figure.show()
    figure.clf()

##############################################
###########     Test Function    #############
##############################################

def test():
    import random
    figure.clf(); figure.clt()
    figure.date_form("d/m/Y");
    figure.take_min()
    figure.plot_size(None, ut.terminal_height())
    #figure.plot_size(108, 70)
    
    figure.plotsize(ut.tw(), ut.th() - 5)
    figure.subplots(2, 2)
    
    subplot = figure.subplot(1, 1)
    subplot.title("Multiple Axes Plot")
    subplot.canvas_color(66); subplot.axes_color(4); subplot.ticks_color(216); subplot.ticks_style('bold italic')
    y = ut.sin(periods = 1); l = len(y)
    subplot.scatter(y, label = "lower left")
    x = [figure.today_datetime() + dt.timedelta(days = i) for i in range(l)]; x = figure.datetimes_to_strings(x)
    subplot.plot(x, x, label = 'upper right - all dates', xside = 2, yside = 2)
    subplot.vline(l / 2, 'red')
    subplot.hline(0, 200)
    subplot.text("origin", l // 2, 0, color = 'red', alignment = 'center')
    subplot.xlabel('x lower'); subplot.xlabel('x upper', 2)
    subplot.ylabel('y left', 'left'); subplot.ylabel('y right', 'right')
    subplot.xfrequency(8); subplot.xfrequency(5, 2);
    subplot.yfrequency(3); subplot.yfrequency(5, 2);
    subplot.grid(1,1)
    
    subplot = figure.subplot(1, 2)
    subplot.theme('innocent')
    xb = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
    y1 = [36, 14, 11, 8, 7, 4]
    y2 = [20, 12, 35, 15, 4, 5]
    subplot.stacked_bar(xb, [y1, y2], labels = ["men", "women"])

    subplot = figure.subplot(2, 1)
    subplot.theme('dreamland')
    ld = 7 * 10 ** 4
    data = [random.gauss(0, 1) for el in range(10 * ld)]
    subplot.hist(data, bins = 60, label="mean 0")
    subplot.frame(1); #subplot.xaxes(1, 0); subplot.yaxes(1, 0)
    
    subplot = figure.subplot(2, 2)
    subplot.canvas_color('gray+'); subplot.axes_color('gray+')
    ut.download(test_image_url, 'cat.jpg')
    subplot.image_plot('cat.jpg', grayscale = False)
    ut.delete_file('cat.jpg')
    subplot.title('A very Cute Cat')
    subplot.frame(0)

    #figure.plotsize(0, 0)
    figure.show()
    figure._get_time()
    figure.save_fig('test.txt')
    figure.save_fig('test.html')
    #figure.clf()

