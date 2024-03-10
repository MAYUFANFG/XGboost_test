# 引入 librosa 函式庫，用於音訊分析
import librosa
import matplotlib.pyplot as plt
#用於顯示音訊數據
import librosa.display

# 設定音訊檔案的路徑
audio_path = './output.wav'

# 使用 librosa 的 load 函數讀取音訊檔案
# x 是音訊數據，sr 是音訊的取樣率
x , sr = librosa.load(audio_path)

# 印出 x 和 sr 的型別
#print(type(x), type(sr))  # <class 'numpy.ndarray'> <class 'int'>

# 印出音訊數據的形狀和取樣率
#print(x.shape, sr)  # (396688,) 22050


# 建立一個新的圖形，設定其大小為 14x5 英吋
plt.figure(figsize=(14, 5))

# 使用 librosa.display 的 waveplot 函數繪製音訊波形
# x 是音訊數據，sr 是音訊的取樣率
librosa.display.waveshow(x, sr=sr, color='b')

# 顯示圖形
plt.show()