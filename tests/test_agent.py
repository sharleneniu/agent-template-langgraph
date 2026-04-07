"""Basic agent tests."""

from agent.graph import build_graph


def test_graph_builds():
    """Test that the graph compiles without errors."""
    graph = build_graph()
    assert graph is not None


def test_graph_invoke():
    """Test basic graph invocation (requires LLM API key)."""
    import os
    if not os.getenv("MODEL_API_KEY") and not os.getenv("LITELLM_API_KEY"):
        return  # Skip if no API key

    graph = build_graph()
    result = graph.invoke({"input": "hello", "messages": []})
    assert "output" in result
    assert len(result["output"]) > 0
