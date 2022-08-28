#%%
import pandas as pd
import numpy as np 
import time
from time import localtime
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import Reader
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split

#%%
#合并user-movie评分数据
movies = pd.read_csv('D:\\13169\data\ez_douban\movies.csv')
ratings = pd.read_csv('D:\\13169\data\ez_douban\\ratings.csv')
 
combine_movie_rating= pd.merge(ratings,movies,on='movieId',how='inner')
combine_movie_rating = combine_movie_rating.dropna(axis = 0 ,subset=['title'])
#%%
#过滤出评分次数多的电影
movie_rating_count=pd.DataFrame(combine_movie_rating.
                    groupby(['movieId'])['rating'].
                    count().
                    reset_index().
                    rename(columns={'rating':'totalRatingCount'})                   
                   )
rating_with_totalRatingCount = combine_movie_rating.merge(movie_rating_count,left_on='movieId',right_on='movieId')
rating_with_totalRatingCount.head()
#%%
#计算头部10%热门评分电影的评分数阈值：为2351
rating_with_totalRatingCount['totalRatingCount'].quantile(np.arange(.9,1,.01))
#%%
#取最热门top10%的电影，将时间戳转换为年份
popular_threshold=2351 
rating_with_totalRatingCount = combine_movie_rating.merge(movie_rating_count,left_on='movieId',right_on='movieId')
popular_movies_rating= rating_with_totalRatingCount.query('totalRatingCount>=@popular_threshold')
print('热门电影数据量：%d' % len(popular_movies_rating))
df = popular_movies_rating[['userId','movieId','rating','timestamp']]
df.index = range(len(df))
df['year'] = df['timestamp'].apply(lambda x:localtime(x)[0])
df = df.drop(['timestamp'],axis = 1)
#%%
#去除时间戳
df = df.drop(['year'],axis = 1)
# %%
#2009年评分数据最多，为79470条，选之
df.sort_values(by="year",axis=0,ascending=True,inplace=True)
df_2009 = df[df['year']==2009]
df_2009 = df_2009.drop(['year'],axis = 1)
df_2009.index = range(len(df_2009))
# %%
#构建user-item矩阵 df_(11092,75) type: dataframe
n_users = df_2009['userId'].drop_duplicates()  #获取index
n_items = df_2009['movieId'].drop_duplicates() #获取column
 
df_ = pd.DataFrame(index=n_users, columns=n_items) #新定义一个数据框df_
for i in range(len(df_2009)):
    row_i = df_2009.loc[[i]]
    movieId = (row_i['movieId'].tolist())[0]
    userId = (row_i['userId'].tolist())[0]
    rating = (row_i['rating'].tolist())[0]
    df_.at[userId,movieId] = rating
# %%
# 输出到csv
df.to_csv('douban.csv', sep=',', encoding='utf-8')
df_.to_csv('douban_2009.csv', sep=',', encoding='utf-8')
# %%
