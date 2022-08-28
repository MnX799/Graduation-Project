#%%
import pandas as pd
import numpy as np
from utils import mat2df,copy_values
from tensor import tensor2_matrix
from detensor import detensor2_matrix
from evaluation import RMSE

from surprise import SVD,SVDpp,NMF,KNNBasic,KNNWithMeans,KNNWithZScore,KNNBaseline
from surprise.model_selection import train_test_split
from surprise import Reader
from surprise import Dataset
from surprise.model_selection import train_test_split

#read data
#X00 = pd.read_csv("df_2009_uxi.csv",index_col = 'userId').values # (11092,75)
X00 = pd.read_csv("douban_uxi.csv",index_col = 'userId').values # (22553,81)
#X00 = pd.read_csv("douban_2005.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2006.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2007.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2008.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2010.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2011.csv",index_col = 'userId').values


#X0 = X00[:3240,:80]
X0 = X00
d = X0.shape[1]
# tensorization
X2 = tensor2_matrix(X0)
data0 = mat2df(X2)

# completion
reader = Reader(rating_scale=(1, 25))
data = Dataset.load_from_df(data0, reader)
train, test = train_test_split(data, test_size=.25, random_state=0)

svd_model = SVD(random_state=0)
#svd_model = SVDpp(random_state=0)
#svd_model = NMF(random_state=0)
#svd_model = KNNBasic()
#svd_model = KNNWithMeans()
#svd_model = KNNWithZScore()
#svd_model = KNNBaseline()

svd_model.fit(train)
predict = svd_model.test(test) 

row_Id = []
col_Id = []
ratings = []
for pre in predict:
    row_Id.append(pre[0])
    col_Id.append(pre[1])
    ratings.append(pre[3])
data = {
        'row':row_Id,
        'col':col_Id,
        'ratings':ratings
            }
new_data = pd.DataFrame(data)

#删去data0中【在new_data中的ui相符的】元素并拼接
df2 = pd.concat([new_data,data0],axis=0)
pre_new = df2.drop_duplicates(subset=['row', 'col'], keep='first')
pre_new = pre_new.sort_values(by=['row','col'])
pre_new.index = range(len(pre_new))

#转化为预测矩阵
row = [i for i in range(X2.shape[0])]  #获取index
col = [j for j in range(X2.shape[1])] #获取column
 
df_pre = pd.DataFrame(index=row, columns=col) #新定义一个数据框df_

for i in range(len(pre_new)):
    row_i = pre_new.loc[[i]]
    row = (row_i['row'].tolist())[0]
    col = (row_i['col'].tolist())[0]
    ratings = (row_i['ratings'].tolist())[0]
    df_pre.at[row,col] = ratings

X2_hat = df_pre.values
X2_hat_0 = np.zeros(X2_hat.shape)
copy_values(X2_hat,X2_hat_0)

# detensorization
X_hat = detensor2_matrix(X2_hat_0,d)

#evaluation
print("RMSE:",RMSE(X0,X_hat))

# %%
