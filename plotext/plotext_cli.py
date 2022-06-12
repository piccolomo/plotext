#!/usr/bin/env python

import plotext as plt
import argparse, sys, os

def build_parser():
    examples = """Access each function documentation for further guidance, eg: plotext scatter -h"""

    parser = argparse.ArgumentParser(
        prog            = "plotext",
        description     = "plotting directly on terminal",
        epilog          = examples,
        formatter_class = argparse.RawDescriptionHelpFormatter)

    parser.set_defaults(type = "scatter")

    path_parser = argparse.ArgumentParser(add_help = False)

    path_parser.add_argument("-p", "--path",
                             action = 'store',
                             #dest   = 'path',
                             type   = str,
                             help   = "file path of the data table; if not used it will read from stdin. Use 'test' to automatically download, in your user folder, some test data/image/gif or video, depending on the function used; the file will be removed after the plot")

    common_parser = argparse.ArgumentParser(add_help = False)
    
    common_parser.add_argument("-clt", "--clear_terminal",
                                nargs   = 1,
                                type = str,
                                default = ["False"],
                                choices = ["True", "False"],
                                help    = "it clears the terminal before plotting, if True (as by default)")

    common_parser.add_argument("-s", "--sleep",
                                nargs   = 1,
                                type = float,
                                default = [0],
                                help    = "it adds a sleeping time after plotting, to reduce flickering when multiple plots are required; 0 by default")

    data_parser = argparse.ArgumentParser(add_help = False)
    
    data_parser.add_argument("-xcol", "--xcolumn",
                         nargs   = "+", # 1 or more
                         type    = str,
                         default = ["none"],
                         help    = "the column number (starting from 1), in the data table, that will be used as x data; by default 'none'")

    data_parser.add_argument("-ycols", "--ycolumns",
                         nargs   = "+", # 1 or more
                         type    = str,
                        default = ["all"],
                        help = "the column numbers (starting from 1), in the data table, that will be used as y data; by default 'all'")

    data_parser.add_argument("-d", "--delimiter",
                         type    = str,
                         default = [' '],
                         nargs   = 1,
                         help    = "character to be used to separate columns in the data table (eg: ;); by default the white space ' '")

    data_parser.add_argument("-l", "--lines",
                         nargs   = "+", # 1 or more
                         type    = int,
                         default = [1000],
                         help    = "number of lines, from data table, to be plotted at each iteration; 1000 by default; data shorter then this will be plotted in a single iteration")
    
    options_parser = argparse.ArgumentParser(add_help = False)

    options_parser.add_argument("-m", "--marker",
                         type    = str,
                         default = ['hd'],
                         nargs   = 1,
                         help    = "character or marker code identifying the data points in the plot, eg: x, braille, sd, heart, fhd; by default hd")

    options_parser.add_argument("-c", "--color",
                         type    = str,
                         default = [None],
                         nargs   = 1,
                         help    = "color of the data points in the plot, between: black, white, red, green, orange, blue, magenta, cyan; add + at the end of the color (except black and white) for clearer colors, eg: red+")

    options_parser.add_argument("-t", "--title",
                         nargs   = 1,
                         type    = str,
                         default = [None],
                         help    = "the plot title")

    options_parser.add_argument("-xl", "--xlabel",
                         nargs   = 1,
                         type    = str,
                         default = [None],
                         help    = "the label of the x axis")

    options_parser.add_argument("-yl", "--ylabel",
                         nargs   = 1,
                         type    = str,
                         default = [None],
                         help    = "the label of the y axis")

    options_parser.add_argument("-g", "--grid",
                         nargs   = 1,
                         type = str,
                         default = ["False"],
                         choices = ["True", "False"],
                         help    = "it add grid lines if True, or removed them if False (as by default)")

    barhist_parser = argparse.ArgumentParser(add_help = False)

    barhist_parser.add_argument("-o", "--orientation",
                                nargs   = 1,
                                type = str,
                                default = ['v'],
                                choices = ['v', 'h'],
                                help    = "bar orientation, v for vertical (as by default), h for horizontal")

    barhist_parser.add_argument("-f", "--fill",
                                nargs   = 1,
                                type = str,
                                default = ["True"],
                                choices = ["True", "False"],
                                help    = "it fills the bars with colored markers if True (as by default), otherwise only the bars skeleton is shown")

    subparser = parser.add_subparsers(dest = 'type',
                                      help = 'the user defined plot type')

    scatter = subparser.add_parser('scatter',
                                   description = "plots a series of data points",
                                   parents = [path_parser, data_parser, common_parser, options_parser],
                                   help = 'plots a series of data points',
                                   epilog = "eg: plotext scatter --file test --columns 2 3 --marker hd --color red+ --title 'Test Scatter Plot' --xlabel Time --ylabel Price --grid True")


    plot = subparser.add_parser('plot',
                                parents = [path_parser, data_parser, common_parser, options_parser],
                                description = "plots lines between consecutive data points",
                                help = 'plots lines between consecutive data points',
                                epilog = "eg: plotext plot --file test --columns 1 3 --marker hd --color magenta --title 'Test Plot' --xlabel Time --ylabel Price --grid False")

    plotter = subparser.add_parser('plotter',
                                   parents = [path_parser, data_parser, common_parser, options_parser],
                                   description = 'plots a series of data points and the lines between consecutive ones', 
                                   help = 'scatter + plot',
                                   epilog = "eg: plotext plotter --file test --columns 1 2 --marker x --color blue+ --title 'Test Plotter' --xlabel x")
 
    bar = subparser.add_parser('bar',
                               parents = [path_parser, data_parser, common_parser, options_parser, barhist_parser],
                               description = 'builds a bar plot',
                               help = 'bar plot',
                               epilog = "eg: plotext bar --file test --columns 1 3 --marker sd --color red+ --fill False --width 0.5")

    bar.add_argument("-w", "--width",
                            nargs   = 1,
                            type = float,
                            default = [None],
                            help    = "bars width as a float between 0 and 1")

    hist = subparser.add_parser('hist',
                                parents = [path_parser, data_parser, common_parser, options_parser, barhist_parser],
                                description = 'builds a histogram plot',
                                help = 'histogram plot',
                                epilog = "eg: plotext hist --file test --columns 1 3 --marker sd --color orange+ --title 'Test Hist Plot' --fill True --bins 15")

    hist.add_argument("-b", "--bins",
                            nargs   = 1,
                            type = int,
                            default = [10],
                            help    = "histogram bins (10 by default)")
    
    image = subparser.add_parser('image',
                                 parents = [path_parser, common_parser],
                                 description = 'plots an image from path',
                                 help = 'plots an image from file path',
                                 epilog = "eg: plotext image --file test")
    
    gif = subparser.add_parser('gif',
                               parents = [path_parser, common_parser],
                               description = 'plays a gif image from path',
                               help = 'plays a gif image from path',
                               epilog = "eg: plotext gif --file test")

    video = subparser.add_parser('video',
                                 parents = [path_parser, common_parser],
                                 description = 'plays a video from path',
                                 help = 'plays a video from path',
                                 epilog = "eg: plotext video --file test --from_youtube True")

    video.add_argument("-fy", "--from_youtube",
                                nargs   = 1,
                                type = str,
                                default = ["False"],
                                choices = ["True", "False"],
                                help    = "set it to True to render the colors correctly for videos downloaded from youtube; default is False")

    youtube = subparser.add_parser('youtube',
                                   description = 'plays a youtube video from url',
                                   help = 'plays a youtube video from url',
                                   epilog = "eg: plotext youtube --url test")

    youtube.add_argument("-u", "--url",
                         action = 'store',
                         dest   = 'url',
                         nargs  = 1,
                         type   = str,
                         help   = "the url of a youtube video; use 'test' for a test video")
    
    return parser


