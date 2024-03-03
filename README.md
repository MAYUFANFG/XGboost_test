# XGboost_test

# EDA (Exploratory Data Analysis) 探索式資料分析
主要概念是透過數據統計的方式視覺化資料。做EDA的好處可以從各種面向先了解資料的狀況，以利後續的模型分析。

# Pandas **Data Frame** 
### 介紹
>可處理 **雙維度**或**多維度**資料
### 安裝
```
$ pip install pandas
```
### 建立Pandas DataFrame
儲存雙維度的資料
```
my_dataframe = pandas.DataFrame(字典或陣列資料)
```
# 關於特徵標準化
![image](https://github.com/MAYUFANFG/XGboost_test/blob/main/4pW0eRh.jpg)
> 這張圖顯示了兩個等高線圖，代表機器學習中的成本函數 J(θ)。這些圖顯示了不同的參數（θ1 和 θ2）對成本的影響，這些參數與房屋的大小和臥室數量相關。這個圖形很有趣，因為它直觀地解釋了機器學習中的優化和收斂。

>在左邊的圖中，你可以看到一個寬廣的碗狀結構，這表示有許多不同的參數組合可以達到相似的成本。在右邊的圖中，你可以看到一個狹窄的碗狀結構，這表示只有很少的參數組合可以達到最低的成本。
>這兩個圖形都顯示了梯度下降算法的工作原理。在梯度下降中，我們從一個隨機的參數開始，然後逐步調整參數以降低成本函數。這個過程就像是從碗狀結構的邊緣滾下來，最終停在碗的底部，也就是成本函數的最小值。

> 這張圖也說明了為什麼 **特徵縮放（或稱為特徵標準化）** 是重要的。如果特徵的尺度差異很大（例如，一個特徵的範圍是 1 到 10，另一個特徵的範圍是 1 到 10000），那麼成本函數可能會變成一個非常狹窄的碗狀結構。這會使得梯度下降算法需要更多的時間來收斂。通過將所有特徵縮放到相同的尺度（例如，使得所有特徵的平均值為 0，標準差為 1），我們可以使得成本函數變成一個更規則的碗狀結構，從而加速梯度下降的收斂。
#### :star:目的：提高精度
## 特徵標準化做法
* min max normalization：
會將特徵數據按比例縮放到0到1的區間，（或是-1到1）。
* standard deviation normalization：
會將所有特徵數據縮放成平均為0、平方差為1。


資料來源：
1. [Pandas教學]資料分析必懂的Pandas DataFrame處理雙維度資料方法
https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html
2.  [Series - 1] NumPy基礎介紹
https://ithelp.ithome.com.tw/articles/10233646
3. Python pandas和numpy的区别
https://www.cnblogs.com/eroeg/p/16163690.html
4. [Day28]機器學習：特徵標準化！
https://ithelp.ithome.com.tw/articles/10197357

