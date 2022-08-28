# 双条形图 douban
import plotly.offline as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace0 = go.Bar(
    x = ['SVD','SVDpp','NMF','KNNBasic','KNNWithMeans','KNNWithZScore','KNNBaseline'],
    y = [0.17979579188635605,0.22146058406527272,0.4610502507105664,
        0.22203037761270725,0.41951334578726684,0.41541392426803647,0.23862522350924084],
    name = 'LADMC'
)
trace1 = go.Bar(
    x = ['SVD','SVDpp','NMF','KNNBasic','KNNWithMeans','KNNWithZScore','KNNBaseline'],
    y = [0.5635548572427637,0.5596426453956544,0.594618338131357,
        0.5807366737755917,0.5709067869440233,0.5692639172912933,0.56171260050451],
    name = 'LRMC'
)
data = [trace0,trace1]

layout = go.Layout(
  xaxis = dict(title = '补全步骤所用算法'),
  yaxis = dict(title = 'RMSE'),
  font = {'size': 20, 'family': 'Times New Roman'}


 )
figure = go.Figure(data = data, layout = layout)
figure.show()
