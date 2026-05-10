# Terminal video playback via ffpyplayer + YouTube wrapper.

import time
from plotext._settings.system import Image, MediaPlayer, yt_dlp
from plotext._methods.image import _render_image


# Play a local video file with synced audio and video; press q to exit.
def video(path, gray = False, ratio = True, loop = True, width = None, height = None):
    from plotext._kernel.api import terminal
    while True:
        player = MediaPlayer(path, ff_opts = {'out_fmt': 'rgb24'})
        last_height = 0
        try:
            while True:
                if terminal.is_pressed('q'): return
                frame, status = player.get_frame()                                  # status: seconds-to-sleep (float) or 'eof' / 'paused'
                if status == 'eof': break
                if status == 'paused':                                              # player paused — short retry
                    time.sleep(0.05); continue
                if frame is None:                                                   # decoder warming up — honour the suggested wait
                    time.sleep(status if isinstance(status, (int, float)) else 0.01); continue
                ff_image, _pts = frame                                              # (image-like, presentation timestamp)
                w, h = ff_image.get_size()
                pil_image = Image.frombytes('RGB', (w, h), bytes(ff_image.to_bytearray()[0]))
                rendered = _render_image(pil_image, gray, ratio, width, height)
                if last_height: terminal.clean(last_height)
                rendered.print()
                last_height = rendered.get_height()
                if isinstance(status, (int, float)) and status > 0:
                    time.sleep(status)                                              # stay on the player's audio clock
        finally:
            player.close_player()
        if not loop: return


# Play a YouTube URL: resolve to a direct stream URL via yt-dlp, then delegate to video().
def youtube(url, gray = False, ratio = True, loop = True, width = None, height = None):
    with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'format': 'best[ext=mp4]/best'}) as ydl:
        info = ydl.extract_info(url, download = False)
    stream_url = info.get('url')
    video(stream_url, gray = gray, ratio = ratio, loop = loop, width = width, height = height)
