import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom as xmldom
import numpy as np
import pandas as pd
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

#从文首获取信息三元组
def getWS(item):
    leix=tree.getElementsByTagName(item)
    rdf= []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='案号':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(getValue('WSMC'))
            temp1.append(getValue('AH'))
            rdf.append(temp1)
        if  leix[0].childNodes[i].getAttribute('nameCN')=='审判程序':
            temp1 = []
            temp1.append(getValue('JBFY'))
            temp1.append( leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append( leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
        if  leix[0].childNodes[i].getAttribute('nameCN')=='案件类型':
            temp1 = []
            temp1.append(getValue('JBFY'))
            temp1.append( leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append( leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
    return rdf

#从当事人(DSR)抽取出当事人信息的三元组

def getDSR(item):
    leix=tree.getElementsByTagName(item)
    rdf= []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='公诉方':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(leix[0].childNodes[0].getAttribute('nameCN'))
            temp1.append(getValue('GSJG'))
            rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN')=='起诉方':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='性别':
                    temp2=[]
                    temp2.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp2.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp2.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp2)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='民族':
                    temp3=[]
                    temp3.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp3.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp3.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp3)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp4=[]
                    temp4.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp4)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='出生日期':
                    temp4=[]
                    temp4.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp4.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp4)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人地址':
                    temp5=[]
                    temp5.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp5.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp5.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp5)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='与被害人关系':
                    temp6=[]
                    temp6.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp6.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp6.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    rdf.append(temp6)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp7=[]
                    temp7.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp7.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp7.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp7)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '职务':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '单位名称':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
            rdf.append(rdf)
        if leix[0].childNodes[i].getAttribute('nameCN')=='应诉方':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='诉讼身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人类型':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='出生日期':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='本审诉讼地位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='特殊行业':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='性别':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '职务':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN') == '单位名称':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='民族':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='羁押场所':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='被捕日期':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='文化程度':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='捕前单位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人地址':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='当事人类别':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='学位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='被逮捕日期':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='强制措施':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='强制措施执行时间':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行时间')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='强制措施执行单位':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行单位')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='强制措施原因组':
                            temp1=[]
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                            temp1.append('执行原因')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[0].getAttribute('value'))
                            rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN')=='代理人':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='国籍':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='诉讼身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '自然人身份':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '单位职务分组':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '辩护对象':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '辩护种类':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '代理人辩护人职业类型':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN') == '参与人诉讼地位':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
            rdf.append(rdf)
    return rdf

#从诉讼记录(SSJL)抽取出庭当事人与法院的三元组
def getSSJL(item):
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
                    rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='起诉日期':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='指控信息':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].childNodes[0].childNodes[0].getAttribute('value'))
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='起诉主案由':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='公诉案号':
            temp1=[]
            temp1.append(getValue('GSJG'))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
        elif leix[0].childNodes[i].getAttribute('nameCN')=='出庭当事人信息':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='出庭人姓名':
                    temp1=[]
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
    return rdf

#从案件基本情况（AJJBQK）抽取被害人信息的三元组
def getAJJBQK(item):
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
                    rdf.append(temp1)
                if leix[0].childNodes[i].childNodes[j].getAttribute('value')=='是':
                    temp2 = []
                    temp2.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
                    temp2.append('人体损伤程度')
                    temp2.append('死亡')
                    rdf.append(temp2)
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
                                                    rdf.append(temp1)
                                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN') == '种类':
                                                    temp1=[]
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value'))
                                                    rdf.append(temp1)
                                                if leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN') == '提交人':
                                                    temp1=[]
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[0].getAttribute('value'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('nameCN'))
                                                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].childNodes[t].childNodes[s].childNodes[r].getAttribute('value'))
                                                    rdf.append(temp1)
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')== '证人信息':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        temp1=[]
                        temp1.append(getValue('JBFY'))
                        temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                        temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                        rdf.append(temp1)
    return rdf

#从裁判分析过程(CPFXGC)获取判罚罪名与法律法条的三元组
def getCPFXGC(item):
    leix=tree.getElementsByTagName(item)
    rdf = []
    for i in range(0,len(leix[0].childNodes)):
        if leix[0].childNodes[i].getAttribute('nameCN')=='量刑情节':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='法定量刑情节':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='酌定量刑情节':
                    temp1=[]
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[0].getAttribute('value'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[1].getAttribute('value'))
                    rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN')=='法律法条分组冗余':
            for j in range(0,len(leix[0].childNodes[i].childNodes)):
                if leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='法律法条':
                    temp1=[]
                    temp1.append(getValue('ZKZM'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
    return rdf

#从判决结果(PJJG) 抽取执行判罚、刑期起止日期、附带民事判决结果、可上诉法院等三元组信息
def getPJJG(item):
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
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='刑期起止日期':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='刑期起始日期':
                            temp1=[]
                            temp1.append(getValue('ZXPF'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='刑期截止日期':
                            temp1 = []
                            temp1.append(getValue('ZXPF'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
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
                            rdf.append(temp1)
                        elif leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='被赔偿总金额':
                            temp1 = []
                            temp1.append(leix[0].childNodes[i].childNodes[1].childNodes[0].getAttribute('value'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='赔偿组':
                    for k in range(0,len(leix[0].childNodes[i].childNodes[j].childNodes)):
                        if leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN')=='赔偿人':
                            temp1=[]
                            temp1.append('赔偿协议')
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('nameCN'))
                            temp1.append(leix[0].childNodes[i].childNodes[j].childNodes[k].getAttribute('value'))
                            rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN') == '可上诉至':
            temp1=[]
            temp1.append(getValue("AH"))
            temp1.append(leix[0].childNodes[i].getAttribute('nameCN'))
            temp1.append(leix[0].childNodes[i].getAttribute('value'))
            rdf.append(temp1)
    return rdf

#从文尾(WW)获取审判组织人员与法院的三元组
def getWW(item):
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
                    rdf.append(temp1)
                elif leix[0].childNodes[i].childNodes[j].getAttribute('nameCN')=='结案年月日':
                    temp1 = []
                    temp1.append(getValue('JBFY'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('nameCN'))
                    temp1.append(leix[0].childNodes[i].childNodes[j].getAttribute('value'))
                    rdf.append(temp1)
        if leix[0].childNodes[i].getAttribute('nameCN')=='审判组织成员':
            temp1=[]
            temp1.append(getValue('JBFY'))
            temp1.append(leix[0].childNodes[i].childNodes[1].getAttribute('value'))
            temp1.append(leix[0].childNodes[i].childNodes[0].getAttribute('value'))
            rdf.append(temp1)
    return rdf


if __name__=="__main__":
    tree = xmldom.parse('D:/Anjian/310.xml')
    itemListforone=["JBFY","WSMC","AH","GSJG","GSAH","BDBRQ","KTRQ","ZKZM","","LARQ",
              "CUS_FLFT_RY","ZXPF","KSSZ","SSCYR","XB","MZ","CSRQ","CSD","DSRDZ",
                "QSRQ","CPSJ","CUS_SJYW","title","AJDXYX"]
    itemListformore=["BHR","QSF","YSF","DLR","QZCS","CTDSRXX","JCYFZ","QSZAY","ZRXX","FDLXQJ",
                     "LXQJ","PCZ","BPCZ","XQQZRQ","SPZZCY"]
    print(getWS('WS'))
    print(getDSR('DSR'))
    print(getSSJL('SSJL'))
    print(getAJJBQK('AJJBQK'))
    print(getCPFXGC('CPFXGC'))
    print(getPJJG('PJJG'))
    print(getWW('WW'))




