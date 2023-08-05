import os
import re
import subprocess

import keyboard as keyboard__x
import psutil
from what_os import check_os
from winregistry import WinRegistry


def get_vlc_path():
    TEST_REG_PATH = r"HKCR\VLC.3g2\shell\AddToPlaylistVLC"
    with WinRegistry() as client:
        test_entry = client.read_entry(TEST_REG_PATH, "Icon")
        try:
            vlcexe = re.findall('"[^"]+vlc.exe"', test_entry.value)[0].strip('"')
        except Exception as Fehler:
            print(Fehler)
            vlcexe = None
    return vlcexe


def play_with_vlc(file, vlc_path=None, exit_keys="ctrl+alt+o"):
    def kill_process():
        try:
            p = psutil.Process(pid)
            p.kill()
            try:
                keyboard__x.remove_hotkey(exit_keys)
            except Exception:
                pass
        except Exception:
            pass

    if exit_keys:
        keyboard__x.add_hotkey(exit_keys, kill_process)
    if check_os() == "windows" and vlc_path is None:
        vlc_path = get_vlc_path()
    vlc_path = os.path.normpath(vlc_path)
    proc = subprocess.Popen(
        [
            vlc_path,
            "--input-repeat=0",
            "-Idummy",
            "--play-and-exit",
            "--qt-minimal-view",
            file,
        ]
    )
    pid = proc.pid
    return proc

