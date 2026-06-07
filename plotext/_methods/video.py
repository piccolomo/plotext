# Terminal video playback via ffpyplayer.

import time
from plotext._settings.system import Image, MediaPlayer, yt_dlp
from plotext._methods.file import correct as _correct_path
from plotext._methods.image import _render_image, _exit_hint


# Resolve a YouTube URL to a direct stream URL via yt-dlp. Returns the stream URL on success or None on failure (with the underlying error printed). Private helper for video() — YouTube stream URLs are time-limited tokens that must be played directly rather than cached, so they take a different path from regular media URLs (which go through _correct_path's download-and-cache).
def _resolve_youtube(url):
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'format': 'best[ext=mp4]/best'}) as ydl:
            info = ydl.extract_info(url, download = False)
    except Exception as e:
        print(f"plotext.video: could not resolve {url!r} ({e})")
        return None
    return info.get('url')


# Play a video (local path, "~/…", direct http/https URL, or a YouTube URL). Local paths and direct URLs are normalized through _correct_path (URLs downloaded once and cached); YouTube URLs (host matches youtube.com / youtu.be) are resolved to a stream URL via _resolve_youtube and played directly. Press q to exit; loop=False (default) plays once; _hint=False suppresses the overlay.
def video(path, gray = False, ratio = True, loop = False, width = None, height = None, _hint = True):
    from plotext._kernel.api import terminal
    if isinstance(path, str) and ('youtube.com' in path or 'youtu.be' in path):
        path = _resolve_youtube(path)
        if path is None: return
    else:
        path = _correct_path(path)
    hint = _exit_hint()
    while True:
        try:
            player = MediaPlayer(path, ff_opts = {'out_fmt': 'rgb24'})
        except Exception as e:
            print(f"plotext.video: could not open {path!r} ({e})")
            return
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
                if _hint: rendered.insert(0, rendered.get_height() - 1, hint)   # overwrite the bottom-left with the exit hint (in place, no extra row)
                if last_height: terminal.clean(last_height, _prompt = 0)        # up exactly the printed rows (frame need not fill the screen)
                rendered.print()
                last_height = rendered.get_height()
                if isinstance(status, (int, float)) and status > 0:
                    time.sleep(status)                                              # stay on the player's audio clock
        finally:
            player.close_player()
        if not loop: return


