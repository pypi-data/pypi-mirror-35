# -*- coding: utf-8 -*-

import cv2
import os


def flv2img(flv="ceshivedio.flv",count=5,star=1,end=100):
    
    list_all=[]
    vc=cv2.VideoCapture(flv)
    c=1
    if vc.isOpened():
        rval=True
    else:
        rval=False
    

    while rval:
        rval,frame=vc.read()
        if c % count==0 :
            if (c/count)>=star and (c/count)<=end:
                list_all.append(frame)
        c+=1
    print list_all
    print "there are %d pictures"%len(list_all)
    return list_all
    vc.release()

if __name__ == '__main__':
    flv2img()