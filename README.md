[![PyPi](https://badge.fury.io/py/plotext.svg)](https://badge.fury.io/py/plotext)
[![GitHub stars](https://img.shields.io/github/stars/piccolomo/plotext.svg)](https://github.com/piccolomo/plotext/stargazers)
[![Downloads](https://pepy.tech/badge/plotext/month)](https://pepy.tech/project/plotext)
[![GitHubIssues](https://img.shields.io/badge/issue_tracking-github-blue.svg)](https://github.com/piccolomo/plotext/issues)
[![GitTutorial](https://img.shields.io/badge/PR-Welcome-%23FF8300.svg?)](https://github.com/piccolomo/plotext/pulls)

![logo](https://raw.githubusercontent.com/piccolomo/plotext/master/data/logo.png)

`plotext` **plots directly on terminal** — scatter, line, bar, histogram, datetime, candlestick, error, event, confusion matrix, heatmap, box, images, GIFs, and video (including YouTube). It has no required dependencies; image/video features ship as optional extras.

![subplots](https://raw.githubusercontent.com/piccolomo/plotext/master/data/subplots.png)

## Install

```bash
pip install plotext            # core
pip install plotext[image]     # + image / GIF support (pillow)
pip install plotext[video]     # + video / YouTube support (ffpyplayer, yt-dlp)
```

## Quick start

```python
import plotext as plt

fig = plt.figure
fig.draw(fig.signal(plt.sin()).lines(True))
fig.title("sine wave")
fig.show()
```

Every plot is built on a single figure (`plt.figure`) — pass signal objects to `fig.draw(...)`, then `fig.show()`.

## Documentation

Full guide and API reference: **[plotext.readthedocs.io](https://plotext.readthedocs.io/)**.
