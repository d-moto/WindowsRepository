import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go

# 株式コードを入力するテキストボックスを作成
st.sidebar.title('Enter Ticker Symbol')
ticker = st.sidebar.text_input('Ticker', 'AAPL')

# Yahoo! Finance APIを使用して株式価格データを取得
ticker_data = yf.Ticker(ticker)
df = ticker_data.history(period='1d', start='2021-01-01', end='2022-04-20')

# データを前処理
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
df.index = pd.to_datetime(df.index)
df.columns = ['開始価格', '最高価格', '最安価格', '終値', '出来高']

# ダッシュボードのタイトルを表示
st.title(f'{ticker} 株価分析ダッシュボード')

# 株価データの表示
st.write('株価データ')
st.write(df)

# 終値の折れ線グラフの表示
st.write('終値の折れ線グラフ')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['終値'], mode='lines', name='終値'))
fig.update_layout(
    title='終値の推移',
    xaxis_title='日付',
    yaxis_title='株価'
)
st.plotly_chart(fig)
