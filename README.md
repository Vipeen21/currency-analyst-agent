[![GitHub followers](https://img.shields.io/github/followers/Vipeen21?style=for-the-badge&color=21262d&labelColor=161b22&logo=github)](https://github.com/Vipeen21)
[![GitHub stars](https://img.shields.io/github/stars/Vipeen21/currency-analyst-agent?style=for-the-badge&color=e3b341&labelColor=161b22&logo=github)](https://github.com/Vipeen21/currency-analyst-agent/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Vipeen21/currency-analyst-agent?style=for-the-badge&color=58a6ff&labelColor=161b22&logo=github)](https://github.com/Vipeen21/currency-analyst-agent/network/members)
[![GitHub license](https://img.shields.io/github/license/Vipeen21/currency-analyst-agent?style=for-the-badge&color=30a14e&labelColor=161b22)](https://github.com/Vipeen21/currency-analyst-agent/blob/main/LICENSE)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=chainlink&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat-square&logo=google-gemini&logoColor=white" alt="Google Gemini API">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">
</p>



# 🤖 Macro-Agent: Currency Volatility Analyst

An end-to-end AI-powered financial agent designed to monitor exchange rate volatility, perform econometric calculations, and generate real-time, actionable market intelligence. 

This project bridges quantitative finance and Generative AI, utilizing a Python-based quantitative engine for data processing and a LangChain-orchestrated LLM for natural language reporting.

---

## 🏗️ System Architecture & Deployment Scheme

The application follows a modular, end-to-end machine learning operational flow:

### 1. Data Ingestion (`src/fetcher.py`)
*   **Source**: Yahoo Finance API via the `yfinance` library[cite: 6].
*   **Process**: Fetches 1-year historical daily close prices for target currency pairs (e.g., USD/INR, EUR/USD, GBP/USD)[cite: 6]. 

### 2. Model Core: Quantitative Engine (`src/engine.py`)
*   **Process**: Computes daily logarithmic returns to normalize price movements[cite: 5].
*   **Mathematics**: Calculates annualized historical volatility using a 21-day rolling window[cite: 5]. The mathematical core relies on `numpy` and `pandas`[cite: 2], executing the following:
    $$R_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$
    $$\sigma_{annual} = \text{std}(R_{t-21:t}) \times \sqrt{252}$$

### 3. AI Orchestration & API Layer (`src/agent.py`)
*   **Framework**: Built using `langchain-core` and `langchain-google-genai`[cite: 2].
*   **LLM Integration**: Utilizes Google's `gemini-3-flash-preview` model via API[cite: 4].
*   **Prompt Engineering**: Injects the quantitative outputs (current price, calculated volatility score) and the specific ticker into a structured PromptTemplate[cite: 4]. The agent dynamically classifies the market as 'Cautious' (volatility > 15%) or 'Stable' (< 15%) to generate a concise, 2-sentence investor briefing[cite: 4].

### 4. Frontend & Orchestration (`app.py`)
*   **Framework**: Streamlit[cite: 3].
*   **UI/UX**: Provides an interactive dashboard with dynamic metric tracking, temporal line charts for both price and volatility (trailing 30 days), and the AI-generated report[cite: 3].

### 5. Deployment & Environment Strategy
*   **Environment**: The repository includes a `.devcontainer` configuration, ensuring consistent, containerized local development environments[cite: 1].
*   **Secrets Management**: Securely loads API credentials using `python-dotenv`[cite: 3].
*   **Production Deployment**: The app is container-ready and optimized for deployment on Streamlit Community Cloud, HuggingFace Spaces, or AWS EC2/ECS. 

### 6. Monitoring (Future Scope)
*   **LLM Observability**: Integration with LangSmith to trace prompt execution, monitor token latency, and debug the LangChain pipeline.
*   **Data Drift**: Tracking deviations in the rolling volatility distribution.

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/currency-analyst-agent.git](https://github.com/yourusername/currency-analyst-agent.git)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Configure Environment:**  
Create a `.env` file in the root directory and add your Google API key:
   ```Plaintext
   GOOGLE_API_KEY=your_api_key_here
   
5. **Run the Application:**

    ```bash
    streamlit run app.py

