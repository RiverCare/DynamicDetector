import time
start = time.time()
import cv2
import numpy as np
import os

f = 'initial4' #assign the directory
no = ['27-1','27-2','27-7','27-10','29-3','28-6','28-7','28-9','28-10',
    '27-3','27-4','27-6','27-8','28-1','28-2','28-8']　#assign the mice's number.

for t in range (0, 1):
    n='27-1'
    cap = cv2.VideoCapture('./'+f+'/'+n+'.avi') #assign video's directory
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS) #fetch the fps of video
    print("Length = ",length)
    print("Width = ", width)
    print("Height = ", height)
    print("fps = ", fps)

    try:
        if not os.path.exists(f+'/'+n+'/'):
            os.makedirs(f+'/'+n)
    except OSError:
        print ('Error: Creating directory of data')
    
    currentFrame = 0
    
    for x in range(0, length-2):
        # Capture frame-by-frame
        ret, frame = cap.read()
    
    
        # Saves image of the current frame in jpg file
        if fps == 16:
            name = './'+f+'/'+n+'/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
            
        elif fps == 40:
    
            if float(x/10).is_integer() == True:
                name = './'+f+'/'+n+'/frame' + str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                currentFrame += 1
            elif float((x+0.5)/2.5).is_integer() == True:
                name = './'+f+'/'+n+'/frame' + str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                currentFrame += 1
            elif float(x/2.5).is_integer() == True:
                name = './'+f+'/'+n+'/frame' + str(currentFrame) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                currentFrame += 1
        else:
            name = './'+f+'/'+n+'/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
        
    

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
print(time.time()-start) 
