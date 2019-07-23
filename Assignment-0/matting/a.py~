import cv2 
import os
from os.path import isfile, join
import numpy as np


dir_path1 = 'fore1'
dir_path2 = 'back1'

def SplitVideobyFrame():
    out = cv2.VideoCapture('forground_video.mp4') 
    frame_count = 1
    while(True):
        retur, frame = out.read() 
        file_name = './Foregound_Images/frame' + str(frame_count) + '.jpg' 
        if(frame_count<=300):
            cv2.imwrite(file_name, frame) 
            print (file_name + ' ...Created')
            frame_count += 1
        else:
            break
            
    out1 = cv2.VideoCapture('background_video.mp4') 
    frame_count = 1
    while(True):
        retur, frame2 = out.read() 
        file_name = './Backgound_Images/frame' + str(frame_count) + '.jpg' 
        if(frame_count<=300):
            cv2.imwrite(file_name, frame2) 
            print (file_name + ' ...Created')
            frame_count += 1
        else:
            break
    
    out.release() 
    cv2.destroyAllWindows()


def Creating_Video():
	images1 = []
	images2 = []
	new_images=[]
	new_frames=[]
	frames_arr=[]
	for img in os.listdir(dir_path1):
	    if isfile(join(dir_path1, img)):
		    images1.append(img)

	for img in os.listdir(dir_path2):
	    if isfile(join(dir_path2, img)):
		    images2.append(img)

	images1.sort(key = lambda x: int(x[5:-4]))
	images2.sort(key = lambda x: int(x[5:-4]))

	image_path = os.path.join(dir_path1, images1[0])
	frame = cv2.imread(image_path)
	height, width, channels = frame.shape

	out = cv2.VideoWriter('output1.avi', cv2.VideoWriter_fourcc(*'mp4v'), 25.0, (width, height))

	for i in range(len(images1)):
		image_path = os.path.join(dir_path1, images1[i])
		frame = cv2.imread(image_path,cv2.IMREAD_COLOR)
		image_path2 = os.path.join(dir_path2, images2[i])
		frame2 = cv2.imread(image_path2,cv2.IMREAD_COLOR)
		height, width, channels = frame.shape
		for i in range(frame.shape[0]):
			for j in range(frame.shape[1]):
				temp=frame[i,j,:]
				alpha=(((temp[0]/255.0) +(temp[2]/255.0))-(temp[1]/255.0))
				if(alpha<=0):
					new_frames.append(frame2[i,j,:])
				else:
					new_frames.append(frame[i,j,:])
			frames_arr.append(new_frames)
		frames_arr=np.array(frames_arr)
		out.write(frames_arr)
	out.release()
	cv2.destroyAllWindows()
	print("The output video is {}".format(output))

Creating_Video()
