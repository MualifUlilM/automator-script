import pyautogui
from pynput import mouse
from math import ceil


def on_click(x, y, button, pressed):
    if pressed:
        text_type = ''
        if y > 100:
            text_type = 'center'
        else:
            text_type = 'html'
        print(f'({ceil(x)}, {ceil(y)}, \'{text_type}\'),')



try:
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print("Done")