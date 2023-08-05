# -*- coding: utf-8 -*-

import cv2
import os
from vcvf import face_detector as fd


def faceimg(flv="ceshivedio.flv",count=2,star=1,end=100):
    face=flv2img(flv,count,star,end)
    fd1=fd.face_detector(2)
    face_list=[]
    for i in range(len(face)):
        img=face[i]
        num,list1,time=fd1.detect_face(img)
        if num>=1:
            face_list.append(img)
 
    print "there are %d face pictures"%len(face_list)
    return face_list


def flv2img(flv="ceshivedio.flv",count=2,star=1,end=100):
    
    list_all=[]
    vc=cv2.VideoCapture(flv)
    c=1
    fps=dps(flv)
    fps=int(fps/count)
    
    if vc.isOpened():
        rval=True
    else:
        rval=False
    
    j=0
    while rval:
        #print c%fps
        rval,frame=vc.read()
        if c%fps==0:
            if (c/fps)>=star and (c/fps)<=end:
                j+=1
                list_all.append(frame)
        c+=1
        if j>end:
            break
            
    if j<(end-star+1):
        print "Sorry,pictures are not enough"
    #print list_all
    print "there are %d pictures"%len(list_all)
    return list_all
    vc.release()


def dps(vedio):
    video = cv2.VideoCapture(vedio)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps
   
   
if __name__ == '__main__':
    faceimg()