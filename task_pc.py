import requests
from multiprocessing import Pool
from lxml import etree
import pandas as pd
import os

#设置网页爬取
def get_home_url(page):
    url = 'https://fs.ke.com/ershoufang/shunde/pg{}/'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Cookie': 'lianjia_uuid=e6a91b7a-b6a4-40b5-88c6-ff67759cbc8a; crosSdkDT2019DeviceId=-51npj6--xbmlw5-f22i5qg8bh36ouv-yttqkmwdf; _ga=GA1.2.121082359.1579583230; ke_uuid=6de1afa21a5799c0874702af39248907; __xsptplus788=788.1.1579583230.1579583347.4%234%7C%7C%7C%7C%7C%23%23Q6jl-k46IlXjCORdTOp6O3JyzHokoUrb%23; select_city=110000; digv_extends=%7B%22utmTrackId%22%3A%2280418605%22%7D; lianjia_ssid=a4ab1bc0-cb04-492f-960c-342c66065da0; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1583897013,1583932737; User-Realip=111.196.247.121; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216fc67f100b140-06f07f8f707639-33365a06-1049088-16fc67f100c603%22%2C%22%24device_id%22%3A%2216fc67f100b140-06f07f8f707639-33365a06-1049088-16fc67f100c603%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1583933576; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjAxZjBjNWU1ZWE1ZGVmYjQxZDFlYTE4MGVkNWI1OGRjYzk5Mzc2MjEwNTcyMWI3ODhiNTQyNTExOGQ1NTVlZDNkMTY2MWE2YWI5YWRlMGY0NDA3NjkwNWEyMzRlNTdhZWExNDViNGFiNWVmMmMyZWJlZGY1ZjM2Y2M0NWIxMWZlMWFiOWI2MDJiMzFmOTJmYzgxNzNiZTIwMzE1ZGJjNTUyMWE2ZjcxYzZmMTFhOWIyOWU2NzJkZTkyZjc3ZDk1MzhiNjhhMTQyZDQ2YmEyNjJhYzJmNjdjNmFjM2I5YzU0MzdjMDkwYWUwMzZmZjVjYWZkZTY5YjllYzY0NzEwMWY2OTc1NmU1Y2ExNzNhOWRmZTdiNGY4M2E1Zjc2NDZmY2JkMGM2N2JiMjdmZTJjNjI2MzNkMjdlNDY4ODljZGRjMjc3MTQ0NDUxMDllZThlZDVmZmMwMjViNjc2ZjFlY1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkMDI2MDk0N1wifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nLzE5MTExMzE5NTEwMTAwMTcxNzU5Lmh0bWwiLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
    }
    text = requests.get(url,headers = headers).text
    html = etree.HTML(text)
    detail_url = html.xpath('//ul[@class="sellListContent"]//li[@class="clear"]/a/@href') #网页详细地址
    return detail_url

