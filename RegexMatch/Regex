import re
import string
def regex():
    f = open("d:/anjian/anjian213.txt", "r")  # 设置文件对象
    str1 = f.read()  # 将txt文件的所有内容读入到字符串str中
    f.close()
    for i in range(1,20):
        j = i + 1
        pattern2 = re.compile(r'(?:：{i1}、|： {i1}、|。 {i1}、|。{i1}、|；{i1}、|； {i1}、)(.*?)(?:。 {i2}、|；{i2}、|。{i2}、|； {i2}、)'.format(i1=i, i2=j))
        str2 = re.findall(pattern2, str1)
        #print(i)
        #print(str2)
        if str2:
           print(str2)
        else:
            pattern2 = re.compile(r'{i1}、(.*?)(?:。|；)'.format(i1=i, i2=j))
            str2 = re.findall(pattern2, str1)
            if str2:
                print(str2)
            else:
                pattern2 = re.compile(r'(?:并有|且有)(.*?)等证据')
                str2 = re.findall(pattern2, str1)
                str3 = str(str2)
                str4 = str3.split('、')
                print(str4)
                break
            break


if __name__ == "__main__":
    regex()
