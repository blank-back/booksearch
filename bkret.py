from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys
import os
import unicodedata as ucd
from retrying import retry
dsturl = "https://www.1qxs.com/all.html"


class book:
    def __init__(self, seq, name):
        self.seq = seq
        self.name = name
        self.exchapt = transbook(seq)[1]
        self.gettpg()
        a=os.getcwd()
        if(not os.path.exists(a+"\\book\\"+str(name))):
            os.mkdir(a+"\\book\\"+str(name))
        self.localdir=a+"\\book\\"+str(name)

    def get_page(self, num,tag):
        if num.isdigit():
            num=int(num)
            if num > self.tpg or num<=0:
                tag=False
                return []
            else:
                if (os.path.exists(self.localdir + "\\"+str(num) + '.txt')):
                    allcon = []
                    data=''
                    with open(self.localdir + "\\"+str(num) + '.txt', "r", encoding='utf-8') as f:  # 打开文本
                        data = f.read()  # 读取文本
                    allcon.append(data)
                else:
                    allcon=[]
                    allcon=getpage(self.exchapt,num)
                    with open(self.localdir + "\\" + str(num) + '.txt', "w", encoding='utf-8') as f:
                        for i in allcon:
                            f.writelines(i)
                return allcon
        else:
            tag=False
            return []

    def gettpg(self):
        pageurl = self.exchapt+'.html'
        pagesoup = BeautifulSoup(get_html(pageurl), "html.parser")
        title = pagesoup.find(attrs={'class': 'catalog panel'})
        content = title.select("ul li a")
        self.tpg=get_num(content[0].get("href"))



def get_num(s):
    a = 0
    n = 0
    begin = False
    end = False
    for i in reversed(s):
        if (i.isdigit() and (not end)):
            begin = True
            i= int(i)* pow(10, n)
            a += i
            n += 1
        else:
            if (begin):
                end = True
    return a


# 给定url,获取对应html，已经解码后
@retry(stop_max_attempt_number=10)
def get_html(url):
    head = {}
    head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    # 模拟浏览器，可以简单避免反爬虫
    req = request.Request(url, headers=head)
    response = request.urlopen(req,timeout =3)
    html = response.read()
    # 获取网页编码方式
    charset = response.info().get_param('charset')
    html = html.decode(charset)
    return html


def get_next_url(html):
    soup = BeautifulSoup(html, 'lxml')
    n = soup.select('.n')
    if len(n) == 1:
        url = n[0].attrs['href']
    elif len(2) == 2:
        url = n[1].attrs['href']
    return "https://www.1qxs.com/all/0_0_0_0_0_" + str(num) + ".html"


def transbook(num):
    listurl = "https://www.1qxs.com/list/" + str(num) + ".html"
    exchapt = "https://www.1qxs.com/xs/" + str(num)
    return [listurl, exchapt]

def getpage(exchapt, chapt):
    pageurl = exchapt + '/' + str(chapt) + '/1.html'
    pagesoup = BeautifulSoup(get_html(pageurl), "html.parser")
    totalpage = int(pagesoup.find('body').get('tpg'))
    allcon=[]
    for i in range(1, totalpage + 1):
        pageurl = exchapt + '/' + str(chapt) + '/' + str(i) + '.html'
        pagesoup = BeautifulSoup(get_html(pageurl), "html.parser")
        title = pagesoup.find(attrs={'class': 'read'})
        content = title.select("div p")
        title = title.select("div[class='title'] h1")
        for h in title:
            allcon.append(ucd.normalize('NFKC', h.text).replace(' ', '')+"\n")
        for seq, h in enumerate(content):
            if seq == 0:
                continue
            if i!=totalpage and seq == len(content) - 1:
                continue
            allcon.append(ucd.normalize('NFKC', h.text).replace(' ', '')+"\n")
    return allcon


def getallbook():
    dict1={}
    listhtml = get_html("https://www.1qxs.com/all.html")
    soup = BeautifulSoup(listhtml, "html.parser")
    taglist = soup.find(attrs={'class': 'page'})
    max1 = 0
    for i in taglist.text.splitlines():
        if i.isdigit():
            max1 = max(max1, int(i))
    a=os.getcwd()
    if (not os.path.exists(a + "\\config\\namenum.txt")):
        with open(a + "\\config\\namenum.txt", "w", encoding="utf-8") as f:
            print("开始获取列表")
            for i in range(max1):
                if(i%100==0):
                    print("收集到{}页".format(i))
                url = "https://www.1qxs.com/all/0_0_0_0_0_" + str(i) + ".html"
                html = get_html(url)
                listsoup = BeautifulSoup(html, "html.parser")
                for i in listsoup.find_all(attrs={'class': 'name line_1'}):
                    f.write(i.text + "=" + str(get_num(i.select('a')[0].get('href'))) + "\n")
            print("收集完毕，共{}本".format(max1))
        print("写入完毕")
    else:
        with open(a + "\\config\\namenum.txt", "r", encoding="utf-8") as f:
            li1 = f.read().splitlines()
        for i in li1:
            tmp = i.split("=")
            if len(tmp) == 2:
                dict1[tmp[0]] = tmp[1]
    return dict1


# 分析处理htmls,得到一个表格，列名：标题、简介、详细url
def anay_htmls(htmls):
    rows = []
    for html in htmls:
        soup = BeautifulSoup(html, 'lxml')
        for i in soup.select('.result'):
            patten = re.compile(r'{"title":"(.*?)","url":"(.*?)"}', re.S)
            if 'c-abstract' in str(i):
                data_tools = patten.findall(i.select('.c-tools')[0].attrs['data-tools'])[0]
                title = data_tools[0]
                detail_url = data_tools[1]
                text = i.select('.c-abstract')[0].text
                row = [title, text, detail_url]
                rows.append(row)
    data = pd.DataFrame(rows, columns=['title', 'text', 'detail_url'])
    return data


def filter_urls(data, wb):
    key_wb = wb.split(" ")
    isbaoliu = []
    for i in data.index:
        flag = True  # 是否保留标志
        title = data.loc[i]['title']
        text = data.loc[i]['text']
        # 多个关键字同时出现
        for key in key_wb:
            # 只要一个关键字不在 title和text中，置否
            if (key not in title) & (key not in text):
                flag = False
                break
        isbaoliu.append(flag)
    data_out = data[isbaoliu]
    return data_out


if __name__ == '__main__':
    getallbook()
    #book1=book(228,"gui")
    #book1.get_page("1")
    #book1.gettpg()
    #getallbook()
    #li1 = transbook(228)
    #getpage(li1[1], 1)