#-获取房源详细数据信息
def get_home_detail_infos(detail_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Cookie': 'lianjia_uuid=e6a91b7a-b6a4-40b5-88c6-ff67759cbc8a; crosSdkDT2019DeviceId=-51npj6--xbmlw5-f22i5qg8bh36ouv-yttqkmwdf; _ga=GA1.2.121082359.1579583230; ke_uuid=6de1afa21a5799c0874702af39248907; __xsptplus788=788.1.1579583230.1579583347.4%234%7C%7C%7C%7C%7C%23%23Q6jl-k46IlXjCORdTOp6O3JyzHokoUrb%23; select_city=110000; digv_extends=%7B%22utmTrackId%22%3A%2280418605%22%7D; lianjia_ssid=a4ab1bc0-cb04-492f-960c-342c66065da0; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1583897013,1583932737; User-Realip=111.196.247.121; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216fc67f100b140-06f07f8f707639-33365a06-1049088-16fc67f100c603%22%2C%22%24device_id%22%3A%2216fc67f100b140-06f07f8f707639-33365a06-1049088-16fc67f100c603%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wybeijing%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1583933576; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjAxZjBjNWU1ZWE1ZGVmYjQxZDFlYTE4MGVkNWI1OGRjYzk5Mzc2MjEwNTcyMWI3ODhiNTQyNTExOGQ1NTVlZDNkMTY2MWE2YWI5YWRlMGY0NDA3NjkwNWEyMzRlNTdhZWExNDViNGFiNWVmMmMyZWJlZGY1ZjM2Y2M0NWIxMWZlMWFiOWI2MDJiMzFmOTJmYzgxNzNiZTIwMzE1ZGJjNTUyMWE2ZjcxYzZmMTFhOWIyOWU2NzJkZTkyZjc3ZDk1MzhiNjhhMTQyZDQ2YmEyNjJhYzJmNjdjNmFjM2I5YzU0MzdjMDkwYWUwMzZmZjVjYWZkZTY5YjllYzY0NzEwMWY2OTc1NmU1Y2ExNzNhOWRmZTdiNGY4M2E1Zjc2NDZmY2JkMGM2N2JiMjdmZTJjNjI2MzNkMjdlNDY4ODljZGRjMjc3MTQ0NDUxMDllZThlZDVmZmMwMjViNjc2ZjFlY1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJkMDI2MDk0N1wifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nLzE5MTExMzE5NTEwMTAwMTcxNzU5Lmh0bWwiLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
    }
    detail_text = requests.get(detail_url,headers = headers).text #文本信息获取
    html = etree.HTML(detail_text)
    all_data = []
    # 所在地址
    szdz = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@data-component="overviewIntro"]//*[@class="overview"]//*[@class="content"]//*[@class="areaName"]//*[@class="info"]/a/text()')[1].replace(" ","").replace("\n","")
    all_data.append(szdz)
    # 小区名称
    xqmc = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@data-component="overviewIntro"]//*[@class="overview"]//*[@class="content"]//*[@class="communityName"]/a/text()')[0]
    all_data.append(xqmc)
    # 总价格
    zjg = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@data-component="overviewIntro"]//*[@class="overview"]//*[@class="content"]//*[@class="price "]/span/text()')[0].replace(" ","").replace("\n","")
    all_data.append(zjg)
    # 单价
    dj = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@data-component="overviewIntro"]//*[@class="overview"]//*[@class="content"]//*[@class="unitPrice"]/span/text()')[0].replace(" ","").replace("\n","")
    all_data.append(dj)
    # 房屋户型
    fwhx = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[1]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(fwhx)
    # 建筑面积
    jzmj = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[2]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(jzmj)
    # 户型结构
    hxjg = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[3]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(hxjg)
    # 建筑类型
    jzlx = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[4]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(jzlx)
    # 所在楼层
    szlc = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[5]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(szlc)
    # 套内面积
    tnmj = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[6]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(tnmj)
    # 房屋朝向
    fwcx = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[7]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(fwcx)
    # 建筑结构
    jzjg = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[8]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(jzjg)
    # 装修情况
    zxqk = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[9]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(zxqk)
    # 梯户比例
    thbl = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[10]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(thbl)
    # 配备电梯
    pbdt = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="content"]/ul/li[10]/text()')[1].replace(" ","").replace("\n","")
    all_data.append(pbdt)
    # 挂牌时间
    gpsj = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[1]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(gpsj)
    # 交易权属
    jyqs = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[2]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(jyqs)
    # 上次交易
    scjy = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[3]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(scjy)
    # 房屋用途
    fwyt = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[4]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(fwyt)
    # 房屋年限
    fwnx = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[5]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(fwnx)
    # 产权所属
    cqss = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[6]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(cqss)
    # 抵押信息
    dyxx = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[7]/span/text()')[1].replace(" ","").replace("\n","")
    all_data.append(dyxx)
    # 房本备件
    fbbj = html.xpath('//*[@id="beike"]//*[@class="sellDetailPage"]//*[@class="m-content"]//*[@class="introContent"]//*[@class="transaction"]//*[@class="content"]/ul/li[8]/text()')[0].replace(" ","").replace("\n","")
    all_data.append(fbbj)
    return all_data

#数据保存至csv文件里（使用pandas中的to_csv保存）
def save_data(data):
    data_frame = pd.DataFrame(data,columns = ['所在地址','小区名称','总价格','单价','房屋户型','建筑面积','户型结构','建筑类型','所在楼层','套内面积','房屋朝向','建筑结构','装修情况','梯户比例','配备电梯','挂牌时间','交易权属','上次交易','房屋用途','房屋年限','产权所属','抵押信息','房本备件'])
    print(data_frame)
    if not os.path.exists('shunde.csv'):
        data_frame.to_csv('shunde.csv',encoding = 'utf_8_sig',mode = 'a',index = False,header = ['所在地址','小区名称','总价格','单价','房屋户型','建筑面积','户型结构','建筑类型','所在楼层','套内面积','房屋朝向','建筑结构','装修情况','梯户比例','配备电梯','挂牌时间','交易权属','上次交易','房屋用途','房屋年限','产权所属','抵押信息','房本备件'])
    else:
        data_frame.to_csv('shunde.csv',encoding = 'utf_8_sig',mode = 'a',index = False,header = False)

#爬虫
def main(page):
    print('开始爬取第{}页的数据！'.format(page))
    urls = get_home_url(page)
    for url in urls:
        print('开始爬取详细网页为{}的房屋详细信息资料！'.format(url))
        all_data = get_home_detail_infos(detail_url = url)
        data = []
        data.append(all_data)
        save_data(data)

#主函数调用进行爬虫
if __name__ == "__main__":
    page = range(0,100)
    print('爬虫开始')
    pool = Pool(processes = 4)
    pool.map(main,page)
    pool.close()
    pool.join()