import keyboard
import time
from pynput import mouse

def log_keystrokes(event):
    if event.event_type == keyboard.KEY_DOWN:
        key_time = time.time()
        with open('ubuntuLogfile.txt', 'a') as f:
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
    if pressed:  # Log only on mouse click press events
        click_time = time.time()
        with open('ubuntuLogfile.txt', 'a') as f:
            f.write(f"[{click_time:.3f}]Mouse Click at ({x}, {y})\n")
            f.flush()

# Hook for keystrokes
keyboard.hook(log_keystrokes)

# Hook for mouse clicks using pynput
mouse_listener = mouse.Listener(on_click=log_mouse_click)
mouse_listener.start()

keyboard.wait('esc')  # Wait for the 'esc' key to be pressed and exit the script
mouse_listener.stop()

