#!/usr/bin/env python

import plotext as plt
import argparse, sys
cl = plt.colorize


def main(argv = None):
    parser = build_parser()
    args = parser.parse_args(argv)
    plot(args)

    
def build_parser():
    examples = """Access each function documentation for further guidance. eg: plotext scatter -h"""

    parser = argparse.ArgumentParser(
        prog            = "plotext",
        description     = "plotting directly on terminal",
        epilog          = examples,
        formatter_class = argparse.RawDescriptionHelpFormatter)

    parser.set_defaults(type = "scatter")

    file_parser = argparse.ArgumentParser(add_help = False)

    file_parser.add_argument("-f", "--file",
                             action = 'store',
                             dest   = 'file',
                             type   = str,
                             help   = "file path of the data table, if not used it will read from stdin. Use 'test_data' to access some internally saved 3 column test data; 'test_image' for a test image; 'test_gif' for a test gif image; 'test_video' for a test video.")

    data_parser = argparse.ArgumentParser(add_help = False)

    data_parser.add_argument("-col", "--columns",
                         nargs   = "+", # 1 or more
                         type    = int,
                         default = [1],
                         help    = "columns from data table to plot, starting from 1. The first one provided is for the x data.")

    data_parser.add_argument("-d", "--delimiter",
                         type    = str,
                         default = [' '],
                         nargs   = 1,
                         help    = "character to be used to separate columns in data file, eg: ';', default is ' ', use apostrophes before and after 'delimiter' to avoid confusion")

    options_parser = argparse.ArgumentParser(add_help = False)

    options_parser.add_argument("-m", "--marker",
                         type    = str,
                         default = ['hd'],
                         nargs   = 1,
                         help    = "character to be used as marker for the data points, eg: 'x', 'sd', 'heart', 'fhd', 'hd' (by default), use apostrophes before and after 'marker' to avoid confusion")

    options_parser.add_argument("-c", "--color",
                         type    = str,
                         default = [None],
                         nargs   = 1,
                         help    = "color used for the data points, between: black, white, red, green, orange, blue, magenta, cyan; add + at the end of the color (except black and white) for clearer colors, eg: red+")

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
                         help    = "add grid lines if True, removed them if False (as by default)")

    barhist_parser = argparse.ArgumentParser(add_help = False)

    barhist_parser.add_argument("-o", "--orientation",
                                nargs   = 1,
                                type = str,
                                default = ['v'],
                                choices = ['v', 'h'],
                                help    = "bar orientation, 'v' for vertical (as by default), 'h' for horizontal")

    barhist_parser.add_argument("-fi", "--fill",
                                nargs   = 1,
                                type = str,
                                default = ["False"],
                                choices = ["True", "False"],
                                help    = "bar are color/marker filled if True (as by default)")

    subparser = parser.add_subparsers(dest = 'type',
                                      help = 'the user defined plot type')

    scatter = subparser.add_parser('scatter',
                                   description = "plots a series of data points",
                                   parents = [file_parser, data_parser, options_parser],
                                   help = 'plots a series of data points',
                                   epilog = "eg: plotext scatter -f test_data -col 2 3 -m hd -c red+ -t 'Test Data' -xl time -yl Price -g True")
    
    plot = subparser.add_parser('plot',
                                parents = [file_parser, data_parser, options_parser],
                                description = "plots lines between consecutive data points",
                                help = 'plots lines between consecutive data points',
                                epilog = "eg: plotext plot -f test_data -col 1 3 -m hd -c magenta -t 'Test Data' -xl time -yl Price")

    plotter = subparser.add_parser('plotter',
                                   parents = [file_parser, data_parser, options_parser],
                                   description = 'plots a series of data points and the lines between consecutive ones', 
                                   help = 'scatter + plot',
                                   epilog = "eg: plotext plotter -f data.txt -col 1 2 -d ';' -m x -c blue+ -t 'a title' -g True")
 
    
    bar = subparser.add_parser('bar',
                               parents = [file_parser, data_parser, options_parser, barhist_parser],
                               description = 'builds a bar plot',
                               help = 'bar plot',
                               epilog = "eg: plotext bar -f data.txt -m sd -c red+ -fi False -w 0.5")

    bar.add_argument("-w", "--width",
                            nargs   = 1,
                            type = float,
                            default = [None],
                            help    = "bars width as a float between 0 and 1")

    hist = subparser.add_parser('hist',
                                parents = [file_parser, data_parser, options_parser, barhist_parser],
                                description = 'builds a histogram plot',
                                help = 'histogram plot',
                                epilog = "eg:  plotext hist -f test_data -col 1 3 -m sd -c orange+ -t 'Test Data'  -fi True -b 15 -n True")

    hist.add_argument("-b", "--bins",
                            nargs   = 1,
                            type = int,
                            default = [10],
                            help    = "histogram bins (10 by default)")
    
    image = subparser.add_parser('image',
                                 parents = [file_parser],
                                 description = 'prints an image from file path',
                                 help = 'prints an image from file path',
                                 epilog = "eg: plotext image -f test_image")
    
    gif = subparser.add_parser('gif',
                               parents = [file_parser],
                               description = 'plays a gif image from file path',
                               help = 'plays a gif image from file path',
                               epilog = "eg: plotext gif -f test_gif")

    video = subparser.add_parser('video',
                                 parents = [file_parser],
                                 description = 'plays a video from file path',
                                 help = 'plays a video from file path',
                                 epilog = "eg: plotext video -f test_video -fy True")

    video.add_argument("-fy", "--from_youtube",
                                nargs   = 1,
                                type = str,
                                default = ["False"],
                                choices = ["True", "False"],
                                help    = "set to True to renders colors correctly if the video has been downloaded from youtube, default is False")

    youtube = subparser.add_parser('youtube',
                                   #parents = [file_parser],
                                   description = 'plays a youtube video from url',
                                   help = 'plays a youtube video from url',
                                   epilog = "eg: plotext youtube --url test_youtube")

    youtube.add_argument("-u", "--url",
                         action = 'store',
                         dest   = 'url',
                         nargs  = 1,
                         type   = str,
                         help   = "Web Page url. Use 'test_url' for a saved url video.")
    
    return parser


