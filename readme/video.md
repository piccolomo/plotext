# Play Videos

- [Introduction](https://github.com/piccolomo/plotext/blob/master/readme/video.md#introduction)
- [Video Plot](https://github.com/piccolomo/plotext/blob/master/readme/video.md#video-plot)
- [Play YouTube](https://github.com/piccolomo/plotext/blob/master/readme/video.md#play-youtube)

[Main Guide](https://github.com/piccolomo/plotext#guide)

## Introduction

- You can stream videos directly on terminal with the functions `play_video()` and `play_youtube(url)`.

- The function `show()` is not necessary in both cases, as it is called internally.

- The frames will adapt to the screen size unless `plot_size()` is used before the steaming functions.

- To download videos from YouTube, use the function `plt.get_youtube()` described [here](https://github.com/piccolomo/plotext/blob/master/readme/utilities.md#file-utilities).

- Both streaming functions may require further development: any bug report or development idea is welcomed. 

## Video Plot

To play a video with audio, use the the function `play_video(path)`. Set the parameter `from_youtube` to `True` to make sure that the color rendering is correct for videos downloaded from YouTube.

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

To play a YouTube video from `url` use the function `play_youtube(url)`, as in this example:

```python
import plotext as plt
plt.play_youtube(plt.test_youtube_url)
```

or directly on terminal:

```console
python3 -c "import plotext as plt; plt.play_youtube(plt.test_youtube_url)"
```

which will render [this youtube video](https://www.youtube.com/watch?v=FZM9Ibf0Guk) on terminal. 

[Main Guide](https://github.com/piccolomo/plotext#guide), [Play Videos](https://github.com/piccolomo/plotext/blob/master/readme/video.md)