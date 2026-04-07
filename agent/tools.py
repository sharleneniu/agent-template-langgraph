"""Agent tools definition."""

from langchain_core.tools import tool


@tool
def search(query: str) -> str:
    """Search for information. Replace this with your actual search implementation."""
    return f"Search result for: {query}"


@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


# Add your custom tools here
TOOLS = [search, calculator]
