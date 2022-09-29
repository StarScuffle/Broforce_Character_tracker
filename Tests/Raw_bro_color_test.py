from PIL import Image
import glob
import numpy as np

images = []

for f in glob.iglob(r'C:\Users\StarScuffle\Documents\Python programs\Broforce character RNG tracker\Raw_bros\*'):
    images.append(np.asarray(Image.open(f)))

images = np.array(images)

target_color = [232,104,18]
target_location = [39,0]
x = 0
n=0
for image in images:
    n+=1
    if all(image[target_location[0]][target_location[1]] == target_color):
        x+=1
        print("n"+str(n))
print(x)
