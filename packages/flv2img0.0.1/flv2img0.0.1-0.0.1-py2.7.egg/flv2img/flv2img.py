# -*- coding: utf-8 -*-

import cv2
import os


def flv2img(flv="ceshivedio.flv",count=5):
    
    list_all=[]
    vc=cv2.VideoCapture(flv)
    c=1
    if vc.isOpened():
        rval=True
    else:
        rval=False
    

    while rval:
        rval,frame=vc.read()
        if c % count== 0:
            list_all.append(frame)
        else:
            '.'
        c+=1
    print list_all
    print "there are %d pictures"%len(list_all)
    return list_all
    vc.release()

if __name__ == '__main__':
    flv2img()