import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_price_chart(df, title):
    fig = go.Figure()
    if 'Close' in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.update_layout(title=title, xaxis_title = 'Date', yaxis_title = 'Price')
    return fig

def plot_candlesticks(df, title):
    fig = go.Figure(data=[go.Candlestick(x = df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=title, xaxis_title = 'Date', yaxis_title = 'Price')
    return fig

def plot_technicals(df, title):
    fig = go.Figure()
    if 'Close' in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    for col in ['SMA_50', 'SMA_200']:
        if col in df.columns:
            fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
    fig.update_layout(title=title, xaxis_title = 'Date', yaxis_title = 'Price')
    return fig

def plot_multiline(df, title, y_columns):
    fig = go.Figure()
    for col in y_columns:
        if col in df.columns:
            fig.add_trace(go.Scatter(x=df.index, y=df[col], mode='lines', name=col))
    fig.update_layout(title=title, xaxis_title = 'Date')
    return fig

