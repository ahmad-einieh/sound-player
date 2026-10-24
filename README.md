# Sound Player

A small Python desktop music player using Tkinter for its interface and Pygame's mixer for playback.

## Requirements

- Python 3, Tkinter, and a graphical desktop session.
- Pygame and a working audio output device.

On Ubuntu/Debian, install `python3-tk` if Tkinter is missing.

## Run

Create and activate a Python virtual environment, then run:

```bash
python -m pip install pygame
python soundplayer.py
```

## Usage

1. Choose a folder containing audio files when the folder dialog opens.
2. Select a file from the playlist.
3. Use **Play Music**, **Stop Music**, **Pause Music**, and **Resume Music** to control playback.

Use audio formats supported by your Pygame/SDL_mixer installation, such as WAV or MP3 where supported.

## Limitations

- The playlist lists every entry in the chosen folder, including non-audio files and subdirectories. Select an actual, supported audio file.
- Cancelling the folder dialog is not handled and can stop startup.
- Playback/device errors are not caught, and there is no automatic next-track playback or volume control.

All application code is in [`soundplayer.py`](soundplayer.py).
