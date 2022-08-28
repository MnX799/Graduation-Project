#%%
import pandas as pd
import numpy as np 
import time
from time import localtime

#合并user-movie评分数据
movies = pd.read_csv('D:\\13169\data\ez_douban\movies.csv')
ratings = pd.read_csv('D:\\13169\data\ez_douban\\ratings.csv')
 
combine_movie_rating= pd.merge(ratings,movies,on='movieId',how='inner')
combine_movie_rating = combine_movie_rating.dropna(axis = 0 ,subset=['title'])
#过滤出评分次数多的电影
movie_rating_count=pd.DataFrame(combine_movie_rating.
                    groupby(['movieId'])['rating'].
                    count().
                    reset_index().
                    rename(columns={'rating':'totalRatingCount'})                   
                   )
rating_with_totalRatingCount = combine_movie_rating.merge(movie_rating_count,left_on='movieId',right_on='movieId')
rating_with_totalRatingCount.head()
#计算头部10%热门评分电影的评分数阈值：为2351
rating_with_totalRatingCount['totalRatingCount'].quantile(np.arange(.9,1,.01))
#取最热门top10%的电影，将时间戳转换为年份
popular_threshold=2351 
rating_with_totalRatingCount = combine_movie_rating.merge(movie_rating_count,left_on='movieId',right_on='movieId')
popular_movies_rating= rating_with_totalRatingCount.query('totalRatingCount>=@popular_threshold')
print('热门电影数据量：%d' % len(popular_movies_rating))
df = popular_movies_rating[['userId','movieId','rating','timestamp']]
df.index = range(len(df))
df['year'] = df['timestamp'].apply(lambda x:localtime(x)[0])
df = df.drop(['timestamp'],axis = 1)

df.sort_values(by="year",axis=0,ascending=True,inplace=True)
df_ = df[df['year']==2011]
df_ = df_.drop(['year'],axis = 1)
df_.index = range(len(df_))

#构建user-item矩阵 type: dataframe
n_users = df_['userId'].drop_duplicates()  #获取index
n_items = df_['movieId'].drop_duplicates() #获取column
 
df_new = pd.DataFrame(index=n_users, columns=n_items) #新定义一个数据框df_new
for i in range(len(df_)):
    row_i = df_.loc[[i]]
    movieId = (row_i['movieId'].tolist())[0]
    userId = (row_i['userId'].tolist())[0]
    rating = (row_i['rating'].tolist())[0]
    df_new.at[userId,movieId] = rating

# 输出到csv
df_new.to_csv('douban_2011.csv', sep=',', encoding='utf-8')
# %%
