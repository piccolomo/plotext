import plotext.plot as plx
import numpy as np

l=3000
x=np.arange(0, l)
y=np.sin(2.*2*np.pi/l*np.array(x)+0.155*0)*np.exp(-0.5*np.pi/l*x)
plx.scatter(x, y, rows=20, cols=100, equations=True, point_color='blue')
plx.show(clear=0)

#input("\n\nPress for a plot demonstration")
l=10
x=range(0, l)
y=np.sin(4.*2*np.pi/l*np.array(x)+0.155*0)
#plx.plot(x, y, cols=500, rows=30, line=True, point=True, point_color="inorm", line_color="inorm", equations=0, axes=1, axes_color="inorm")
#plx.show()

#input("\n\nPress for another demonstration")
#plx.scatter(x, y, point_color="iblue", axes=False, ticks=0, equations=0)
#plx.show()

run=0
i=0
while run:
    l=1000
    x=range(0, l)
    y=np.sin(2.*2*np.pi/l*np.array(x)+0.05*i)
    plx.scatter(x, y, point_color="green")
    plx.show(clear=1, sleep=True)
    i+=1
