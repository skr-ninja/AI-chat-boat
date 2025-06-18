import os

import streamlit as st
from agent.workflow import support_app  # ✅ Import your graph here
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv()

# Access OpenAI API key
# Try Streamlit Secrets first, fallback to env vars
api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")

if not api_key:
    st.warning("⚠️ OpenAI API key not found in Streamlit secrets or environment variables.")

st.title("🧠 AI Customer Support Agent")

user_query = st.text_input("Enter your support query")

if user_query:
    result = support_app.invoke({"query": user_query})
    st.write("### Category:", result["category"])
    st.write("### Sentiment:", result["sentiment"])
    st.write("### Response:", result["response"])
