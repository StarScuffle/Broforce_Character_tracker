from tkinter import *
from Bro_list import get_brolist

def find_broforce_window():
    s = display_text.get()
    s += '1\n'
    display_text.set(s)

root = Tk()

frame = Frame(root)
frame.pack()

mainmenu = Menu(frame)
mainmenu.add_command(label = "Find Broforce", command = find_broforce_window)

root.config(menu = mainmenu)

display_text = StringVar()
bro_display_string = ''

display_text.set(bro_display_string)
display = Label(root, textvariable=display_text, justify=LEFT)
display.pack()

def update_brolist(brolist):
    string_temp_holder = ''
    for bros in brolist:
        string_temp_holder += bros + '/n'

    display_text.set(string_temp_holder)
