#Broforce character logger
from Bro_list import initalize_characters, get_brolist
from Windows import get_broforce_window
import time

character_handler = initalize_characters()
character_ordered_list = get_brolist()

'''
initalize_windows()
'''
broforce_window = (0, 0, -1, -1)
while broforce_window[3]<0:
    broforce_window = get_broforce_window()

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

        itteration_number += 1
        if itteration_number%100 == 0:
            print(((time.time()-init_t) * frame_rate)-itteration_number)


    
