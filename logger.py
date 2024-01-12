import pyautogui
import keyboard
import time
from pynput import mouse

current_window = None

def log_keystrokes(event):
    global current_window

    if event.event_type == keyboard.KEY_DOWN:
        key_time = time.time()
        with open('logfile.txt', 'a') as f:
            active_window = pyautogui.getActiveWindow()

            if current_window != active_window:
                # If the active window has changed, update window information
                current_window = active_window
                f.write(f"\nWindow Title: {current_window.title}\n")
                
                if current_window.left == 0 and current_window.top == 0:
                    f.write("Window Position: No-Window Selected\n")
                else:
                    f.write(f"Window Position: ({current_window.left}, {current_window.top})\n")
                    
                f.write("Keystrokes and Mouse Clicks:\n")

            if event.name == 'enter':
                f.write('\n')
            elif event.name == 'space':
                f.write(f"[{key_time:.3f}]space\n")
            elif event.name == 'backspace':
                f.write(f"[{key_time:.3f}]lbackspace\n")
            elif event.name == 'ctrl':
                # Handling Ctrl+C as a special case
                next_key_event = keyboard.read_event()
                if next_key_event.event_type == keyboard.KEY_DOWN and next_key_event.name == 'c':
                    f.write(f"[{key_time:.3f}]ctrlc\n")
                else:
                    f.write(f"[{key_time:.3f}]ctrl\n")
                    keyboard.write(event.name)  # Write the Ctrl key without Ctrl+C
            else:
                f.write(f"[{key_time:.3f}]{event.name}\n")
            f.flush()

def log_mouse_click(x, y, button, pressed):
    global current_window

    if pressed:  # Log only on mouse click press events
        click_time = time.time()
        active_window = pyautogui.getActiveWindow()

        with open('logfile.txt', 'a') as f:
            if current_window != active_window:
                # If the active window has changed, update window information
                current_window = active_window
                f.write(f"\nWindow Title: {current_window.title}\n")
                
                if current_window.left == 0 and current_window.top == 0:
                    f.write("Window Position: No-Window Selected\n")
                else:
                    f.write(f"Window Position: ({current_window.left}, {current_window.top})\n")

            f.write(f"[{click_time:.3f}]Mouse Click at ({x}, {y})\n")
            f.flush()

# Hook for keystrokes
keyboard.hook(log_keystrokes)

# Hook for mouse clicks using pynput
mouse_listener = mouse.Listener(on_click=log_mouse_click)
mouse_listener.start()

keyboard.wait('esc')  # Wait for the 'esc' key to be pressed and exit the script
mouse_listener.stop()
