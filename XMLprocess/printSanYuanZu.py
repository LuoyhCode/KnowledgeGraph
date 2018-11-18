import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom
import csv
import re

#对于有孩子节点的处理
def XMLregexformore(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    # print(len(leix))
    if(leix):
        for i in range(0, len(leix)):
            leiname = leix[i]
            if i == 0:
                #print(leiname.getAttribute('nameCN'), leiname.getAttribute('value'))
                return leiname.getAttribute('value')
            print("------------------------------------")
            for j in range(0, len(leix[i].childNodes)):
                second_entity = leix[i].childNodes[j]
                #print(second_entity.getAttribute('nameCN'), second_entity.getAttribute("value"))
                return second_entity.getAttribute("value")
                for k in range(0,len(leix[i].childNodes[j].childNodes)):
                    third_entity = leix[i].childNodes[j].childNodes[k]
                    #print(third_entity.getAttribute('nameCN'), third_entity.getAttribute("value"))
                    return third_entity.getAttribute("value")
        #print(" ")
    else:
        return None

#对于无孩子节点的处理
def XMLregexforone(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    if(leix):
        for i in range(0,len(leix)):
            entity=leix[i]
            #print(entity.getAttribute('nameCN'), entity.getAttribute('value'))
            return (entity.getAttribute('value'))
    else:
        return None



def printSPY():
    root = tree.documentElement  # root为 Element元素
    leix1 = root.getElementsByTagName("SPRYXM")
    leix2 = root.getElementsByTagName("SPRYJS")
    if (leix1):
        for i in range(0, len(leix1)):
            entity1 = leix1[i]
            entity2 = leix2[i]
            print(entity1.getAttribute('value')+ ',' +entity2.getAttribute('value')+ ','+str(XMLregexforone("JBFY")))
    else:
        return None

def printQZCS():
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName("QZCSZL")  # NodeList元素
    if (leix):
        for i in range(0, len(leix)):
            entity = leix[i]
            print(str(XMLregexforone("QZCSZXDW")) + ',强制措施种类,' + str(entity.getAttribute('value')))
            #return (entity.getAttribute('value'))QZCSZXDW
def printFT():
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName("CUS_FLFT_RY")
    if (leix):
        for i in range(0, len(leix)):
            entity1 = leix[i]
            print(entity1.getAttribute('value') + ',法律依据,' + str(XMLregexforone("ZKZM")))
    else:
        return None

def printQZCSZLSJ():
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName("QZCS")  # NodeList元素
    if (leix):
        for i in range(0, len(leix)):
            print(str(leix[i].childNodes[0].getAttribute('value')) + ',强制措施时间,' + str(leix[i].childNodes[1].getAttribute('value')))
def printSanYuanZu():

    #检查员-检察院
    print(str(XMLregexforone("JCY")) + ',' + str(XMLregexforone("JS")) + ',' + str(XMLregexforone("GSJG")))

    #公诉机关-公诉案号
    print(str(XMLregexforone("GSJG")) + ',起诉书,' + str(XMLregexforone("GSAH")))

    # 法院-指控罪名
    print(str(XMLregexforone("ZKZM")) + ',判罚罪名,' + str(XMLregexforone("JBFY")))

    #判决结果-法院
    print(str(XMLregexforone("JBFY")) + ',判罚结果,' + str(XMLregexforone("DZPF")))

    #法院-证据
    print(str(XMLregexforone("JBFY")) + ',证据,' + str(XMLregexforone("ZKZJ")))

    #交通肇事罪-起诉书
    print(str(XMLregexforone("ZKZM")) + ',起诉类型,' + str(XMLregexforone("GSAH")))

    #起诉书-检察院
    print(str(XMLregexforone("GSAH")) + ',起诉方,' + str(XMLregexforone("GSJG")))

    #刑书-检察院
    print(str(XMLregexforone("AH")) + ',公诉机关,' + str(XMLregexforone("GSJG")))

    #被告人-法院
    print(str(XMLregexforone("CTRXM")) + ',' + str(XMLregexforone("SSDW")) + ',' + str(XMLregexforone("JBFY")))

    #被告人-刑书
    print(str(XMLregexforone("CTRXM")) + ',' + str(XMLregexforone("SSDW")) + ',' + str(XMLregexforone("AH")))

    #公安局-强制措施
    printQZCS()

    printFT()
    printSPY()

    #强制措施时间
    printQZCSZLSJ()
    #print(str(XMLregexforone("AH")) + ',公诉机关,' + str(XMLregexforone("GSJG")))

    #结案日期
    print(str(XMLregexforone("AH")) + ',结案日期,' + str(XMLregexforone("CUS_JANYR")))

    #裁判时间
    print(str(XMLregexforone("AH")) + ',裁判时间,' + str(XMLregexforone("CPSJ")))


    #写入到csv
    #with open("D:/anjian/anjian1.csv", "a+") as csvfile:
     #   writer = csv.writer(csvfile)
      #  writer.writerow([str(XMLregexforone("JCY")),str(XMLregexforone("JS")),str(XMLregexforone("GSJG"))])
       # writer.writerow([str(XMLregexforone("GSJG")),"起诉书",str(XMLregexforone("GSAH"))])
        #writer.writerow([str(XMLregexforone("ZKZM")),"判罚罪名",str(XMLregexforone("JBFY"))])
        #writer.writerow([str(XMLregexforone("ZKZM")),"判罚结果",str(XMLregexforone("DZPF"))])
 # 判决结果-法条



if __name__=="__main__":
    tree = xmldom.parse('D:/anjian/17.xml')
    itemListforone=["JBFY","WSMC","AH","GSJG","GSAH","BDBRQ","KTRQ","ZKZM","","LARQ",
              "CUS_FLFT_RY","ZXPF","KSSZ","SSCYR","XB","MZ","CSRQ","CSD","DSRDZ",
                "QSRQ","CPSJ","CUS_SJYW","title","AJDXYX"]
    itemListformore=["BHR","QSF","YSF","DLR","QZCS","CTDSRXX","JCYFZ","QSZAY","ZRXX","FDLXQJ",
                     "LXQJ","PCZ","BPCZ","XQQZRQ","SPZZCY"]

    #for i in range(0,len(itemListforone)):
        #XMLregexforone(itemListforone[i])

    #for i in range(0,len(itemListformore)):
        #XMLregexformore(itemListformore[i])
    #with open("D:/anjian/anjian1.csv", "a+") as csvfile:
     #   writer = csv.writer(csvfile)
    #写入列名
      #  writer.writerow(["实体", "关系", "实体"])

    printSanYuanZu()
