# /usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
###########    Initialization    #############
##############################################

from plotext._figure import _figure_class
import plotext._utility.doc as doc
import plotext._utility as _ut
from time import time as timing
from time import sleep as _sleep

figure = _figure_class()

##############################################
#########    Subplots Functions    ###########
##############################################

def subplots(rows = None, cols = None):
    return figure._active.subplots(rows, cols)

def subplot(row = None, col = None):
    return figure.subplot(row, col)

def main():
    return figure.main()

def active():
    return figure._active

##############################################
#######    Outside Set Functions    ##########
##############################################

def plot_size(width = None, height = None):
    return figure._active.plot_size(width, height)
plotsize = plot_size

def limit_size(width = None, height = None):
    #figure._master._set_size()
    return figure._master._limit_master_size(width, height)
limitsize = limit_size

def take_min():
    return figure._active.take_min()
takemin = take_min

def title(label):
    return figure._active.title(label)

def xlabel(label = None, xside = None):
    return figure._active.xlabel(label = label, xside = xside)

def ylabel(label = None, yside = None):
    return figure._active.ylabel(label = label, yside = yside)

def xlim(lower = None, upper = None, xside = None):
    return figure._active.xlim(lower = lower, upper = upper, xside = xside)

def ylim(left = None, right = None, yside = None):
    return figure._active.ylim(left = left, right = right, yside = yside)

def xscale(scale = None, xside = None):
    return figure._active.xscale(scale = scale, xside = xside)

def yscale(scale = None, yside = None):
    return figure._active.yscale(scale = scale, yside = yside)

def xticks(ticks = None, labels = None, xside = None):
    return figure._active.xticks(ticks = ticks, labels = labels, xside = xside)

def yticks(ticks = None, labels = None, yside = None):
    return figure._active.yticks(ticks = ticks, labels = labels, yside = yside)

def xfrequency(frequency = None, xside = None):
    return figure._active.xfrequency(frequency = frequency, xside = xside)

def yfrequency(frequency = None, yside = None):
    return figure._active.yfrequency(frequency = frequency, yside = yside)

def xaxes(lower = None, upper = None):
    return figure._active.xaxes(lower = lower, upper = upper)

def yaxes(left = None, right = None):
    return figure._active.yaxes(left = left, right = right)

def frame(frame = None):
    return figure._active.frame(frame = frame)

def grid(horizontal = None, vertical = None):
    return figure._active.grid(horizontal = horizontal, vertical = vertical)

def canvas_color(color = None):
    return figure._active.canvas_color(color)

def axes_color(color = None):
    return figure._active.axes_color(color)

def ticks_color(color = None):
    return figure._active.ticks_color(color)

def ticks_style(style = None):
    return figure._active.ticks_style(style)

def theme(theme = None):
    return figure._active.theme(theme)

##############################################
###########    Clear Functions    ############
##############################################

def clear_figure(): 
    figure._active.clear_figure()
clf = clear_figure

def clear_data(): 
    figure._active.clear_data()
cld = clear_data

def clear_color(): 
    figure._active.clear_color()
clc = clear_color

clear_terminal = _ut.clear_terminal
clt = clear_terminal

##############################################
######    Main Plotting Functions    #########
##############################################

def scatter(*args, xside = None, yside = None, marker = None, color = None, style = None, fillx = None, filly = None, label = None):
    figure._active.scatter(*args, xside = xside, yside = yside, marker = marker, color = color, style = style, fillx = fillx, filly = filly, label = label)

def plot(*args, xside = None, yside = None, marker = None, color = None, style = None, fillx = None, filly = None, label = None):
    figure._active.plot(*args, xside = xside, yside = yside, marker = marker, color = color,  fillx = fillx, filly = filly, label = label)

def error(*args, xerr = None, yerr = None, xside = None, yside = None, marker = None, color = None, label = None):
    figure.error(*args, xerr = xerr, yerr = yerr, xside = xside, yside = yside, marker = marker, color = color, label = label)

def candlestick(dates, data, orientation = None, colors = None, label = None):
    figure._active.candlestick(dates, data, orientation = orientation, colors = colors, label = label)

def bar(*args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
    figure._active.bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)

def multiple_bar(*args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
    figure._active.multiple_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)

