# Play audio with VLC (headless) without blocking the console

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install play-audio-with-vlc

from play_audio_with_vlc import play_with_vlc

play_with_vlc(
    file=r"F:\misfits-skulls.mp3", vlc_path=None, exit_keys="ctrl+alt+o"
)


```



