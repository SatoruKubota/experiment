import pandas as pd

# givnu.csvを読み込む
file_path = "givnu.../givnu/givnu_csv/givnu.csv"
df = pd.read_csv(file_path)

# 列名を変更
df.rename(columns={"left": "x", "top": "y"}, inplace=True)

# 確認のためデータフレームを表示
print(df.head())

# 必要に応じて、変更後のデータフレームを新しいCSVファイルに保存
output_path = "givnu.csv"
df.to_csv(output_path, index=False)
print(f"列名を変更したCSVを保存しました: {output_path}")
