'''
Created on 2022/01/24

@author: mokos
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# データ生成------------------------------------------------------------------------------------------------------------

## 乱数を固定
np.random.seed(seed=1)

## X（年齢）の上限と下限（表示用）
X_min = 4
X_max = 30

## データの個数
X_n = 16

## Xの生成(年齢)
X = 5 + 25 * np.random.rand(X_n)

## 生成パラメータ
Prm_c = [170, 108, 0.2]

## XからTを生成(身長)
T = Prm_c[0] - Prm_c[1] * np.exp(-Prm_c[2] * X) + 4 * np.random.randn(X_n)

## 生成したデータを保存
np.savez('ch5_data.npz', X=X, X_min=X_min, X_max=X_max, X_n=X_n, T=T)

## X,Tを小数点以下2桁で表したものを表示
# print(np.round(X, 2))
# print(np.round(T, 2))

# 関数----------------------------------------------------------------------------------------------------------

## 平均誤差関数の定義
## xは年齢,tは実際の身長,wは直線の式の切片と傾きw[0]が傾き、w[1]が切片
def mse_line(x, t, w):

    ## yは直線の式
    y = w[0] * x + w[1]

    ## 二乗誤差関数
    mse = np.mean((y - t)**2)
    return mse

## パラメータを表示するための関数
def prinPara(a):
    print('----------------------------------------------------------------------------------------------------------')
    print('## parameter information ')
    # print('----------------------------------------------------------------------------------------------------------')
    # print(a)
    print(type(a))
    print(np.shape(a))

## 平均誤差関数の勾配を調べる関数
def dmse_line(x, t, w):
    y = w[0] * x + w[1]
    d_w0 = 2 * np.mean((y - t) * x)
    d_w1 = 2 * np.mean(y - t)
    return d_w0, d_w1

## 勾配法の実装
def fit_line_num(x, t):
    w_init = [10.0, 165.0] ## 初期パラメータ
    alpha = 0.001 ## 学習率
    tau_max = 100000 ## 繰り返しの最大値
    eps = 0.1 ## 繰り返しをやめる勾配の絶対値の閾値
    w_hist = np.zeros([tau_max, 2]) ## パラメータの変化を記録するための配列を作成
    w_hist[0, :] = w_init ## パラメータの初期値を代入
    for tau in range(1, tau_max):
        dmse = dmse_line(x, t, w_hist[tau - 1])
        w_hist[tau, 0] = w_hist[tau - 1, 0] - alpha * dmse[0]
        w_hist[tau, 1] = w_hist[tau - 1, 1] - alpha * dmse[1]
        if max(np.absolute(dmse)) < eps: ## 終了判定
            break

    w0 = w_hist[tau, 0]
    w1 = w_hist[tau, 1]
    w_hist = w_hist[:tau, :]
    return w0, w1, dmse, w_hist

## フィッティング。wの計算結果を実データのグラフへ重ねる。
def show_line(w):
    xb = np.linspace(X_min, X_max, 100)
    y = w[0] * xb + w[1]
    plt.plot(xb, y, color=(.5, .5, .5), linewidth=4)

# 計算------------------------------------------------------------------------------------------------------------------
## 等高線の解像度
xn = 100

## w0とw1の範囲
w0_range = [-25, 25]
w1_range = [120, 170]

## 実際のw0とw1を作成。w0_rangeとw1_rangeを使用して、等間隔に分割。
w0 = np.linspace(w0_range[0], w0_range[1], xn)
w1 = np.linspace(w1_range[0], w1_range[1], xn)

## メッシュグリッドを作成。二次元の配列を作成する。
ww0, ww1 = np.meshgrid(w0, w1)

## 誤差関数 J を定義。要素がすべてゼロのw0行、w1列の行列を作る。
J = np.zeros((len(w0), len(w1)))

## J に上で定義したmse_line関数の値を代入する。
for i0 in range(len(w0)):
    for i1 in range(len(w1)):
        J[i1,i0] = mse_line(X, T, (w0[i0], w1[i1])) ## X=実際の年齢のデータ,T=実際の身長のデータ,

W0, W1, dMSE, W_history = fit_line_num(X, T)
W = np.array([W0, W1])

prinPara(X)
prinPara(T)
prinPara(xn)
prinPara(w0)
prinPara(w1)
prinPara(J)
prinPara(ww0)
prinPara(ww1)
print(' w = [{0:.6f}, {1:.6f}]'.format(W0, W1))
# データグラフの表示----------------------------------------------------------------------------------------------------

## グラフ領域の設定
plt.figure(figsize=(20, 12))
plt.subplots_adjust(wspace=0.5)

## 平均誤差関数のプロット(3D)
ax = plt.subplot(2, 2, 3, projection='3d', facecolor='azure') ## subplotはarg1行、arg2列で、arg3の領域に配置する。
ax.plot_surface(ww0, ww1, J, rstride=10, cstride=10, alpha=0.3, color='blue', edgecolor='black')
ax.set_xticks([-20, 0, 20])
ax.set_yticks([120, 140, 160])
ax.view_init(20, -60)
plt.title('Mean Squared Error J', fontsize=20)
plt.subplots_adjust(hspace=0.6)
plt.grid(True)

## 平均誤差関数の等高線プロット
plt.subplot(2, 2, 4)
cont = plt.contour(ww0, ww1, J, 30, colors='black', levels=[100, 1000, 10000, 100000])
cont.clabel(fmt='%1.0f', fontsize=8)
plt.title('Mean Squared Error Contour Line', fontsize=20)
plt.grid(True)

# 実データのプロット
ax2 = plt.subplot(2, 2, 1)
ax2.scatter(X, T, c='blue')
ax2.set_xlim(X_min, X_max)
ax2.set_xlabel('AGE', fontsize=10)
ax2.set_ylabel('TALL', fontsize=10)
show_line(W)
plt.title('Real Data', fontsize=20)
plt.grid(True)
ax2.set_axisbelow(True)

# wの履歴を等高線に重ねて表示
plt.subplot(2, 2, 4)
cont2 = plt.plot(W_history[:, 0], W_history[:, 1], '.-', color='gray', markersize=10, markeredgecolor='cornflowerblue')
plt.grid(True)

plt.show()
