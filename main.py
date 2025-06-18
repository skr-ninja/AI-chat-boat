from agent.workflow import support_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sample query
query = "My internet connection keeps dropping. Can you help?"
result = support_app.invoke({"query": query})

print(f"Query: {query}")
print(f"Category: {result['category']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Response: {result['response']}")
