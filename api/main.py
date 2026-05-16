"""
MRIA FastAPI Backend — Backend-for-frontend serving the agent endpoints.
"""

import os
import json
import asyncio
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

# Google ADK imports
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Import our agent
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from agent.agent import root_agent


# Session management
session_service = InMemorySessionService()
APP_NAME = "mria"
USER_ID = "default_user"

# Create runner
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    print("🚌 MRIA API starting up...")
    yield
    print("🚌 MRIA API shutting down...")


app = FastAPI(
    title="MRIA API",
    description="Matatu Route Intelligence Agent - Backend API",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    message: str
    session_id: Optional[str] = None


class QueryResponse(BaseModel):
    response: str
    session_id: str
    agent_name: str


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "mria-api", "version": "1.0.0"}


@app.post("/api/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
    """Send a query to the MRIA agent and get a response."""
    session_id = request.session_id or f"session_{id(request)}"

    # Create or get session
    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )
    if session is None:
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=session_id,
        )

    # Create user message
    user_message = types.Content(
        role="user",
        parts=[types.Part(text=request.message)]
    )

    # Run agent
    final_response = ""
    agent_name = "MRIAOrchestrator"

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session_id,
        new_message=user_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response = event.content.parts[0].text
                agent_name = event.author or agent_name

    return QueryResponse(
        response=final_response,
        session_id=session_id,
        agent_name=agent_name,
    )


@app.post("/api/stream")
async def stream_query(request: QueryRequest):
    """Stream a query response from the MRIA agent."""
    session_id = request.session_id or f"session_{id(request)}"

    session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=session_id,
    )
    if session is None:
        session = await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=session_id,
        )

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=request.message)]
    )

    async def event_generator():
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=session_id,
            new_message=user_message,
        ):
            event_data = {
                "author": event.author or "system",
                "is_final": event.is_final_response(),
            }
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        event_data["text"] = part.text
                    if part.function_call:
                        event_data["tool_call"] = {
                            "name": part.function_call.name,
                            "args": dict(part.function_call.args) if part.function_call.args else {}
                        }
                    if part.function_response:
                        event_data["tool_response"] = {
                            "name": part.function_response.name,
                        }

            yield f"data: {json.dumps(event_data)}\n\n"

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


@app.post("/api/sms/webhook")
async def sms_webhook(request: Request):
    """Africa's Talking inbound SMS webhook."""
    form_data = await request.form()
    # Process incoming SMS from routers
    sender = form_data.get("from", "")
    message = form_data.get("text", "")
    # In production: store in Firestore, trigger agent wake-up
    print(f"📱 Incoming SMS from {sender}: {message}")
    return {"status": "received"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
