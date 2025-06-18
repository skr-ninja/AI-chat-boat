from typing import TypedDict


class State(TypedDict, total=False):
    query: str
    category: str
    sentiment: str
    response: str
