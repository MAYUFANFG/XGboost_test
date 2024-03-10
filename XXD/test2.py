import numpy as np
import wave
import struct

# 音檔參數
n_samples = 44100  # 樣本數 (44.1kHz)
sample_rate = 44100  # 取樣率
duration = 10  # 持續時間 (秒)
freq = 440.0  # 頻率 (Hz)

# 產生音檔
file = wave.open('output.wav', 'w')
file.setparams((1, 2, sample_rate, n_samples, 'NONE', 'not compressed'))

samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * freq / sample_rate)).astype(np.float32).tobytes()

for i in range(n_samples):
    packed_value = struct.pack('h', int(samples[i]))
    file.writeframes(packed_value)

file.close()
