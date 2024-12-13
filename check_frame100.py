import cv2
import pandas as pd
import matplotlib.pyplot as plt

# データを読み込む
df = pd.read_csv('../givnu/givnu_csv/givnu.csv')

# 動画から特定のフレームを取得して描画
def plot_frame_on_video(video_path, frame_index, data_frame):
    # 動画を読み込む
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # 指定フレームまで移動
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()
    if not ret:
        print(f"Error: Could not read frame {frame_index}.")
        cap.release()
        return

    # フレームにデータを描画
    frame_data = data_frame[data_frame["frameIndex"] == frame_index]
    for _, row in frame_data.iterrows():
        left, top = int(row["x"]), int(row["y"])
        person_id = int(row["personId"])
        # 座標に円とIDを描画
        cv2.circle(frame, (left, top), radius=5, color=(0, 0, 255), thickness=-1)  # 赤い点
        cv2.putText(frame, f"ID {person_id}", (left + 10, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)  # 緑のテキスト

    # フレームを表示
    cv2.imshow(f"Frame {frame_index}", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # フレームを保存（必要に応じて）
    output_path = f"../givnu/givnu_video/frame_{frame_index}.jpg"
    cv2.imwrite(output_path, frame)
    print(f"Frame {frame_index} saved as {output_path}.")

    cap.release()

# 動画ファイルパスとフレーム番号を指定して実行
video_path = "../givnu/givnu_video/givnu_ori.mp4"  # 動画ファイルのパスを指定
frame_index_to_plot = 100  # 描画したいframeIndexを指定
plot_frame_on_video(video_path, frame_index_to_plot, df)