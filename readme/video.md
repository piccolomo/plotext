# Play Videos

- [Video Plot](https://github.com/piccolomo/plotext/blob/master/readme/video.md#video-plot)
- [Play YouTube](https://github.com/piccolomo/plotext/blob/master/readme/video.md#play-youtube)

[Plotext Guide](https://github.com/piccolomo/plotext#guide)


## Video Plot

To play a video with audio use the the function `play_video()`, as explained here:

```python
import plotext as plt
plt.play_video(plt.test_video_path, from_youtube = True)
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.play_video(plt.test_video_path, from_youtube = True);"
```
which will render [this video](https://raw.githubusercontent.com/piccolomo/plotext/master/images/moonwalk.mp4) on terminal.

- The function `show()` is not necessary in this case, as it is called internally.

- The frames will adapt to the screen size unless `plot_size()` is used before.

- Set the parameter `from_youtube` to True (False by default) to make sure that the color rendering is correct for videos downloaded from youtube.

- This function may require further development.

- Access the full documentation of the function `plt.play_video()` with `plt.doc.play_video()`.

[Plotext Guide](https://github.com/piccolomo/plotext#guide), [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)



## Play YouTube

To plot an image use the function `image_plot()` as in this example:

```python
import plotext as plt
plt.play_youtube(plt.test_youtube_url)
```
or directly on terminal:
```console
python3 -c "import plotext as plt; plt.play_youtube(plt.test_youtube_url)"
```

which will render [this youtube video](https://www.youtube.com/watch?v=2Z4s8xbuegQ) on terminal. 

- The function `show()` is not necessary in this case, as it is called internally.

- The frames will adapt to the screen size unless `plot_size()` is used before.

- To download a YouTube video use the function `get_youtube()`.

- This function may require further development.

- Yes! I am a Michael Jackson fan! He is number one!

- Access the full documentation of the function `plt.play_youtube()` with `plt.doc.play_youtube()`.


[Plotext Guide](https://github.com/piccolomo/plotext#guide), [2D Plots](https://github.com/piccolomo/plotext/blob/master/readme/2d-plots.md#2d-plots)