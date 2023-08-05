import numpy as np
import cv2
import traceback

import micral_utils

def norm(t):
    return np.sqrt(np.square(t[0])+np.square(t[1]))

def movingAverage(tab, n):
    avtab = np.zeros(tab.shape)
    lentab = len(avtab)
    for i in range(lentab):
        avtab[i] = tab[max(0,i-n):min(i+n,lentab-1)].mean()
    return avtab
def movingMedian(tab, n):
    avtab = np.zeros(tab.shape)
    lentab = len(avtab)
    for i in range(lentab):
        avtab[i] = np.median(tab[max(0,i-n):min(i+n,lentab-1)])
    return avtab

def to1DSpec(spec2d):
    weigth = np.zeros(int(norm(spec2d.shape)/2)+5)
    h, w = spec2d.shape
    for y in range(h):
        for x in range(w):
            weigth[int(norm((y-h/2,x-w/2)))] += np.square(abs(spec2d[y,x]))
    for i in range(len(weigth)):
        weigth[i] = np.sqrt(weigth[i])/(2*np.pi*(i+1))
    return weigth

def findValues(tab,limit):    
    left = 0
    while tab[left] < limit:
        left += 1
    # y = a*(x-x1)+y1
    # a = (y2-y1)/(x2-x1 (=1))
    # x = (y-y1)/(y2-y1) + x2
    
    if tab[left]-tab[left-1] != 0:
        left = (limit-tab[left-1])/(tab[left]-tab[left-1])+(left-1)
    
    right = len(tab)-1
    while tab[right] < limit:
        right -= 1
        
    if tab[right+1]-tab[right] != 0:
        right = (limit-tab[right])/(tab[right+1]-tab[right])+(right)
    
    return left,right

def harmonicMeasurementProcessor(img, plotFull, param):
    
    output_dict = dict()
    
    if img.shape == (0,0):
        return output_dict
    
    output_dict['process'] = dict()
    
    border = 3
    img = cv2.Laplacian(img,cv2.CV_64F,ksize=int(param[0]))[border:-border,border:-border]
    img = (img-img.mean())/img.std()
    
    dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
    mag = np.abs(np.fft.fftshift(dft)[:,:,0])
    mag = (mag-mag.mean())/mag.std()
    if plotFull:
         output_dict['process']['spectrum2d'] = mag
    
    spec = (to1DSpec(mag))
    spec = np.insert(spec, 0, 0)
    limit = spec.max()/param[1]
    left, right = findValues(spec,limit)
    if plotFull:
        output_dict['process']['spectrum1d'] = spec
        output_dict['process']['limit'] = limit
        output_dict['process']['left'] = left
        output_dict['process']['right'] = right
    
    maxHarmonicity = 3.0
    output_dict['harmonicity'] = np.clip((maxHarmonicity-np.sqrt(((right-left)**2)/((right+left)/2)))/maxHarmonicity * 100.0, 0, 100)
    output_dict['argmax'] = np.argmax(spec)
    
    return output_dict

def harmonicMeasurementCore(images, plotFull, plotTimeline, parameters):
    output_dict = dict()
    images = micral_utils.formatInput(images)
    parameters = micral_utils.formatInput(parameters, length=len(images))
    for numImage in range(len(images)):
        try:
            data, name = micral_utils.loadData(images[numImage], numImage)
            parameter = micral_utils.checkParameter(parameters[numImage], (3, np.sqrt(2)))
            output_dict[name] = harmonicMeasurementProcessor(data, plotFull, parameter)
        except Exception as e:
            print("image " + str(numImage) + " raise : " + str(e.__doc__))
            traceback.print_exc()
            pass
    return micral_utils.removeEmptyDict(output_dict)