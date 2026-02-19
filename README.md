# Mouse Macro Script

A Python-based automation script for recording and playing back mouse clicks and keyboard interactions.

## Features

- Record custom mouse positions
- Playback recorded mouse clicks and movements
- Keyboard hotkey support (Ctrl+M to start macro, Ctrl+Q to quit)
- Save and load position data from JSON
- Support for multiple position recording

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python MouseMacro.py
```

### Menu Options

1. **Run macro** - Executes the automated macro sequence
2. **Get mouse coord + key press capture** - Displays live mouse coordinates in the terminal
3. **Record custom positions** - Records 5 custom mouse positions
4. **Exit** - Quit the application

### Keyboard Controls (during recording/capture modes)

- **c** - Capture current mouse position
- **q** - Quit current mode and return to menu

## Files

- `MouseMacro.py` - Main automation script
- `positions.json` - Stores recorded mouse positions
  
## Notes

This script uses `pynput` for cross-platform mouse and keyboard control, and `pyautogui` for additional automation support.