def stacked_bar( *args, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
    figure._active.stacked_bar(*args, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)

def hist(data, bins = None, norm = None, xside = None, yside = None, marker = None, color = None, fill = None, width = None, orientation = None, label = None, minimum = None):
    figure._active.hist(data, bins = bins, norm = norm, xside = xside, yside = yside, marker = marker, color = color, fill = fill, width = width, orientation = orientation, label = label, minimum = minimum)

def matrix_plot(matrix, marker = None, style = None, fast = False):
    figure._active.matrix_plot(matrix, marker = marker, style = style, fast = fast)

def image_plot(path, marker = None, style = None, grayscale = False, fast = False):
    figure._active.image_plot(path, marker = marker, style = style, grayscale = grayscale, fast = fast)

##############################################
###########    Plotting Tools    #############
##############################################

def event_plot(data, orientation = None, marker = None, color = None, side = None):
    figure._active.event_plot(data, orientation = orientation, marker = marker, color = color, side = side)
eventplot = event_plot

def vertical_line(coordinate, color = None, xside = None):
    figure._active.vertical_line(coordinate, color = color, xside = xside)
vline = vertical_line

def horizontal_line(coordinate, color = None, yside = None):
    figure._active.horizontal_line(coordinate, color = color, yside = yside)
hline = horizontal_line

def text(text, x, y, xside = None, yside = None, color = None, style = None, alignment = None):
    figure._active.text(text, x, y, xside = xside, yside = yside, color = color, style = style, alignment = alignment)

##############################################
##########    Build Functions    #############
##############################################

def show():
    figure.show()

def build():
    return figure.build()

def sleep(time = 0):
    _sleep(time)

def time(show = True):
    return figure._get_time(show)

def save_fig(path = None, keep_colors = False):
    figure.save_fig(path, keep_colors)
savefig = save_fig

##############################################
##########     Date Functions    #############
##############################################

def date_form(input_form = None, output_form = None):
    figure._active.date_form(input_form, output_form)
    
def set_time0(string, input_form = None):
    return figure._active.set_time0(string, input_form = input_form)

def today_datetime():
    return figure._active.today_datetime()

def today_string(output_form = None):
    return figure._active.today_string(output_form)

def datetime_to_string(datetimes, output_form = None):
    return figure._active.datetime_to_string(datetimes, output_form = output_form)

def datetimes_to_string(datetimes, output_form = None):
    return figure._active.datetimes_to_string(datetimes, output_form = output_form)

def string_to_datetime(string, input_form = None):
    return figure._active.string_to_datetime(string, input_form = input_form)

def string_to_time(string, input_form = None):##########ADD DOC############
    return figure._active.string_to_time(string, input_form = input_form)

def strings_to_time(string, input_form = None):##########ADD DOC############
    return figure._active.strings_to_time(string, input_form = input_form)

##############################################
##########     Other Functions    ############
##############################################

def colorize(string, fullground = None, style = None, background = None, show = False):
    return _ut.colorize(string, fullground = fullground, style = style, background = background, show = show)

def uncolorize(string):
    return _ut.uncolorize(string)

terminal_size = _ut.terminal_size
ts = terminal_size

terminal_width = lambda: ts()[0]
tw = terminal_width

terminal_height = lambda: ts()[1]
th = terminal_height


version = _ut.version

platform = _ut.platform


colors = _ut.colors_doc

styles = _ut.styles_doc


def sin(periods = 2, length = 200, amplitude = 1, phase = 0, decay = 0):
    return _ut.sin(periods = periods, length = length, amplitude = amplitude, phase = phase, decay = decay)

def transpose(data):
    return _ut.transpose(data)

script_folder = _ut.script_folder

def parent_folder(path, level = 1):
    return _ut.parent_folder(path, level = level)

def join_paths(*args):
    return _ut.join_paths(*args)

def save_text(text, path, log = True):
    return _ut.save_text(text, path, log = log)

def read_data(path, delimiter = None, columns = None):
    return _ut.read_data(path, delimiter = delimiter, columns = columns)

def write_data(data, path, delimiter = None, columns = None, log = True):
    return _ut.write_data(data, path, delimiter = delimiter, columns = columns, log = log)

def download(url, path, log = True):
    return _ut.download(url, path, log)

def delete_file(path, log = True):
    return _ut.delete_file(path, log = log)

test_data_url = "https://raw.githubusercontent.com/piccolomo/plotext/master/images/data.txt"
test_bar_data_url = "https://raw.githubusercontent.com/piccolomo/plotext/master/images/bar_data.txt"
test_image_url  = "https://raw.githubusercontent.com/piccolomo/plotext/master/images/cat.jpg"
test_gif_url    = "https://raw.githubusercontent.com/piccolomo/plotext/master/images/homer.gif"
test_video_url  = "https://raw.githubusercontent.com/piccolomo/plotext/master/images/moonwalk.mp4"
test_youtube_url = 'https://www.youtube.com/watch?v=2Z4s8xbuegQ'

##############################################
##########     Video Functions    ############
##############################################

def play_gif(path):
    from PIL import Image, ImageSequence
    path = _ut.correct_path(path)
    if not _ut.is_file(path):
        return
    im = Image.open(path)
    index = 1
    for image in ImageSequence.Iterator(im):
        load_time = timing()
        clt()
        image = image.convert('RGB')
        figure.monitor._draw_image(image, fast = True)
        show()
        load_time = timing() - load_time
        frame_time = image.info['duration'] / 10 ** 3
        if load_time < frame_time:
             sleep(frame_time - load_time)

def play_video(path, from_youtube = False):
    path = _ut.correct_path(path)
    if not _ut.is_file(path):
        return
    _play_video(path, from_youtube)


def play_youtube(url):
    import pafy
    video = pafy.new(url)
    best = video.getbest()
    _play_video(best.url, from_youtube = True)

def get_youtube(url, path):
    import pafy
    video = pafy.new(url)
    best = video.getbest(preftype = "mp4")
    path = _ut.correct_path(path)
    path = best.download(filepath = path)
    print('video downloaded in', path)
    return path

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
    pt = lambda time: f'{round(10 ** 3 * time, 1):05.1f}' + '  '
    real_time = video_time = 0
    while True:
        load_time = timing()
        check_video, frame = cap.read();
        audio, check_audio = player.get_frame(show = False)
        load_time = timing() - load_time
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
            show_time = timing()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) if from_youtube else frame
            #frame = to_list(frame)
            image = Image.fromarray(frame)
            clt()
            figure.monitor._draw_image(image, fast = True)
            show()
            show_time = timing() - show_time
        sleep_time = 0
        if real_time < video_time:
            sleep_time = timing()
            sleep(video_time - real_time)
            sleep_time = timing() - sleep_time
        total_time = load_time + show_time + sleep_time
        real_time += show_time + sleep_time
        #print('load: ' + pt(load_time), 'show: ' + pt(show_time), 'sleep: ' + pt(sleep_time), 'total: ' + pt(total_time), 'frame: ' + pt(frame_time), 'real: ' + pt(real_time), 'video: ' + pt(video_time), 'r/v:', round(real_time / video_time, 3)) if shown else None
    player.close_player()
    cap.release()
    cv2.destroyAllWindows()
    clf()

