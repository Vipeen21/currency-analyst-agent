🤖 Macro-Agent: Currency Volatility AnalystMacro-Agent is an end-to-end, AI-powered macroeconomic research platform deployed on Streamlit Cloud. It ingests real-time financial data, computes quantitative risk metrics, and orchestrates an LLM (Large Language Model) to synthesize complex market volatility into actionable investment intelligence.🔗 Live Application | 📂 GitHub Repository🏗️ End-to-End ArchitectureThis project is built using a decoupled, modular architecture mimicking enterprise-grade AI applications.1. Data Ingestion Layer (src/fetcher.py)Tooling: yfinance, pandasProcess: Programmatically queries the Yahoo Finance API to extract 1-year historical daily close prices for major currency pairs (e.g., USD/INR, EUR/USD).Optimization: Squeezes multidimensional DataFrames into clean, 1D Pandas Series for lightweight downstream processing.2. Quantitative Model Core (src/engine.py)Tooling: numpy, pandasProcess: Transforms raw price series into daily logarithmic returns ($R_t = \ln(P_t / P_{t-1})$) to ensure statistical stationarity.Metric Calculation: Computes the Annualized Volatility using a 21-day rolling standard deviation, scaled by the square root of 252 (trading days in a year).3. AI & Orchestration Layer (src/agent.py)Tooling: langchain-google-genai, langchain-coreProcess: Acts as the "Brain" of the application. Uses LangChain PromptTemplates to inject the calculated quantitative metrics (price, volatility) into an engineered prompt context.Inference: Calls the gemini-3-flash-preview model to generate a strictly formatted, human-readable 2-sentence financial report advising investors on market stability (Threshold: 15% volatility).4. Frontend & API Layer (app.py)Tooling: streamlitProcess: Provides a reactive, interactive UI. Handles asynchronous state management (st.spinner), captures user inputs (currency tickers), and visually plots 30-day historical trends and volatility curves.5. Deployment & MonitoringInfrastructure: Streamlit Community CloudSecurity: API keys and environment variables are securely managed via Streamlit Secrets and .env (locally ignored via .gitignore).CI/CD: Continuous deployment pipeline connected directly to the GitHub main branch.🗂️ Project Structurecurrency-analyst-agent/
│
├── src/
│   ├── fetcher.py       # API calls and data extraction
│   ├── engine.py        # Mathematical transformations & quant logic
│   └── agent.py         # LangChain orchestration and LLM prompts
│
├── app.py               # Main Streamlit application and UI
├── requirements.txt     # Dependency management
├── .gitignore           # Git tracking exclusions
└── README.md            # Project documentation
🚀 Local Setup & InstallationTo run this project locally on your machine, follow these steps:1. Clone the repositorygit clone [https://github.com/Vipeen21/currency-analyst-agent.git](https://github.com/Vipeen21/currency-analyst-agent.git)
cd currency-analyst-agent
2. Install dependenciesIt is recommended to use a virtual environment (venv or conda).pip install -r requirements.txt
3. Configure Environment VariablesCreate a .env file in the root directory and add your Google Gemini API Key:GOOGLE_API_KEY="your_api_key_here"
4. Run the Applicationstreamlit run app.py
🤝 ContributingContributions, issues, and feature requests are welcome! Feel free to check the issues page.📄 LicenseThis project is MIT licensed.
