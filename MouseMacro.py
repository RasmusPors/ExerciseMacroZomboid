from pynput import mouse, keyboard
import time
import threading
import pyautogui
import json
import os
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller as KeyboardController

# Global variable to store recorded positions
POSITIONS_FILE = "positions.json"
recorded_positions = {
    "pos1": [2867, 402],
    "pos2": [1837, 1022],
    "pos3": [2237, 1322],
    "pos4": [2477, 1322],
    "pos5": [0, 0],
}

def load_positions():
    """Load positions from file if it exists, otherwise use defaults"""
    global recorded_positions
    if os.path.exists(POSITIONS_FILE):
        try:
            with open(POSITIONS_FILE, 'r') as f:
                recorded_positions = json.load(f)
            print("Positions loaded from file.")
        except:
            print("Error loading positions, using defaults.")
    return recorded_positions

def save_positions():
    """Save positions to file"""
    with open(POSITIONS_FILE, 'w') as f:
        json.dump(recorded_positions, f, indent=2)
    print(f"Positions saved to {POSITIONS_FILE}")

def record_positions():
    """
    Record 5 custom mouse positions.
    User will move mouse and press 'c' for each position.
    """
    global recorded_positions
    pos_lock = threading.Lock()
    current_pos = [0, 0]
    positions_captured = []
    position_names = ["Position 1", "Position 2", "Position 3", "Position 4", "Position 5"]
    position_keys = ["pos1", "pos2", "pos3", "pos4", "pos5"]
    
    def on_move(x, y):
        nonlocal current_pos
        with pos_lock:
            current_pos = [x, y]

    def on_press(key):
        try:
            k = key.char.lower()
        except AttributeError:
            k = None

        if k == "c":
            with pos_lock:
                pos = current_pos.copy()
            positions_captured.append(pos)
            print(f"\n✓ {position_names[len(positions_captured)-1]} captured: x={pos[0]}, y={pos[1]}")
            
            if len(positions_captured) < 5:
                print(f"\nMove to {position_names[len(positions_captured)]} and press 'c'")
            else:
                print("\n✓ All positions recorded!")
                return False  # stop listener
                
        elif k == "q":
            print("\nRecording cancelled.")
            return False

    # Start mouse listener
    m_listener = mouse.Listener(on_move=on_move)
    m_listener.start()

    print("\n=== Recording Custom Positions ===")
    print(f"Move to {position_names[0]} and press 'c' (or 'q' to cancel)\n")

    # Start keyboard listener
    with keyboard.Listener(on_press=on_press) as k_listener:
        while len(positions_captured) < 5:
            with pos_lock:
                x, y = current_pos
            print(f"\rMouse: x={x:4d}, y={y:4d}", end="", flush=True)
            time.sleep(0.05)

    m_listener.stop()
    
    # Save positions if all 5 were captured
    if len(positions_captured) == 5:
        for i, key in enumerate(position_keys):
            recorded_positions[key] = positions_captured[i]
        save_positions()
        print("\nPositions updated successfully!")
        return True
    return False


def coord_and_key_capture():
    """
    Prints mouse coordinates repeatedly.
    Press:
      - 'c' to capture current mouse position
      - 'q' to quit this mode
    """
    pos_lock = threading.Lock()
    current_pos = (0, 0)
    stop_flag = threading.Event()

    def on_move(x, y):
        nonlocal current_pos
        with pos_lock:
            current_pos = (x, y)

    def on_press(key):
        try:
            k = key.char.lower()
        except AttributeError:
            k = None

        if k == "c":
            with pos_lock:
                x, y = current_pos
            print(f"\nCaptured position: x={x}, y={y}")
        elif k == "q":
            print("\nExiting coordinate mode.")
            stop_flag.set()
            return False  # stop keyboard listener

    # Start mouse listener (updates current_pos)
    m_listener = mouse.Listener(on_move=on_move)
    m_listener.start()

    print("\nCoordinate mode running.")
    print("Press 'c' to capture current position, 'q' to quit.\n")

    # Start keyboard listener (captures/quit)
    with keyboard.Listener(on_press=on_press) as k_listener:
        while not stop_flag.is_set():
            with pos_lock:
                x, y = current_pos
            print(f"\rMouse: x={x:4d}, y={y:4d}   (c=capture, q=quit)", end="", flush=True)
            time.sleep(0.05)

    m_listener.stop()


def run_macro():
    load_positions()  # Load latest positions
    
    pyautogui.sleep(1)
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')
    
    # Move to Position 1
    pyautogui.moveTo(recorded_positions["pos1"][0], recorded_positions["pos1"][1], duration=2) 
    pyautogui.mouseDown(button='left')
    time.sleep(0.3)
    pyautogui.mouseUp(button='left')
    pyautogui.sleep(30)
    
    pyautogui.keyDown('s')
    time.sleep(0.3)
    pyautogui.keyUp('s')
    time.sleep(0.2)
    pyautogui.keyDown('s')
    time.sleep(0.3)
    pyautogui.keyUp('s')
    
    # Move to Position 2
    pyautogui.moveTo(recorded_positions["pos2"][0], recorded_positions["pos2"][1], duration=2)
    pyautogui.mouseDown(button='right')
    time.sleep(0.3)
    pyautogui.mouseUp(button='right')
    
    # Move to Position 3
    pyautogui.moveTo(recorded_positions["pos3"][0], recorded_positions["pos3"][1], duration=1)
    # Move to Position 4
    pyautogui.moveTo(recorded_positions["pos4"][0], recorded_positions["pos4"][1], duration=1)
    
    pyautogui.mouseDown(button='left')
    time.sleep(0.3)
    pyautogui.mouseUp(button='left')

    #Move to Position 5 Painkillers
    pyautogui.moveTo(recorded_positions["pos5"][0], recorded_positions["pos5"][1], duration=2)

    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')

    pyautogui.sleep(90)  
    run_macro()  # repeat indefinitely
    
def run_macro_test():
    pyautogui.moveTo(2867, 402, duration=2) 
    pyautogui.keyDown('9')
    time.sleep(0.3)
    pyautogui.keyUp('9')
    time.sleep(0.2)
    pyautogui.keyDown('9')
    time.sleep(0.3)
    pyautogui.keyUp('9')
    
def main_menu():
    while True:
        print("\n=== Menu ===")
        print("1) Run macro")
        print("2) Get mouse coord + key press capture in terminal")
        print("3) Record custom positions (5s positions)")
        print("4) Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            pyautogui.moveTo(10, 10, duration=2)
            pyautogui.click()
            pyautogui.sleep(1)
            run_macro()
            print("Macro executed!")
            
        elif choice == "2":
            coord_and_key_capture()
        elif choice == "3":
            record_positions()
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try 1, 2, 3, or 4.")


if __name__ == "__main__":
    load_positions()  # Load positions at startup
    main_menu()
    