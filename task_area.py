import pandas
import jieba
import wordcloud
from pyecharts import options
from pyecharts.charts import Pie 

#所在地址分析
all_data = pandas.read_csv('shunde_new.csv',encoding = 'utf-8')
data = all_data['所在地址']

#去重
l = []
for i in data:
    if i not in l:
        l.append(i)

#由于最后一行为UTF-8编码所以删除
l.pop() 
print(l)

#data转txt文件
f = open("area.txt","w",encoding = 'utf-8')
f.writelines(data)
f.close()

#分词
with open("area.txt",encoding = "utf-8") as f:
    s = f.read()
ls = jieba.lcut(s) # 生成分词列表
text = ' '.join(ls) # 连接成字符串

#词云图
wc = wordcloud.WordCloud(font_path = "msyh.ttc",width = 1000,height = 700,background_color = 'white',max_words = 100)
wc.generate(text)
wc.to_file("area.png")

#字典计数
dict_cnt = {}  
for item in data:
   if item in dict_cnt: #直接判断key在不在字典中
      dict_cnt[item] += 1
   else:
      dict_cnt[item] = 1

#由于字典计数存在关键字，所以仅抽取数量
c = []
for i in l:
   c.append(dict_cnt[i])

#富文本
rich_text = {
    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
    "b": {"fontSize": 12, "lineHeight": 33},
    "per": {
        "color": "#eee",
        "backgroundColor": "#334455",
        "padding": [2, 4],
        "borderRadius": 2,
    },
}

#饼状图
pie = (Pie(init_opts = options.InitOpts(theme = 'dark',width = '800px',height = '560px'))
            .add('二手房源数', [list(z) for z in zip(l, c)],
            radius = 200, #设置饼图半径
            label_opts = options.LabelOpts(position = 'outsiede',formatter = "{b|{b}: }{c}  {per|{d}%}  ",rich = rich_text))
            .set_global_opts(legend_opts = options.LegendOpts(is_show = False),title_opts = options.TitleOpts(title = "顺德区各街道二手房源数量占比")))

#生成图文件
pie.render()