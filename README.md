# 用CNN圖形辨識

## Table of Contents
	- 讀入 MNIST 數據庫
	- 打造CNN
	- 訓練CNN
	- 結果測試
	- 進行圖形辨識
  
## 讀入 MNIST 數據庫
	- 由 Keras 讀入 MNIST
	- 將測試資料和訓練資料匯入
from keras.datasets import mnist

## 打造CNN
	- 決定神經網路架構、讀入相關套件，然後組裝
打開個空白的神經網路
設成 same 是每個 filter 會輸出原來 28x28 一樣大小的矩陣。

然後Max-Pooling後再Convolution三次
![image](https://user-images.githubusercontent.com/91310381/209751055-0d2e22fe-4a36-4471-b915-eca6312b39c9.png)

然後開始組裝
![image](https://user-images.githubusercontent.com/91310381/209751180-d62b4a84-c0b7-49e9-9163-16b225058a6f.png)
檢視神經網路
![image](https://user-images.githubusercontent.com/91310381/209751233-0c7d4026-233c-4693-954a-47954e0f5534.png)


## 訓練CNN
	- 開始對此進行測試
	
![image](https://user-images.githubusercontent.com/91310381/209751350-6ff9292e-3c62-4d76-8808-a22ea32783b5.png)
	
## 結果測試
	- 看測試資料的正確率
	
![image](https://user-images.githubusercontent.com/91310381/209751413-4efb9997-086b-45bb-9a1b-234c7be930aa.png)

測試資料的 loss: 0.01919
測試資料的正確率: 0.8677999973297119

儲存結果

![image](https://user-images.githubusercontent.com/91310381/209751569-1fce794e-aa1d-4a1a-82af-c5951513288a.png)

## 進行圖形辨識
	- 最後進行實地操作，使用匯入的1萬筆資料中選5個讓其辨識
	
![你娘](https://user-images.githubusercontent.com/91310381/209751871-590ccfb3-ea5e-43bf-a175-36cac94fd1bf.PNG)


	
  <!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
