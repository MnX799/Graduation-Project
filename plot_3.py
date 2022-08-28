#框架时间消耗
import plotly.graph_objects as go

# 生成画布
fig = go.Figure()

fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,15.6],
    name='2005',
    orientation='h',
    marker=dict(
        color='rgba(255, 0, 0, 0.6)',
        line=dict(color='rgba(255, 0, 0, 1)',width=3)
    )
))

fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,60.1],
    name='2006',
    orientation='h',
    marker=dict(
        color='rgba(255, 165, 0, 0.6)',
        line=dict(color='rgba(255, 165, 0, 1)',width=3)
    )
))

fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,89.1],
    name='2007',
    orientation='h',
    marker=dict(
        color='rgba(255, 255, 0, 0.6)',
        line=dict(color='rgba(255, 255, 0, 1)',width=3)
    )
))
fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,206.1],
    name='2008',
    orientation='h',
    marker=dict(
        color='rgba(0, 255, 0, 0.6)',
        line=dict(color='rgba(0, 255, 0, 1)',width=3)
    )
))
fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,328.7],
    name='2009',
    orientation='h',
    marker=dict(
        color='rgba(0, 255, 255, 0.6)',
        line=dict(color='rgba(0, 255, 255, 1)',width=3)
    )
))
fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,236.1],
    name='2010',
    orientation='h',
    marker=dict(
        color='rgba(0, 0, 255, 0.6)',
        line=dict(color='rgba(0, 0, 255, 1)',width=3)
    )
))
fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[0,89.8],
    name='2011',
    orientation='h',
    marker=dict(
        color='rgba(139, 0, 255, 0.6)',
        line=dict(color='rgba(139, 0, 255, 1)',width=3)
    )
    
))

fig.add_trace(go.Bar(
    y=['不应用框架', '应用框架'],
    x=[1810.6,0],
    name='混合年份',
    orientation='h',
    marker=dict(
        color='rgba(209, 186, 116, 0.6)',
        line=dict(color='rgba(209, 186, 116, 1)',width=3)
    )
    
))


fig.update_layout(barmode='stack')  # 堆叠模式:['stack', 'group', 'overlay', 'relative']


fig.show()
