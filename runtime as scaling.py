# runtime as scaling
import numpy as np
import plotly.express as px

data = [[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,898.3],
        [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,540.5,713.9],
        [np.nan,np.nan,np.nan,np.nan,np.nan,303.1,438.3,558.8],
        [np.nan,np.nan,np.nan,np.nan,154.3,220.7,308.9,409.7],
        [np.nan,np.nan,np.nan,66.4,104.3,145.4,209.1,265.7],
        [np.nan,np.nan,36.6,117.7,121.5,89.7,120.2,160.7],
        [np.nan,9.8,18.8,33.1,49.6,71.3,109.5,125.5],
        [4.1,4.1,6.8,11.1,15.9,21.2,28.4,36.3]]


fig = px.imshow(
    data,  # 传入数据
    # 轴标签设置
    labels=dict(x="用户数N", y="电影数d", color="耗时（秒）",text_auto = 'True'),  
    # 轴刻度设置
    x = ['55','210','465','820','1275','1830','2485','3240'],
    y = ['80','70','60','50','40','30','20','10']
    )

fig.show()