"""LangGraph graph definition."""

import os
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AIMessage
from agent.state import AgentState
from agent.nodes import agent_node, input_node
from agent.tools import TOOLS


def get_llm():
    """Get the LLM instance based on environment configuration."""
    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "bedrock":
        from langchain_aws import ChatBedrock
        return ChatBedrock(
            model_id=os.getenv("MODEL_ID", "anthropic.claude-3-sonnet-20240229-v1:0"),
            region_name=os.getenv("AWS_REGION", "us-east-1"),
        ).bind_tools(TOOLS)
    else:
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(
            model=os.getenv("MODEL_ID", "gpt-4o-mini"),
            api_key=os.getenv("MODEL_API_KEY") or os.getenv("LITELLM_API_KEY"),
            base_url=os.getenv("MODEL_BASE_URL"),
        ).bind_tools(TOOLS)


def should_continue(state: AgentState) -> str:
    """Determine if the agent should continue or end."""
    messages = state["messages"]
    last_message = messages[-1]
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"
    return "end"


def build_graph() -> StateGraph:
    """Build and compile the agent graph."""
    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node("input", input_node)
    graph.add_node("agent", agent_node)
    graph.add_node("tools", ToolNode(TOOLS))

    # Add edges
    graph.set_entry_point("input")
    graph.add_edge("input", "agent")
    graph.add_conditional_edges("agent", should_continue, {
        "tools": "tools",
        "end": END,
    })
    graph.add_edge("tools", "agent")

    return graph.compile()
