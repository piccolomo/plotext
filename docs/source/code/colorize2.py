import plotext as plt
white = (255, 255, 255) # whiter than "white"

s1 = plt.colorize("Hi ", ("blue+", white))
s2 = plt.colorize("there!", ("red+", white))
s3 = plt.colorize("How ", ("green+", white))
s4 = plt.colorize("are you?", ("magenta+", white))

sa = s1 + s2 # or sa = s1.hstack(s2) this returns: Hi there!
sb = s3 + s4 # or sb = s3.hstack(s4) this returns: How are you?

s = sa / sb # or s = s1.vstack(s2)

s.print()
