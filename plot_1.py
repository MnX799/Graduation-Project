# 双条形图 douban_2009
import plotly.offline as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace0 = go.Bar(
    x = ['SVD','SVDpp','NMF','KNNBasic','KNNWithMeans','KNNWithZScore','KNNBaseline'],
    y = [0.45067382375035014,0.5378999018344192,0.6414984384294871,
        0.4689710698019906,0.8344237026869508,0.8249301060420109,0.5556788143868251],
    name = 'LADMC',
)
trace1 = go.Bar(
    x = ['SVD','SVDpp','NMF','KNNBasic','KNNWithMeans','KNNWithZScore','KNNBaseline'],
    y = [0.563121997441783,0.5529193745087212,0.6090118633124804,
        0.5758221881313996,0.5631395107839678,0.5659559754799094,0.55522929045803],
    name = 'LRMC',
)
data = [trace0,trace1]

layout = go.Layout(
  xaxis = dict(title = '补全步骤所用算法'),
  yaxis = dict(title = 'RMSE'),
  font = {'size': 20, 'family': 'Times New Roman'}
 )
figure = go.Figure(data = data, layout = layout)
figure.show()
