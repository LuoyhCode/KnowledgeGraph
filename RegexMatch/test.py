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
    pattern_ins_jianchayuan=re.compile(r'(?:江西省|浙江省|江苏省|湖北省|河北省|山西省|辽宁省|黑龙江省|安徽省|'
                                  r'福建省|山东省|河南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|北京市|天津市|'
                                  r'上海市|重庆市|内蒙古自治区|广西壮族自治区|西藏自治区|宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区)?'
                                  r'(?:[\u4e00-\u9fa5]{2,4}?(?:市|区))?(?:[\u4e00-\u9fa5]{1,3}?(?:区|县))?人民检察院')
    #公安
    pattern_ins_gongan = re.compile(r'[\u4e00-\u9fa5]{1,6}?(?:市|县|区)(?:公安局|派出所)')
    #交警大队
    pattern_ins_jiaojing = re.compile(r'(?:江西省|浙江省|江苏省|湖北省|河北省|山西省|辽宁省|黑龙江省|安徽省|'
                                  r'福建省|山东省|河南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|北京市|天津市|'
                                  r'上海市|重庆市|内蒙古自治区|广西壮族自治区|西藏自治区|宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区)?'
                                  r'[\u4e00-\u9fa5]{,4}(?:市|县|区)?[\u4e00-\u9fa5]{,4}(?:公安局交通警察|公安局交通管理|公安局交警|交通警察|公安交通警察支队|交警)(?:[\u4e00-\u9fa5]{2,6})?大队')
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
    pattern_event_site=re.compile(r'驾驶[\u4e00-\u9fa5]+?(?:沿|从)[/ \u3000-\u303f\ufb00-\ufffd\u4e00-\u9fa5]{1,50}(?:处|时)')
    #肇事工具
    pattern_event_vehicle=re.compile(r'(?:两轮摩托车|二轮摩托车)')
    #人体损伤程度
    pattern_injury=re.compile(r'(?:构成|致人|伤属)(?:重伤一级|重伤二级|重伤三级|死亡)')
    #证据

    #罪名
    pattern_crime=re.compile(r'(?:构成)(?:交通肇事罪)')
    #赔偿方
    #被赔偿方
    #赔偿金额
    #被告人属性
    #被害人属性
    #情节
    pattern_plot=re.compile(r'(?:自首|悔罪|坦白)')
    #判罚结果
    pattern_penalty=re.compile(r'判决如下[/ \u3000-\u303f\ufb00-\ufffd\u4e00-\u9fa5]{,30}。')
    #其他信息
    #人名
    pattern_name=re.compile(r'[\u4e00-\u9fa5]{1}(?:某甲|某乙|某丙|某丁|某某|某)')
    #被告人
    pattern_defendant=re.compile(r'被告人[\u4e00-\u9fa5]{1,2}(?:某某|某甲|某乙|某丙|某丁|某)(?:[\u4e00-\u9fa5]{0,1}?)?')
    #辩护人
    pattern_defender=re.compile(r'辩护人[\u4e00-\u9fa5]{2,3}')
    #被害人
    pattern_victim = re.compile(r'被害人[\u4e00-\u9fa5]{1,2}(?:某某|某甲|某乙|某丙|某丁|某)(?:[\u4e00-\u9fa5]{0,1}?)?')
    #原告人
    pattern_plaintiff=re.compile(r'原告人[\u4e00-\u9fa5]{1,2}(?:某某|某甲|某乙|某丙|某丁|某)')
    #证人
    pattern_witness = re.compile(r'证人(?:[\u4e00-\u9fa5、]{1,8})?(?:[\u4e00-\u9fa5]{1,5})?(?:某某|某甲|某乙|某丙|某丁|某)')
    #检察院
    pattern_inspector=re.compile(r'检察员[\u4e00-\u9fa5]{2,3}')
    #审判长
    pattern_cheifJudge=re.compile(r'审判长[\u4e00-\u9fa5]{2,3}')
    #陪审员
    pattern_juror=re.compile(r'(?:陪审员|审判员)[\u4e00-\u9fa5]{2,3}')
    #书记员
    pattern_courtClerk=re.compile(r'书记员[\u4e00-\u9fa5]{2,3}')
    #主要责任人
    pattern_first=re.compile(r'[\u4e00-\u9fa5]{1}(?:某某|某)[\u4e00-\u9fa5]{2,6}(?:主要责任|全部责任)')
    #次要责任人
    pattern_second = re.compile(r'[\u4e00-\u9fa5]{1}(?:某某|某)[\u4e00-\u9fa5]{2,6}(?:次要责任)')
    #刑事判决书
    pattern_document_xin=re.compile(r'（[0-9]{4}）[\u4e00-\u9fa5]{1,2}刑[\u4e00-\u9fa5]{1,3}[0-9]{1,6}号')
    #起诉书
    pattern_document_su=re.compile(r'[\u4e00-\u9fa5]{1}?检[\u4e00-\u9fa5]{1,5}（[0-9]{4}）[0-9]{1,3}号')
    #交通事故认定书
    pattern_document_jiao=re.compile(r'[\u4e00-\u9fa5]{1}公[\u4e00-\u9fa5]{1,5}（[0-9]{4}）第[0-9]{1,7}号')
    #法条
    pattern_statute=re.compile(r'(?:《中华人民共和国刑法》|《中华人民共和国侵权责任法》|《中华人民共和国刑事诉讼法》|《中华人民共和国民法通则》|《中华人民共和国道路交通安全法》'
                               r'《关于审理人身损害赔偿案件适用法律若干问题的解释》|《关于审理交通肇事刑事案件具体应用法律若干问题的解释》)?(?:第[\u4e00-\u9fa5]{1,6}条)?(?:第[\u4e00-\u9fa5]{1,6}款)?')
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
    #被告 原告 证人 检察员等角色
    defendant=reduce(func, [[],] + pattern_defendant.findall(words))
    defender=reduce(func,[[],]+pattern_defender.findall(words))
    victim=reduce(func, [[],] + pattern_victim.findall(words))
    plaintiff=reduce(func, [[],] + pattern_plaintiff.findall(words))
    witness=reduce(func,[[],]+pattern_witness.findall(words))
    inspector=pattern_inspector.findall(words)
    cheifJudge=pattern_cheifJudge.findall(words)
    juror=pattern_juror.findall(words)
    courtClerk=pattern_courtClerk.findall(words)
    #罪名 伤情 措施
    typeOfCM=reduce(func,[[],]+pattern_typeOfCM.findall(words))
    injury=reduce(func,[[],]+pattern_injury.findall(words))
    crime=reduce(func,[[],]+pattern_crime.findall(words))
    #事件
    event=reduce(func,[[],]+pattern_event.findall(words))
    event_time=reduce(func,[[],]+pattern_event_time.findall(words))
    event_site=reduce(func,[[],]+pattern_event_site.findall(words))
    event_vehicle=reduce(func,[[],]+pattern_event_vehicle.findall(words))
    #情节 判罚结果
    plot=reduce(func,[[],]+pattern_plot.findall(words))
    penalty=pattern_penalty.findall(words)

    inspector_rectify(inspector)

    print("*********************基本信息***********************")
    print("时间："+str(time))
    print("法院："+str(institution_fayuan))
    print("刑事判决书：" + str(document_xin))
    print("检察院：" + str(institution_jianchayuan))
    print("公安局："+str(institution_gongan))
    print("交警大队："+str(institution_jiaojing))
    print("伤情鉴定研究所："+str(institution_yanjiusuo))
    print("律师事务所："+str(institution_shiwusuo))
    print("强制措施类型："+str(typeOfCM))
    print("人体损伤程度："+str(injury))
    print("事件类型："+str(event))
    print("事件时间："+str(event_time))
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
    print("情节："+str(plot))
    print("判罚结果："+str(penalty))
    print("检察员："+str(inspector))
    print("审判长："+str(cheifJudge))
    print("陪审员："+str(juror))
    print("书记员："+str(courtClerk))
    print("起讼书："+str(document_su))
    print("交通事故认定书："+str(document_jiao))
    print("法条："+str(statute))
    return time

def inspector_rectify(inspector):
    str_i=str(inspector[len(inspector)-1])
    str_i.strip()
    if str_i.endswith("出"):
        inspector[len(inspector)-1]=str_i[0:5]

if __name__=="__main__":
    with open('./Anjian/anjian_35.txt','r+') as lines:
        line=lines.readline()
        print(line)
        regexMatch(line)
