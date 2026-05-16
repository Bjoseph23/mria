# mRai — Matatu Route Intelligence Agent 🚌🇰🇪

mRai (Matatu Route Intelligence Agent) is a multi-agent Nairobi transit assistant that fuses official GTFS route data with real-time SMS crowdsourced intelligence from human "routers" on the ground.

### 🌐 Live Demo: [team-project-tracker-7585858596.europe-west2.run.app](https://team-project-tracker-7585858596.europe-west2.run.app/)
### 📂 GitHub Repository: [github.com/Bjoseph23/mria](https://github.com/Bjoseph23/mria)

---

![MRIA UI Interface](./public/screenshots/mria_interface.png)

## 🌟 The Problem
Navigating Nairobi's matatu network is notoriously difficult for both locals and visitors. While canonical routes exist (Digital Matatus GTFS), real-time conditions like traffic jams ("jam mbaya"), police checks, and matatu shortages frequently make "official" data obsolete. Commuters often rely on word-of-mouth or Twitter (X) reports, which are fragmented and hard to synthesize while on the move.

**MRIA solves this by acting as a smart orchestrator that cross-references structured data with real-time human intelligence.**

## 🧠 Agent Architecture
MRIA is built using a hierarchical multi-agent system powered by **Google ADK** and **Gemini 2.5 Pro**.

### Agents:
1.  **MRIA Orchestrator (Gemini 2.5 Pro):** The root agent that manages the workflow, resolves conflicts between data sources, and synthesizes the final travel plan.
2.  **Intent Parser (Gemini 2.5 Flash):** Fast entity extraction from free-text (extracting origin, destination, and urgency).
3.  **Route Resolver (Gemini 2.5 Pro):** Specialized in querying the **GTFS MCP Server** to build the "canonical skeleton" of the trip.
4.  **Crowd Gatherer (Gemini 2.5 Pro):** Manages the **Africa's Talking SMS** loop, selecting relevant "routers" on the ground and collecting their real-time reports.

### Tools:
*   **GTFS MCP Server:** A FastMCP server wrapping a SQLite database of Nairobi's transit network.
*   **Africa's Talking SMS Tool:** Interface for broadcasting queries to a network of human ground reporters.
*   **Offline Cache (IndexedDB):** Ensures previously viewed routes are accessible even without a data connection.

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js 18+
*   Google Gemini API Key
*   Africa's Talking API Key

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Bjoseph23/mria.git
    cd mria
    ```

2.  **Backend Setup:**
    ```bash
    # Create venv and install deps
    python3 -m venv venv
    source venv/bin/activate
    pip install -r agent/requirements.txt -r api/requirements.txt
    
    # Configure .env
    cp agent/.env.example agent/.env
    # Add your API keys to agent/.env
    
    # Run the API
    export PYTHONPATH=$PYTHONPATH:.
    python3 api/main.py
    ```

3.  **Frontend Setup:**
    ```bash
    cd web
    npm install
    npm run dev
    ```

## 🛠 Technology Stack
*   **Frontend:** Next.js 15 (App Router), CopilotKit, Tailwind CSS, shadcn/ui.
*   **Backend:** FastAPI, Google ADK (Agentic Development Kit).
*   **LLMs:** Gemini 2.5 Pro (Reasoning), Gemini 2.5 Flash (Extraction).
*   **Database:** SQLite (GTFS), Firestore (Crowdsourced data).
*   **Communications:** Africa's Talking SMS API.

## 👥 Team
*   **Brian Joseph** — Lead Architect & AI Engineering

---
*Built for the Google ADK Hackathon / Nairobi Transit Innovation Challenge.*