def plot(args):
    type = args.type
    
    plots = ['scatter', 'plot', 'plotter', 'bar', 'hist']

    if type in plots:
        marker = args.marker[0]
        color = args.color[0]
        plt.title(args.title[0])
        plt.xlabel(args.xlabel[0])
        plt.ylabel(args.ylabel[0])
        grid = True if args.grid[-1] == 'True' else False
        plt.grid(grid, grid)
        x, Y = read_file(args)
        width = args.width[0]  if type == 'bar' else 0
        orien = args.orientation[0] if type in ['bar', 'hist']  else 'v'
        fill = args.fill[0] == 'True' if type in ['bar', 'hist'] else False
        bins = args.bins[0] if type in 'hist' else None

        for y in Y:
            plt.plot(x, y, marker = marker, color = color) if type in ['plot', 'plotter'] else None
            plt.scatter(x, y, marker = marker, color = None if type == 'plotter' else color) if type in ['scatter', 'plotter'] else None
            plt.bar(x, y, marker = marker, color = color, width = width, orientation = orien, fill = fill) if type == 'bar' else None
            plt.hist(y, marker = marker, color = color, orientation = orien, fill = fill, bins = bins) if type == 'hist' else None
            plt.show()

    if type == 'image':
        if args.file == 'test_image':
            args.file = plt.test_image_path
        plt.image_plot(args.file, fast = True)
        plt.show()

    if type == 'gif':
        if args.file == 'test_gif':
            args.file = plt.test_gif_path
        plt.play_gif(args.file)
    
    if type == 'video':
        if args.file == 'test_video':
            args.file = plt.test_video_path
        from_youtube = True if args.from_youtube[-1] == 'True' else False
        plt.play_video(args.file, from_youtube)
        
    if type == 'youtube':
        args.url = args.url[-1]
        if args.url == 'test_youtube':
            args.url = plt.test_youtube_url
        plt.play_youtube(args.url)
        

def read_file(args):
    if args.type == 'youtube':
        return [], [[]]
    columns = args.columns
    delimiter = args.delimiter[0]

    if args.file == 'test_data':
        args.file = plt.test_data_path
        
    if args.file != None:
        path = args.file
        print(path)
        data = plt.read_data(path, columns = columns, delimiter = delimiter)
    else:
        lines = sys.stdin
        data = plt._utility.read_lines(lines, columns = columns, delimiter = delimiter)
    x = data[0]; Y = data[1:]
    return x, Y


if __name__ == "__main__":
    sys.exit(main())
