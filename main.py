import random
import requests
import csv
from bs4 import BeautifulSoup as bs
from ua_info import ua_list

def get_html():
    url = 'http://www.baidu.com'
    header = {'User-Agent':random.choice(ua_list)}
    response = requests.get(url=url,headers=header)
    print(response.status_code)
    return response

def url_format(i):
    url = 'https://sh.esf.fang.com/house/i3{}/'
    params = str(i)
    url = url.format(params)
    return url

if __name__ == '__main__':
    csvfile=open('record.csv','w',newline='')
    fieldnames=['标题','房屋属性','面积','所在楼层(总楼层)','朝向','建造年份','小区名称','地址','附近交通','总价格','平均价格']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    #response=get_html()
    #soup=bs(response.text,'lxml')
    #print(soup)
    soup=bs(open('新建文本文档.html',encoding='utf8'), 'lxml')
    soup=soup.select('.shop_list')[0].select('dl')

    for i in range(len(soup)):
        if(soup[i].select('div' '.pic')):
            continue
        name=soup[i].select('.tit_shop')[0].text.strip() #标题
        temp = soup[i].select('.tel_shop')[0]
        temp.span.decompose() #其他信息
        spilt_result=temp.text.split('|')
        for j in range(len(spilt_result)):
            spilt_result[j]="".join(spilt_result[j].split())
        temp=soup[i].select('.add_shop')[0]   #地址公寓名
        dName=temp.a.text.strip()          #公寓名
        dAdd=temp.span.text.strip()        #地址
        temp = soup[i].select('span' '.bg_none')   #附近
        if(temp):
            pNear=temp[0].text.strip()
        else:
            pNear=" "
        temp = soup[i].select('.price_right')[0].select('span') #价格
        dTotal=temp[0].text.strip()
        dPer=temp[1].text.strip()
        writer.writerow({'标题':name,'房屋属性':spilt_result[0],'面积':spilt_result[1],'所在楼层(总楼层)':spilt_result[2],'朝向':spilt_result[3],'建造年份':spilt_result[4],'小区名称':dName,'地址':dAdd,'附近交通':pNear,'总价格':dTotal,'平均价格':dPer})
    csvfile.close()