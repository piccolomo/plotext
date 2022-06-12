from plotext._utility.color import color_sequence, no_color

##############################################
###########    Color Themes    ###############
##############################################

themes = {}
ls = len(color_sequence)

themes["default"] = ["white", "white", "black", no_color, color_sequence]

sequence = [no_color] * ls
themes['clear'] = [no_color, no_color, no_color, no_color, sequence]

themes['pro'] = [no_color, no_color, no_color, no_color, color_sequence]

sequence = [(0, 255, 65), (0, 143, 17), (0, 59, 0)]
sequence += [el for el in color_sequence if el not in sequence]
themes['matrix'] = [(13,2,8), (13,2,8), sequence[0], 'bold', sequence]

blue = (0, 64, 239); red = (242,80,34); yellow = (255,185,0); green = (127,186,0)
sequence = [blue, red, green, yellow]
sequence += [el for el in color_sequence if el not in sequence]
themes['windows'] = ['gray+', 'gray+', 'black', no_color, sequence]

sequence = ['blue', 22, 54]
sequence += [el for el in color_sequence if el not in sequence]
themes['dark'] = ['black', 'black', 'orange', no_color, sequence]

sequence = [21, 41, 196]
sequence += [el for el in color_sequence if el not in sequence]
themes['retro'] = [250, 234, 186, no_color, sequence]
            
sequence = [111, 174, 186]
sequence += [el for el in color_sequence if el not in sequence]
themes['elegant'] = [66, 4, 216, "bold", sequence]

sequence = [39, 202, 228]
sequence += [el for el in color_sequence if el not in sequence]
themes['mature'] = [180, 24, 184, "bold", sequence]

sequence = [6, 125, 190]
sequence += [el for el in color_sequence if el not in sequence]
themes['dreamland'] = [180, 2, 221, "bold", sequence]

sequence = [27, 88, 11]
sequence += [el for el in color_sequence if el not in sequence]
themes['grandpa'] = [66, 94, 155, "bold", sequence]

sequence = [142, 124, 57]
sequence += [el for el in color_sequence if el not in sequence]
themes['salad'] = [95, 22, 221, "bold", sequence]

pink = (255, 200, 200)
sequence = [(86, 186, 236), 'green+']
sequence += [el for el in color_sequence if el not in sequence]
themes['girly'] = [pink, pink, 'blue+', no_color, sequence]

sequence = [27, 34, 52]
sequence += [el for el in color_sequence if el not in sequence]
themes['serious'] = [95, 52, 190, "bold", sequence]

sequence = [39, 202, 228]
sequence += [el for el in color_sequence if el not in sequence]
themes['sahara'] = [180, 172, 192, "bold", sequence]

sequence = [26, 85, 124]
sequence += [el for el in color_sequence if el not in sequence]
themes['scream'] = [130,88,227, "bold", sequence]
