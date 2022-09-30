#Broforce character logger
from Bro_list import initalize_characters, get_brolist
from Windows import get_broforce_window
import time
from tkinter import *
#import Broforce_GUI as gui

character_handler = initalize_characters()
character_ordered_list = get_brolist()

def find_broforce_window():
    pass

def update_brolist(brolist):
    string_temp_holder = ''
    for bros in brolist:
        string_temp_holder += bros + '/n'

    display_text.set(string_temp_holder)

    
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


broforce_window = (0, 0, -1, -1)
while broforce_window[3]<0:
    broforce_window = get_broforce_window()

def main():
    n = 0
    itteration_number = 0
    init_t = time.time()
    frame_rate = 10
    while True:
        if (time.time()-init_t) * frame_rate > itteration_number:
            
            current_character = character_handler.get_current_character()


            if not current_character == character_ordered_list[len(character_ordered_list)-1] and not current_character == 'Unknown':
                character_handler.update_character_list(character_ordered_list,current_character)
                if n >26:
                    print('-------------------')
                    for x in range(9):
                        print(character_ordered_list[x])
                    print('-------------------')
                print('current Bro is '+current_character)
                n += 1
                update_brolist(character_ordered_list)

            itteration_number += 1



