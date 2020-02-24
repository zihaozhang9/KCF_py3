# -*- coding: utf-8 -*
import numpy as np 
import cv2
import sys
from time import time

import kcftracker
from copy import deepcopy



def vedio_detect():
    tracker = kcftracker.KCFTracker(True, True, True) 
    
    video = cv2.VideoCapture(0)#("F:\\software\\Project\\car_vedio\\2018-12-06-15-26-06.avi")#"D:\\temp\\A.mp4"
    ok, frame = video.read()
    org_h,org_w,_ = frame.shape
    #frame = cv2.resize(frame,(  int(0.4*org_w),int(0.4*org_h) ))
    while ok:
        ret, frame = video.read()
        org_h,org_w,_ = frame.shape
        #frame = cv2.resize(frame,(  int(0.4*org_w),int(0.4*org_h) ))
        cv2.imshow('img2',frame)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    init_rect = cv2.selectROI(frame, False)  #(215, 127, 240, 340)
    cv2.destroyAllWindows()
    tracker.init(list(init_rect), frame)
    
    ret, frame = video.read()
    org_h,org_w,_ = frame.shape
    #frame = cv2.resize(frame,(  int(0.4*org_w),int(0.4*org_h) ))
    t0 = cv2.getTickCount()
    while ret:

        boundingbox,peak_value = tracker.update(frame)
        #print(boundingbox)
        boundingbox = [int(i) for i in boundingbox] #map(int, )
        im_show = deepcopy(frame) 
        
        cv2.rectangle(im_show,(boundingbox[0],boundingbox[1]), (boundingbox[0]+boundingbox[2],boundingbox[1]+boundingbox[3]), (0,255,255), 1)
        cv2.putText(im_show, 'peak_value:%.2f '%(peak_value), (8,80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        
        t = (cv2.getTickCount()-t0)/cv2.getTickFrequency()
        fps = (1.0 / t);
        cv2.putText(im_show, str('%.2f'%(t) ), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        cv2.putText(im_show, str('%.2f'%(fps)), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 2)
        t0 = cv2.getTickCount()
            
        cv2.imshow('tracking', im_show)
        c = cv2.waitKey(1) & 0xFF
        if c==27 or c==ord('q'):
            break
        ret, frame = video.read()
        org_h,org_w,_ = frame.shape
        #frame = cv2.resize(frame,(  int(0.4*org_w),int(0.4*org_h) ))

    video.release()
    cv2.destroyAllWindows()
     
def play():
    video = cv2.VideoCapture("D:\\temp\\A.mp4")
    ok, frame = video.read()
    while ok:
        ret, frame = video.read()
        cv2.imshow('img2',frame)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
     
if __name__ == '__main__':
    vedio_detect()
    #play()
