#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 只需要在顶部声明 CurrentConfig.ONLINE_HOST 即可 
from pyecharts.globals import CurrentConfig, OnlineHostType 
# OnlineHostType.NOTEBOOK_HOST 默认值为 http://localhost:8888/nbextensions/assets/ 
CurrentConfig.ONLINE_HOST = OnlineHostType.NOTEBOOK_HOST

import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts


# # 导入并查看数据

# In[2]:


data_user = pd.read_csv('C:/Users/luoyiming/Downloads/tianchi_mobile_recommend_train_user.csv')
data_user.head()


# In[3]:


data_user.info()


# 各字段含义：
# 
# user_id	用户标识
# 
# item_id	商品标识
# 
# behavior_type	用户对商品的行为类型,包括浏览、收藏、加购物车、购买，对应取值分别是1、2、3、4
# 
# user_geohash	用户位置的空间标识，可以为空	
# 
# item_category	商品分类标识	
# 
# time	行为时间,精确到小时

# In[4]:


data_user.isnull().sum()


# 观察到用户位置这一列存在大量的缺失值，故在后续数据处理中删除该列。

# # 数据处理

# In[5]:


del data_user['user_geohash']
data_user.reset_index(drop=True,inplace=True)
data_user['date'] = data_user['time'].apply(lambda x:x.split(' ')[0])
data_user['hour'] = data_user['time'].apply(lambda x:x.split(' ')[1])
data_user['time'] = pd.to_datetime(data_user['time'])
data_user['date'] = pd.to_datetime(data_user['date'])
data_user['hour'] = data_user['hour'].astype('int64')
data_user.info()


# In[6]:


data_user.head()


# # 整体情况概览

# In[7]:


print('总浏览量：%d' %len(data_user))
print('总浏览人数：%d' %data_user['user_id'].nunique())
print('总订单数：%d' %data_user[data_user['behavior_type']==4].behavior_type.count())
user_type = data_user.groupby(['user_id']).behavior_type.value_counts().unstack()
pv_nu = user_type[user_type[1] == user_type.sum(axis=1)]
print('跳出率：%.2f%%' %(len(pv_nu)/data_user['user_id'].nunique()*100))
date_rebuy = data_user[data_user.behavior_type==4].groupby('user_id')['date'].apply(lambda x:len(x.unique())).rename('rebuy_count')
print('复购率：%.2f%%' %(date_rebuy[date_rebuy>=2].count()/date_rebuy.count()*100))


# 平均每用户的浏览量为1225次，订单数为12单，跳出率极低，复购率极高，说明用户的忠诚度较高，且在浏览商品时有很强的针对性。

# # PV,UV分析

# In[8]:


pv_daily=data_user.groupby('date')['user_id'].count().rename('pv').reset_index()
uv_daily=data_user.groupby('date')['user_id'].nunique().rename('uv').reset_index()


# In[9]:


