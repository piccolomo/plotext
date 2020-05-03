#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import plotext.plot as plt
import os
import numpy as np

cur_dir=os.path.dirname(os.path.realpath(__file__))
images_dir=os.path.join(cur_dir, "images")

images_list = [ f for f in os.listdir(images_dir) if f.endswith(".png") ]
for f in images_list:
    os.remove(os.path.join(images_dir, f))

#configuration
font_size=12
cols, rows=100,30
width=int(1.57*cols*font_size)
height=int(3.1*rows*font_size)
back_ground_color=(48, 10, 36)
font_size=36
font_color=(255,255,255)
unicode_font=ImageFont.truetype("UbuntuMono-R.ttf", font_size)
frames=60
l=30*frames

for i in range(frames):
    x=np.arange(0,l)
    y=np.sin(3*np.pi/l*x+2*np.pi/frames*i)
    plt.scatter(x, y, cols=cols, rows=rows, equations=0, ticks=1, axes=1)
    plt.show(clear=1)
    text=plt.get_canvas(False)
    img=Image.new("RGB", (width,height), back_ground_color)
    draw=ImageDraw.Draw(img)
    draw.text((10,10), text, font=unicode_font, fill=font_color)
    num='0'*(len(str(frames))-len(str(i)))+str(i)
    name=os.path.join(images_dir, num+'.png')
    img.save(name)
    

# import glob
# frames=[]
# imgs=glob.glob(os.path.join(images_dir,'*.png'))
# imgs.sort()
# for i in imgs:
#     frames.append(Image.open(i))
 
# frames[0].save(os.path.join(cur_dir,'anim.gif'), format='GIF',
#                append_images=frames[1:],
#                save_all=True,
#                duration=100, loop=0)
    
