# Records the front page animation into a looping gif: it runs the guide example itself, with the terminal calls replaced so that every frame is captured instead of printed.
import os, subprocess, sys
from PIL import Image

import plotext as plt

folder = '/tmp/showcase_frames'
os.makedirs(folder, exist_ok = True)

width, height = 310, 70          # the terminal the animation is recorded at
count = 32                       # one full loop, as the example counts it

captured = []

plt.terminal.limit(False, False)
plt.terminal.size = lambda update = False: (width, height)
plt.terminal.clean = lambda *arguments: None
plt.terminal.is_pressed = lambda key: len(captured) >= count
plt.sleep = lambda seconds: None
plt.figure.show = lambda flush = False: captured.append(plt.figure.build().string())

source = open('git/docs/source/code/showcase.py').read().replace('"docs/source/images/', '"git/docs/source/images/')   # the example reads its picture from inside git/, this tool runs from the root
exec(compile(source, 'showcase.py', 'exec'), {'__name__': '__main__', 'print': lambda *arguments: None})

for number, frame in enumerate(captured[:count]):
    path = f'{folder}/{number:02}.ansi'
    open(path, 'w').write(frame)
    subprocess.run([sys.executable, 'git/docs/render/render_ansi.py', path, path.replace('.ansi', '.png')], check = True, capture_output = True)

# saved as a webp: it keeps every color, where a gif is limited to 256 and has to throw the rest away
pictures = [Image.open(f'{folder}/{number:02}.png') for number in range(count)]
pictures[0].save('git/docs/source/images/showcase.webp', save_all = True, append_images = pictures[1:], duration = 90, loop = 0, quality = 85, method = 5)
print('frames:', count, '| size:', pictures[0].size)
