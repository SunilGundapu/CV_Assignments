import cv2 
import os
import argparse
import numpy as np
video_name="1.mp4"

#Creating Directory for saving the extracted images

try:  
	if not os.path.exists('Images_data'): 
		os.makedirs('Images_data') 
except OSError: 
	print (' Creating directory of "Images_data" ') 




##Arguments:
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='jpg', help="extension name. default is 'jpg'.")
ap.add_argument("-o", "--output", required=False, default='Created_Video_Composited.avi', help="output video file")
args = vars(ap.parse_args())

dir_path = 'fore'
dir_path2 = 'back'
ext = args['extension']
output = args['output']



def Extracting_Images(video):
	camera= cv2.VideoCapture(video)
	count_Img= 0
	while(True):
		occur,frame = camera.read()
		if occur:
			name = './Images_data/image_' + str(count_Img) + '.jpg'
			cv2.imwrite(name, frame)
			count_Img+= 1
			#print(name)
		else: 
			break
		if(count_Img==2222):  #some threshold
			break
	print("extracting images are completed...\n")
	camera.release() 
	cv2.destroyAllWindows() 
			


######################## Calling Functions ####################


##calling extracting_images function
#Extracting_Images(video_name)


def Creating_Video():
	#all images into one list
	images = []
	for img in os.listdir(dir_path):
	    if img.endswith(ext):
		    images.append(img)

	images.sort(key = lambda x: int(x[5:-4]))
	#print("images: ",images)
	print("\n########################################### 1 \n")


	images2 = []
	for img in os.listdir(dir_path2):
	    if img.endswith(ext):
		    images2.append(img)

	images2.sort(key = lambda x: int(x[5:-4]))
	#print("images: ",images2)
	print("\n########################################### 2 \n")

	image_path = os.path.join(dir_path, images[0])
	frame = cv2.imread(image_path)
	cv2.imshow('video',frame)
	height, width, channels = frame.shape

	new_images=[]
	fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
	out = cv2.VideoWriter(output, fourcc, 25.0, (width, height))

	for i in range(len(images)):
		image_path = os.path.join(dir_path, images[i])
		frame = cv2.imread(image_path,cv2.IMREAD_COLOR)

		image_path2 = os.path.join(dir_path2, images2[i])
		frame2 = cv2.imread(image_path2,cv2.IMREAD_COLOR)

		cv2.imshow('video',frame)
		#print(type(frame),frame)
		ll=list(frame)
		#print("\n")
		#print(type(ll),len(ll),len(ll[0]),len(ll[1]),len(ll[2]),len(ll[3]),len(ll[700]))
		
		b1_r, b1_g, b1_b = frame[:,:,0], frame[:,:,1], frame[:,:,2]
		#print("b1_r, b1_b, b1_g : ",b1_r.shape,b1_g.shape,b1_b.shape,b1_r)
		height, width, channels = frame.shape
		print(frame.shape)
		#exit()
		new_frame=[]
		for i in range(frame.shape[0]):
			c=0
			s=0
			new_cl=[]
			for j in range(frame.shape[1]):
				temp=frame[i,j,:]
				#print(temp[0]+temp[2]-temp[1]) #R+B-G
				alpha=(((temp[0]/255.0) +(temp[2]/255.0))-(temp[1]/255.0))
				if(alpha<=0):
					#print(" Add second frame pixles.. BG")
					s+=1
					new_cl.append(frame2[i,j,:])
				else:
					#print(" Keep first frame pixels.. FG")
					c+=1
					new_cl.append(frame[i,j,:])
			#exit()
			new_frame.append(new_cl)
		new_frame=np.array(new_frame)
		print(type(new_frame),new_frame.shape,new_frame)
		print("\n")
		out.write(new_frame)
		
		print("new_frame: ",len(new_frame),np.array(new_frame).shape)
		#exit()
	out.release()
	cv2.destroyAllWindows()
	print("The output video is {}".format(output))

Creating_Video()
