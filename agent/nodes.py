"""Agent node implementations."""

from langchain_core.messages import HumanMessage
from agent.state import AgentState


def agent_node(state: AgentState) -> dict:
    """Main agent node that processes messages using the LLM."""
    from agent.graph import get_llm
    llm = get_llm()

    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response], "output": response.content}


def input_node(state: AgentState) -> dict:
    """Process user input into a message."""
    return {"messages": [HumanMessage(content=state["input"])]}