pv_line=(
    Line(init_opts=opts.InitOpts(width="1000px",height="500px"))
    .add_xaxis(xaxis_data=list(pv_daily.date.astype('str').tolist()))
    .add_yaxis(
        "PV",
        np.around(pv_daily.pv/10000,decimals=2),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name="UV",
        yaxis_index=1,
        y_axis=np.around(uv_daily.uv/1,decimals=2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="UV",
            type_="value",
            min_=6000,
            max_=10000,
            interval=1000,
            axislabel_opts=opts.LabelOpts(formatter="{value} 人"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,trigger="axis",axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True,type_="line"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="PV",
            type_="value",
            min_=10,
            max_=80,
            interval=15,
            axislabel_opts=opts.LabelOpts(formatter="{value} 万次"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="PV,UV情况（按天）",pos_left='left'),
        legend_opts=opts.LegendOpts(is_show=True,pos_top='95%')
    )
)
pv_line.render_notebook()


# In[10]:


pv_hour=data_user.groupby('hour')['user_id'].count().rename('pv').reset_index()
uv_hour=data_user.drop_duplicates(['date','hour','user_id']).groupby('hour')['user_id'].count().rename('uv').reset_index()


# In[11]:


line=(
    Line(init_opts=opts.InitOpts(width="1000px",height="500px"))
    .add_xaxis(xaxis_data=list(pv_hour.hour.tolist()))
    .add_yaxis(
        "PV",
        np.around(pv_hour.pv/10000,decimals=2),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add_yaxis(
        series_name="UV",
        yaxis_index=1,
        y_axis=np.around(uv_hour.uv/10000,decimals=2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="UV",
            type_="value",
            min_=0,
            max_=9,
            interval=1.5,
            axislabel_opts=opts.LabelOpts(formatter="{value} 万人"),
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,trigger="axis",axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True,type_="line"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="PV",
            type_="value",
            min_=0,
            max_=120,
            interval=20,
            axislabel_opts=opts.LabelOpts(formatter="{value} 万次"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="PV,UV情况（按小时）",pos_left='left'),
        legend_opts=opts.LegendOpts(is_show=True,pos_top='95%')
    )
)
line.render_notebook()


# 每天活跃人数大约在6500人左右波动，用户点击数也在每天40万左右波动，在双十二当天两项指标大幅增加，活动结束后又迅速恢复正常水平。
# 
# 用户最活跃的时间段为18时-24时，整体行为规律与人们日常工作等的时间规律相符，平台活动的宣传推广应重点放在这个时间段。

# # 其他指标分析

# In[12]:


#用户消费次数分布
data_user_buy = data_user[data_user['behavior_type']==4].groupby('user_id')['behavior_type'].count().reset_index().rename(columns={'behavior_type':'buy_num'})
user_buy = data_user_buy.groupby('buy_num')['user_id'].count()

#用户消费间隔分布
data_day_buy = data_user[data_user['behavior_type']==4].groupby(['user_id','date'])['behavior_type'].count().reset_index(level='date')
data_day_buy.drop(columns='behavior_type',inplace=True)
repeat_buy=data_day_buy.groupby('user_id').date.diff(1).dropna()
repeat_buy=repeat_buy.map(lambda x:x.days).value_counts()

#用户日均消费次数
ARPU_num = data_user[data_user['behavior_type']==4].groupby('date')['user_id'].count().rename('pv').reset_index()
ARPU_num['num'] = ARPU_num['pv']/uv_daily['uv']
del ARPU_num['pv']


# In[13]:


buy_num = (
    Bar()
    .add_xaxis(user_buy.index.tolist())
    .add_yaxis("",user_buy.values.tolist(),label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(xaxis_opts=opts.AxisOpts(min_=0, max_=80)
        ,title_opts=opts.TitleOpts(title="用户消费次数分布情况"))
)


repeat_buy_num = (
    Bar()
    .add_xaxis(repeat_buy.index.tolist())
    .add_yaxis("",repeat_buy.values.tolist(),label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="用户复购间隔情况"))
)

arpu_num = (
    Line()
    .add_xaxis(list(ARPU_num.date.astype('str').tolist()))
    .add_yaxis("",np.around(ARPU_num.num.tolist(),2),label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="每用户平均购买量"))
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False))
)

tab = Tab()
tab.add(buy_num, "用户消费次数分布情况")
tab.add(repeat_buy_num, "用户复购间隔情况")
tab.add(arpu_num, "每用户平均购买量")
tab.render_notebook()


# 大部分用户的购买次数在10次之内,消费次数随着消费时间间隔的增加而不断下降，在1-10天之内复购的用户较多，10天之后用户较少再次在平台内进行购买，每用户的平均购买量在0.5左右波动，双十二期间接近2。

# # 用户行为转化分析

# In[14]:


behavior_count = data_user.groupby(['behavior_type','user_id','item_id'])['item_category'].count().reset_index().rename(columns={'item_category':'total'})
pv_count = behavior_count[behavior_count['behavior_type'] == 1]
fav_count = behavior_count[behavior_count['behavior_type'] == 2]
cart_count = behavior_count[behavior_count['behavior_type'] == 3]
buy_count = behavior_count[behavior_count['behavior_type'] == 4]

all_data = pd.merge(pv_count,fav_count,how='left',on=['user_id','item_id']).rename(columns={'behavior_type_x':'pv','behavior_type_y':'fav','total_x':'total_pv','total_y':'total_fav'})
all_data = pd.merge(all_data,cart_count,how='left',on=['user_id','item_id'])
all_data = pd.merge(all_data,buy_count,how='left',on=['user_id','item_id']).rename(columns={'behavior_type_x':'cart','behavior_type_y':'buy','total_x':'total_cart','total_y':'total_buy'})
all_data = all_data.fillna(0)
all_data


# In[15]:


#用户点击—购买路径表
pv_buy = all_data.loc[(all_data['fav']==0)&(all_data['cart']==0)]
#用户点击—收藏—购买路径表
pv_fav_buy = all_data.loc[(all_data['fav']==2)&(all_data['cart']==0)]
#用户点击—加购—购买路径表
pv_cart_buy = all_data.loc[(all_data['fav']==0)&(all_data['cart']==3)]
#用户点击—收藏和加购—购买路径表
pv_fav_cart_buy = all_data.loc[(all_data['fav']==2)&(all_data['cart']==3)]


# In[16]:


#用户点击—购买转换漏斗
attr_1 = ['点击','购买']
values_1 = [np.around(pv_buy['total_pv'].sum()/pv_buy['total_pv'].sum()*100,2)
        ,np.around(pv_buy['total_buy'].sum()/pv_buy['total_pv'].sum()*100,2)]
pv_buy_rate = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_1, values_1)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—收藏—购买转换漏斗
attr_2 = ['点击','收藏','购买']
values_2 = [np.around(pv_fav_buy['total_pv'].sum()/pv_fav_buy['total_pv'].sum()*100,2)
        ,np.around(pv_fav_buy['total_fav'].sum()/pv_fav_buy['total_pv'].sum()*100,2)
        ,np.around(pv_fav_buy['total_buy'].sum()/pv_fav_buy['total_pv'].sum()*100,2)]
