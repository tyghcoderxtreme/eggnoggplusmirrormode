"""
eggnoggmirrormode.py - A Stupid Mirror Mode Mapper for Eggnogg Plus
Dependencies: pynput
"""

from pynput import keyboard

controller = keyboard.Controller()

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
        if key.char == 'w':
            controller.press(keyboard.Key.up)
        elif key.char == 's':
            controller.press(keyboard.Key.down)
        elif key.char == 'a':
            controller.press(keyboard.Key.right)
        elif key.char == 'd':
            controller.press(keyboard.Key.left)
        elif key.char == 'b':
                controller.press('.')
        elif key.char == 'v':
                controller.press(',')

    except AttributeError:
        print(f"Special key pressed: {key}")


def on_release(key):
    try:
        print(f"{key} released")
        if key.char == 'w':
            controller.release(keyboard.Key.up)
        elif key.char == 's':
            controller.release(keyboard.Key.down)
        elif key.char == 'a':
            controller.release(keyboard.Key.right)
        elif key.char == 'd':
            controller.release(keyboard.Key.left)
        elif key.char == 'b':
                controller.release('.')
        elif key.char == 'v':
                controller.release(',')
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        return False

def main():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    )

    listener.start()

    listener.join()

if __name__ == "__main__":
    main()