##############################################
#########     Matplotlib Backend    ##########
##############################################

def from_matplotlib(fig):
    fig.canvas.draw()
    slots = (rows, cols) = fig.axes[0].get_subplotspec().get_gridspec().get_geometry()
    main().clf(); #clt()
    subplots(*slots)
    round10 = lambda data: [round(el, 10) for el in data]
    to_rgb = lambda rgb_norm: tuple([round(255 * el) for el in rgb_norm[:3]])
    axes_color(to_rgb(fig.patch.get_facecolor()))
    for sub in fig.axes[:]:
        p = sub.get_geometry()[2]
        row = int((p - 1) / cols + 1)
        col = p - (row - 1) * cols
        subplot(row, col)
        xlabel(sub.get_xlabel())
        ylabel(sub.get_ylabel())
        title(sub.get_title())
        xscale(sub.get_xscale())
        yscale(sub.get_yscale())
        xticks(round10(sub.get_xticks()))
        yticks(round10(sub.get_yticks()))
        canvas_color(to_rgb(sub.get_facecolor()))
        for point in sub.collections:
            label = point.get_label()
            label = label if label[0] != '_' else ''
            #point.set_offset_position('data')
            x, y = _ut.transpose(point.get_offsets())
            color = [to_rgb(point.to_rgba(el)) for el in point.get_facecolors()[0]]
            # can't find the right point colors
            scatter(x, y, label = label, marker= 'x')
        for line in sub.get_lines():
            label = line.get_label()
            label = label if label[0] != '_' else ''
            x, y = line.get_data()
            plot(x, y, color = line.get_c(), label = label)
        for b in sub.patches:
            label = b.get_label()
            label = label if label[0] != '_' else ''
            color = b.get_facecolor()
            color = to_rgb(color)
            box = b.get_bbox()
            x0, y0, x1, y1 = box.x0, box.y0, box.x1, box.y1
            x = [x0, x0, x1, x1, x0]
            y = [y0, y1, y1, y0, y0]
            fill = b.get_fill()
            fillx = fill if y0 == 0 else False
            filly = fill if x0 == 0 else False
            plot(x, y, fillx = fillx, filly = filly, color = color, label = label)
        xlim(*sub.get_xlim())
        ylim(*sub.get_ylim())
        
