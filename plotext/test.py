# -*- coding: utf-8 -*-
from plotext._utility.color import no_color_name, color_sequence
from plotext._utility.marker import marker_sequence
from plotext._utility.image import *
import plotext as plt
import unittest
import os

class TestPlotext(unittest.TestCase):
    def test_subplots(self):
        print("subplots")
        plt.subplots()
        self.assertEqual([plt.figure.rows, plt.figure.cols], [1, 1])
        plt.subplots(2)
        self.assertEqual([plt.figure.rows, plt.figure.cols], [2, 1])
        plt.subplots(2, 3)
        self.assertEqual([plt.figure.rows, plt.figure.cols], [2, 3])
        plt.clf()

    def test_subplot(self):
        print("subplot")
        plt.subplots(3, 3)
        self.assertEqual([plt.figure.row, plt.figure.col], [0, 0])
        plt.subplot(2)
        self.assertEqual([plt.figure.row, plt.figure.col], [1, 0])
        plt.subplot(2, 3)
        self.assertEqual([plt.figure.row, plt.figure.col], [1, 2])
        plt.clf()

    def test_clf(self):
        print("clf")
        plt.subplots(30, 40)
        plt.clf()
        self.assertEqual([plt.figure.rows, plt.figure.cols], [1, 1])
        plt.clf()

    def test_cls(self):
        print("cls")
        plt.subplots(2)
        plt.figure.subplot.ticks_color = "red"
        plt.cls()
        self.assertEqual([plt.figure.subplots[0][0].ticks_color, plt.figure.subplots[1][0].ticks_color], [no_color_name] * 2)
        plt.clf()

    def test_clp(self):
        print("clp")
        plt.figure.subplot.width = 300
        plt.clp()
        self.assertEqual(plt.figure.subplot.width, None)
        plt.clf()

    def test_cld(self):
        print("cld")
        plt.figure.subplot.x = [1, 2, 3]
        plt.cld()
        self.assertEqual(plt.figure.subplot.x, [])
        plt.clf()

    def test_clc(self):
        print("clc")
        plt.figure.subplot.ticks_color = "red"
        plt.clc()
        self.assertEqual(plt.figure.subplot.ticks_color, no_color_name)
        plt.clf()

    def test_plots_ize(self):
        print("plotsize")
        plt.clf()
        plt.plotsize()
        self.assertEqual(plt.figure.subplot.size, [None, None])
        plt.plotsize(2)
        self.assertEqual(plt.figure.subplot.size, [2, None])
        plt.subplots(2, 2)
        plt.subplot(2, 2)
        plt.plotsize(2.91898, 3.14569)
        self.assertEqual(plt.figure.subplots[1][1].size, [2, 3])
        plt.clf()

    def test_limit_size(self):
        print("limitsize")
        plt.limit_size()
        self.assertEqual(plt.figure.limit_size, [True, True])
        plt.limitsize(True, False)
        self.assertEqual(plt.figure.limit_size, [True, False])
        plt.clf()
        
    def test_title(self):
        print("title")
        plt.title()
        self.assertEqual(plt.figure.subplot.title, None)
        plt.title(23)
        self.assertEqual(plt.figure.subplot.title, "23")
        plt.title("   test  ")
        self.assertEqual(plt.figure.subplot.title, "test")
        plt.clf()

    def test_xlabel(self):
        print("xlabel")
        plt.xlabel()
        self.assertEqual(plt.figure.subplot.xlabel, [None] * 2)
        plt.xlabel(23)
        self.assertEqual(plt.figure.subplot.xlabel, ['23', None])
        plt.clf()
        
    def test_ylabel(self):
        print("ylabel")
        plt.ylabel()
        self.assertEqual(plt.figure.subplot.ylabel, [None] * 2)
        plt.ylabel(23)
        self.assertEqual(plt.figure.subplot.ylabel, ['23', None])
        plt.clf()

    def test_xaxis(self):
        print("xaxis")
        plt.xaxis()
        self.assertEqual(plt.figure.subplot.xaxes, plt.figure.subplot.default.xaxes)
        plt.xaxis(0, "lower")
        self.assertEqual(plt.figure.subplot.xaxes, [False, True])
        plt.clf()
        
    def test_yaxis(self):
        print("yaxis")
        plt.yaxis()
        self.assertEqual(plt.figure.subplot.yaxes, plt.figure.subplot.default.yaxes)
        plt.yaxis(0, "left")
        self.assertEqual(plt.figure.subplot.yaxes, [False, True])
        plt.clf()

    def test_frame(self):
        print("frame")
        plt.frame(0)
        self.assertEqual(plt.figure.subplot.xaxes, [False] * 2)
        self.assertEqual(plt.figure.subplot.yaxes, [False] * 2)
        plt.frame(1)
        self.assertEqual(plt.figure.subplot.xaxes, [True] * 2)
        self.assertEqual(plt.figure.subplot.yaxes, [True] * 2)
        plt.clf()

    def test_grid(self):
        print("grid")
        plt.grid()
        self.assertEqual(plt.figure.subplot.grid, plt.figure.subplot.default.grid)
        plt.grid(1, 0)
        self.assertEqual(plt.figure.subplot.grid, [True, False])
        plt.clf()

    def test_canvas_color(self):
        print("canvas_color")
        plt.canvas_color()
        self.assertEqual(plt.figure.subplot.canvas_color, plt.figure.subplot.default.canvas_color)
        plt.canvas_color("blue")
        self.assertEqual(plt.figure.subplot.canvas_color, "blue")
        plt.canvas_color((0, 1, 0))
        self.assertEqual(plt.figure.subplot.canvas_color, (0, 1, 0))
        plt.clf()
        
    def test_axes_color(self):
        print("axes_color")
        plt.axes_color()
        self.assertEqual(plt.figure.subplot.axes_color, plt.figure.subplot.default.axes_color)
        plt.axes_color("red")
        self.assertEqual(plt.figure.subplot.axes_color, "red")
        plt.axes_color((1, 2, 3))
        self.assertEqual(plt.figure.subplot.axes_color, (1, 2, 3))
        plt.clf()

    def test_ticks_color(self):
        print("ticks_color")
        plt.ticks_color()
        self.assertEqual(plt.figure.subplot.ticks_color, plt.figure.subplot.default.ticks_color)
        plt.ticks_color("green")
        self.assertEqual(plt.figure.subplot.ticks_color, "green")
        plt.ticks_color((0, -1, 0))
        self.assertEqual(plt.figure.subplot.ticks_color, plt.figure.subplot.default.ticks_color)
        plt.clf()

    def test_xlim(self):
        print("xlim")
        plt.xlim()
        self.assertEqual(plt.figure.subplot.xlim, [[None] * 2] * 2)
        plt.xlim(1, 2, "upper")
        self.assertEqual(plt.figure.subplot.xlim, [[None] * 2, [1, 2]])
        plt.clf()

    def test_ylim(self):
        print("yim")
        plt.ylim()
        self.assertEqual(plt.figure.subplot.ylim, [[None] *2] * 2)
        plt.ylim(1, 2, "right")
        self.assertEqual(plt.figure.subplot.ylim, [[None] *2, [1, 2]])
        plt.clf()

    def test_xscale(self):
        print("xscale")
        plt.xscale()
        self.assertEqual(plt.figure.subplot.xscale, ["linear"] * 2)
        plt.xscale("log")
        self.assertEqual(plt.figure.subplot.xscale, ["log", "linear"])
        plt.clf()

    def test_yscale(self):
        print("yscale")
        plt.yscale()
        self.assertEqual(plt.figure.subplot.yscale, ["linear"] * 2)
        plt.yscale("log")
        self.assertEqual(plt.figure.subplot.yscale, ["log", "linear"])
        plt.clf()

    def test_xfrequency(self):
        print("xfrequency")
        plt.xfrequency()
        self.assertEqual(plt.figure.subplot.xfrequency, plt.figure.subplot.default.xfrequency)
        plt.xfrequency(3, "upper")
        self.assertEqual(plt.figure.subplot.xfrequency, [plt.figure.subplot.default.xfrequency[0], 3])
        plt.clf()

    def test_yfrequency(self):
        print("yfrequency")
        plt.yfrequency()
        self.assertEqual(plt.figure.subplot.yfrequency, plt.figure.subplot.default.yfrequency)
        plt.yfrequency(3, "right")
        self.assertEqual(plt.figure.subplot.yfrequency, [plt.figure.subplot.default.yfrequency[0], 3])
        plt.clf()

    def test_xticks(self):
        print("xticks")
        plt.xticks()
        self.assertEqual(plt.figure.subplot.xticks, plt.figure.subplot.default.xticks)
        self.assertEqual(plt.figure.subplot.xlabels, plt.figure.subplot.default.xticks)
        self.assertEqual(plt.figure.subplot.xfrequency, plt.figure.subplot.default.xfrequency)
        plt.clp()
        t = (1, 2, 3); l = tuple(map(str, t))
        plt.xticks(t, xside = "lower")
        self.assertEqual(plt.figure.subplot.xticks, [t, plt.figure.subplot.default.xticks[1]])
        self.assertEqual(plt.figure.subplot.xlabels, [l, plt.figure.subplot.default.xticks[1]])
        self.assertEqual(plt.figure.subplot.xfrequency, [len(t), plt.figure.subplot.default.xfrequency[1]])
        plt.clf()
        plt.xticks(t, xside = "upper")
        self.assertEqual(plt.figure.subplot.xticks, [plt.figure.subplot.default.xticks[0], t])
        self.assertEqual(plt.figure.subplot.xlabels, [plt.figure.subplot.default.xticks[0], l])
        self.assertEqual(plt.figure.subplot.xfrequency, [plt.figure.subplot.default.xfrequency[0], len(t)])
        plt.clf()

    def test_yticks(self):
        print("yticks")
        plt.yticks()
        self.assertEqual(plt.figure.subplot.yticks, plt.figure.subplot.default.yticks)
        self.assertEqual(plt.figure.subplot.ylabels, plt.figure.subplot.default.yticks)
        self.assertEqual(plt.figure.subplot.yfrequency, plt.figure.subplot.default.yfrequency)
        plt.clp()
        t = (1, 2, 3); l = tuple(map(str, t))
        plt.yticks(t, yside = "left")
        self.assertEqual(plt.figure.subplot.yticks, [t, plt.figure.subplot.default.yticks[1]])
        self.assertEqual(plt.figure.subplot.ylabels, [l, plt.figure.subplot.default.yticks[1]])
        self.assertEqual(plt.figure.subplot.yfrequency, [len(t), plt.figure.subplot.default.yfrequency[1]])
        plt.clf()
        plt.yticks(t, yside = "right")
        self.assertEqual(plt.figure.subplot.yticks, [plt.figure.subplot.default.yticks[0], t])
        self.assertEqual(plt.figure.subplot.ylabels, [plt.figure.subplot.default.yticks[0], l])
        self.assertEqual(plt.figure.subplot.yfrequency, [plt.figure.subplot.default.yfrequency[0], len(t)])
        plt.clf()

    def test_draw(self):
        print("draw")
        plt.clf()
        plt.figure.subplot.draw(xside = "lower")
        self.assertEqual(plt.figure.subplot.xside, ["lower"])
        
        plt.clp()
        plt.figure.subplot.draw(yside = "random")
        self.assertEqual(plt.figure.subplot.yside, [plt.figure.subplot.default.yside[0]])
        
        plt.clp()
        plt.figure.subplot.draw([1], marker = "x")
        plt.figure.subplot.draw([1], marker = "dot")
        plt.figure.subplot.draw([1], marker = "     ")
        plt.figure.subplot.draw([1], marker = None)
        self.assertEqual(plt.figure.subplot.marker, ['x', "dot", ' ', marker_sequence[0]])
        
        plt.clp()
        plt.figure.subplot.draw()
        plt.figure.subplot.draw(lines=True)
        plt.figure.subplot.draw(lines=False)
        self.assertEqual(plt.figure.subplot.lines, [False, True, False])
        
        plt.clp()
        plt.figure.subplot.draw([1], color = "red")
        plt.figure.subplot.draw([1], color = None)
        plt.figure.subplot.draw([1], color = "random")
        c = ["red"] + plt.figure.subplot.color_sequence[:2]
        self.assertEqual(plt.figure.subplot.color, c)
        
        plt.clp()
        plt.figure.subplot.draw([2, 3, 4])
        plt.figure.subplot.draw([0, 1], [2, 3])
        plt.figure.subplot.draw()
        self.assertEqual(plt.figure.subplot.x, [[1, 2, 3], [0, 1], []])
        self.assertEqual(plt.figure.subplot.y, [[2, 3, 4], [2, 3], []])
        
        plt.clp()
        plt.figure.subplot.draw()
        plt.figure.subplot.draw(fillx = True)
        plt.figure.subplot.draw(fillx = False)
        self.assertEqual(plt.figure.subplot.fillx, [plt.figure.subplot.default.fillx, True, False])
        
        plt.clp()
        plt.figure.subplot.draw()
        plt.figure.subplot.draw(filly = True)
        plt.figure.subplot.draw(filly = False)
        self.assertEqual(plt.figure.subplot.filly, [plt.figure.subplot.default.filly, True, False])
        plt.clf()
        
        plt.clp()
        plt.figure.subplot.draw(label = "a label ")
        self.assertEqual(plt.figure.subplot.label, ["a label"])
        plt.clf()

    def test_plot(self):
        print("plot")
        plt.clf()
        plt.plot([1,3,1], label = "l1", color = "blue")
        plt.plot([3,1,3], label = "l2", color = "red", xside = "upper", yside = "right", marker = "fhd")
        plt.cls()
        plt.plotsize(22, 8)
        plt.title("a title")
        plt.xlabel("lx")
        plt.xlabel("ux", "upper")
        plt.ylabel("ly")
        plt.ylabel("ry", "right")
        canvas = plt.build()
        expected = """       a title        \n    1.00    2.50      \n   ┌┴─────────┴───┐   \n3.0┤ 🬏🬏🬏 l1 L 🬭🬭🬋🬂├3.0\n1.0┤ 🬏🬏🬏 l2 ⅂ 🬂🬂🬋🬭├1.0\n   └┬─────────┬───┘   \n    1.00    2.50      \n[y] ly [x] lx   ry [y]\n"""
        #print(repr(canvas))
        #print(canvas)
        #print(expected)
        #print(repr(canvas))
        #print(repr(expected))
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_subplots_sizes(self):
        print("subplots sizes")
        plt.subplots(3, 3)

        plt.subplot(1, 1)
        plt.plotsize(10, 3)
        plt.span(None, 1)
        
        plt.subplot(1, 2)
        plt.span(2)

        plt.subplot(2, 1)
        plt.plotsize(20, 3)
        plt.span(3, 1)

        plt.subplot(3, 1)
        plt.plotsize(10, 3)
        plt.span(None, 2)
        
        plt.build()
        self.assertEqual(plt.figure.subplots[0][0].size, [10, 3])
        self.assertEqual(plt.figure.subplots[0][1].size, [12, 3])
        self.assertEqual(plt.figure.subplots[0][2].size, [0, 3])
        self.assertEqual(plt.figure.subplots[1][0].size, [22, 3])
        self.assertEqual(plt.figure.subplots[1][1].size, [0, 3])
        self.assertEqual(plt.figure.subplots[1][2].size, [0, 3])
        self.assertEqual(plt.figure.subplots[2][0].size, [10, 3])
        self.assertEqual(plt.figure.subplots[2][1].size, [6, 3])
        self.assertEqual(plt.figure.subplots[2][2].size, [6, 3])
        plt.clf()

    def test_datetime(self):
        print("datetime")
        plt.datetime.set_datetime_form('%d/%m/%Y', '%H:%M')
        dates = ["13/07/2000 13:45", "14/07/2000 18:45", "21/07/2000 13:45"]
        values = [1, 4, 5]
        plt.plot_date(dates, values)
        plt.scatter_date(dates, values, color = "red")
        plt.cls()
        plt.plotsize(21, 5)
        canvas = plt.build()
        expected = """   ┌────────────────┐\n5.0┤  •🬋🬋🬋🬋🬋🬋🬋🬅🬂🬂🬂🬂•│\n1.0┤•🬂              │\n   └┬───────────────┘\n    13/07/2000 13:45 \n"""
        #print(repr(canvas))
        #print(repr(expected))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_bar(self):
        print("bar")
        plt.clf()
        plt.bar(["a", "b", "c"],[1, 3, 2])
        plt.cls()
        plt.plotsize(14, 5)
        canvas = plt.build()
        expected = """   ┌─────────┐\n3.0┤   ███🬭🬭🬭│\n0.9┤🬭🬭🬭██████│\n   └─┬──┬──┬─┘\n     a  b  c  \n"""
        #print(repr(canvas))
        #print(repr(expected))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_multiple_bar(self):
        print("multiple_bar")
        plt.clf()
        plt.multiple_bar(["a", "b", "c"],[[1, 3, 2], [3, 1, 4]])
        plt.cls()
        plt.plotsize(50, 5)
        canvas = plt.build()
        expected = """   ┌─────────────────────────────────────────────┐\n4.0┤       🬦🬹🬹🬹🬹🬹🬹🬓🬦🬹🬹🬹🬹🬹🬹                ▐██████│\n0.7┤🬭🬭🬭🬭🬭🬭🬏▐██████▌▐██████ 🬭🬭🬭🬭🬭🬭🬏▐██████▌▐██████│\n   └───────┬──────────────┬──────────────┬───────┘\n           a              b              c        \n"""
        #print(repr(canvas))
        #print(repr(expected))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_stacked_bar(self):
        plt.stacked_bar(["a", "b", "c"], [[1, 3, 2], [3, 1, 4]])
        plt.cls()
        plt.plotsize(50, 5)
        canvas = plt.build()
        expected = """   ┌─────────────────────────────────────────────┐\n6.0┤🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭   🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭🬭   █████████████│\n0.8┤█████████████   █████████████   █████████████│\n   └──────┬───────────────┬───────────────┬──────┘\n          a               b               c       \n"""
        #print(repr(canvas))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_hist(self):
        print("hist")
        data = [1,2,2,3,3,3,4,4,5]
        plt.hist(data, bins = 5)
        plt.cls()
        plt.plotsize(20, 5)
        canvas = plt.build()
        expected = """   ┌───────────────┐\n3.0┤   🬭🬭🬭███🬭🬭🬭   │\n0.9┤🬭🬭🬭█████████🬭🬭🬭│\n   └┬──────┬──────┬┘\n    0.6   3.0   5.4 \n"""
        #print(repr(canvas))
        # print(repr(expected))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_matrix_plot(self):
        print("matrix_plot")
        rows, cols = 3, 10
        matrix = range(rows * cols)
        matrix = [[matrix[cols * r + c]for c in range(cols)][::(-1)**(r)]  for r in range(rows)]
        plt.clp()
        plt.plotsize(cols + 3, rows + 4)
        #plt.matrix_plot(matrix) # this doesn't work for some reason in unittest only!! 
        plt.figure.subplot.draw_matrix(matrix)
        plt.cls()
        canvas = plt.build()
        expected = """ ┌──────────┐\n1┤██████████│\n2┤██████████│\n3┤██████████│\n └┬──┬──┬───┘\n  1  4  7    \n [x] column  \n"""
        #print(repr(canvas))
        # print(expected)
        # print(canvas)
        self.assertEqual(canvas, expected)
        plt.clf()

    def test_image_plot(self):
        print("image_plot")
        rows, cols = 3, 10
        matrix = range(rows * cols)
        matrix = [[0, 30, 100],[200, 130, 160],[200, 230, 255]]
        image = matrix_to_image(matrix)
        home = os.path.expanduser("~")
        path = os.path.join(home, "temp.jpeg")
        image.save(path)
        size = plt.figure.subplot.draw_image(path, size = [cols, rows], resample = False)
        plt.cls()
        plt.plotsize(*size)
        plt.frame(0)
        os.remove(path)
        canvas = plt.build()
        expected = "██████████\n██████████\n██████████\n" 
        #print(repr(canvas))
        #print(repr(expected))
        #print(canvas)
        #print(expected)
        self.assertEqual(canvas, expected)
        plt.clf()

        
if __name__ == "__main__":
    unittest.main()
