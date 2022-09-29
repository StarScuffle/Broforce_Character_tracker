Zero_zero_seven = [[[22,116],[198,179,181]],
                   [[21,42],[0,0,0]],
                   [[2,119],[45,50,68]]]
                   
Ander = [[[4,121],[39,45,47]],
         [[17,17],[15,15,15]],
         [[62,7],[229,171,144]]]

Ash = [[[95,12],[15,15,15]],
       [[4,103],[20,23,24]],
       [[58,8],[233,150,115]]]

Barbarian = [[[66,44],[128,74,62]],
            [[12,63],[64,26,7]],
             [[0,34],[76,53,37]]]

Black = [[[39,12],[103,64,23]],
         [[22,127],[209,214,219]],
         [[96,125],[0,0,0]]]

Boondock = [[[16,32],[61,25,0]],
            [[5,123],[72,84,88]],
            [[3,30],[99,69,48]]]

Brade = [[[70,20],[107,61,44]],
         [[9,125],[39,45,47]],
         [[30,80],[90,49,34]]]

Brochete = [[[20,30],[64,26,7]],
            [[72,6],[233,150,115]],
            [[50,113],[8,0,0]]]

Pred = [[[90,90],[131,131,131]],
        [[86,8],[176,176,176]],
        [[24,104],[245,227,133]]]

Brode = [[[3,48],[255,200,41]],
         [[88,11],[255,223,74]],
         [[20,112],[189,140,24]]]

Broden = [[[14,96],[166,152,142]],
          [[0,17],[116,100,88]],
          [[85,10],[237,162,124]]]

Brofession = [[[5,5],[41,41,41]],
              [[40,36],[85,105,123]],
              [[40,119],[91,43,31]]]

Terminate = [[[81,48],[116,130,141]],
             [[11,31],[77,39,25]],
             [[11,102],[20,23,24]]]

Command = [[[89,18],[167,113,78]],
           [[10,37],[77,39,25]],
           [[1,97],[191,130,113]]]

BA = [[[27,13],[74,39,27]],
      [[14,122],[208,176,0]],
      [[16,59],[0,0,0]]]

Mac = [[[12,57],[217,188,133]],
       [[27,131],[164,132,100]],
       [[22,75],[153,86,36]]]

Cherry = [[[31,58],[167,74,55]],
          [[75,57],[255,166,122]],
          [[13,60],[6,8,17]]]

Cop = [[[20,50],[55,62,68]],
       [[33,90],[22,20,23]],
       [[0,45],[168,174,180]]]

Dirty = [[[77,1],[118,72,30]],
         [[47,6],[216,120,91]],
         [[6,135],[146,89,38]]]

Dredd = [[[78,45],[198,7,7]],
         [[20,66],[97,33,24]],
         [[46,2],[40,32,15]]]

Hard = [[[15,36],[57,28,17]],
        [[4,124],[120,87,51]],
        [[2,60],[167,74,55]]]

Heart = [[[88,29],[214,66,57]],
         [[38,18],[175,161,217]],
         [[30,130],[93,63,37]]]

Indania = [[[88,37],[158,98,55]],
           [[17,42],[53,27,17]],
           [[5,101],[216,120,91]]]

James = [[[48,18],[12,33,5]],
         [[1,38],[232,104,18]],
         [[11,87],[160,56,8]]]

Lander = [[[10,128],[146,89,38]],
          [[49,4],[118,72,30]],
          [[0,118],[106,61,22]]]

Lee = [[[50,8],[59,53,62]],
       [[0,37],[23,21,24]],
       [[2,115],[121,52,38]]]

Max = [[[83,56],[185,57,32]],
       [[70,7],[15,15,15]],
       [[7,128],[63,68,92]]]

Rambro = [[[7,110],[206,0,0]],
          [[17,73],[0,0,0]],
          [[0,109],[115,0,9]]]

Ripbro = [[[11,107],[0,0,0]],
          [[4,134],[161,161,161]],
          [[65,59],[216,120,91]]]

Rocket = [[[3,85],[123,100,23]],
          [[1,110],[133,73,52]],
          [[7,130],[72,46,35]]]

Snake = [[[98,53],[48,28,14]],
         [[10,71],[66,39,20]],
         [[13,133],[167,74,55]]]

Soilder = [[[40,134],[85,85,85]],
           [[10,25],[49,49,49]],
           [[10,110],[63,63,63]]]

Tank = [[[25,75],[255,192,0]],
        [[16,73],[192,151,26]],
        [[8,75],[144,119,18]]]

Time = [[[2,132],[9,18,57]],
        [[25,134],[24,37,92]],
        [[9,59],[167,74,55]]]

Walker = [[[82,11],[227,230,232]],
          [[21,129],[58,56,90]],
          [[0,39],[232,104,18]]]

basis = [0,900]

from ctypes import windll
dc = windll.user32.GetDC(0)

def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

bros = [Zero_zero_seven,Ander,Ash,Barbarian,Black,Boondock,Brade,Brochete,Pred,Brode,
        Broden,Brofession,Terminate,Command,BA,Mac,Cherry,Cop,Dirty,Dredd,
        Hard,Heart,Indania,James,Lander,Lee,Max,Rambro,Ripbro,Rocket,
        Snake,Soilder,Tank,Time,Walker]

def decimal_to_RGB(color_number):
    color_hex = hex(color_number)
    if len(color_hex)<8:
        lenght = len(color_hex)
        color_hex = color_hex[:2]+'0'*(8-lenght)+color_hex[2:]

    blue = int(color_hex[2:4],16)
    green = int(color_hex[4:6],16)
    red = int(color_hex[6:8],16)

    return[red,green,blue]

from PIL import ImageGrab

def get_pixel_batch(pixel_list):
    screen = ImageGrab.grab()
    color_data = []

    for pixel in pixel_list:
        color_data.append(screen.getpixel((pixel[0],pixel[1])))

    return color_data


import time

bro_names = ['007','ander','ash','barbarian','black','boondock','brade','brochete','Predator','Brode',
             'Broden','Brofessional','Brominator','Bromanndo','Boracus','Brover','Cherry','Cop','Dirty','Dredd',
             'Hard','Heart','Indania','James','Lander','Lee','Max','Rambro','Ripbro','Rocket',
             'Snake','Soilder','Tank','Time','Walker']

time.sleep(5)
current_bro = 'None'
last_known_bro = 'None'
while True:
    n = 0
    is_known = False
    for bro in bros:
        is_correct = 0
        for code in bro:
            x = code[0][0]+basis[0]
            y = code[0][1]+basis[1]
            color = decimal_to_RGB(getpixel(x,y))
            if color == code[1]:
                is_correct+=1
            if is_correct == 3:
                current_bro = bro_names[n]
                is_known = True
        n+=1

    if not is_known:
        current_bro = 'None'
    if not(current_bro == last_known_bro):
        print('current bro is now ' +current_bro)
        last_known_bro = current_bro