#tc = lambda x: plt.colorize(x, 'green+', 'bold') # title color

#

def main(argv = None):
    parser = build_parser()
    args = parser.parse_args(argv)

    type = args.type
    if type != "youtube":
        path = args.path
        clt = True if args.clear_terminal[-1] == 'True' else False
        sleep = args.sleep[0]

    def get_xY(data):
        l = len(data)
        xcol = args.xcolumn[0]
        ycols = args.ycolumns
        xcol = "none" if xcol == "none" else int(xcol) if int(xcol) - 1 in range(l) else "none"
        all_ycols = [el for el in range(l) if el != xcol]
        ycols = all_ycols if ycols == ["all"] else [int(el) for el in ycols if int(el) - 1 in range(l)]
        x = list(range(1, len(data[0]) + 1)) if xcol == "none" else data[xcol - 1]
        Y = [data[i - 1] for i in ycols]
        return x, Y

    def plot(x, Y):
        for y in Y:
            plt.plot(x, y, marker = marker, color = color) if type in ['plot', 'plotter'] else None
            plt.scatter(x, y, marker = marker, color = None if type == 'plotter' else color) if type in ['scatter', 'plotter'] else None
            plt.bar(x, y, marker = marker, color = color, width = width, orientation = orientation, fill = fill) if type == 'bar' else None
            plt.hist(y, marker = marker, color = color, orientation = orientation, fill = fill, bins = bins) if type == 'hist' else None
        plt.clt() if clt else None
        plt.show()
        plt.cld()
        plt.sleep(sleep)
    
    data_plot = ['scatter', 'plot', 'plotter', 'bar', 'hist']
    test_path = 'test'
    
    if type in data_plot:
        lines = args.lines[0]
        delimiter = args.delimiter[0]
        title = args.title[0]
        xlabel = args.xlabel[0]
        ylabel = args.ylabel[0]
        grid = True if args.grid[-1] == 'True' else False

        orientation = args.orientation[0] if type in ['bar', 'hist']  else 'v'
        fill = args.fill[0] == 'True' if type in ['bar', 'hist'] else False
        width = args.width[0]  if type == 'bar' else 0
        bins = args.bins[0] if type in 'hist' else None
        
        marker = args.marker[0]
        color = args.color[0]

        plt.title(title);
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(grid)
        
        if path == test_path:
            plt.plotsize(None, plt.th() - 2)
            if type != "bar":
                plt.download(plt.test_data_url, test_path, log = False)
            else:
                plt.download(plt.test_bar_data_url, test_path, log = False)
            path = test_path
            
        if path is None:
            def plot_text(text):
                data = plt._utility.read_lines(text, delimiter = delimiter)
                data = plt.transpose(data)
                x, Y = get_xY(data)
                plot(x, Y)
            
            text = []
            i = 0
            for line in iter(sys.stdin.readline, ''):
                text.append(line)
                i+=1;
                if len(text) == lines:
                    plot_text(text)
                    text = []
            if len(text) > 0: # this is when there is some residual data to be plotted, not lines long
                plot_text(text)
                text = []

        else:
            data = plt.read_data(path, delimiter = delimiter)
            data = plt.transpose(data)
            x, Y = get_xY(data)
            chunks = len(x) // lines + (1 if len(x) % lines else 0)
            for c in range(chunks):
                xc = x[c * lines: (c + 1) * lines]
                Yc = [y[c * lines: (c + 1) * lines] for y in Y]
                plot(xc, Yc)

    elif type == 'image':
        if path == test_path:
            plt.plotsize(None, plt.th() - 1)
            plt.download(plt.test_image_url, test_path, log = False)
            path = test_path
        plt.image_plot(path, fast = True)
        plt.clt() if clt else None
        plt.show()

    elif type == 'gif':
        if path == test_path:
            plt.plotsize(None, plt.th() - 1)
            plt.download(plt.test_gif_url, test_path, log = False)
            path = test_path
        plt.play_gif(path)
        
    elif type == 'video':
        if path == test_path:
            plt.plotsize(None, plt.th() - 1)
            plt.download(plt.test_video_url, test_path, log = False)
            path = test_path
        from_youtube = True if args.from_youtube[-1] == 'True' else False
        plt.play_video(path, from_youtube)
    
    elif type == 'youtube':
        url = args.url[-1]
        url = plt.test_youtube_url if url == test_path else url
        plt.play_youtube(url)

    if os.path.isfile(test_path):
        plt.delete_file(test_path, True)

            
if __name__ == "__main__":
    sys.exit(main())
