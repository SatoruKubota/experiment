import cv2

def get_video_fps(video_path):
    # 動画を読み込む
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: {video_path} を開けませんでした")
        return None

    # FPSを取得
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()  # 動画を閉じる
    return fps

# ファイルパスを指定
video1_path = "../givnu/givnu_video/givnu_ori.mp4"
video2_path = "../givnu/givnu_video/rslt_givnu.mp4"

# FPSを取得して表示
fps1 = get_video_fps(video1_path)
fps2 = get_video_fps(video2_path)

if fps1 is not None:
    print(f"{video1_path} のFPS: {fps1}")
if fps2 is not None:
    print(f"{video2_path} のFPS: {fps2}")
