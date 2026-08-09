# Records one of the guide animations into a webp: it runs the example itself, with the terminal calls replaced so that every frame is captured rather than printed.
#     python3 docs/render/animate.py docs/source/code/heatmap_rain.py images/rain.webp 16 200 50

import os, subprocess, sys
from PIL import Image

import plotext as plt

script, picture, count = sys.argv[1], sys.argv[2], int(sys.argv[3])
width, height = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (310, 70)

folder = '/tmp/plotext_frames'
os.makedirs(folder, exist_ok = True)
for old in os.listdir(folder):
    os.remove(f'{folder}/{old}')

captured = []

plt.terminal.limit(False, False)
plt.terminal.size = lambda update = False: (width, height)
plt.terminal.clean = lambda *arguments: None
plt.terminal.is_pressed = lambda key: len(captured) >= count
plt.sleep = lambda seconds: None
plt.figure.show = lambda flush = False: captured.append(plt.figure.build().string())

here = os.path.dirname(script)
source = open(script).read().replace('"docs/source/images/', '"' + here.replace('code', 'images') + '/')
exec(compile(source, os.path.basename(script), 'exec'), {'__name__': '__main__', 'print': lambda *arguments: None})

for number, frame in enumerate(captured[:count]):
    path = f'{folder}/{number:02}.ansi'
    open(path, 'w').write(frame)
    subprocess.run([sys.executable, 'docs/render/render_ansi.py', path, path.replace('.ansi', '.png')], check = True, capture_output = True)

pictures = [Image.open(f'{folder}/{number:02}.png') for number in range(count)]
pictures[0].save(f'docs/source/{picture}', save_all = True, append_images = pictures[1:], duration = 90, loop = 0, quality = 85, method = 5)
print('frames:', count, '| size:', pictures[0].size, '|', round(os.path.getsize(f'docs/source/{picture}') / 1e6, 2), 'MB')
