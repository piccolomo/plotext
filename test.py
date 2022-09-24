import plotext as plx
import numpy as np

l=3000
x=np.arange(0, l)
y=np.sin(2.*2*np.pi/l*np.array(x)+0.155*0)*np.exp(-0.5*np.pi/l*x)
plx.scatter(x, y, point_color='blue')
plx.show()

l=10
x=range(0, l)
y=np.sin(4.*2*np.pi/l*np.array(x)+0.155*0)

run=1
i=0
while run:
    l=1000
    x=range(0, l)
    y=np.sin(2.*2*np.pi/l*np.array(x)+0.05*i)
    plx.scatter(x, y, point_color="green")
    plx.show()
    i+=1
    plx.clear_terminal()
    plx.clear_plot()
