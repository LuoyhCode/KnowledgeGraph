import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom
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
                print(leiname.getAttribute('nameCN'), leiname.getAttribute('value'))
            print("------------------------------------")
            for j in range(0, len(leix[i].childNodes)):
                second_entity = leix[i].childNodes[j]
                print(second_entity.getAttribute('nameCN'), second_entity.getAttribute("value"))

                for k in range(0,len(leix[i].childNodes[j].childNodes)):
                    third_entity = leix[i].childNodes[j].childNodes[k]
                    print(third_entity.getAttribute('nameCN'), third_entity.getAttribute("value"))

        print(" ")
    else:
        return None

#对于无孩子节点的处理
def XMLregexforone(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    if(leix):
        for i in range(0,len(leix)):
            entity=leix[i]
            print(entity.getAttribute('nameCN'), entity.getAttribute('value'))
    else:
        return None


if __name__=="__main__":
    tree = xmldom.parse('D:/Anjian/310.xml')
    itemListforone=["JBFY","WSMC","AH","GSJG","GSAH","BDBRQ","KTRQ","ZKZM","","LARQ",
              "CUS_FLFT_RY","ZXPF","KSSZ","SSCYR","XB","MZ","CSRQ","CSD","DSRDZ",
                "QSRQ","CPSJ","CUS_SJYW","title","AJDXYX"]
    itemListformore=["BHR","QSF","YSF","DLR","QZCS","CTDSRXX","JCYFZ","QSZAY","ZRXX","FDLXQJ",
                     "LXQJ","PCZ","BPCZ","XQQZRQ","SPZZCY"]

    for i in range(0,len(itemListforone)):
        XMLregexforone(itemListforone[i])

    for i in range(0,len(itemListformore)):
        XMLregexformore(itemListformore[i])







    #ET处理xm文件
    # print(root.tag)
    # print(root.attrib)
    # pattern_JBFY = re.compile(r'(?<=JBFY)(?:.){,20}')
    # print(JBFY=pattern_JBFY.findall(tree))
    # for child in root:
    #     print(child.tag, child.attrib)
    #     for grand in child:
    #         print(grand.tag, grand.attrib)
    #         for grand_2 in grand:
    #             print(grand_2.tag, grand_2.attrib)
    #             for grand_3 in grand_2:
    #                 print(grand_3.tag, grand_3.attrib)
    #                 for grand_4 in grand_3:
    #                     print(grand_4.tag, grand_4.attrib)
    #                     for grand_5 in grand_4:
    #                         print(grand_5.tag,grand_5.attrib)

    # print(root[0][0][2].tag, root[0][0][2].attrib)
    # QW=root.childNodes
    # print(QW[0].attributes)
