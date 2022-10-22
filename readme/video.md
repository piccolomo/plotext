# Play Videos

- [Introduction](https://github.com/piccolomo/plotext/blob/master/readme/video.md#introduction)
- [Video Plot](https://github.com/piccolomo/plotext/blob/master/readme/video.md#video-plot)
- [Play YouTube](https://github.com/piccolomo/plotext/blob/master/readme/video.md#play-youtube)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Introduction

- You can **stream videos** directly on terminal with the functions `play_video()` and `play_youtube()`.

- The function `show()` is not necessary in both cases, as it is called internally.

- The **frames size** will adapt to the screen size, unless `plot_size()` is used before the steaming functions.

- To **download videos** from the given YouTube `url` to the specified `path`, use the `get_youtube()` method.

- Both streaming functions may require further development. Any [bug report](https://github.com/piccolomo/plotext/issues/new) or development idea is welcomed. 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)

## Video Plot

To play a video with audio, use the the `play_video()` function. Set the parameter `from_youtube` to `True` to make sure that the color rendering is correct for videos downloaded from YouTube.

In this example, a test video is downloaded in the home folder, streamed and finally removed:

```python
import plotext as plt
path = 'moonwalk.mp4'
plt.download(plt.test_video_url, path)
plt.play_video(path, from_youtube = True)
plt.delete_file(path)
```

or directly on terminal:

```console
python3 -c "import plotext as plt; path = 'moonwalk.mp4'; plt.download(plt.test_video_url, path); plt.play_video(path, from_youtube = True); plt.delete_file(path)"
```

which will render [this video](https://raw.githubusercontent.com/piccolomo/plotext/master/data/moonwalk.mp4) on terminal. Yes! I am a Michael Jackson fan: he is number one (also [innocent](https://www.youtube.com/watch?v=O42IJ7opJFQ)), not my fault! 

More documentation can be accessed with `doc.play_video()`.

[Main Guide](https://github.com/piccolomo/plotext#guide), [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)

## Play YouTube

To play a YouTube video from `url` use the function `play_youtube()`, as in this example:

```python
import plotext as plt
plt.play_youtube(plt.test_youtube_url)
```

or directly on terminal:

```console
python3 -c "import plotext as plt; plt.play_youtube(plt.test_youtube_url)"
```

which will render [this youtube video](https://www.youtube.com/watch?v=ZNAvVVc4b3E&t=75s) on terminal. 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)