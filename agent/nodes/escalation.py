from agent.state import State

def escalate(state: State) -> State:
    """Escalate the query to a human agent due to negative sentiment."""
    return {
        "response": "This query has been escalated to a human agent due to its negative sentiment."
    }

def route_query(state: State) -> str:
    """Route the query based on its sentiment and category."""
    if state["sentiment"] == "Negative":
        return "escalate"
    elif state["category"] == "Technical":
        return "handle_technical"
    elif state["category"] == "Billing":
        return "handle_billing"
    else:
        return "handle_general"
