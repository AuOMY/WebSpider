import pandas
import os

#获取数据
all_data = pandas.read_csv('shunde.csv',encoding = 'utf-8')

#删除
data = all_data.drop([348,349,2859,3787,5447])

#新数据保存
def save_data(data):
    data_frame = pandas.DataFrame(data,columns = ['所在地址','小区名称','总价格','单价','房屋户型','建筑面积','户型结构','建筑类型','所在楼层','套内面积','房屋朝向','建筑结构','装修情况','梯户比例','配备电梯','挂牌时间','交易权属','上次交易','房屋用途','房屋年限','产权所属','抵押信息','房本备件'])
    print(data_frame)
    if not os.path.exists('shunde_new.csv'):
        data_frame.to_csv('shunde_new.csv',encoding = 'utf_8_sig',mode = 'a',index = False,header = ['所在地址','小区名称','总价格','单价','房屋户型','建筑面积','户型结构','建筑类型','所在楼层','套内面积','房屋朝向','建筑结构','装修情况','梯户比例','配备电梯','挂牌时间','交易权属','上次交易','房屋用途','房屋年限','产权所属','抵押信息','房本备件'])
    else:
        data_frame.to_csv('shunde_new.csv',encoding = 'utf_8_sig',mode = 'a',index = False,header = False)

#调用
save_data(data)