pv_fav_buy_rate = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_2, values_2)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—收藏—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—加购—购买转换漏斗
attr_3 = ['点击','加入购物车','购买']
values_3 = [np.around(pv_cart_buy['total_pv'].sum()/pv_cart_buy['total_pv'].sum()*100,2)
        ,np.around(pv_cart_buy['total_cart'].sum()/pv_cart_buy['total_pv'].sum()*100,2)
        ,np.around(pv_cart_buy['total_buy'].sum()/pv_cart_buy['total_pv'].sum()*100,2)]
pv_cart_buy_rate = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_3, values_3)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—加入购物车—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—收藏和加购—购买转换漏斗
attr_4 = ['点击','收藏和加入购物车','购买']
values_4 = [np.around(pv_fav_cart_buy['total_pv'].sum()/pv_fav_cart_buy['total_pv'].sum()*100,2)
        ,np.around((pv_fav_cart_buy['total_cart'].sum()+pv_fav_cart_buy['total_fav'].sum())/pv_fav_cart_buy['total_pv'].sum()*100,2)
        ,np.around(pv_fav_cart_buy['total_buy'].sum()/pv_fav_cart_buy['total_pv'].sum()*100,2)]
pv_fav_cart_buy_rate = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_4, values_4)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—收藏和加入购物车—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#可视化各行为路径漏斗图
tab = Tab()
tab.add(pv_buy_rate, "点击—购买转化漏斗")
tab.add(pv_fav_buy_rate, "点击—收藏—购买转化漏斗")
tab.add(pv_cart_buy_rate, "点击—加入购物车—购买转化漏斗")
tab.add(pv_fav_cart_buy_rate, "点击—收藏和加入购物车—购买转化漏斗")
tab.render_notebook()


# “点击—加入购物车—购买”的转化率最高，说明加购的的行为是用户购买意向的体现，平台可以根据用户加购列表里的商品开展营销活动。
# 
# “点击—收藏—购买”的转化率与“点击—购买”的转化率相当，说明收藏并不能促进用户购买。

# # RFM分析 

# R:最近一次购买日期  F：一段时间内的购买频率  M：一段时间内的花费金额
# 因为源数据中没有提供有关M的任何信息，所以只基于R和F两个维度。

# In[17]:


data_rfm=data_user[data_user.behavior_type==4].reset_index(drop=True)
recent=data_rfm.date.max() 
data_rfm=data_rfm.groupby(['user_id'],as_index=False).agg({'date': lambda x: (recent - x.max()).days,'time': 'count'}).rename(columns = {'date': 'Recency','time': 'Frequency'})


# In[18]:


