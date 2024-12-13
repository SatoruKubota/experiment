import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, Polygon

# CSVファイルを読み込み
df = pd.read_csv('../givnu/givnu_csv/givnu.csv')

# 列名を確認
print(df.head())
print(df.columns)


# 4点の座標を指定
points = [[511, 335], [986, 353], [1084, 709], [53, 513]]

# ポリゴンを作成
polygon = Polygon(points)

# ポリゴン内のデータを保持するフィルタリング関数
###############     ピッチ内の選手のみカウント   ##################
def is_inside_polygon(row, polygon):
    point = Point(row['x'], row['y'])
    return polygon.contains(point)

# データフレームをフィルタリング
df_filtered = df[df.apply(is_inside_polygon, axis=1, args=(polygon,))]

# フィルタリング結果をCSVファイルに出力
#output_path = 'filtered_points.csv'
output_path = '../givnu/givnu_csv/givnu_points.csv'

df_filtered.to_csv(output_path, index=False)

print(f'Filtered data saved to {output_path}')