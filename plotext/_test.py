def test():
    import plotext as plt
    import datetime as dt
    
    plt.clf(); plt.clt()
    plt.date_form("d/m/Y");
    plt.take_min()
    plt.plot_size(None, plt.th())
    #plt.plot_size(108, 70)
    
    y1 = plt.sin(periods = 1)
    y2 = plt.sin(periods = 2)
    y3 = plt.sin(periods = 3)
    l = len(y1)
    x = [plt.today_datetime() + dt.timedelta(days = i) for i in range(l)]
    x = plt.datetimes_to_string(x)
    
    plt.subplots(2, 2)
    
    plt.subplot(1, 1)
    plt.subplots(2, 2)
    plt.plotsize(plt.tw() // 2, plt.th() // 2)
    plt.canvas_color(66); plt.axes_color(4); plt.ticks_color(216); plt.ticks_style('bold')
    plt.scatter(y1, label = "lower left")
    plt.scatter(y2, xside = "lower", yside = "left", label = "lower left")
    plt.plot(y3, xside = "upper", yside = "right", label = "upper right")
    plt.vline(len(y1) / 2, 'red')
    plt.hline(0, 200)
    plt.text("origin", l // 2 + 3, 0.1, color = 'red')
    ##plt.xlim(-10 , l + 10)
    plt.title("Multiple Axes Plot")
    plt.xlabel('x lower'); plt.xlabel('x upper', 2)
    plt.ylabel('y left', 'left'); plt.ylabel('y right', 'right')
    plt.xfrequency(8); plt.xfrequency(5, 2);
    plt.yfrequency(3); plt.yfrequency(5, 2);
    
    plt.subplot(1, 2)
    plt.theme('innocent')
    plt.ticks_style('italic bold')
    plt.plotsize(1000, plt.th() // 2)
    plt.plot(x, y1, label = 'x date - y number')
    plt.plot(x, x, yside = 2, label = 'x date - y date')
    plt.vline(x[l // 2], 'red')
    plt.hline(0, 200)
    plt.text("minimum", x[3*l//4], -1.1, alignment = 'center', color = 'red')
    plt.ylim(-1.1, 1.1);
    ##plt.xlim(x[0],x[-1]) #### ERROR!!!!
    #plt.xaxes(1, 0); plt.yaxes(1, 0)
    #plt.title('Date Plot')
    
    plt.subplot(2, 1)
    plt.theme('elegant')
    plt.bar(['a', 'b'], [1, 2], label = "bar plot", fill = False, minimum = 0)
    plt.stacked_bar(['c', 'd'], [[2, 3], [4, 2]], label = ["stacked plot 1", "stacked plot 2"])
    plt.multiple_bar(['e', 'f'], [[2, 1], [3, 4]], label = ["multiple plot 1", "multiple plot 2"])
    plt.hline(3); plt.vline("b")
    plt.frame(1); #plt.xaxes(1, 0); plt.yaxes(1, 0)
    ## Label ERROR
    plt.text("b", "b", 2.1, color = 'red') # it does not accept bar coordinate
    plt.xlabel('x axis')
    
    plt.subplot(2, 2)
    plt.canvas_color('gray+'); plt.axes_color('gray+')
    size = [plt.tw() // 2, 30]
    plt.plotsize(*size)
    plt.download(plt.test_image_url, 'cat.jpg')
    plt.image_plot('cat.jpg', grayscale = False)
    plt.delete_file('cat.jpg')
    plt.title('Adam by Michelangelo')
    plt.frame(0)
    plt.text("Adam", 10, 20, color = 'red', style = 'bold') # it does not accept bar coordinate
    
    # Add save plot total
    
    plt.show()
    plt.time()
    #plt.save_fig('~/tot.txt', 1)
    #plt.save_fig('~/tot.html')
    plt.clf()
