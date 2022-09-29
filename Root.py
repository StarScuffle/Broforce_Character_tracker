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
mass_bro_string = ''
bros = get_brolist()
for b in bros:
    mass_bro_string += b + '\n'

display_text.set(mass_bro_string)
display = Label(root, textvariable=display_text, justify=LEFT)
display.pack()

