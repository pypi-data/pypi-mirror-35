import cv2
import numpy as np
import traceback

import micral_utils

def removeBlob2(img, treshold, oldColor, newColor):
    params = cv2.SimpleBlobDetector_Params()
     
    params.minThreshold = 0
    params.maxThreshold = 256
    
    params.filterByArea = True
    params.minArea = 0
    params.maxArea = treshold
    
    params.filterByColor = True
    params.blobColor = oldColor
    
    params.filterByCircularity = False
    params.filterByInertia = False
    params.filterByConvexity = False
    
    params.minDistBetweenBlobs = 0
    
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs
    keypoints = detector.detect(img)
    for key in keypoints:
        img_cpy = np.copy(img)
        size = cv2.floodFill(img_cpy, None, (int(key.pt[0]),int(key.pt[1])), (newColor))[0]
        if size <= treshold:
            cv2.floodFill(img, None, (int(key.pt[0]),int(key.pt[1])), (newColor))[0]
        
    return img

def removeBlob(img, sizeMinCristal, sizeMinFin):
    img = removeBlob2(img, sizeMinCristal, 0, 255)
    img = removeBlob2(img, sizeMinFin, 255, 0)
    return img

def norm(t):
    return np.sqrt(np.square(t[0])+np.square(t[1]))
def to0DSpec(spec2d):
    weigth = 0
    h, w = spec2d.shape
    return np.sum(spec2d)/(h*w)
    for y in range(h):
        for x in range(w):
            weigth += (abs(spec2d[y,x]))*norm((y-h/2,x-w/2))
    return weigth/(w*h)

def indice(x,y,t):
    return np.clip(x, 0, t.shape[1]-1), np.clip(y, 0, t.shape[0]-1)

def localfft(img_in, size):
    img = np.zeros(img_in.shape, dtype=np.float32)
    for y in range(img_in.shape[0]):
        for x in range(img_in.shape[1]):
            x1, y1 = indice(x-size, y-size, img_in)
            x2, y2 = indice(x+size, y+size, img_in)
            dft = cv2.dft(np.float32(img_in[y1:y2,x1:x2]), flags = cv2.DFT_COMPLEX_OUTPUT)
            mag = np.abs(np.fft.fftshift(dft)[:,:,0])
            mag = (mag-mag.mean())/mag.std()
            img[y,x] = to0DSpec(mag)
    return img

def localeq(img_in, size):
    img = np.zeros(img_in.shape, dtype=np.float32)
    for y in range(img_in.shape[0]):
        for x in range(img_in.shape[1]):
            #x1, y1 = indice(x-size, y-size, img_in)
            #x2, y2 = indice(x+size, y+size, img_in)
            minAround = 0#•np.min(img_in[y1:y2,x1:x2])
            maxAround = 1#np.max(img_in[y1:y2,x1:x2])
            img[y,x] = (img_in[y,x] - minAround) / (maxAround- minAround)
    return img

def printIm(img, plotFull, plotDetails, plotNum):
    if img.max()-img.min() != 0:
        img = np.uint8((img - img.min())/(img.max()-img.min()) * 255.0)
    else:
        img = np.uint8(img)
    output_dict = dict()
    if plotFull or plotDetails:
        output_dict['id'] = plotNum
    if plotFull:
        output_dict['full'] = np.clip(img, 0, 255).astype('uint8')
    if plotDetails is not None and plotDetails is not False:
        length = int(np.sqrt(np.square(plotDetails[0]-plotDetails[2]) + np.square(plotDetails[1]-plotDetails[3])))
        img_out = np.empty(length, dtype=np.uint8)
        for i in range(length):
            x = int(plotDetails[0] + i/length * (plotDetails[2]-plotDetails[0]))
            y = int(plotDetails[1] + i/length * (plotDetails[3]-plotDetails[1]))
            img_out[i] = np.uint8(img[y,x])
        output_dict['details'] = img_out
    return img, plotNum+1, output_dict

