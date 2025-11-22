from pathlib import Path
import streamlit as st


st.set_page_config(
    page_title="Stock Prediction App",
    page_icon="😎",
)
st.title("Stock Prediction App")

# Introduction and explanation
st.markdown("""
This app is designed to provide users with insights and predictions on stock prices. 
Utilizing advanced statistical models and real-time data, the app aims to assist users in making informed investment decisions.

## How It Works
1. **Select a stock ticker**: Users can choose from a wide range of stock tickers.
2. **View historical data**: The app fetches historical stock data using YFinance.
3. **Get predictions**: Based on the historical data, the app uses the ARIMA model to forecast future stock prices.
4. **Interactive charts**: Users can visualize both historical and predicted stock prices through interactive Plotly charts.

## Key Features
- Real-time data fetching
- ARIMA forecasting for robust predictions
- Interactive and responsive design for a seamless user experience

Whether you're a seasoned investor or new to the stock market, this app provides valuable insights to enhance your investment strategy.
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Stock Prediction App. All Rights Reserved.")
