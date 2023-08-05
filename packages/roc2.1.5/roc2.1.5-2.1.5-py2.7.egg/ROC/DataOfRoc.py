# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from Analyze import Analyze
import os.path


def DataOfRoc(standard_path="truth",test_path="test"):
    db=[]
    pos,db,temp=Analyze(standard_path,test_path)
    
    tp,fp = 0., 0.		
    for i in range(len(db)):
        tp += db[i][0]#wrong
        fp += db[i][1]#right
        
    rate=fp/pos
    print " checking wrong num=%f\n standard true num=%f\n recall rate=%f"%(tp,pos,rate)
    return tp,pos,rate
    

if __name__ == '__main__':
    DataOfRoc()
    