##############################################
############     Docstrings    ###############
##############################################        

subplots.__doc__ = doc._subplots
subplot.__doc__ = doc._subplot
main.__doc__ = doc._main
active.__doc__ = doc._active

plot_size.__doc__ = doc._plot_size
limit_size.__doc__ = doc._limit_size
take_min.__doc__ = doc._take_min

title.__doc__ = doc._title
xlabel.__doc__ = doc._xlabel
ylabel.__doc__ = doc._ylabel
xlim.__doc__ = doc._xlim
ylim.__doc__ = doc._ylim
xscale.__doc__ = doc._xscale
yscale.__doc__ = doc._yscale
xticks.__doc__ = doc._xticks
yticks.__doc__ = doc._yticks
xfrequency.__doc__ = doc._xfrequency
yfrequency.__doc__ = doc._yfrequency
xaxes.__doc__ = doc._xaxes
yaxes.__doc__ = doc._yaxes
frame.__doc__ = doc._frame
grid.__doc__ = doc._grid
canvas_color.__doc__ = doc._canvas_color
axes_color.__doc__ = doc._axes_color
ticks_color.__doc__ = doc._ticks_color
ticks_style.__doc__ = doc._ticks_style
theme.__doc__ = doc._theme

clear_figure.__doc__ = doc._clear_figure
clear_data.__doc__ = doc._clear_data
clear_color.__doc__ = doc._clear_color
clear_terminal.__doc__ = doc._clear_terminal

scatter.__doc__ = doc._scatter
plot.__doc__ = doc._plot
candlestick.__doc__ = doc._candlestick
bar.__doc__ = doc._bar
multiple_bar.__doc__ = doc._multiple_bar
stacked_bar.__doc__ = doc._stacked_bar
hist.__doc__ = doc._hist
matrix_plot.__doc__ = doc._matrix_plot
image_plot.__doc__ = doc._image_plot

event_plot.__doc__ = doc._event_plot
vertical_line.__doc__ = doc._vertical_line
horizontal_line.__doc__ = doc._horizontal_line
text.__doc__ = doc._text

show.__doc__ = doc._show
build.__doc__ = doc._build
sleep.__doc__ = doc._sleep
time.__doc__ = doc._time
save_fig.__doc__ = doc._save_fig

date_form.__doc__ = doc._date_form
set_time0.__doc__ = doc._set_time0
today_datetime.__doc__ = doc._today_datetime
today_string.__doc__ = doc._today_string
datetime_to_string.__doc__ = doc._datetime_to_string
datetimes_to_string.__doc__ = doc._datetimes_to_string
string_to_datetime.__doc__ = doc._string_to_datetime

colorize.__doc__ = doc._colorize
uncolorize.__doc__ = doc._uncolorize
terminal_size.__doc__ = doc._terminal_size
terminal_width.__doc__ = doc._terminal_width
terminal_height.__doc__ = doc._terminal_height

version.__doc__ = doc._version

sin.__doc__ = doc._sin

script_folder.__doc__ = doc._script_folder
parent_folder.__doc__ = doc._parent_folder
join_paths.__doc__ = doc._join_paths
save_text.__doc__ = doc._save_text
read_data.__doc__ = doc._read_data
write_data.__doc__ = doc._write_data
download.__doc__ = doc._download
delete_file.__doc__ = doc._delete_file

play_gif.__doc__ = doc._play_gif
play_video.__doc__ = doc._play_video
play_youtube.__doc__ = doc._play_youtube
get_youtube.__doc__ = doc._get_youtube

from_matplotlib.__doc__ = doc._from_matplotlib