Recency_avg = data_rfm.Recency.mean()
Frequency_avg = data_rfm.Frequency.mean()
data_rfm['user_type'] = 1
data_rfm.loc[(data_rfm['Recency']<Recency_avg)&(data_rfm['Frequency']>Frequency_avg),'user_type'] = '重要价值客户'
data_rfm.loc[(data_rfm['Recency']>Recency_avg)&(data_rfm['Frequency']>Frequency_avg),'user_type'] = '重要保持用户'
data_rfm.loc[(data_rfm['Recency']<Recency_avg)&(data_rfm['Frequency']<Frequency_avg),'user_type'] = '重要发展用户'
data_rfm.loc[(data_rfm['Recency']>Recency_avg)&(data_rfm['Frequency']<Frequency_avg),'user_type'] = '重要挽留用户'


# In[19]:


rfm=data_rfm.groupby('user_type')['user_id'].count()
rfm


# In[20]:


pie = (
    Pie()
    .add(
        '',
        [z for z in zip(rfm.index, rfm.values.tolist())]
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="客户群体分析"),
                     legend_opts=opts.LegendOpts(is_show=True),)
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
      )
pie.render_notebook()


# 重要价值客户：最近有过购买记录，且消费频率很高，需要重点关注这些用户，既要保持其粘性，又要继续激发这些用户的购买欲望。 
# 
# 重要发展用户：最近有过购买记录，且消费频率不高，应尽量提高其消费次数。
# 
# 重要保持用户：有一段时间未购物，且消费频率很高，应注重对这些用户的重新唤醒，促进复购。
# 
# 重要挽留客户：有一段时间未购物，且消费频率不高，若不加以挽留，会有流失的可能，需要进一步研究其兴趣和需求，采取有效的运营策略。

# # 双十二期间用户行为分析

# In[21]:


data_12 = data_user[(data_user['date'] <='2014-12-13') & (data_user['date'] >='2014-12-11')]

pv_12_num = data_12.groupby('behavior_type').get_group(1).groupby('time').count()['user_id']
fav_12_num = data_12.groupby('behavior_type').get_group(2).groupby('time').count()['user_id']
cart_12_num = data_12.groupby('behavior_type').get_group(3).groupby('time').count()['user_id']
buy_12_num = data_12.groupby('behavior_type').get_group(4).groupby('time').count()['user_id']
num_12 = pd.concat([pv_12_num,fav_12_num,cart_12_num,buy_12_num],axis=1)
num_12.columns =['浏览','收藏','加购物车','购买']
num_12.head()


# In[22]:


