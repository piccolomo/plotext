#!/usr/bin/env python

import plotext as plt

import sys
import argparse
from collections import defaultdict


def split_columns(x):
    """Helper function to parse pair of indexes of columns


    This function is called by ArgumentParser
    """
    try:
        a, b = map(int, x.split(","))
        # columns from command line are numbered starting from 1
        # but internally we start counting from 0
        return a - 1, b - 1
    except ValueError as ex:
        message = """ 
        Cannot understand the pair of columns you want to print.
        Columns are identified by numbers starting from 1. Each pair
        of columns is identified by two numbers separated by a comma
        without a space 1,2 1,5 6,4\n\n\n"""
        print(message, ex)
        raise ex


def build_parser():
    """Define command line args
    """
    examples = """
    examples:


    # plot data from stdin
    $ cat data.txt | plotext

    # plot data from a file
    $ plotext -f data.txt

    # bar plot of second-first column
    $ cat data.txt | plotext --bar --columns 2,1

    # linespoints of first-second and first-third column
    $ plotext -f data.txt --linespoints --columns 1,2 1,3

    """
    parser = argparse.ArgumentParser(
        prog="plotext",
        description="plots directly on terminal",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Read data from file. If this flag is not used, plotext reads from stdin",
    )

    # supported types of plots. only one type at time is allowed
    # e.g., we cannot pass flags -s -b together
    # this is caught by ArgumentParser because we add the flags
    # to a set of mutually exclusive group
    plots = parser.add_mutually_exclusive_group()
    plots.add_argument(
        "-s",
        "--scatter",
        dest="plot",
        help="Scatter plot. This is the default",
        action="store_const",
        const="scatter",
    )
    plots.add_argument(
        "-l",
        "--line",
        dest="plot",
        help="Line plot.",
        action="store_const",
        const="line",
    )
    plots.add_argument(
        "-lp",
        "--linespoints",
        dest="plot",
        help="Linespoints plot.",
        action="store_const",
        const="linespoints",
    )
    plots.add_argument(
        "-b", "--bar", dest="plot", help="Bar plot.", action="store_const", const="bar"
    )

    parser.add_argument(
        "-c",
        "--columns",
        help="""Pairs of columns to plot: 1,2 1,3 4,2. By default, the first two columns are used""",
        nargs="*",
        type=split_columns,
        default=[(0, 1)],
    )

    parser.add_argument("-xl", "--xlabel", help="Set x label", nargs="?")

    parser.add_argument("-yl", "--ylabel", help="Set y label", nargs="?")

    parser.add_argument("-t", "--title", help="Set plot title", nargs="?")

    parser.add_argument("-g", "--grid", help="Enable grid", action="store_true")

    parser.add_argument(
        "-d", "--delimiter", help="Use delimiter instead of spaces for field delimiter"
    )

    parser.set_defaults(plot="scatter", delimiter=None)
    return parser


def parse_args(argv):
    """Helper function: return namespace populated by ArgumentParser"""

    parser = build_parser()
    return parser.parse_args(argv)


def post_process_all_floats(columns, plot_type):
    """Convert all data read from file or stdin to float. 
    This function is invoked by get_data()"""
    for k, v in columns.items():
        try:
            columns[k] = list(map(float, v))
        except ValueError:
            print("All elements of a", plot_type, "plot must numbers.")
            print("Cannot convert elements of column", k + 1, "to float.\n\n")
            raise
    return columns


def post_process_bar(columns, pairs):
    """Convert y-axis values into float. x-axis values are left str"""
    # in a bar plot, x-axis elements are left string
    # y elements, must be conveterd to float

    # get all y indexs
    idx = {i for _, i in pairs}

    for i in idx:
        try:
            columns[i] = list(map(float, columns[i]))
        except ValueError:
            print("In a bar plot, elements on the y-axis must be numbers.")
            print("Cannot convert elements of column", i + 1, "to float.\n\n")
            raise
    return columns


def get_data_from(file_descriptor, args):
    """Read line from file_descriptor, which is a file or stdin. 

    Each line is plit according to the delimiter passed from command line. 

    Returns a dictionary with column-id:['list', 'of', 'values']"""

    # the user can pass several pairs of columns where one column is repeated
    # e.g., 1,2 1,3 1,4
    # therefore, we remove duplicates using a set
    idx = {i for t in args.columns for i in t}

    d = defaultdict(list)
    for line in file_descriptor:
        line = line.split(sep=args.delimiter)
        for i in idx:
            d[i].append(line[i])
    return d


def get_data(args):
    """returns dict{idx:[values]}. 

    Depending on the plot type selected, [values] may contain floats or strings
    """

    if args.file:
        with open(args.file) as f:
            columns = get_data_from(f, args)
    else:
        columns = get_data_from(sys.stdin, args)

    # here we basically convert x and/or y elements to float
    if args.plot == "bar":
        columns = post_process_bar(columns, args.columns)
    else:
        columns = post_process_all_floats(columns, args.plot)

    return columns


def plot_properties(args):
    """Apply optional configurations to the plot"""
    if args.xlabel:
        plt.xlabel(args.xlabel)

    if args.ylabel:
        plt.ylabel(args.ylabel)

    if args.title:
        plt.title(args.title)

    if args.grid:
        plt.grid(True)


def plot(data, args):
    """Draw the plot."""

    pairs = args.columns

    for i, j in pairs:
        if args.plot == "scatter":
            plt.scatter(data[i], data[j])
        elif args.plot == "bar":
            plt.bar(data[i], data[j])
        elif args.plot == "line":
            plt.plot(data[i], data[j])
        elif args.plot == "linespoints":
            plt.plot(data[i], data[j], marker=".")
            plt.scatter(data[i], data[j], marker="small")

    plot_properties(args)
    plt.show()


def main(argv=None):
    # parse command line args
    args = parse_args(argv)

    # get relevant data from stdin or file
    data = get_data(args)

    plot(data, args)


if __name__ == "__main__":
    sys.exit(main())
