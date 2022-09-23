import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np
from matplotlib import rcParams
from datetime import datetime
# rcParams配置文件，用来定义各种变量的，这里用来定义字体
config = {
    "font.family":'serif',
    "font.size": 18,
    "mathtext.fontset":'stix', # 表示可以用latex写公式，stix类似于Time News Romen
    "font.serif": ['SimSun'], # 表示中文用的是宋体
    "figure.constrained_layout.use" : False,
}
rcParams.update(config) # 后更新配置，防止字体设置被覆盖
data_df=pd.read_csv('月度数据.csv',encoding='gbk')
data_df['date'] = [datetime.strptime(d, "%Y-%m") for d in data_df['date']]
# data_df['date'] = pd.to_datetime(data_df.date, format='%Y/%m/%d') 
# data_df['date'] = data_df['date'].dt.strftime('%Y-%m-%d')
fig, ax = plt.subplots(1,1)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

# plt.xticks(rotation=90)


# sns.lineplot(data=data_df, x='date', y='index', hue='keyword',style="keyword")
sns.lineplot(x='date',y='index',hue='keyword',data=data_df)
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
# ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
plt.ylabel('log百度指数')
plt.show()




sns.lineplot(data=flights, x="year", y="passengers", hue="month")
flights.head()
plt.xticks(np.arange(0, 1.1, step=0.1))
sns.lineplot(data=data_df, x='date', y='index', hue='keyword',style="keyword")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.DataFrame({'date': ['1/2/2021',
                            '1/3/2021',
                            '1/4/2021',
                            '1/5/2021',
                            '1/6/2021',
                            '1/7/2021',
                            '1/8/2021'],
                   'value': [4, 7, 8, 13, 17, 15, 21]})

sns.lineplot(x='date', y='value', data=df)
