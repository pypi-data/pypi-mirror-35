####

Operation method £º
      
    Bofore Operation install "ROC,transform,nms"£º
    pip install roc2.1.6


    roc:
        input£ºtruth£¨folder with Annotation results£©,test£¨folder with Model output£©,stdscore(standard score to Judge right or wrong £©£¬result(path of txt file to besaved£©£¬roc(path of image to besaved£©
        python 
                from ROC import roc
                roc.roc("truth","test",stdscore£¬"result","roc")
        output£ºroc and score image,txt file
        PS:'result' and 'roc' not have format £¨such as£º'D:\\python_work\\result')
 

    drawpic:
        input:pre_file(folder with txt files£©,image(path of image to besaved£©,titlestr(title of image£©
        python 
                from ROC import drawpic
                drawpic.drawpic("pre_file","image","titlestr")
        output£ºroc image 
        PS:'image' not have format £¨such as£º'D:\\python_work\\image') 


    IOU:
        input£ºReframe,GTframe£¨two lists with information of Rectangle £¬[Xmin,Ymin,Xmax,Ymax])
        python 
                from ROC import IOU
                IOU.IOU(Reframe,GTframe)
        output£ºratio(Rectangle area overlap rate £©   
   

    DataOfRoc:
        input£ºtruth£¨folder with Annotation results£©,test£¨folder with Model output£©
        python 
                from ROC import DataOfRoc
                DataOfRoc.DataOfRoc("truth","test")
        output£ºtp(wrong num£©,pos£¨Total correct number £©,rate£¨recall rate£©


    scoreRoc:
        input£ºlistdata(list[1/0,1/0,score]),image(path of image to besaved£©,titlestr(title of image£©
        python 
                from ROC import scoreRoc
                scoreRoc.scoreRoc(listdata,"image","titlestr")
        output£ºroc image
        PS:'image' not have format£¨such as£º'D:\\python_work\\image')


    txt2xml:
        input£ºtxt_file(folder with txt format Annotation information£©
        python
                from transform import txt2xml
                txt2xml.txt2xml("txt_file","xml_file")
        output£ºxml_file(folder with xml format Annotation information£©  


    xml2txt:
        input£ºxml_file(folder with xml format Annotation information£©
        python
                from transform import xml2txt
                xml2txt.xml2txt("xml_file","txt_file")
        output£ºtxt_file(folder with txt format Annotation information£©


    
    nms:
        input£º
        python
                from nms import nms
                nms.nms()
        output£º




####

                      
                
   
