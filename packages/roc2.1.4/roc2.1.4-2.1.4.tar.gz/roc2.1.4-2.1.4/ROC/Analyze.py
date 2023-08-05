# -*- coding: utf-8 -*-
import xml.dom.minidom 
import os.path
from read import read
from IOU import IOU
import os

def Analyze(standard_path,test_path):
    '''
    return:pos_num,ratio_info
    ratio_info:wrong,right,ratio/sore
    
    '''
    wrong,right,num_pos=0,0,0
    ratio=0.
    ratio_info=[]#返回值
    frame_stand=frame_test=[]#read result
    
    folder_stand=standard_path#文件夹路径
    folder_test=test_path
    
    files_stand = os.listdir(folder_stand)#文件列表  标x.s 标x.d 
    files_test = os.listdir(folder_test)           #测x.s 测x.d
    files_all=files_test                           #所有文件并集
    files_temp=[]                                  #只有标准文件的名字列表
    
    temp_y=0
    
    
    for File in files_stand:# all xmlfile
        path_test=os.path.join(folder_test,File)
        path_stand=path_test.replace(folder_test,folder_stand)
        if not os.path.isfile(path_test):
            files_all.append(File)# 测x.s 测x.d 标x.s
            files_temp.append(File)#标x.s
            
    for File in files_all:            
        if File in files_temp:#标x.s      每一个框都是一个实际正确 漏读
            path_stand=os.path.join(folder_stand,File)
            dom_stand=xml.dom.minidom.parse(path_stand)
            root_stand=dom_stand.documentElement
            frame_stand=read(root_stand)
            boxnum_stand=len(frame_stand)
            num_pos+=boxnum_stand
            num_info=len(frame_test[0])
            wrong=0
            right=0
            ratio=0.
            for i in range(0,boxnum_stand):
                if num_info==5:
                    temp_y=1
                    ratio_info.append([wrong,right,frame_test[i][4]])                       
                else:
                    ratio_info.append([wrong,right,ratio])
               
            
        else:                 #测x.s 测x.d
            path_test=os.path.join(folder_test,File)
            path_stand=path_test.replace(folder_test,folder_stand)
            
            if not os.path.isfile(path_stand): #测x.s         每一个框都是一个实际错误 误读(ratio=0)
                dom_test=xml.dom.minidom.parse(path_test)
                root_test=dom_test.documentElement
                frame_test=read(root_test)
                boxnum_test=len(frame_test)
                num_info=len(frame_test[0])
                wrong=1
                right=0
                ratio=0.
                for i in range(0,boxnum_test):
                    if num_info==5:
                         ratio_info.append([wrong,right,frame_test[i][4]])                        
                    else:
                         ratio_info.append([wrong,right,ratio])                       
                
            else:   #测x.d

                dom_test=xml.dom.minidom.parse(path_test) #测x.d
                root_test=dom_test.documentElement
                frame_test=read(root_test)
                boxnum_test=len(frame_test)
                
                num_info=len(frame_test[0])
                
                dom_stand=xml.dom.minidom.parse(path_stand)#标x.d
                root_stand=dom_stand.documentElement
                frame_stand=read(root_stand)
                boxnum_stand=len(frame_stand)
                
                num_pos+=boxnum_stand#标的框都是实际正确的
                for i in range(0,boxnum_test):
                    boxnum_stand=len(frame_stand)
                    wrong=right=0
                    if  boxnum_stand==0:
                        wrong=1
                        ratio=0.
                        if num_info==5:
                            ratio_info.append([wrong,right,frame_test[i][4]])            
                        else:
                            ratio_info.append([wrong,right,ratio])
                    else:
                        for j in range(0,boxnum_stand):
                            ratio=IOU(frame_test[i],frame_stand[j])  
                            if ratio>=0.5:
                                right=1
                                if num_info==5:
                                    ratio_info.append([wrong,right,frame_test[i][4]])            
                                else:
                                    ratio_info.append([wrong,right,ratio])
                                del frame_stand[j]
                                break
                            
                    if right==0 :
                        wrong=1
                        if num_info==5:
                            ratio_info.append([wrong,right,frame_test[i][4]])                   
                        else:
                            ratio_info.append([wrong,right,ratio])
                   

    #print num_pos
    #print len(ratio_info)
    
    return num_pos,ratio_info,temp_y
                            
                                
                                
                               
if __name__ == '__main__':
    Analyze('D:\\python_work\\bndbox_test\\roc-2.1.1\\ROC\\truth','D:\\python_work\\bndbox_test\\roc-2.1.1\\ROC\\test')                           

          
                        
                
                
                
            
        
        