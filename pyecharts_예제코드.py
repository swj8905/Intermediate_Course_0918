from pyecharts import Bar3D

bar3d = Bar3D("감성 분석 결과", width=1200, height=600)
x_axis = []
y_axis = ["매우긍정", "긍정", "중립", "부정", "매우부정"]
data = [[0,0,10], [1,0,15], [2,0,40], [3,0,30], [4,0,40]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True, visual_range=[0, 40], visual_range_color=range_color,
    grid3d_width=40, grid3d_depth=200, grid3d_shading="lambert")
bar3d.render("./bar3d.html")

# HTML 파일 자동으로 열기
import webbrowser
import os
ap = os.path.abspath("./bar3d.html")
# webbrowser.open(ap) # 윈도우
webbrowser.open("file://" + ap) # 맥