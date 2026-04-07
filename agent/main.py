"""Agent HTTP server entry point."""

import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from agent.graph import build_graph

load_dotenv()

app = FastAPI(title="LangGraph Agent", version="1.0.0")
graph = build_graph()


class InvokeRequest(BaseModel):
    input: str


class InvokeResponse(BaseModel):
    output: str


@app.post("/invoke", response_model=InvokeResponse)
async def invoke(request: InvokeRequest):
    """Invoke the agent with user input."""
    result = graph.invoke({"input": request.input, "messages": []})
    return InvokeResponse(output=result.get("output", ""))


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("AGENT_PORT", "8000"))
    uvicorn.run("agent.main:app", host="0.0.0.0", port=port, reload=True)
