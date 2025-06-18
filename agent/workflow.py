from langgraph.graph import StateGraph, END
from agent.state import State
from agent.nodes.categorization import categorize
from agent.nodes.sentiment import analyze_sentiment
from agent.nodes.handlers import handle_technical, handle_billing, handle_general
from agent.nodes.escalation import escalate, route_query

# Create the graph
workflow = StateGraph(State)
workflow.add_node("categorize", categorize)
workflow.add_node("analyze_sentiment", analyze_sentiment)
workflow.add_node("handle_technical", handle_technical)
workflow.add_node("handle_billing", handle_billing)
workflow.add_node("handle_general", handle_general)
workflow.add_node("escalate", escalate)

workflow.add_edge("categorize", "analyze_sentiment")
workflow.add_conditional_edges("analyze_sentiment", route_query, {
    "handle_technical": "handle_technical",
    "handle_billing": "handle_billing",
    "handle_general": "handle_general",
    "escalate": "escalate",
})
workflow.add_edge("handle_technical", END)
workflow.add_edge("handle_billing", END)
workflow.add_edge("handle_general", END)
workflow.add_edge("escalate", END)

workflow.set_entry_point("categorize")
support_app = workflow.compile()
