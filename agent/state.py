"""Agent state definition."""

from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[list, add_messages]
    input: str
    output: str
