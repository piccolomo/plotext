# Image Plots

- [Image Plot](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plot)
- [GIF Plot](https://github.com/piccolomo/plotext/blob/master/readme/image.md#gif-plot)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Image Plot

To plot an image use the `image_plot(path)` function. 

- It is recommended to use the `plotsize()` method before `image_plot()`, especially for larger images, to initially reduce the image size and so the computational load.

- To plot much faster set the `fast` parameter to `True`. In this case, the plot dimensions will be locked to the whatever size was previously chosen, and won't adapt to the terminal or subplot size; also any setting method which follows will not have any effect (like `xlabel()`, `frame()` and so on).

- A curious visual effect is obtained using for example `marker = list("CuteCat")` with `style = 'inverted'`: try it out! :-)

- Use the parameter `grayscale` to plot in gray-scale.

- To easily manipulate file paths, use the tools described in [this section](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities).

- To plot images **beyond the terminal size** use the function `plt.limit_size()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/settings.md#plot-size), or the app developed [here](https://github.com/piccolomo/plotext/blob/master/readme/environments.md#tkinter), using `tkinter`.

- To save the result **in colors**, as an `html` page, use the function `plt.savefig()`, described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#useful-functions).

In this example, a [test image](https://raw.githubusercontent.com/piccolomo/plotext/master/data/cat.jpg) is downloaded in the home folder, visualized and finally removed:

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

More documentation can be accessed with `doc.image_plot()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Image Plots](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plots)

## GIF Plot

To render a GIF image use the function `play_gif(path)`. Note that the function `show()` is not necessary in this case, as it is called internally.

In this example, a [test GIF](https://raw.githubusercontent.com/piccolomo/plotext/master/data/homer.gif) is downloaded in the home folder, visualized and finally removed:

```python
import plotext as plt
path = 'homer.gif'
plt.download(plt.test_gif_url, path)
plt.play_gif(path)
plt.delete_file(path)
```

or directly on terminal:

```console
python3 -c "import plotext as plt; path = 'homer.gif'; plt.download(plt.test_gif_url, path); plt.play_gif(path); plt.show(); plt.delete_file(path)"
```

which will play the following GIF on terminal:

![image](https://raw.githubusercontent.com/piccolomo/plotext/master/data/homer-rendered.gif)

More documentation can be accessed with `doc.play_gif()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Image Plots](https://github.com/piccolomo/plotext/blob/master/readme/image.md#image-plots)