def grainSeparatorProcessor(img_ori, name, plot, plotFull, plotDetails, param):
    image_dict = dict()
    
    if img_ori.shape == (0,0):
        return image_dict
    
    img = np.copy(img_ori)
    
    image_dict['process'] = dict()
    
    if plotDetails is not None and plotDetails is not False:
        if isinstance(plotDetails,list) and len(plotDetails) == 4:
            plotDetails = list(plotDetails)
        else:
            plotDetails = [-1]*4
        for i, val in enumerate([img_ori.shape[0]*0.25,img_ori.shape[0]*0.5,img_ori.shape[0]*0.75,img_ori.shape[0]*0.5]):
            if plotDetails[i] < 0:
                plotDetails[i] = int(val)
        img_out = img_ori.copy()
        cv2.line(img_out,(plotDetails[0],plotDetails[1]),(plotDetails[2],plotDetails[3]),(255,0,0), 5)
        image_dict['process']['preprocess'] = dict(id=0, details=img_out)
    
    
    plotNum = 1
    img, plotNum, image_dict['process']['input'] = printIm(img, plotFull, plotDetails, plotNum)
    
    img = np.sqrt(np.square(cv2.Sobel(img,cv2.CV_64F,1,0,ksize=int(param[0]))) + np.square(cv2.Sobel(img,cv2.CV_64F,0,1,ksize=int(param[0]))))
    img = img[int(param[0]):-int(param[0]),int(param[0]):-int(param[0])]
    img_ori = img_ori[int(param[0]):-int(param[0]),int(param[0]):-int(param[0])]
    img, plotNum, image_dict['process']['derivate'] = printIm(img, plotFull, plotDetails, plotNum)
    
    img = cv2.medianBlur(img, int(param[1]))
    img, plotNum, image_dict['process']['median'] = printIm(img, plotFull, plotDetails, plotNum)
    
    img = cv2.blur(img,(int(param[2]),int(param[2])))
    img, plotNum, image_dict['process']['average'] = printIm(img, plotFull, plotDetails, plotNum)
    
    th, img = cv2.threshold(img, int(param[3]), 255, cv2.THRESH_BINARY)
    img, plotNum, image_dict['process']['threshold'] = printIm(img, plotFull, plotDetails, plotNum)
    
    img = removeBlob(img, int(param[4]), int(param[5]))
    img, plotNum, image_dict['process']['blob'] = printIm(img, plotFull, plotDetails, plotNum)
    
    unique, counts = np.unique(img, return_counts=True)
    
    if plot:
        alpha = 0.3
        tresh_color = np.zeros((img.shape[0],img.shape[1],3), dtype=np.uint8)
        tresh_color[:,:,0] = img
        tresh_color[:,:,1] = 255-img
        image_dict['overlay'] = cv2.addWeighted(tresh_color, alpha, cv2.cvtColor(img_ori, cv2.COLOR_GRAY2RGB), 1 - alpha, 0)
    
    if len(counts) < 2:
        image_dict['coarse'] = unique[0]/255 * 100.0
    else:
        image_dict['coarse'] = counts[0]/(counts[0]+counts[1])*100.0
    
    image_dict['ultrafine'] = 100-image_dict['coarse']
    
    if image_dict['ultrafine'] != 0:
        image_dict['ratio'] = image_dict['coarse'] / image_dict['ultrafine']
        
    return image_dict
    
def grainSeparatorCore(images, plot, plotFull, plotDetails, parameters):
    output = dict()
    images = micral_utils.formatInput(images)
    parameters = micral_utils.formatInput(parameters, length=len(images))
    for numImage in range(len(images)):
        try:
            data, name = micral_utils.loadData(images[numImage], numImage)
            parameter = micral_utils.checkParameter(parameters[numImage], (3,15,10,95,1000,6000))
            output[name] = grainSeparatorProcessor(data, name, plot, plotFull, plotDetails, parameter)
        except Exception as e:
            print("image " + str(numImage) + " raise : " + str(e.__doc__))
            traceback.print_exc()
            pass
    return micral_utils.removeEmptyDict(output)