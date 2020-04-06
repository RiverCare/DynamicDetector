import numpy as np
from skimage import color
from skimage import io
import time
import matplotlib


start = time.time()

fo='initial4'　#assign the directory
number=['27-1','27-2','27-7','27-10','29-3','28-6','28-7','28-9','28-10',
    '27-3','27-4','27-6','27-8','28-1','28-2','28-8']　#assign mice's numbers

for t in range (0, 1):
    no = number[t]
    x = 0
    y = 0
    min_f = [227,296,252,307,223,317,240,140,167,207,211,240,318,127,212,220]　#assign the start frame index of each mice's numbers.
    mf = min_f[t]
    max_f = mf+4780 #assign the maximum end frame index
    for n in range(mf,max_f):
        f = "frame"+str(n)
        fx ="frame"+str(n+1)
        im = color.rgb2gray(io.imread("./"+fo+"/"+no+"/"+f+".jpg"))
    
        imx = color.rgb2gray(io.imread("./"+fo+"/"+no+"/"+fx+".jpg"))
        
        imsub = imx-im
        
        imzero = imsub
        imzero[imzero<0.12] = 0 # values from 0.11 to 0.15 are the best parameters
        matplotlib.image.imsave('imzero'+str(n)+'.png', imzero)
    
        x += np.sum(imzero)
        y += imzero
        
    print(x)
    matplotlib.image.imsave(fo+'/'+no+"all.png", y)
print(int(time.time()-start))
 
