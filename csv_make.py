import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, Polygon

# CSVファイルを読み込み
df = pd.read_csv('../givnu_csv/rslt_givnu.csv')

# 列名を変更
df.rename(columns={"left": "x", "top": "y"}, inplace=True)

# 条件に合う行を抽出
# 新しいyの列を計算
###############  y座標が足になるように  ######################
df['y'] = df['y'] + df['height']
df['x'] = df['x'] + df['width'] / 2

# 結果を表示
print(df)

# フィルタリング結果をCSVファイルに出力
output_path = f'../givnu_csv/givnu.csv'
df.to_csv(output_path, index=False)