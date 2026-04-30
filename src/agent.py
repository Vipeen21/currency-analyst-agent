import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# 1. Add 'ticker' as the third argument here:
def generate_report(volatility_score, current_price, ticker):
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview", 
        temperature=0,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    # 2. Change USD/INR to {ticker} here:
    template = """
    You are a world-class Financial Analyst. 
    A math engine has given you the following data for the currency pair {ticker}:
    - Current Price: {price}
    - Annualized Volatility: {vol_score}%
    
    Explain this to an investor in 2 sentences. 
    If volatility is above 15%, tell them to be 'Cautious'.
    If it is below 15%, tell them the market is 'Stable'.
    """

    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    
    return chain.invoke({
        "ticker": ticker, # 3. Pass the ticker variable to the AI here
        "price": current_price, 
        "vol_score": round(volatility_score * 100, 2)
    }).content # (Added .content so it returns clean text instead of the messy JSON!)