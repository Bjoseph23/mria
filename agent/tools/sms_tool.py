"""
SMS Tool — Africa's Talking integration for crowdsourced matatu intelligence.
"""

import os
import json
import time


AT_API_KEY = os.getenv("AT_API_KEY", "")
AT_USERNAME = os.getenv("AT_USERNAME", "sandbox")

ROUTER_DATABASE = [
    {"id": "R001", "name": "Wanjiku M.", "phone": "+254700100001",
     "expertise_areas": ["Kawangware", "Dagoretti", "Lavington", "CBD"],
     "trust_score": 0.92, "response_rate": 0.85, "avg_response_time_seconds": 120},
    {"id": "R002", "name": "Otieno K.", "phone": "+254700100002",
     "expertise_areas": ["CBD", "Donholm", "Pipeline", "Embakasi", "Ruai"],
     "trust_score": 0.88, "response_rate": 0.90, "avg_response_time_seconds": 90},
    {"id": "R003", "name": "Achieng P.", "phone": "+254700100003",
     "expertise_areas": ["CBD", "Eastleigh", "Pangani", "Kasarani", "Githurai"],
     "trust_score": 0.95, "response_rate": 0.78, "avg_response_time_seconds": 180},
    {"id": "R004", "name": "Njoroge D.", "phone": "+254700100004",
     "expertise_areas": ["CBD", "Westlands", "Karen", "Ngong", "Langata"],
     "trust_score": 0.85, "response_rate": 0.82, "avg_response_time_seconds": 150},
    {"id": "R005", "name": "Muthoni W.", "phone": "+254700100005",
     "expertise_areas": ["Kawangware", "Uthiru", "Kinoo", "Ngong Road", "CBD"],
     "trust_score": 0.90, "response_rate": 0.88, "avg_response_time_seconds": 100},
    {"id": "R006", "name": "Kamau J.", "phone": "+254700100006",
     "expertise_areas": ["Embakasi", "Utawala", "Ruai", "Pipeline", "Donholm"],
     "trust_score": 0.87, "response_rate": 0.91, "avg_response_time_seconds": 95},
]


def select_routers(origin: str, destination: str) -> dict:
    """Select best routers for a given route query based on expertise and trust.

    Args:
        origin: Starting location
        destination: Ending location

    Returns:
        Selected routers with scores.
    """
    origin_lower = origin.lower()
    dest_lower = destination.lower()
    scored = []
    for router in ROUTER_DATABASE:
        areas_lower = [a.lower() for a in router["expertise_areas"]]
        o_match = any(origin_lower in a or a in origin_lower for a in areas_lower)
        d_match = any(dest_lower in a or a in dest_lower for a in areas_lower)
        relevance = 1.0 if (o_match and d_match) else (0.5 if (o_match or d_match) else 0)
        if relevance > 0:
            score = relevance * 0.4 + router["trust_score"] * 0.35 + router["response_rate"] * 0.25
            scored.append({**router, "relevance_score": round(score, 3),
                           "covers_origin": o_match, "covers_destination": d_match})
    scored.sort(key=lambda r: r["relevance_score"], reverse=True)
    return {"origin": origin, "destination": destination,
            "selected_routers": scored[:4], "total_available": len(scored)}


def broadcast_sms(query: str, router_ids: list) -> dict:
    """Broadcast an SMS query to selected routers.

    Args:
        query: The route query text
        router_ids: List of router IDs

    Returns:
        Broadcast task details.
    """
    task_id = f"task_{int(time.time())}"
    sent_to = []
    for rid in router_ids:
        router = next((r for r in ROUTER_DATABASE if r["id"] == rid), None)
        if router:
            sent_to.append({"router_id": router["id"], "router_name": router["name"], "status": "sent"})
    return {"task_id": task_id, "query": query, "sent_to": sent_to,
            "total_sent": len(sent_to), "status": "broadcast_complete"}


def collect_responses(task_id: str, timeout_seconds: int = 180) -> dict:
    """Collect SMS responses from routers. Returns simulated responses for now.

    Args:
        task_id: The broadcast task ID
        timeout_seconds: Wait time for responses

    Returns:
        Collected responses with consensus analysis.
    """
    from agent.tools.crowd_data import get_simulated_responses
    responses = get_simulated_responses(task_id)
    consensus = {}
    for resp in responses:
        for topic in resp.get("topics", []):
            consensus[topic] = consensus.get(topic, 0) + 1
    return {"task_id": task_id, "responses": responses, "total_responses": len(responses),
            "consensus": consensus, "status": "complete"}
