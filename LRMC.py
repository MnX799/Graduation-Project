#%%
import pandas as pd
from surprise import SVD,SVDpp,NMF,KNNBasic,KNNWithMeans,KNNWithZScore,KNNBaseline
from surprise.model_selection import train_test_split
from surprise import Reader
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split

from utils import mat2df

#X00 = pd.read_csv("df_2009_uxi.csv",index_col = 'userId').values # (11092,75)
X00 = pd.read_csv("douban_uxi.csv",index_col = 'userId').values # (22553,81)
#X00 = pd.read_csv("douban_2005.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2006.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2007.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2008.csv",index_col = 'userId').values
#X00 = pd.read_csv("douban_2010.csv",index_col = 'userId').values
X00 = pd.read_csv("douban_2011.csv",index_col = 'userId').values

#X0 = X00[:1300,:50]
X0 = X00

data0 = mat2df(X0)

reader = Reader(rating_scale=(0.5, 5))
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
print("RMSE: ",accuracy.mae(predict, verbose=False))
# %%
