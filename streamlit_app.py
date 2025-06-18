import streamlit as st
from agent.workflow import support_app  # ✅ Import your graph here
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("🧠 AI Customer Support Agent")

user_query = st.text_input("Enter your support query")

if user_query:
    result = support_app.invoke({"query": user_query})
    st.write("### Category:", result["category"])
    st.write("### Sentiment:", result["sentiment"])
    st.write("### Response:", result["response"])
