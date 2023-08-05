
import numpy as np
import cv2

def printDict(d, printType=False, nbtab=0):
    if isinstance(d,dict):
        for k, v in d.items():
            data = "\t"*nbtab+str(k) + " : "
            if printType:
                data += str(type(v)).split('\'')[1] + " "
            if isinstance(v,np.ndarray):
                data += "shape="+str(v.shape)
            elif not isinstance(v,dict):
                data += str(v)
            print(data)
            printDict(v, printType, nbtab+1)
    elif nbtab==0:
        print("Empty dict")

def removeEmptyDict(d):
    if not isinstance(d,dict):
        return d
    cleaned_dict = dict()
    for k,v in d.items():
        r = removeEmptyDict(v)
        if r is not None:
            cleaned_dict[k] = r
    if len(cleaned_dict)==0:
        return None
    else:
        return cleaned_dict

def formatInput(inputs, length=-1):
    if not isinstance(inputs,list):
        inputs = [inputs]
    if isinstance(length,int) and length > 0:
        if len(inputs) != length:
            inputs = [inputs[0]]*length
    return inputs

def checkParameter(parameter, default):
    if (isinstance(parameter, list) or isinstance(parameter, tuple)) and len(parameter)==len(default):
        parameter = list(parameter)
        for i in range(len(parameter)):
            if not ( isinstance(parameter[i], int) or isinstance(parameter[i], float) ) :
                parameter[i] = default[i]
    else:
        parameter = list(default)
    return np.array(parameter)

def loadData(image, numImage):
    if isinstance(image, str):
        data = cv2.imread(image)
        name = image
        if len(data.shape) == 3:
            data = cv2.cvtColor(data, cv2.COLOR_BGR2GRAY)
    else:
        data = image
        name = "unknown_image" + str(numImage)
        if len(data.shape) == 3:
            data = cv2.cvtColor(data, cv2.COLOR_RGB2GRAY)
    return data, name