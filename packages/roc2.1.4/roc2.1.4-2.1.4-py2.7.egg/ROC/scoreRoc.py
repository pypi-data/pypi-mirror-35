# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from flv2jpg import avi2jpg

cnames = ('aquamarine','black','blue',
          'blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue',
          'crimson','cyan','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta',
          'darkolivegreen','darkorange','darkorchid','darkred','darkseagreen','darkslateblue','darkslategray',
          'darkturquoise','darkviolet','deeppink','deepskyblue','dimgray','firebrick','forestgreen',
          'fuchsia','gold','goldenrod','gray','green','hotpink','indianred',
          'indigo','lawngreen','lime','limegreen',
          'magenta','maroon','navy','olive','olivedrab',
          'orange','orchid','palevioletred','peru',
          'plum','purple','red','sienna','skyblue','slateblue','slategray','springgreen','steelblue',
          'tan','teal','thistle','turquoise','violet','yellow')

listdata=avi2jpg()
def roc(listdata=[],labela='data',image='image'):

    ab=listdata 
    #ab=drawpic()
    ab = sorted(ab, key=lambda x:x[2], reverse=True)#sorted() 
    mux=0
  
    for i in range(len(ab)):
        x = [_a[0] for _a in ab[i]]
        y = [_a[1] for _a in ab[i]]
        z = [_a[2] for _a in ab[i]]       
        plt.xlabel("False Count")
        plt.ylabel("True Positive Rate")
        plt.title("ROC")
        plt.plot(x, y,color=cnames[i%69],label=labela)
        plt.plot(x, z,color=cnames[i%69])
        for i in range(len(x)):
            if x[i]>mux:
                mux=x[i]
    image+='.jpg'
    
    
        
    xmajorLocator   = MultipleLocator(mux/8) 
    xminorLocator   = MultipleLocator(mux/16) 
    ymajorLocator   = MultipleLocator(0.2) 
    yminorLocator   = MultipleLocator(0.05) 
    
    ax = plt.subplot() 
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)

    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.xaxis.grid(True, which='major') 
    ax.yaxis.grid(True, which='minor') 
    
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2,ncol=3, mode='expand', borderaxespad=0.)
    plt.grid() 
    plt.grid(color='y' , linestyle='--')
    
    plt.savefig(image)
    plt.show() 
    print "Run successfully"
    
    
if __name__ == '__main__':
    roc()

