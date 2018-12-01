import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom
import re

def RegexMatch(item):
    # 事件
    # pattern_event = re.compile(r'(?:交通事故)')
    # 事件时间
    pattern_event_time1 = re.compile(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日(?:凌晨|晚)?(?:[0-9]{1,2}时)?(?:许)?(?:[0-9]{1,2}分)?')
    # pattern_event_time2 = re.compile(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日[0-9](?:凌晨){1,2}时(?:许)?(?:[0-9]{1,2}分)?')
    # 事件地点
    pattern_event_site = re.compile(r'(?:沿|从|由|在|至)(?:.){1,80}?(?:处|时|口|路段)')
    # 肇事工具
    pattern_event_vehicle = re.compile(r'(?<=驾驶|某骑)(?:.){1,40}(?:越野车|牵引车|轿车|挂车|摩托车|货车|面包车|电动车|自行车|客车|自卸车|冷藏车|出租车|汽车)')
    # 人体损伤程度
    pattern_injury = re.compile(r'(?<=构成|致人|伤属|伤而|度为|当场|克而)(?:重伤一级|重伤二级|重伤三级|死亡)')
    #责任方
    pattern_responsibility=re.compile(r'(?:次要责任|无责任)')
    #主要责任人
    pattern_event_beigao=re.compile(r'[\u4e00-\u9fa5]{1}(?:某甲|某乙|某丙|某丁|某某|某)')
    #被害人
    pattern_event_beihai = re.compile(r'(?<=行人|害人)[\u4e00-\u9fa5]{1,2}(?:某甲|某乙|某丙|某丁|某某|某)')
    #event = pattern_event.findall(content)

    event_time=pattern_event_time1.findall(item)
    event_vehicle = pattern_event_vehicle.findall(item)
    event_site = pattern_event_site.findall(item)
    injury = pattern_injury.findall(item)
    beigao=pattern_event_beigao.findall(item)
    beihai=pattern_event_beihai.findall(item)
    # responsibility = pattern_responsibility.findall(item)
    result=[]
    result.append(event_time)
    result.append(event_site)
    result.append(injury)
    result.append(splitEntity(event_vehicle))
    result.append(beigao)
    result.append(beihai)
    return result

def splitEntity(item):
    for i in range(0,len(item)):
        strItem=str(item[i])
        if strItem[0]=='的':
            item[i]=strItem[1:]
    return item

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
            return (entity.getAttribute('value'))
    else:
        return None

#获取标签的value值
def getValue(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    if (leix):
        for i in range(0, len(leix)):
            entity = leix[i]
            return (entity.getAttribute('value'))
    else:
        return None

#获取标签的nameCN值
def getNameCN(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    if (leix):
        for i in range(0, len(leix)):
            entity = leix[i]
            # print(entity.getAttribute('nameCN'), entity.getAttribute('value'))
            return (entity.getAttribute('nameCN'))
    else:
        return None

def getNode(item):
    root = tree.documentElement  # root为 Element元素
    leix = root.getElementsByTagName(item)  # NodeList元素
    return leix

#从文首获取信息三元组
def getWS(item,sourcefile):
 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix=tree.getElementsByTagName(item)
    rdf= []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='案号':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(getValue('WSMC'))
            temp1.append(getValue('AH'))
            writer.writerow([getValue('JBFY'),
                             getValue('WSMC'),
                             getValue('AH')])
            rdf.append(temp1)
        if  leix[0].childNodes[i].getAttribute('nameCN')=='审判程序':
            temp1 = []
            temp1.append(getValue('JBFY'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue('JBFY'),
                             leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
        if  leix[0].childNodes[i].getAttribute('nameCN')=='案件类型':
            temp1 = []
            temp1.append(getValue('JBFY'))
            temp1.append( leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append( leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue('JBFY'),
                             leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
    return rdf

#从当事人(DSR)抽取出当事人信息的三元组
def getDSR(item,sourcefile):
 leix=tree.getElementsByTagName(item)
 rdf = []

 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')

    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='公诉方':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(leix[0].childNodes[0].getAttribute('nameCN'))
            temp1.append(getValue('GSJG'))
            rdf.append(temp1)
            #writer.writerow([getValue('JBFY'), leix[0].childNodes[0].getAttribute('nameCN'), getValue('GSJG')])
        if leix[0].childNodes[i].getAttribute('nameCN')=='起诉方':
            temp=[]
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='性别':
                    temp2=[]
                    temp2.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp2.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp2.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp2)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                    leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                    leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='民族':
                    temp3=[]
                    temp3.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp3.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp3.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp3)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp4=[]
                    temp4.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp4)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '出生日期':
                    temp4 = []
                    temp4.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    rdf.append(temp4)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人地址':
                    temp5=[]
                    temp5.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp5.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp5.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp5)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='与被害人关系':
                    temp6=[]
                    temp6.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp6.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp6.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    temp.append(temp6)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp7=[]
                    temp7.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp7.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp7.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp7)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    for k in range(0, len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '职务':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '单位名称':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
            rdf.append(temp)
        if leix[0].childNodes[i].getAttribute('nameCN')=='应诉方':
            temp = []
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='诉讼身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人类型':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '出生日期':
                    temp1 = []
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    rdf.append(temp1)
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='本审诉讼地位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='特殊行业':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='性别':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    for k in range(0, len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '职务':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '单位名称':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='民族':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='羁押场所':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='被捕日期':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='文化程度':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='捕前单位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人地址':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人类别':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='学位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='被逮捕日期':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '强制措施':
                    for k in range(0, len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '强制措施执行时间':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行时间')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                             '执行时间',
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '强制措施执行单位':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行单位')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                             '执行单位',
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '强制措施原因组':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行原因')
                            temp1.append(
                                leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[0].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                             '执行原因',
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[0].getAttribute('value')])
                            rdf.append(temp1)
            rdf.append(temp)
        if leix[0].childNodes[i].getAttribute('nameCN')=='代理人':
            temp=[]
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='诉讼身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '辩护对象':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '辩护种类':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '代理人辩护人职业类型':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '参与人诉讼地位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    temp.append(temp1)
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
            rdf.append(temp)
    return rdf

#从诉讼记录(SSJL)抽取出庭当事人（CTDSRXX）与法院的三元组
def getSSJL(item,sourcefile):
 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix=tree.getElementsByTagName(item)
    rdf = []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='出庭检察员':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='检察员分组':
                    temp1=[]
                    temp1.append(getValue('GSJG'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    writer.writerow([getValue('GSJG'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value')])
                    rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='起诉日期':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue('GSJG'),
                             leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='指控信息':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('value'))
            writer.writerow([getValue('GSJG'),
                             leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('nameCN'),
                             leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('value')])
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='起诉主案由':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue('GSJG'),leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='公诉案号':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue('GSJG'),leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='出庭当事人信息':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='出庭人姓名':
                    temp1=[]
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([getValue('JBFY'),leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    rdf.append(temp1)
    return rdf

#从案件基本情况（AJJBQK）抽取被害人信息的三元组
def getAJJBQK(item,sourcefile):
 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix = tree.getElementsByTagName(item)
    rdf=[]
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='被害人':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '被害人姓名':
                    temp1=[]
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([getValue('JBFY'),
                                     leix[0].childNodes[i].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    rdf.append(temp1)
                if leix[0].childNodes[i].childNodes[j].getAttribute('value')=='是':
                    temp2 = []
                    temp2.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp2.append('人体损伤程度')
                    temp2.append('死亡')
                    writer.writerow([leix[0].childNodes[i].childNodes[0].getAttribute('value'),
                                     '人体损伤程度',
                                     '死亡'])
                    rdf.append(temp2)
        elif leix[0].childNodes[i].getAttribute('nameCN') == '指控段落':
            content = leix[0].childNodes[i].getAttribute('value')
            print(content)
            result = RegexMatch(content)
            if len(result[0])>0:
                writer.writerow(['交通事故','肇事时间',result[0][0]])
            if len(result[1])>0:
                writer.writerow(['交通事故', '肇事地点', result[1][0]])
            if len(result[3])>0:
                writer.writerow(['交通事故', '肇事工具', result[3][0]])
            if len(result[4])>0:
                writer.writerow(['交通事故', '主要责任', result[4][0]])
            beihai=[]
            beihai.append(getValue('BHRXM'))
            if len(beihai)>1:
                for i in range(0,len(beihai)):
                    writer.writerow(['交通事故', '次要责任', beihai[i]])
            elif len(result[5])>0:
                writer.writerow(['交通事故', '次要责任', result[5][0]])
                writer.writerow([getValue('JBFY'),'被害人',result[5][0]])
            if len(result[2])>0&len(result[5])>0:
                print(result)
                print(result[2][0])
                writer.writerow([result[5][0], '人体损伤程度', result[2][0]])
        elif leix[0].childNodes[i].getAttribute('nameCN')=='本审审理段':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='证据信息':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='证据分组':
                            for t in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes)):
                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].getAttribute('nameCN')=='证据记录':
                                    for s in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes)):
                                        if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].getAttribute('nameCN')=='证据明细':
                                            for r in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes)):
                                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN')=='名称':
                                                    temp1=[]
                                                    temp1.append(getValue('JBFY'))
                                                    temp1.append('证据')
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value'))
                                                    writer.writerow([getValue('JBFY'),
                                                                             '证据',
                                                                            leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value')])
                                                    rdf.append(temp1)
                                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN') == '种类':
                                                    temp1=[]
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value'))
                                                    writer.writerow(
                                                        [leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'),
                                                         leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'),
                                                         leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value')])
                                                    rdf.append(temp1)
                                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN') == '提交人':
                                                    temp1=[]
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value'))
                                                    writer.writerow( [leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'),
                                                                     leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'),
                                                                     leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value')])

                                                    rdf.append(temp1)
                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].getAttribute('nameCN') == '认定事实':
                                    content=leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].getAttribute('value')
                                    result = RegexMatch(content)
                                    if len(result[0]) > 0:
                                        writer.writerow(['交通事故', '肇事时间', result[0][0]])
                                    if len(result[1]) > 0:
                                        writer.writerow(['交通事故', '肇事地点', result[1][0]])
                                    if len(result[3]) > 0:
                                        writer.writerow(['交通事故', '肇事工具', result[3][0]])
                                    if len(result[4]) > 0:
                                        writer.writerow(['交通事故', '主要责任', result[4][0]])
                                        beihai=[]
                                    beihai = []
                                    beihai.append(getValue('BHRXM'))
                                    if len(beihai) > 1:
                                        for i in range(0, len(beihai)):
                                            writer.writerow(['交通事故', '次要责任', beihai[i]])
                                    elif len(result[5]) > 0:
                                        writer.writerow(['交通事故', '次要责任', result[5][0]])
                                        writer.writerow([getValue('JBFY'), '被害人', result[5][0]])
                                    if len(result[2]) > 0 & len(result[5]) > 0:
                                        print(result)
                                        print(result[2][0])
                                        writer.writerow([result[5][0], '人体损伤程度', result[2][0]])
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')== '证人信息':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        temp1=[]
                        temp1.append(getValue('JBFY'))
                        temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                        temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                        writer.writerow([getValue('JBFY'),
                                         leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                         leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                        rdf.append(temp1)
    return rdf

#从裁判分析过程(CPFXGC)获取判罚罪名与法律法条的三元组
def getCPFXGC(item,sourcefile):
  with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix=tree.getElementsByTagName(item)
    rdf = []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='量刑情节':
            temp=[]
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='法定量刑情节':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    writer.writerow([leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value')])
                    temp.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='酌定量刑情节':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    writer.writerow([leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value')])
                    temp.append(temp1)
            rdf.append(temp)
        if leix[0].childNodes[i].getAttribute('nameCN')=='法律法条分组冗余':
            temp=[]
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='法律法条':
                    temp1=[]
                    temp1.append(getValue('ZKZM'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([getValue('ZKZM'),leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    temp.append(temp1)
            rdf.append(temp)
    return rdf

#从判决结果(PJJG) 抽取执行判罚、刑期起止日期、附带民事判决结果、可上诉法院等三元组信息
def getPJJG(item,sourcefile):
 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix = tree.getElementsByTagName(item)
    rdf=[]
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='刑事判决结果分组':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='本审判决结果':
                    temp1=[]
                    temp1.append(getValue('JBFY'))
                    temp1.append(getNameCN('ZXPF'))
                    temp1.append(getValue('ZXPF'))
                    writer.writerow([getValue('JBFY'),
                                     getNameCN('ZXPF'),
                                     getValue('ZXPF')])
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='刑期起止日期':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='刑期起始日期':
                            temp1=[]
                            temp1.append(getValue('ZXPF'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([getValue('ZXPF'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='刑期截止日期':
                            temp1 = []
                            temp1.append(getValue('ZXPF'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([getValue('ZXPF'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                            rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN') == '附带民事判决结果分组':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='被赔偿组':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='被赔偿人':
                            temp1=[]
                            temp1.append('赔偿协议')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow(['赔偿协议',
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='被赔偿总金额':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[1].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow([leix[0].childNodes[i].childNodes[1].childNodes[0].getAttribute('value'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='赔偿组':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='赔偿人':
                            temp1=[]
                            temp1.append('赔偿协议')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            writer.writerow(['赔偿协议',
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'),
                                             leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value')])
                            rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN') == '可上诉至':
            temp1=[]
            temp1.append(getValue("AH"))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            writer.writerow([getValue("AH"),
                             leix[0].childNodes[i].getAttribute('nameCN'),
                             leix[0].childNodes[i].getAttribute('value')])
            rdf.append(temp1)
    return rdf

#从文尾(WW)获取审判组织人员与法院的三元组
def getWW(item,sourcefile):
 with open(sourcefile, "a+", newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    leix=tree.getElementsByTagName(item)
    rdf = []
    #从1开始获取，0为裁判时间，需要特殊处理
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='裁判时间':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='结案年度':
                    temp1= []
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].getAttribute('value'))
                    writer.writerow([getValue('JBFY'),leix[0].childNodes[i].getAttribute('nameCN'),
                                      leix[0].childNodes[i].getAttribute('value')])
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='结案年月日':
                    temp1 = []
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    writer.writerow([ getValue('JBFY'),leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'),
                                     leix[0].childNodes[i].childNodes[j].getAttribute('value')])
                    rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN')=='审判组织成员':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(leix[0].childNodes[i].childNodes[1].getAttribute('value'))
            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
            writer.writerow([getValue('JBFY'),leix[0].childNodes[i].childNodes[1].getAttribute('value'),
                             leix[0].childNodes[i].childNodes[0].getAttribute('value')])
            rdf.append(temp1)
    return rdf

if __name__=="__main__":
    tree = xmldom.parse('D:/Anjian/130.xml')
    sourcefile = "D:/SanYuanZu/130.csv"
    print(getWS('WS',sourcefile))
    print(getDSR('DSR',sourcefile))
    print(getSSJL('SSJL',sourcefile))
    print(getAJJBQK('AJJBQK',sourcefile))
    print(getCPFXGC('CPFXGC',sourcefile))
    print(getPJJG('PJJG',sourcefile))
    print(getWW('WW',sourcefile))

    # itemListforone=["JBFY","WSMC","AH","GSJG","GSAH","BDBRQ","KTRQ","ZKZM","","LARQ",
    #           "CUS_FLFT_RY","ZXPF","KSSZ","SSCYR","XB","MZ","CSRQ","CSD","DSRDZ",
    #             "QSRQ","CPSJ","CUS_SJYW","title","AJDXYX"]
    # itemListformore=["BHR","QSF","YSF","DLR","QZCS","CTDSRXX","JCYFZ","QSZAY","ZRXX","FDLXQJ",
    #                  "LXQJ","PCZ","BPCZ","XQQZRQ","SPZZCY"]