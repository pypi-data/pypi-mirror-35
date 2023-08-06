import xlrd
import pdb
import jieba

def wr(cont):
    with open("./reg.txt", "a+") as f:
       print(cont)
       f.write(cont)
       f.write("\n")
       #pdb.set_trace()

filename = "./address.xlsx"
data = xlrd.open_workbook(filename)
allNames = data.sheet_names()

for sheetname in allNames:
   sheet = data.sheet_by_name(sheetname)
   for i in range(1,sheet.nrows):
       cellLst = [i.value for i in sheet.row(i)[1:]]
       #cellValueSet = list(set(cellLst))
       cellValueSet = cellLst
       print(cellValueSet)
       cnt = 0
       word = ""
       for v in cellValueSet:
           if v == "":
               cnt+=1
               continue
           regStr = ""
           targetStr = ""
           for char in list(v):
               #for index,char in enumerate(list(v)):
               #print("c,i: ", char, index)
               #regStr+="\\%d/%d "%(int(index)+1,cnt)
               #targetStr+="(%s)/. "%(char)
               word+="%s/%d "%(char,cnt)
           cnt+=1
       wr(word)
       #wr(targetStr)

"""
for sheetname in allNames:
   sheet = data.sheet_by_name(sheetname)
   for i in range(1,sheet.ncols):
       cnt = i-1
       cellLst = [i.value for i in sheet.col(i)[1:]]
       #cellValueSet = list(set(cellLst))
       cellValueSet = list(cellLst)
       print(cellValueSet)
       for v in cellValueSet:
           word = ""
           if v == "":
               continue
           regStr = ""
           targetStr = ""
           for index,char in enumerate(list(v)):
               print("c,i: ", char, index)
               regStr+="\\%d/%d "%(int(index)+1,cnt)
               targetStr+="(%s)/. "%(char)
               word+="%s/%d "%(char,cnt)
       wr(word)
       pdb.set_trace()
       #wr(targetStr)

"""
print("all the reg is genrate ok")

