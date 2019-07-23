import cv2, os
import numpy as np
from os.path import isfile, join

path = './Frames/' # Path of images folder
frame_array = []
files = []
for f in os.listdir(path): # Storing the image names in a list
    if isfile(join(path, f)):
        files.append(f)
        
files.sort(key = lambda x: int(x[5:-4])) # Arrange the image files in ascending order

for i in range(len(files)): #
    filename = path+files[i]
    img = cv2.imread(filename)
    frame_array.append(img)
   
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 25.0, (img.shape[1], img.shape[0])) #VideoWriter will take 4 arguments: (output file name, Video Codec, Frames per Second, image height, width)

for i in range(len(frame_array)): # Combine the images 
    out.write(frame_array[i])
print("output video stored")
out.release()
cv2.destroyAllWindows()
