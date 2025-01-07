import pandas as pd
import cv2
import matplotlib.pyplot as plt

# 入力ファイルと画像のパス
csv_file = "../givnu_csv/new_data2.csv"  # CSVファイルのパス
image_file = "../givnu_video/field_template.jpg"      # 背景画像のパス

# frameIndex のリスト
frame_indices = [13560]

# CSVデータを読み込み
df = pd.read_csv(csv_file)

# 指定された frameIndex に該当する行を抽出
filtered_df = df[df["frameIndex"].isin(frame_indices)]

# 背景画像を読み込み
background = cv2.imread(image_file)
if background is None:
    raise FileNotFoundError(f"背景画像 {image_file} が見つかりません。")

# BGRからRGBに変換 (matplotlibで正しく表示するため)
background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

# プロットの準備
plt.figure(figsize=(10, 6))
plt.imshow(background)
plt.axis("off")  # 軸を非表示にする

# 座標をプロット
for _, row in filtered_df.iterrows():
    x = row["x_projected"]
    y = row["y_projected"]
    plt.scatter(x, y, c="red", s=50)  # 座標を赤色でプロット
    plt.text(x, y, f'({int(row["frameIndex"])})', fontsize=8, color="white", ha="center")


# 結果を表示（オプション）
plt.show()
