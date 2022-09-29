from Windows import get_pixel_batch

class Character:
    def __init__(self, character_name, pixel_identifiers):
        self.character_name = character_name
        self.pixel_identifiers = pixel_identifiers

class Character_handler:
    def __init__(self,character_objects,character_names):
        self.character_objects = character_objects
        self.character_names = character_names
        
    def get_current_character(self):
        pixel_list = []
        for Bros in self.character_objects:
            for pixel_set in Bros.pixel_identifiers:
                pixel_list.append([pixel_set[0][0],pixel_set[0][1]])

        color_pixel_set = get_pixel_batch(pixel_list,(0, 900, 100, 1037))
        n = 0
        for Bro in self.character_objects:
            correct_pixels = 0
            for pixel_set in Bro.pixel_identifiers:
                if pixel_set[1] == color_pixel_set[n]:
                    correct_pixels += 1
                n += 1
                if correct_pixels == len(Bro.pixel_identifiers):
                    return (Bro.character_name)
                
        return('Unknown')

    def update_character_list(self, character_list, current_character):
        if current_character == 'Unknown':
            return(character_list)
        
        current_character_index = character_list.index(current_character)

        character_list.append(character_list.pop(current_character_index))
        return(character_list)


def get_brolist():
    bros = ['Rambro', 'Brommando', 'B.A. Broracus', 'Brodell Walker', 'Bro Hard', 'MacBrover', 'Brade', 'Bro Dredd', 'Bro in Black', 'Snake Broskin',
                      'Brominator', 'Brobocop', 'Indiana Brones', 'Ash Brolliams', 'Mr. Anderbro', 'The Boondock Bros', 'Brochete', 'Bronan the Brobarian',
                      'Ellen Ripbro', 'Time Bro', 'Broniversal Soldier', 'Colonel James Broddock', 'Cherry Broling', 'Bro Max', 'The Brode', 'Double Bro Seven',
                      'Brodator', 'Brocketeer', 'Broheart', 'The Brofessional', 'Brolander', 'Broden', 'Dirty Brory', 'Tank Bro', 'Bro Lee']

    return (bros)

