import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルを読み込み
#df = pd.read_csv('filtered_points.csv')
pt_df = pd.read_csv('../givnu_csv/givnu_points.csv')


#追加
# 各frameIndexの出現回数をカウント
frame_counts = pt_df['frameIndex'].value_counts()

# 出現回数が8回以上のframeIndexを取得
frequent_frame_indices = frame_counts[frame_counts >= 8].index
#frequent_frame_indices = frame_counts.index

# 該当するframeIndexのみをフィルタリング
df = pt_df[pt_df['frameIndex'].isin(frequent_frame_indices)]

df.to_csv('../givnu_csv/givnu_data.csv', index=False)
print("新しいCSVファイルが作成されました。")


################# 変換行列を求める #############
# 画像上の座標
original_points = [[511, 335], [986, 353], [1084, 709], [53, 513]]
original_points = np.array(original_points, dtype=np.float32)

# 仮想コートの座標
field_template = cv2.imread("../givnu_video/field_template.jpg")
height, width = field_template.shape[:2]
corners = [[0, 0], [width/2, 0], [width/2, height], [0, height]]
print(corners)
corners = np.array(corners, dtype=np.float32)

# 変換行列の取得
M = cv2.getPerspectiveTransform(original_points, corners)
np.set_printoptions(precision=5, suppress=True)
print(M)

# x, y列を取り出して同次座標に変換
points = df[['x', 'y']].to_numpy(dtype=np.float32)
points = np.expand_dims(points, axis=1)  # shapeを(N, 1, 2)にする

# cv2.perspectiveTransformを使用して射影変換を適用
transformed_points = cv2.perspectiveTransform(points, M)

# assignを使用して新しい列を追加
df = df.assign(
    x_projected=transformed_points[:, 0, 0],  # x座標
    y_projected=transformed_points[:, 0, 1]   # y座標
)

# CSVとして保存
df.to_csv('../givnu_csv/new_data2.csv', index=False)

