import plotext as plt
white = (255, 255, 255) # whiter than "white"

sa = plt.colorize("Hi\nthere! ", ("blue+", white)) # the first 2-lines string: Hi there!
sb = plt.colorize("How\nare you?", ("green+", white)) # the second 2-lines string: How are you?

s = sa + sb # or s = s1.hstack(s2)

s.print()