def initalize_characters():

    """pixel identifiers standard
    [coordinate to look at],(RGB color to search for)
    """

    Rambro = Character('Rambro', [[[  7,110],(206,  0,  0)],
                                  [[ 17, 73],(  0,  0,  0)],
                                  [[  0,109],(115,  0,  9)]])

    Brommando = Character('Brommando', [[[ 89, 18],(167,113, 78)],
                                        [[ 10, 37],( 77, 39, 25)],
                                        [[  1, 97],(191,130,113)]])

    Broracus = Character('B.A. Broracus', [[[ 27, 13],( 74, 39, 27)],
                                           [[ 14,122],(208,176,  0)],
                                           [[ 16, 59],(  0,  0,  0)]])

    Walker = Character('Brodell Walker', [[[ 82, 11],(227,230,232)],
                                          [[ 21,129],( 58, 56, 90)],
                                          [[  0, 39],(232,104, 18)]])

    Hard = Character('Bro Hard', [[[ 15, 36],( 57, 28, 17)],
                                  [[  4,124],(120, 87, 51)],
                                  [[  2, 60],(167, 74, 55)]])

    Brover = Character('MacBrover', [[[ 12, 57],(217,188,133)],
                                     [[ 27,131],(164,132,100)],
                                     [[ 22, 75],(153, 86, 36)]])

    Brade = Character('Brade', [[[ 70, 20],(107, 61, 44)],
                                [[  9,125],( 39, 45, 47)],
                                [[ 30, 80],( 90, 49, 34)]])

    Dredd = Character('Bro Dredd', [[[ 78, 45],(198,  7,  7)],
                                    [[ 20, 66],( 97, 33, 24)],
                                    [[ 46,  2],( 40, 32, 15)]])

    Black = Character('Bro in Black', [[[ 39, 12],(103, 64, 23)],
                                       [[ 22,127],(209,214,219)],
                                       [[ 96,125],(  0,  0,  0)]])

    Snake = Character('Snake Broskin', [[[ 98, 53],( 48, 28, 14)],
                                        [[ 10, 71],( 66, 39, 20)],
                                        [[ 13,133],(167, 74, 55)]])

    Terminator = Character('Brominator', [[[ 81, 48],(116,130,141)],
                                          [[ 11, 31],( 77, 39, 25)],
                                          [[ 11,102],( 20, 23, 24)]])

    Cop = Character('Brobocop', [[[ 20, 50],( 55, 62, 68)],
                                 [[ 33, 90],( 22, 20, 23)],
                                 [[  0, 45],(168,174,180)]])

    Indiana = Character('Indiana Brones', [[[ 88, 37],(158, 98, 55)],
                                           [[ 17, 42],( 53, 27, 17)],
                                           [[  5,101],(216,120, 91)]])

    Ash = Character('Ash Brolliams', [[[ 95, 12],( 15, 15, 15)],
                                      [[  4,103],( 20, 23, 24)],
                                      [[ 58,  8],(233,150,115)]])

    Ander = Character('Mr. Anderbro', [[[  4,121],( 39, 45, 47)],
                                       [[ 17, 17],( 15, 15, 15)],
                                       [[ 62,  7],(229,171,144)]])

    Boondock = Character('The Boondock Bros', [[[ 16, 32],( 61, 25,  0)],
                                               [[  5,123],( 72, 84, 88)],
                                               [[  3, 30],( 99, 69, 48)]])

    Brochete = Character('Brochete', [[[ 20, 30],( 64, 26,  7)],
                                      [[ 72,  6],(233,150,115)],
                                      [[ 50,113],(  8,  0,  0)]])

    Bronan = Character('Bronan the Brobarian', [[[ 66, 44],(128, 74, 62)],
                                                [[ 12, 63],( 64, 26,  7)],
                                                [[  0, 34],( 76, 53, 37)]])

    Ripbro = Character('Ellen Ripbro', [[[ 11,107],(  0,  0,  0)],
                                        [[  4,134],(161,161,161)],
                                        [[ 65, 59],(216,120, 91)]])

    Time = Character('Time Bro', [[[  2,132],(  9, 18, 57)],
                                  [[ 25,134],( 24, 37, 92)],
                                  [[  9, 59],(167, 74, 55)]])

    Soldier = Character('Broniversal Soldier', [[[ 40,134],( 85, 85, 85)],
                                                [[ 10, 25],( 49, 49, 49)],
                                                [[ 10,110],( 63, 63, 63)]])

    James = Character('Colonel James Broddock', [[[ 48, 18],( 12, 33,  5)],
                                                 [[  1, 38],(232,104, 18)],
                                                 [[ 11, 87],(160, 56,  8)]])

    Cherry = Character('Cherry Broling', [[[ 31, 58],(167, 74, 55)],
                                          [[ 75, 57],(255,166,122)],
                                          [[ 13, 60],(  6,  8, 17)]])

    Max = Character('Bro Max', [[[ 83, 56],(185, 57, 32)],
                                [[ 70,  7],( 15, 15, 15)],
                                [[  7,128],( 63, 68, 92)]])

    Brode = Character('The Brode', [[[  3, 48],(255,200, 41)],
                                    [[ 88, 11],(255,223, 74)],
                                    [[ 20,112],(189,140, 24)]])

    Zero_zero_seven = Character('Double Bro Seven', [[[ 22,116],(198,179,181)],
                                                     [[ 14, 42],(  0,  0,  0)],
                                                     [[  91,128],( 20, 23, 24)]])

    Predator = Character('Brodator', [[[ 90, 90],(131,131,131)],
                                      [[ 86,  8],(176,176,176)],
                                      [[ 24,104],(245,227,133)]])

    Rocket = Character('Brocketeer', [[[  3, 85],(123,100, 23)],
                                      [[  1,110],(133, 73, 52)],
                                      [[  7,130],( 72, 46, 35)]])

    Heart = Character('Broheart', [[[ 88, 29],(214, 66, 57)],
                                   [[ 38, 18],(175,161,217)],
                                   [[ 30,130],( 93, 63, 37)]])

    Brofession = Character('The Brofessional', [[[  5,  5],( 41, 41, 41)],
                                                [[ 40, 36],( 85,105,123)],
                                                [[ 40,119],( 91, 43, 31)]])

    Lander = Character('Brolander', [[[ 10,128],(146, 89, 38)],
                                     [[ 49,  4],(118, 72, 30)],
                                     [[  0,118],(106, 61, 22)]])

    Broden = Character('Broden', [[[ 14, 96],(166,152,142)],
                                  [[  0, 17],(116,100, 88)],
                                  [[ 85, 10],(237,162,124)]])

    Dirty = Character('Dirty Brory', [[[ 77,  1],(118, 72, 30)],
                                      [[ 47,  6],(216,120, 91)],
                                      [[  6,135],(146, 89, 38)]])

    Tank = Character('Tank Bro', [[[ 25, 75],(255,192,  0)],
                                  [[ 16, 73],(192,151, 26)],
                                  [[  8, 75],(144,119, 18)]])

    Lee = Character('Bro Lee', [[[ 50,  8],( 59, 53, 62)],
                                [[  0, 37],( 23, 21, 24)],
                                [[  2,115],(121, 52, 38)]])

    Bro_object_list = [Rambro, Brommando, Broracus, Walker, Hard, Brover, Brade, Dredd, Black, Snake, Terminator, Cop, Indiana, Ash, Ander,
                       Boondock, Brochete, Bronan, Ripbro, Time, Soldier, James, Cherry,  Max, Brode, Zero_zero_seven, Predator, Rocket, Heart,
                       Brofession, Lander, Broden, Dirty, Tank, Lee]

    Bro_names_list = get_brolist()

    handler = Character_handler(Bro_object_list,Bro_names_list)

    return(handler)
