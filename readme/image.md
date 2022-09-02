# Image Plots
- [Image Plot](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plot)
- [GIF Plot](https://github.com/piccolomo/plotext/blob/master/readme/image.md#gif-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)


## Image Plot
To plot an image use the function `image_plot(path)`. In this example, a test image is downloaded in the home folder, visualized and finally removed:
```python
import plotext as plt
path = 'cat.jpg'
plt.download(plt.test_image_url, path)
plt.image_plot(path)
plt.title("A very Cute Cat")
plt.show()
plt.delete_file(path)
```
or directly on terminal:
```console
python3 -c "import plotext as plt; path = 'cat.jpg'; plt.download(plt.test_image_url, path); plt.image_plot(path); plt.title('A very Cute Cat'); plt.show(); plt.delete_file(path)"
```

![image](https://raw.githubusercontent.com/piccolomo/plotext/master/data/image.png)

- It is recommended to use the function `plotsize()` before `image_plot()`, especially for larger images, to initially reduce the image size and so the computational load,
- the parameter `fast`, if set to True, allows to plot much faster, but the plot final dimensions will be locked to the whatever size was previously chosen, and won't adapt to the terminal or subplot size; also any setting function which follows will not have any effect (like `xlabel()`, `frame()` and so on),
- a curious visual effect is obtained using for example `marker = list("CuteCat")` with `style = 'inverted'`: try it out :-),
- use the parameter `grayscale` to plot in gray-scale,
- to easily manipulate file paths, use the tools described in [this section](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities),
- to save the result **in colors**, as an `html` page, use the function `plt.savefig()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions),
- to plot images **beyond the terminal size** use the function `plt.limit_size()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size), or the app developed [here](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter), using `tkinter`,
- access the full documentation of the `image_plot()` function with `doc.image_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Image Plots](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plots)


## Gif Plot
To render a GIF image use the function `play_gif(path)`. In this example, a test GIF is downloaded in the home folder, visualized and finally removed:
```python
import plotext as plt
path = 'homer.gif'
plt.download(plt.test_gif_url, path)
plt.play_gif(path)
plt.show()
plt.delete_file(path)
```
or directly on terminal:
```console
python3 -c "import plotext as plt; path = 'homer.gif'; plt.download(plt.test_gif_url, path); plt.play_gif(path); plt.show(); plt.delete_file(path)"
```
which will play the following GIF on terminal:

![image](https://raw.githubusercontent.com/piccolomo/plotext/master/data/homer-rendered.gif)


[Main Guide](https://github.com/piccolomo/plotext#guide), [Image Plots](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plots)