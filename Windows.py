import win32gui
from PIL import ImageGrab

def get_broforce_window():
    window_id = win32gui.FindWindowEx(None, None, None, 'Broforce')
    if not(window_id == 0):
        return win32gui.GetWindowRect(window_id)
    else:
        return (0, 0, -1, -1)

def get_pixel_batch(pixel_list, box):
    screen = ImageGrab.grab(bbox = box)
    color_data = []

    for pixel in pixel_list:
        color_data.append(screen.getpixel((pixel[0],pixel[1])))

    return color_data
