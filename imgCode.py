from ddddocr import DdddOcr

class imgCode:

    #code


   def getCode(file):
       orc = DdddOcr()
       imgfile=open(file,'rb')
       img=imgfile.read()
       code =orc.classification(img)
       return code



'''
ocr=DdddOcr()
file=open('111.png','rb')
img=file.read()
imgCode=ocr.classification(img)
print(imgCode)
'''
cc=imgCode.getCode("111.png")
print(cc)