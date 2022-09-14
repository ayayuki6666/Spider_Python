import random
import requests
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
    #response=get_html()
    #soup=bs(response.text,'lxml')
    #print(soup)
    soup=bs(open('新建文本文档.html',encoding='utf8'), 'lxml')
    soup=soup.select('.shop_list')[0].select('dl')
    soup=soup[0]


    name=soup.select('.tit_shop')[0].text.strip() #标题
    print(name)
    temp = soup.select('.tel_shop')[0]
    temp.span.decompose() #其他信息
    spilt_result=temp.text.split('|')
    for i in range(len(spilt_result)):
        spilt_result[i]="".join(spilt_result[i].split())
    print(spilt_result)
    temp=soup.select('.add_shop')[0]   #地址公寓名
    dName=temp.a.text.strip()          #公寓名
    dAdd=temp.span.text.strip()        #地址
    print(dName+" "+dAdd)
    temp = soup.select('span' '.bg_none')   #附近
    if(temp):
        pNear=temp[0].text.strip()
    else:
        pNear=" "
    print(pNear)
    temp = soup.select('.price_right')[0].select('span') #价格
    dTotal=temp[0].text.strip()
    dPer=temp[1].text.strip()
    print(dTotal+" "+dPer)
