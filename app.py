import os
from dotenv import load_dotenv
import streamlit as st
from src.fetcher import get_exchange_data
from src.engine import calculate_volatility
from src.agent import generate_report

# This is the magic command that loads your .env file
load_dotenv()

# 1. Setup the Page Title
st.set_page_config(page_title="Macro-Agent Analyst", layout="wide")
st.title("🤖 Macro-Agent: Currency Volatility Analyst")
st.markdown("Professional-grade econometric insights powered by AI.")

# 2. The Sidebar (The Control Panel)
st.sidebar.header("Settings")
ticker = st.sidebar.selectbox("Select Currency Pair", ["USDINR=X", "EURUSD=X", "GBPUSD=X"])

# 3. The 'Action' Button
if st.button("Run Analysis"):
    with st.spinner("Robot is thinking..."):
        # STEP 1: EARS (Fetch)
        prices = get_exchange_data(ticker)
        
        # STEP 2: BRAIN (Math)
        vol = calculate_volatility(prices)
        current_vol = vol.iloc[-1]
        current_price = prices.iloc[-1]
        
        # STEP 3: FACE (Charts)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Price", f"{float(current_price):.2f}")
            st.line_chart(prices.tail(30)) # Show the last month
        with col2:
            st.metric("Annualized Volatility", f"{float(current_vol)*100:.2f}%")
            st.line_chart(vol.tail(30)) # Show the wiggle history
            
        # STEP 4: MOUTH (AI Report)
        st.subheader("AI Analyst Report")
        # Pass the ticker name as the third argument!
        report = generate_report(current_vol, current_price, ticker) 
        st.write(report)
        