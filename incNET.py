#!/usr/bin/python
__author__ = "Ehsan Kourkchi"
__copyright__ = "Copyright 02-11-2020"
__version__ = "v1.0"
__status__ = "Production"

import sys
import os
import subprocess
from math import *
import numpy as np
from datetime import *
from pylab import *
import scipy.ndimage
import requests
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

###############################################################
def converIMAGE(img_arr, angle=0., scale=1., size=64):

    img_arr = scipy.ndimage.rotate(img_arr, -angle)

    d1, d2, ch = img_arr.shape

    if scale<1:
        dmax = int(np.max([d1,d2])/scale)
        new_arr = np.zeros((dmax,dmax,ch)).astype(np.uint8)+255
        x1 = int((dmax-d1)/2)
        x2 = x1+d1
        y1 = int((dmax-d2)/2)
        y2 = y1+d2
        new_arr[x1:x2,y1:y2,:] = img_arr
        img_arr = new_arr
    else:
        N = img_arr.shape
        d = N[0]
        p = int(d / scale)
        d1 = int(d / 2 - p / 2)
        d2 = int(d1 + p)
        img_arr = img_arr[d1:d2, d1:d2, :]


    img = Image.fromarray(img_arr, 'RGB').resize((size, size))

    return img

###############################################################
def openImage(params):

    if not 'scale' in params:
        scale = 1
    else:
        scale = params["scale"]
    if not 'angle' in params:
        angle = 0 
    else:
        angle = params["angle"]
    try:
        fileName = params['fileName']
        img = Image.open(fileName)
        img_arr = np.asarray(img)

        if len(img_arr.shape) == 2:
            img_arr = np.stack((img_arr,) * 3, axis=-1)
        elif len(img_arr.shape) == 1:
            return(None, scale, angle)

        if len(img_arr.shape) == 3 and img_arr.shape[2] > 3:
            img_arr = img_arr[:, :, 0:3]
    except:
        return(None, scale, angle)

    
    return img_arr, scale, angle

###############################################################
def predictor_binary(model, All_images):
    
    prediction = model.predict(All_images)

    ## return the likelihood of rejection in %
    return np.median(prediction[:,1])*100

###############################################################
def predictor(model, All_images):

    prediction = model.predict(All_images)
    prediction = np.median(prediction)
    prediction = 0.5*(prediction+1.)*45.+45.
    prediction = np.round(prediction)
    if prediction > 90:
        prediction = 90.
    
    return prediction

###############################################################

def scaleFileName(params):

    if 'fileName' in params:
        scaledImage = '128x128_' + params['fileName'].split('.')[-1] + 'jpg'
    else:
        scaledImage = '128x128_' + str(time.time()).replace('.','_') + '.jpg'

    return scaledImage

###############################################################

def model(params, myModels, saveRescaled=True, scaledImage=None):

    evalINCs = {}

    try: 
        if len(params) == 6:
            RA    = params['alfa']
            Dec   = params['delta']
            npix  = params['npix']
            scale = params['scale']
            angle = params['angle']
            pix   = params['pix']

            url = "http://skyserver.sdss.org/dr12/SkyserverWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra=" + \
                str(RA) + "&dec=" + str(Dec) + "&scale=" + str(pix) + "&width=" + str(npix) + "&height=" + str(npix)
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            img_arr = np.asarray(img)
        else:
            img_arr, scale, angle = openImage(params)
    except:
        return(evalINCs)

    

    if img_arr is None:
        return(evalINCs)
  

    ###############################
    img = converIMAGE(img_arr, angle=angle, scale=scale, size=128)

    if scaledImage is None:
        scaledImage = scaleFileName(params)

    if saveRescaled:
        img.save('./static/tempImages/resized/'+scaledImage, "JPEG")

    img_arr_ = np.asarray(img)
    nx, ny, channels = img_arr_.shape
    All_images = np.zeros((4, nx, ny, channels), dtype=np.dtype('>i4'))
    All_images[0] = img_arr_.reshape(1, nx, ny, channels)

    i = 1
    for delAngle in range(90,360,90):
        img = converIMAGE(img_arr, angle=angle+delAngle, scale=scale, size=128)
        img_arr_ = np.asarray(img)
        All_images[i] = img_arr_.reshape(1, nx, ny, channels)
        i+=1

    All_images = tf.cast(All_images, tf.float32)
    ###############################

    evalRej = {}
    for Model in myModels[0]:
        evalINC = {}
        modelName = Model[0]
        evalRej[modelName] = predictor_binary(Model[1], All_images)

    
    for i, modelGroup in enumerate(myModels[1:]):

        evalINC = {}
        
        for Model in modelGroup:
            modelName = Model[0]
            evalINC[modelName] = predictor(Model[1], All_images)

        gKey = "Group_"+str(i)
        evalINCs[gKey] = evalINC
        
    return evalINCs, evalRej
            
            
