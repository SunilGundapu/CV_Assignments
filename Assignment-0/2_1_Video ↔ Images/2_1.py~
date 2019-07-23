import cv2, os
import numpy as np
from os.path import isfile, join
try: 
    if not os.path.exists('Frames'): 
        os.makedirs('Frames')   
except OSError: 
    print ('Getting problem while creating folder') 

def SplitVideobyFrame():
    out = cv2.VideoCapture('example.mp4') 
    frame_count = 1
    while(True):
        retur, frame = out.read() 
        file_name = './Frames/frame' + str(frame_count) + '.jpg' 
        if(frame_count<=300):
            cv2.imwrite(file_name, frame) 
            print (file_name + ' ...Created')
            frame_count += 1
        else:
            break
    
    out.release() 
    cv2.destroyAllWindows()

def ImagestoVideo():
    path = './Frames/'
    frame_array = []
    files = []
    for f in os.listdir(path):
        if isfile(join(path, f)):
            files.append(f)
            
    print(files)
    files.sort(key = lambda x: int(x[5:-4]))
    
    for i in range(len(files)): 
        filename = path+files[i]
        img = cv2.imread(filename)
        frame_array.append(img)
        
    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 10.0, (img.shape[1], img.shape[0]))
    
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    print("output video stored")
    out.release()
    cv2.destroyAllWindows()
    
SplitVideobyFrame()
ImagestoVideo()
