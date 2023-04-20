import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 株式コードのリストを作成
tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'FB']

# ドロップダウンメニューを作成
st.sidebar.title('Select Ticker Symbol')
ticker = st.sidebar.selectbox('Ticker', tickers)

# 開始日と終了日のデフォルト値を設定
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# ユーザーが選択した日付を取得
start_date = st.sidebar.date_input('Start Date', start_date)
end_date = st.sidebar.date_input('End Date', end_date)

# 開始日と終了日の範囲をチェック
if start_date >= end_date:
    st.error('エラー：開始日が終了日よりも後に設定されています。')
else:
    # Yahoo! Finance APIを使用して株式価格データを取得
    ticker_data = yf.Ticker(ticker)
    df = ticker_data.history(period='1d', start=start_date, end=end_date)

    # データを前処理
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.index = pd.to_datetime(df.index)
    df.columns = ['開始価格', '最高価格', '最安価格', '終値', '出来高']

    # ダッシュボードのタイトルを表示
    st.title(f'{ticker} 株価分析ダッシュボード')

    # 株価データの表示
    st.write('株価データ')
    st.dataframe(df.style.background_gradient(cmap='Blues', axis=None, subset=['開始価格', '最高価格', '最安価格', '終値']).format({'出来高': '{:,.0f}'}))

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
