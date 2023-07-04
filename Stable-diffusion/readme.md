# Stable Diffusion 環境構築

## オンライン or オフライン
stable diffusionはオンラインまたは、オフラインで利用できる。

オンラインで利用する場合。
参考：
https://huggingface.co/spaces/stabilityai/stable-diffusion

主にオフラインで利用する場合のメモ。

## Stable Diffusionをローカルで使用する為に必要なスペック
```
デスクトップ型
OS：Windows
CPU：あまり気にしなくてOK
メモリ：16GB以上
GPU（グラボ）：VRAMが12GB以上
```

python のバージョン指定アップ
```
(base) PS C:\Users\mokos> python
Python 3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(base) PS C:\Users\mokos> conda install python=3.10.6
```