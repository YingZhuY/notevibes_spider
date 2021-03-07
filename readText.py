
import os   #os模块中包含很多操作文件和目录的函数
import sys

#获取当前文件夹中的文件名称列表   
filepath='D:\\dream\\ToSpeech\\text\\'     #输入文件存放路径
filenames = os.listdir(filepath)

i=1

for filename in filenames:      #遍历文件夹
    #遍历单个文件
    temppath=filepath+filename
    tempf=open(temppath,'r',encoding='utf-8')
    s=tempf.read()
    if(len(s)>10000):
        s=s[0:10000]
    print(s)                    #处理放在这
    print("已经下载文件语音 "+str(i))
    if(i>9):
        break
    i+=1

