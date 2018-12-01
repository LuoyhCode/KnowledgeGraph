import re
import sys
from functools import reduce




#字符匹配
def regexMatch(words):
    func=(lambda x,y:x if y in x else x+[y])
    #时间
    pattern_time=re.compile(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日(?:[0-9]{1,2}时(?:许)?(?:[0-9]{1,2}分)?)?')
    #法院
    pattern_ins_fayuan=re.compile(r'(?:江西省|浙江省|江苏省|湖北省|河北省|山西省|辽宁省|黑龙江省|安徽省|'
                                  r'福建省|山东省|河南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|北京市|天津市|'
                                  r'上海市|重庆市|内蒙古自治区|广西壮族自治区|西藏自治区|宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区)'
                                  r'(?:[\u4e00-\u9fa5]{2,4}?(?:市|区))?(?:[\u4e00-\u9fa5]{1,3}?(?:区|县))?[\u4e00-\u9fa5]{2,4}?法院')
    #检察院
    pattern_ins_jianchayuan=re.compile(r'公诉机关[\u4e00-\u9fa5]{,15}人民检察院')
    #公安
    pattern_ins_gongan = re.compile(r'(?:由|被|经|到)[\u4e00-\u9fa5]{,8}公安局')
    #交警大队
    # pattern_ins_jiaojing = re.compile(r'(?:江西省|浙江省|江苏省|湖北省|河北省|山西省|辽宁省|黑龙江省|安徽省|'
    #                               r'福建省|山东省|河南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|北京市|天津市|'
    #                               r'上海市|重庆市|内蒙古自治区|广西壮族自治区|西藏自治区|宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区)?'
    #                               r'[\u4e00-\u9fa5]{,4}(?:市|县|区)?[\u4e00-\u9fa5]{,4}(?:公安局交通警察|公安局交通管理|公安局交警|交通警察|公安交通警察支队|交警)(?:[\u4e00-\u9fa5]{2,6})?大队')
    pattern_ins_jiaojing=re.compile(r'(?:经|由|，)[\u4e00-\u9fa5]{,25}大队')
    #律师事务所
    pattern_ins_shiwusuo=re.compile(r'[\u4e00-\u9fa5]{3,9}事务所')
    #伤情鉴定所
    pattern_ins_yanjiusuo=re.compile(r'[\u4e00-\u9fa5]{,15}(?:研究所|鉴定所|鉴定中心)')
    #强制措施类型
    pattern_typeOfCM=re.compile(r'(?:取保候审|行政拘留|刑事拘留|逮捕)')
    #事件
    pattern_event=re.compile(r'(?:交通事故)')
    #事件时间
    pattern_event_time=re.compile(r'[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日[0-9]{1,2}时(?:许)?(?:[0-9]{1,2}分)?')
    #事件地点
    pattern_event_site=re.compile(r'驾驶(?:.){1,30}(?:沿|从|由|在)(?:.){1,50}(?:处|时)')
    #肇事工具
    pattern_event_vehicle=re.compile(r'驾驶[\u4e00-\u9fa5/A-Za-z\d/×/＊/&times；/ ]{4,20}车')
    #人体损伤程度
    pattern_injury=re.compile(r'(?:构成|致人|伤属|而)(?:重伤一级|重伤二级|重伤三级|死亡)')
    #证据

    #罪名
    pattern_crime=re.compile(r'(?:交通肇事罪)')
    #赔偿协议类型
    pattern_protocol=re.compile(r'达成(?:.)+?协议')
    #赔偿方
    #被赔偿方
    #赔偿金额
    pattern_compensation=re.compile(r'(?:赔偿损失|经济损失|赔偿|损失)(?:.){,20}元')
    #被告人属性
    #被害人属性
    #情节
    pattern_plot=re.compile(r'(?:自首|悔罪|坦白)')
    #判罚结果
    pattern_penalty_test=re.compile(r'判决如下(?:.|/n){1,10}')
    pattern_penalty_one=re.compile(r'判决如下(?:.|/n){,50}(?:；|。）|。)')
    pattern_penalty_many=re.compile(r'判决如下(?:.|/n){,3}(?:一、)(?:.|\n){,200}(?:二、)(?:.|\n){,200}(?:三、)(?:.|\n){,50}(?:。)')
    #其他信息
    #人名
    pattern_name=re.compile(r'[\u4e00-\u9fa5]{1}(?:某甲|某乙|某丙|某丁|某某|某)')
    #被告人
    pattern_defendant=re.compile(r'被告人(?:.){1,4}(?:，|。)')
    #辩护人
    pattern_defender=re.compile(r'辩护人[\u4e00-\u9fa5]{2,3}')
    #被害人
    pattern_victim = re.compile(r'(?<=行人|害人)[\u4e00-\u9fa5]{1,2}(?:某甲|某乙|某丙|某丁|某某|某)')
    #原告人
    pattern_plaintiff=re.compile(r'(?<=原告人)[\u4e00-\u9fa5]{1,2}(?:某甲|某乙|某丙|某丁|某某|某)')
    #证人
    pattern_witness = re.compile(r'证人(?:[\u4e00-\u9fa5、]{1,15})?(?:[\u4e00-\u9fa5]{1,5})?(?:.)')
    #检察院
    pattern_inspector=re.compile(r'检察员(?:.|\n){2,10}(?:出)')
    #审判长
    pattern_cheifJudge=re.compile(r'审判长[\u4e00-\u9fa5]{2,3}')
    #陪审员
    pattern_juror=re.compile(r'(?:陪审员|审判员)[\u4e00-\u9fa5]{2,3}')
    #书记员
    pattern_courtClerk=re.compile(r'书记员[\u4e00-\u9fa5]{2,3}')
    #主要责任人
    pattern_first=re.compile(r'[\u4e00-\u9fa5]{1}(?:某某|某)[\u4e00-\u9fa5]{2,15}(?:主要责任|全部责任)')
    #次要责任人
    pattern_second = re.compile(r'[\u4e00-\u9fa5]{1}(?:某某|某)[\u4e00-\u9fa5]{,6}(?:次要责任|无责任)')
    #刑事判决书
    pattern_document_xin=re.compile(r'（[0-9]{4}）[\u4e00-\u9fa5]{1,2}刑[\u4e00-\u9fa5]{1,3}[0-9]{1,6}号')
    #起诉书
    pattern_document_su=re.compile(r'以[\u4e00-\u9fa5]{1,2}?检[\u4e00-\u9fa5]{1,5}（[0-9]{4}）(?:第)?[0-9]{1,6}号')
    #交通事故认定书
    pattern_document_jiao=re.compile(r'[\u4e00-\u9fa5]{1}公交[\u4e00-\u9fa5]{1,5}（[0-9]{4}）(?:第)?[0-9]{1,7}号')
    #文书时间
    pattern_document_time=re.compile(r'(?:.){4}年[\u4e00-\u9fa5]{1,3}月[\u4e00-\u9fa5]{1,3}日')
    #法条
    pattern_statute=re.compile(r'(?:《中华人民共和国刑法》|《中华人民共和国侵权责任法》|《中华人民共和国刑事诉讼法》|《中华人民共和国民法通则》|《中华人民共和国道路交通安全法》'
                               r'|《关于审理人身损害赔偿案件适用法律若干问题的解释》|《关于审理交通肇事刑事案件具体应用法律若干问题的解释》|《最高人民法院关于处理自首和立功具体应用法律若干问题的解释》'
                               r'|《最高人民法院关于审理交通肇事刑事案件具体应用法律若干问题的解释》)?(?:第[\u4e00-\u9fa5]{1,6}条)?(?:第[\u4e00-\u9fa5]{1,6}款)?')
    #机构
    time=reduce(func, [[],] + pattern_time.findall(words))
    institution_fayuan=reduce(func, [[],] + pattern_ins_fayuan.findall(words))
    institution_jianchayuan = reduce(func, [[], ] + pattern_ins_jianchayuan.findall(words))
    institution_gongan=reduce(func, [[],] + pattern_ins_gongan.findall(words))
    institution_jiaojing=reduce(func, [[],] + pattern_ins_jiaojing.findall(words))
    institution_shiwusuo=pattern_ins_shiwusuo.findall(words)
    institution_yanjiusuo=reduce(func, [[],] + pattern_ins_yanjiusuo.findall(words))
    #人名 文书 法条 主/次要责任人
    name=reduce(func, [[],] + pattern_name.findall(words))
    document_xin=pattern_document_xin.findall(words)
    document_su=pattern_document_su.findall(words)
    statute=reduce(func, [[],] + pattern_statute.findall(words))
    document_jiao=pattern_document_jiao.findall(words)
    first=reduce(func, [[],] + pattern_first.findall(words))
    second=reduce(func, [[],] + pattern_second.findall(words))
    document_time=pattern_document_time.findall(words)
    #被告 原告 证人 检察员等角色
    defendant=pattern_defendant.findall(words)
    defender=reduce(func,[[],]+pattern_defender.findall(words))
    victim=reduce(func, [[],] + pattern_victim.findall(words))
    plaintiff=reduce(func, [[],] + pattern_plaintiff.findall(words))
    witness=reduce(func,[[],]+pattern_witness.findall(words))
    inspector=pattern_inspector.findall(words)
    cheifJudge=pattern_cheifJudge.findall(words)
    juror=pattern_juror.findall(words)
    courtClerk=pattern_courtClerk.findall(words)
    #罪名 伤情 措施 赔偿
    typeOfCM=reduce(func,[[],]+pattern_typeOfCM.findall(words))
    injury=reduce(func,[[],]+pattern_injury.findall(words))
    crime=reduce(func,[[],]+pattern_crime.findall(words))
    protocol=reduce(func,[[],]+pattern_protocol.findall(words))
    compensation=reduce(func,[[],]+pattern_compensation.findall(words))
    #事件
    event=reduce(func,[[],]+pattern_event.findall(words))
    event_time=reduce(func,[[],]+pattern_event_time.findall(words))
    event_site=reduce(func,[[],]+pattern_event_site.findall(words))
    event_vehicle=reduce(func,[[],]+pattern_event_vehicle.findall(words))
    # str_event_vehicle=str(event_vehicle[0])
    # event_vehicle[0]=str_event_vehicle[2:]
    #情节 判罚结果
    plot=reduce(func,[[],]+pattern_plot.findall(words))
    penalty_test=pattern_penalty_test.findall(words)
    str_penalty = str(penalty_test)
    if str_penalty[8:10] == "一、":
        penalty=pattern_penalty_many.findall(words)
    else:
        penalty=pattern_penalty_one.findall(words)

    #数据处理
    inspector_rectify(inspector)
    entity_rectify(cheifJudge)
    entity_rectify(juror)
    entity_rectify(courtClerk)
    entity_rectify(victim)
    entity_rectify(defender)
    # entity_rectify(plaintiff)
    # statute=statute[1:]
    # jianchayuan_rectify(institution_jianchayuan)
    # institution_gongan=reduce(func,[[],]+qushou_rectify(institution_gongan))
    # institution_jiaojing=reduce(func,[[],]+qushou_rectify(institution_jiaojing))
    # qushou_rectify(document_su)
    # defendant=reduce(func,[[],]+defendant_rectify(defendant))



    print("*********************基本信息***********************")
    print("时间："+str(time))
    print("法院："+str(institution_fayuan))
    print("刑事判决书：" + str(document_xin))
    print("起讼书："+str(document_su))
    print("交通事故认定书：" + str(document_jiao))
    print("检察院：" + str(institution_jianchayuan))
    print("公安局："+str(institution_gongan))
    print("交警大队："+str(institution_jiaojing))
    print("伤情鉴定研究所："+str(institution_yanjiusuo))
    print("律师事务所："+str(institution_shiwusuo))
    print("强制措施类型："+str(typeOfCM))
    print("人体损伤程度："+str(injury))
    print("事件类型："+str(event))
    print("事件时间："+str(event_time))
    print("肇事者："+str(defendant))
    print("事件地点："+str(event_site))
    print("肇事工具："+str(event_vehicle))
    print("罪名："+str(crime))
    print("人名："+str(name))
    print("被告人："+str(defendant))
    print("辩护人："+str(defender))
    print("受害人："+str(victim))
    print("原告人："+str(plaintiff))
    print("证人："+str(witness))
    print("主要责任："+str(first))
    print("次要责任："+str(second))
    print("赔偿类型："+str(protocol))
    print("赔偿方："+str(defendant))
    print("赔偿金额："+str(compensation))
    print("情节："+str(plot))
    print("判罚结果："+str(penalty))
    print("检察员："+str(inspector))
    print("审判长："+str(cheifJudge))
    print("陪审员："+str(juror))
    print("书记员："+str(courtClerk))
    print("文书时间："+str(document_time))
    print("法条："+str(statute))
    return time

#检察员数据处理：针对一个和多个检察员的处理
def inspector_rectify(item):
    if item:
        if len(str(item[0]))<8:
            str_inspector=str(item[0])
            # str_inspector=str_inspector.rstrip('出')
            # print(item)
            # print(str_inspector[3:-1])
            item[0]=str_inspector[3:-1]
        elif len(item[0])>=8:
            str_inspector_test=str(item[0]).split("、")
            item.pop(0)
            item.append(str_inspector_test[0][3:])
            item.append(str_inspector_test[1][:-1])
            return item
    else:
        return

def entity_rectify(item):
    for i in range(len(item)):
        list=item[i]
        item[i]=list[3:]

def jianchayuan_rectify(item):
    str=item[0]
    item[0]=str[4:]

def qushou_rectify(item):
    for i in range(len(item)):
        str_i = str(item[i])
        item[i] = str_i[1:]
    return item

#被告人纠正 取3到-1
def defendant_rectify(item):
    if item[0]:
        str_1=str(item[0])
        # print("str:"+str2)
        # print(len(item))
        for i in range(0,len(item)):
            item[i]=str_1[3:-1]
    return item

# def penalty_rectify(item):


if __name__=="__main__":
    with open('./Anjian/anjian_64.txt','r+') as lines:
        line=lines.readline()
        print(line)
        regexMatch(line)