line_area = (
    Line()
    .add_xaxis(num_12.index.tolist())
    .add_yaxis("浏览", num_12['浏览'].tolist(),yaxis_index=0,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("收藏", num_12['收藏'].tolist(), yaxis_index=1,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("加购物车", num_12['加购物车'].tolist(),yaxis_index=1,label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("购买", num_12['购买'].tolist(), yaxis_index=1,label_opts=opts.LabelOpts(is_show=False))
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="次数",
            type_="value",
            min_=0,
            max_=3000,
            interval=500,
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True,trigger="axis",axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True,type_="line"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="次数",
            type_="value",
            min_=0,
            max_=60000,
            interval=10000,
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(title="双十二前后用户各行为情况",pos_left='left'),
        legend_opts=opts.LegendOpts(is_show=True,pos_top='95%')
    )
)
line_area.render_notebook()


# 双十二活动主要有两个高峰时间段，12月11日18时-12月12日1时和12月12日的18时-24时，在双十二之前会出现用户的点击、收藏和加购行为的大幅增加，特别是加入购物车的行为，说明用户在双十二前依旧在大量筛选商品，对于有购买意向的商品用户会优先选择加入购物车。

# In[23]:


data_12 = data_user[(data_user['date'] =='2014-12-12') ]
behavior_count_12 = data_12.groupby(['behavior_type','user_id','item_id'])['item_category'].count().reset_index().rename(columns={'item_category':'total'})
pv_count_12 = behavior_count_12[behavior_count_12['behavior_type'] == 1]
fav_count_12 = behavior_count_12[behavior_count_12['behavior_type'] == 2]
cart_count_12 = behavior_count_12[behavior_count_12['behavior_type'] == 3]
buy_count_12 = behavior_count_12[behavior_count_12['behavior_type'] == 4]

all_data_12 = pd.merge(pv_count_12,fav_count_12,how='left',on=['user_id','item_id']).rename(columns={'behavior_type_x':'pv','behavior_type_y':'fav','total_x':'total_pv','total_y':'total_fav'})
all_data_12 = pd.merge(all_data_12,cart_count_12,how='left',on=['user_id','item_id'])
all_data_12 = pd.merge(all_data_12,buy_count_12,how='left',on=['user_id','item_id']).rename(columns={'behavior_type_x':'cart','behavior_type_y':'buy','total_x':'total_cart','total_y':'total_buy'})
all_data_12 = all_data_12.fillna(0)


# In[24]:


#用户点击—购买路径表
pv_buy_12 = all_data_12.loc[(all_data_12['fav']==0)&(all_data_12['cart']==0)]
#用户点击—收藏—购买路径表
pv_fav_buy_12 = all_data_12.loc[(all_data_12['fav']==2)&(all_data_12['cart']==0)]
#用户点击—加购—购买路径表
pv_cart_buy_12 = all_data_12.loc[(all_data_12['fav']==0)&(all_data_12['cart']==3)]
#用户点击—收藏和加购—购买路径表
pv_fav_cart_buy_12 = all_data_12.loc[(all_data_12['fav']==2)&(all_data_12['cart']==3)]


# In[25]:


#用户点击—购买转换漏斗
attr_1 = ['点击','购买']
values_1 = [np.around(pv_buy_12['total_pv'].sum()/pv_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_buy_12['total_buy'].sum()/pv_buy_12['total_pv'].sum()*100,2)]
pv_buy_rate_12 = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_1, values_1)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—收藏—购买转换漏斗
attr_2 = ['点击','收藏','购买']
values_2 = [np.around(pv_fav_buy_12['total_pv'].sum()/pv_fav_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_fav_buy_12['total_fav'].sum()/pv_fav_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_fav_buy_12['total_buy'].sum()/pv_fav_buy_12['total_pv'].sum()*100,2)]
pv_fav_buy_rate_12 = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_2, values_2)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—收藏—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—加购—购买转换漏斗
attr_3 = ['点击','加入购物车','购买']
values_3 = [np.around(pv_cart_buy_12['total_pv'].sum()/pv_cart_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_cart_buy_12['total_cart'].sum()/pv_cart_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_cart_buy_12['total_buy'].sum()/pv_cart_buy_12['total_pv'].sum()*100,2)]
pv_cart_buy_rate_12 = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_3, values_3)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—加入购物车—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#用户点击—收藏和加购—购买转换漏斗
attr_4 = ['点击','收藏和加入购物车','购买']
values_4 = [np.around(pv_fav_cart_buy_12['total_pv'].sum()/pv_fav_cart_buy_12['total_pv'].sum()*100,2)
        ,np.around((pv_fav_cart_buy_12['total_cart'].sum()+pv_fav_cart_buy_12['total_fav'].sum())/pv_fav_cart_buy_12['total_pv'].sum()*100,2)
        ,np.around(pv_fav_cart_buy_12['total_buy'].sum()/pv_fav_cart_buy_12['total_pv'].sum()*100,2)]
pv_fav_cart_buy_rate_12 = (
    Funnel()
    .add("商品", [list(z) for z in zip(attr_4, values_4)],
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="点击—收藏和加入购物车—购买转化漏斗"),
    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='90%'))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
)


#可视化各行为路径漏斗图
tab = Tab()
tab.add(pv_buy_rate_12, "点击—购买转化漏斗")
tab.add(pv_fav_buy_rate_12, "点击—收藏—购买转化漏斗")
tab.add(pv_cart_buy_rate_12, "点击—加入购物车—购买转化漏斗")
tab.add(pv_fav_cart_buy_rate_12, "点击—收藏和加入购物车—购买转化漏斗")
tab.render_notebook()


# # 结论与建议

# 双十二活动的效果立竿见影，各项指标均得到一定幅度的提升，但是此类大型活动不宜频繁，因此需要通过其他途径来提高平台收入，这需要从提高用户点击、提高用户点击转化率、提高用户平均订单数等方面入手。
# 
# 在提高用户点击量方面，可以着重在用户的浏览的高峰时间段进行促销活动，以及一些相关的营销推广。
# 
# 在提高用户点击转化率方面，可以针对用户进行收藏和加入购物车的商品，提供如发放优惠券，满减活动，分期免息等优惠的方式，刺激用户购买。
# 
# 在提高用户平均订单数方面，可以针对10天内购买过的用户可以提高对平台商品的推送频率，进一步刺激用户的购买欲。
# 

# In[ ]:




