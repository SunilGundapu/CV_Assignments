import cv2, os

try: 
    if not os.path.exists('Frames'): # Creating frames folder if it's not exist
        os.makedirs('Frames') 
  
except OSError: 
    print ('Getting problem while creating folder') 

out = cv2.VideoCapture('1.mp4') #Taking input video

frame_count = 1
while(True):
    retur, frame = out.read() # Capturing Frames
    file_name = './Frames/frame' + str(frame_count) + '.jpg' # Creating file names
    #if(frame_count<=100):
    cv2.imwrite(file_name, frame) #Saving images
    print (file_name + ' ...Created')
    frame_count += 1
    #else:
     #   break
    
out.release() # When everything done, release the capture
cv2.destroyAllWindows()
