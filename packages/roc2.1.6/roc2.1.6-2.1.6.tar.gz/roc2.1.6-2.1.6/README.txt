####

Operation method ��
      
    Bofore Operation install "ROC,transform,nms"��
    pip install roc2.1.6


    roc:
        input��truth��folder with Annotation results��,test��folder with Model output��,stdscore(standard score to Judge right or wrong ����result(path of txt file to besaved����roc(path of image to besaved��
        python 
                from ROC import roc
                roc.roc("truth","test",stdscore��"result","roc")
        output��roc and score image,txt file
        PS:'result' and 'roc' not have format ��such as��'D:\\python_work\\result')
 

    drawpic:
        input:pre_file(folder with txt files��,image(path of image to besaved��,titlestr(title of image��
        python 
                from ROC import drawpic
                drawpic.drawpic("pre_file","image","titlestr")
        output��roc image 
        PS:'image' not have format ��such as��'D:\\python_work\\image') 


    IOU:
        input��Reframe,GTframe��two lists with information of Rectangle ��[Xmin,Ymin,Xmax,Ymax])
        python 
                from ROC import IOU
                IOU.IOU(Reframe,GTframe)
        output��ratio(Rectangle area overlap rate ��   
   

    DataOfRoc:
        input��truth��folder with Annotation results��,test��folder with Model output��
        python 
                from ROC import DataOfRoc
                DataOfRoc.DataOfRoc("truth","test")
        output��tp(wrong num��,pos��Total correct number ��,rate��recall rate��


    scoreRoc:
        input��listdata(list[1/0,1/0,score]),image(path of image to besaved��,titlestr(title of image��
        python 
                from ROC import scoreRoc
                scoreRoc.scoreRoc(listdata,"image","titlestr")
        output��roc image
        PS:'image' not have format��such as��'D:\\python_work\\image')


    txt2xml:
        input��txt_file(folder with txt format Annotation information��
        python
                from transform import txt2xml
                txt2xml.txt2xml("txt_file","xml_file")
        output��xml_file(folder with xml format Annotation information��  


    xml2txt:
        input��xml_file(folder with xml format Annotation information��
        python
                from transform import xml2txt
                xml2txt.xml2txt("xml_file","txt_file")
        output��txt_file(folder with txt format Annotation information��


    
    nms:
        input��
        python
                from nms import nms
                nms.nms()
        output��




####

                      
                
   
