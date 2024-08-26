import plotext as plt; 

l = 1000
x = list(range(l))
y = plt.sin(2, l)
m = 'hd'
px = plt.pixel_class().set_fullground_code("blue").set_background_code("white")

p = plt.points_class(l)
[p.add(xi, yi, m, px) for (xi, yi) in zip(x, y)]

c = plt.canvas(245, 55)
c.set_xlim(0, l)
c.set_ylim(-1, 1)

c.draw(p)
#c.show()

# plt.clf(); 

# #plt.subplots(2,2)

# plt.xlabel('ciao')
# plt.xlim(0,6)
# plt.scatter([1,2,3], [5,6,7])
# plt.scatter([1,2,3], [50,6,7], yside = 2)


# plt.show()