###############################################################

def model2html(params, myModels):

    scaledImage = scaleFileName(params)
    evalINCs, evalRej  = model(params, myModels, scaledImage = scaledImage)

    results = """
    <div style="border: 1px solid black;margin: 15px;padding:15px">

                    <table margin="15px">
                    <tr><td>


                        <p>Input image: 128x128 pixels</p>

                        <div id="incImage">
                        <img src="/static/tempImages/resized/" """ + scaledImage + """"  width="256px" height="256px">
                        </div>


                    </td></tr>
                    <tr><td valign="top">

                        <div id="incResults">

                        <p>Neural Network Evaulation ....</p>

                        
    """ 
    allincs = []
    for key, evalGroup in evalINCs.items():
        incs = []
        # results += "<hr>"
        # results += '<p style="background-color:gray;"><b>' + key + '</b></p>'
        for modelName, prediction in evalGroup.items():
            # results += "<p><b>"+modelName+": </b>" + str('%d' % prediction) + "&nbsp;[deg]</p>"
            incs.append(prediction)
            allincs.append(prediction)
        incs = np.asarray(incs)
        med = np.median(incs)
        mean = np.mean(incs)
        # results += "<p style=\"color:blue;\"><b>Med/Mean: </b>" + str('%d' % med) + '/' + str('%d' % mean) + "&nbsp;[deg]</p>"
        # results += "<p style=\"color:blue;\"><b>Median: </b>" + str('%d' % med) + "&nbsp;[deg]</p>"
    
    results += "<hr>"
    results += '<p style="background-color:yellow;"><b>Evaluated Inclinations</b></p>'
    allincs = np.asarray(allincs)
    med = np.median(allincs)
    mean = np.mean(allincs)
    stdev = np.std(allincs)
    # results += "<p style=\"color:green;\"><b>Med/Mean: </b>" + str('%d' % med) + '/' + str('%d' % mean) + "&nbsp;[deg]</p>"
    results += "<p style=\"color:blue;\"><b>Median: </b>" + str('%d' % med) + "&nbsp;[deg]</p>"
    results += "<p style=\"color:blue;\"><b>Mean: </b>" + str('%d' % mean) + "&nbsp;[deg]</p>"
    results += "<p style=\"color:blue;\"><b>Stdev: </b>" + str('%d' % stdev) + "&nbsp;[deg]</p>"


    results += "<hr>"
    results += '<p style="background-color:yellow;"><b>Rejetion Likelihood</b></p>'

    rejs = []
    for rejmodel, rejlike in evalRej.items():
        # results += "<p><b>"+rejmodel+": </b>" + '%.0f'%(rejlike) + '%</p>'
        rejs.append(rejlike)
    
    med = np.median(rejs)
    mean = np.mean(rejs)
    stdev = np.std(rejs)
    # results += "<p style=\"color:red;\"><b>Med/Mean: </b>" + '%.0f'%(med) + '/' + '%.0f'%(mean) + ' %</p>'

    color = 'green'
    if med > 50:
        color = 'red'
    results += "<p style=\"color:"+color+";\"><b>Median: </b>" + '%.0f'%(med) + ' %</p>'
    results += "<p style=\"color:"+color+";\"><b>Mean: </b>" + str('%d' % mean) + ' %</p>'
    results += "<p style=\"color:"+color+";\"><b>Stdev: </b>" + str('%d' % stdev) + ' %</p>'


    results += """
                        </div>


                    </td></tr>
                    </table>
    </div>
    """

    return results, scaledImage
