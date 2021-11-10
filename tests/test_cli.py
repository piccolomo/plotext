# # add parent directory to PYTHONPATH
# # https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder

# import sys
# import os

# sys.path.insert(1, os.path.join(sys.path[0], ".."))
import pathlib
import os

import plotext.plotext_cli as cli
import pytest


def test_column():
    assert cli._column("1") == (0,)


def test_split_columns():
    assert cli._split_columns("1,3") == (0, 2)

    # when we pass from command line pairs contaning spaces
    # e.g.,
    # 1, 3
    # 1 ,3
    # 1 , 3
    # ArgumentParser will pass just the first token
    with pytest.raises(ValueError):
        cli._split_columns("1,")
        cli._split_columns("1")


@pytest.fixture
def parser():
    return cli._build_parser()


def test_parser(parser):

    # test default values
    args = cli.parse_args(["scatter"])
    assert args.delimiter == None
    assert args.bins == 10
    assert args.columns == [(0, 1)]
    assert args.file == None
    assert args.grid == False
    assert args.title == None
    assert args.xlabel == None
    assert args.ylabel == None
    assert args.size == None

    args = parser.parse_args("scatter -f a_file".split())
    assert args.file == "a_file"

    args = parser.parse_args(["bar"])
    assert args.plot == "bar"

    args = parser.parse_args(["scatter"])
    assert args.plot == "scatter"

    args = parser.parse_args(["line"])
    assert args.plot == "line"

    args = parser.parse_args(["linespoints"])
    assert args.plot == "linespoints"

    args = parser.parse_args(["hist"])
    assert args.plot == "hist"

    args = cli.parse_args("scatter -c 1,2 1,3".split())
    assert args.columns == [(0, 1), (0, 2)]

    args = cli.parse_args("scatter --size 10,20".split())
    assert args.size == (10, 20)
    args = cli.parse_args("scatter -s 10,20".split())
    assert args.size == (10, 20)

    with pytest.raises(SystemExit):
        # no plot type defined
        parser.parse_args([""])

        # no spaces between column numbers
        cli.parse_args("bar -c 1 ,2".split())

        # cannot set plots different types
        cli.parse_args(["bar", "scatter"])

        # no spaces between plot dimensions
        cli.parse_args("bar --size 10, 20".split())

        # plot dimensions are integers
        cli.parse_args("bar --size 10.5,20".split())

    args = parser.parse_args("bar --xlabel xlabel".split())
    assert args.xlabel == "xlabel"
    args = parser.parse_args("bar -xl xlabel".split())
    assert args.xlabel == "xlabel"

    args = parser.parse_args("bar --ylabel ylabel".split())
    assert args.ylabel == "ylabel"
    args = parser.parse_args("bar -yl ylabel".split())
    assert args.ylabel == "ylabel"

    args = parser.parse_args("bar --title title".split())
    assert args.title == "title"
    args = parser.parse_args("bar -t title".split())
    assert args.title == "title"

    args = parser.parse_args("bar -g".split())
    assert args.grid == True


@pytest.fixture
def this_dir():
    return os.path.dirname(__file__)


@pytest.fixture
def numerical_data_txt(this_dir):
    return os.path.join(this_dir, "numerical_data.txt")


@pytest.fixture
def numerical_data_csv(this_dir):
    return os.path.join(this_dir, "numerical_data.csv")


@pytest.fixture
def str_data_txt(this_dir):
    return os.path.join(this_dir, "str_data.txt")


def test_get_numerical_data(parser, numerical_data_txt):
    args = cli.parse_args(f"scatter -f {numerical_data_txt} -c 1,2 1,3".split())
    data = cli.get_data(args)
    assert data[0] == [1.0, 2.0, 4.0, 8.0]
    # data[1] == [2.17446, 1.248573, 0.961571, 0.429465]
    for a, b in zip(data[1], [2.17446, 1.248573, 0.961571, 0.429465]):
        assert a == pytest.approx(b)

    # data[2] == [1.0, 1.742, 2.261, 5.063]
    for a, b in zip(data[2], [1.0, 1.742, 2.261, 5.063]):
        assert a == pytest.approx(b)

    args_str = f"-f {numerical_data_txt} -c 1,2 1,3"
    for p in "scatter bar line linespoints".split():
        args = cli.parse_args(f"{p} {args_str}".split())
        data = cli.get_data(args)

    args = cli.parse_args(f"hist -f {numerical_data_txt} -c 1 2 3".split())


def test_get_str_data(parser, str_data_txt):

    # str_data.txt can work with just bar plot
    args = cli.parse_args(f"bar -f {str_data_txt} -c 2,1".split())
    data = cli.get_data(args)

    assert data[0] == [2950.0, 56.0, 157.0, 133.0, 9043.0]
    assert data[1] == ["DC", "QC", "ON", "VI", "NY"]

    # scatter, line, linespoints cannot use this dataset
    # because they try to convert strings into float
    with pytest.raises(ValueError):
        args_str = f"-f {str_data_txt} -c 2,1"
        for p in "scatter line linespoints".split():
            args = cli.parse_args(f"{p} {args_str}".split())
            data = cli.get_data(args)


def test_get_numerical_data_csv(parser, numerical_data_csv):
    # default delimiter should not work
    with pytest.raises(IndexError):
        args = cli.parse_args(f"scatter -f {numerical_data_csv}".split())
        data = cli.get_data(args)

    # columns are delimited by "," so we pass "-d ,"
    args = cli.parse_args(f"scatter -f {numerical_data_csv} -c 1,2 1,3 -d ,".split())
    data = cli.get_data(args)
    assert data[0] == [1.0, 2.0, 4.0, 8.0]
    # data[1] == [2.17446, 1.248573, 0.961571, 0.429465]
    for a, b in zip(data[1], [2.17446, 1.248573, 0.961571, 0.429465]):
        assert a == pytest.approx(b)

    # data[2] == [1.0, 1.742, 2.261, 5.063]
    for a, b in zip(data[2], [1.0, 1.742, 2.261, 5.063]):
        assert a == pytest.approx(b)

    # this works with all supported plots
    args_str = f"-f {numerical_data_csv} -c 1,2 1,3 -d ,"
    for p in "scatter bar line linespoints".split():
        args = cli.parse_args(f"{p} {args_str}".split())
        data = cli.get_data(args)


def test_main(numerical_data_txt):
    cmd_line = f"-f {numerical_data_txt} -xl xlabel -yl ylabel -t title -g"
    # use all plot types
    for p in "scatter bar line linespoints".split():
        cli.main(f"{p} {cmd_line}".split())
