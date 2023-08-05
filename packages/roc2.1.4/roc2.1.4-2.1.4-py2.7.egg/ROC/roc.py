# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from Analyze import Analyze
import os.path
import random
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def roc(standard_path="truth",test_path="test",stdscore=0.32,result_roc='result_roc',image='image'):
    db=[]
    dd=[]
    conpos=0
    pos,db,temp=Analyze(standard_path,test_path)                     #get data from IOU

    if temp==0:
        print"there are not tag \"score\" in xml files" 
        return

    db = sorted(db, key=lambda x:x[2], reverse=True)#sorted()   
    
  
    for i in range(0,len(db)):                                       #select wrong and right 
        dbscore=db[i][2]
        #print dbscore
        if dbscore>=stdscore and db[i][0]==0 and db[i][1]==1:
            dd.append([0,1,dbscore])
            conpos+=1
        elif dbscore<stdscore and db[i][0]==1 and db[i][1]==0:
            dd.append([0,1,dbscore])
            conpos+=1
        elif dbscore<stdscore and db[i][0]==0 and db[i][1]==1:
            dd.append([1,0,dbscore])
        elif dbscore<stdscore and db[i][0]==0 and db[i][1]==1:
            dd.append([1,0,dbscore])
        else:
            '.'                                                 
    for i in range(len(dd)):                                        #random to draw picture
        a=random.random()
        dd[i][2]=round(a, 5)
    dd = sorted(dd, key=lambda x:x[2], reverse=True)#sorted()    
        
    xy_arr = []
    score =[]
    tp,fp = 0., 0.		
    for i in range(len(dd)):
        tp += dd[i][0]#wrong
        fp += dd[i][1]#right
        xy_arr.append([tp,fp/conpos])
        score.append(dd[i][2])
    #print score
    auc = 0.			
    prev_x = 0
    for x,y in xy_arr:
	    if x != prev_x:
		    auc += (x - prev_x) * y
		    prev_x = x     
         
    x = [_a[0] for _a in xy_arr]
    y = [_a[1] for _a in xy_arr]
    z = [_a for _a in score]
    
    #print z
    result_roc+='.txt'                                                 #parameter of picture
    image+='.png'
    plt.title("ROC (AUC = %.4f)" % (auc))
    plt.xlabel("False Count")
    plt.ylabel("True Positive Rate")
    plt.plot(x, y,color='blue',label='rate')
    plt.plot(x, z,color='black',label='score')
    xmajorLocator   = MultipleLocator(tp/8)
    xminorLocator   = MultipleLocator(tp/16) 
    ymajorLocator   = MultipleLocator(0.2)
    yminorLocator   = MultipleLocator(0.05) 
    
    ax = plt.subplot()
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(True, which='minor')
    plt.legend(bbox_to_anchor=(0., 1.08, 1., .102), loc=2,ncol=2, mode='expand', borderaxespad=0.)
    plt.grid() 
    plt.grid(color='y' , linestyle='--')
    
    plt.savefig(image)
    plt.show()
    
    with open(result_roc, 'w') as fp:                                  #save datas
        for i in range(len(dd)):
            fp.write("%d %f %f \n" % (x[i], y[i],z[i]))
    
if __name__ == '__main__':
    roc()