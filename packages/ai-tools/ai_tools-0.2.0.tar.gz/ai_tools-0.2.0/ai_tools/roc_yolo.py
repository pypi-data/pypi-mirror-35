# -*- coding: utf-8 -*-
import pylab as pl
from Analyze_txt import Analyze_txt
import sys
from ai_tools import draw
from ai_tools import save2server
def txt2xml(xmlfilename,txtfilename):
    with open(xmlfilename,'r') as fs:
            managerList=[]
            doc = xml.dom.minidom.Document()
            root = doc.createElement('Recognition')
            root.setAttribute('type', 'face')
            doc.appendChild(root)

            str=fs.read()
            line=str.split()
            print line
            for i in range(0,int(line[1])):
                managerList.append([{'xmin':line[2+i*4],'ymin':line[3+i*4],'xmax':line[4+i*4],'ymax':line[5+i*4]}])

            for i in managerList :
                for j in range(len(i)):
                    nodeManager = doc.createElement('bndbox')
                    nodeXmin = doc.createElement("xmin")
                    nodeXmin.appendChild(doc.createTextNode(i[j]['xmin']))
                    nodeYmin = doc.createElement("ymin")
                    nodeYmin.appendChild(doc.createTextNode(i[j]['ymin']))
                    nodeXmax = doc.createElement("xmax")
                    nodeXmax.appendChild(doc.createTextNode(i[j]['xmax']))
                    nodeYmax = doc.createElement("ymax")
                    nodeYmax.appendChild(doc.createTextNode(i[j]['ymax']))


                    nodeManager.appendChild(nodeXmin)
                    nodeManager.appendChild(nodeYmin)
                    nodeManager.appendChild(nodeXmax)
                    nodeManager.appendChild(nodeYmax)
                    root.appendChild(nodeManager)

            print line[0]
            #pathn=os.path.join(after_file,line[0])
            #pathn=os.path.join(pathn,".xml")
            #pathn+=".xml"
            #fp = open(pathn, 'w')
            fp = open(txtfilename, 'w')
            doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

def roc(standard_path="truth",test_path="test",result_roc='roc.txt',result_jpg='roc.jpg'):

    db=[]
    print "analyze_xml:"
    db,pos=Analyze_txt(standard_path,test_path)
    db = sorted(db, key=lambda x:x[2], reverse=True)#sorted() 
    
    print pos 
    xy_arr = []
    tp,fp = 0., 0.			
    for i in range(len(db)):
        #print db
        fp += db[i][1]#wrong
        tp += db[i][0]#creat
        xy_arr.append([fp,tp/pos,db[i][2]])
   

    auc = 0.			
    prev_x = 0
    for x,y,t in xy_arr:
	    if x != prev_x:
		    auc += (x - prev_x) * y
		    prev_x = x
            
    print xy_arr[-1]        
    x = [_a[0] for _a in xy_arr]
    y = [_a[1] for _a in xy_arr]
    y1 = [_a[2] for _a in xy_arr]
    #pl.title("ROC (AUC = %.4f)" % (auc/float(x[-1])))
    #pl.xlabel("False Count")
    #pl.ylabel("True Positive Rate")
    #pl.plot(x, y)
    #pl.show()
    xl=[x,x]
    yl=[y,y1]
    img=draw.draw_curve_new(xl,yl,width=512,height=512,title='ROC (AUC=%.4F)'%(auc/float(x[-1])),xlabel='FalseAlarm Count',ylabel='True Positive Rate') 
    save2server.save2server(result_jpg,img)
    with open(result_roc, 'w') as fp:
        for i in range(len(xy_arr)):
            fp.write("%f %f %f \n" % (xy_arr[i][0], xy_arr[i][1],xy_arr[i][2]))
def sort_matrix(db,pos):
    db = sorted(db, key=lambda x:x[2], reverse=True)#sorted() 
    
    print pos 
    xy_arr = []
    tp,fp = 0., 0.			
    for i in range(len(db)):
        #print db
        fp += db[i][1]#wrong
        tp += db[i][0]#creat
        xy_arr.append([fp,tp/pos,db[i][2]])
   

    auc = 0.			
    prev_x = 0
    for x,y,t in xy_arr:
	    if x != prev_x:
		    auc += (x - prev_x) * y
		    prev_x = x
            
    print xy_arr[-1]        
    x = [_a[0] for _a in xy_arr]
    y = [_a[1] for _a in xy_arr]
    y1 = [_a[2] for _a in xy_arr]
    #pl.title("ROC (AUC = %.4f)" % (auc/float(x[-1])))
    #pl.xlabel("False Count")
    #pl.ylabel("True Positive Rate")
    #pl.plot(x, y)
    #pl.show()
    xl=[x,x]
    yl=[y,y1]
    return xl,yl 
def roc_title(gt_dir,pre_dir,title_add='merge',save_path='./',max_fa=3500):
    roc_m,pos_number=roc_matrix(gt_dir,pre_dir)
    xl,yl=sort_matrix(roc_m,pos_number)
    func=lambda x: return x[:max_fa]
    xl[0]=func(xl[0])  
    xl[1]=func(xl[1])  
    yl[0]=func(yl[0])  
    yl[1]=func(yl[1])  
    img=draw.draw_curve_new(xl,yl,width=512,height=512,title='ROC (AUC=%.4F)'%(auc/float(x[-1])),xlabel='FalseAlarm Count',ylabel='True Positive Rate') 
    result_jpg=os.path.join(save_path,'roc.jpg')
    result_txt=os.path.join(save_path,'roc_matrix.txt')
    save2server.save2server(result_jpg,img)
    with open(result_txt, 'w') as fp:
        for i in range(len(xl[0])):
            fp.write("%f %f %f \n" % (xl[0][i],yl[0][i],yl[1][i]))
    
    
if __name__ == '__main__':
    gt_dir=sys.argv[1]
    resultdir=sys.argv[2]
    print gt_dir
    print resultdir
    roc(gt_dir,resultdir,'result_roc.txt',"roc.jpg")
