import cv2,os

try: 
    if not os.path.exists('Frames'): # Creating frames folder if it's not exist
        os.makedirs('Frames') 
  
except OSError: 
    print ('Getting problem while creating folder') 

out = cv2.VideoCapture(-1) # Opening WebCam
frames_count = 1

while(True):
    retur, frame = out.read()
    cv2.imshow('frame',frame)
    if retur: 
        file_name = './Frames/frame' + str(frames_count) + '.jpg'
        print (file_name + 'Created') 
        cv2.imshow('image', frame)
        cv2.imwrite(file_name, frame) # Extracted images stored in folder
        frames_count += 1
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: 
        break

out.release()
cv2.destroyAllWindows()
