"""
Crowd Data — Simulated crowdsourced responses for testing.
Pre-crafted responses that mimic what real matatu routers would report.
"""


# Simulated crowd responses for different route scenarios
SIMULATED_RESPONSES = {
    "kawangware_ruai": [
        {
            "router_id": "R001", "router_name": "Wanjiku M.",
            "timestamp": "2026-05-16T08:15:00+03:00",
            "message": "46 imejaa sana Kawangware. Wacha chukua 33 via Ngong Road to CBD, then 120 to Ruai. Faster now.",
            "translated": "Route 46 is very full at Kawangware. Take route 33 via Ngong Road to CBD, then 120 to Ruai. Faster now.",
            "topics": ["congestion", "alternative_route", "route_46_full"],
            "confidence": 0.9, "source": "direct_observation"
        },
        {
            "router_id": "R002", "router_name": "Otieno K.",
            "timestamp": "2026-05-16T08:12:00+03:00",
            "message": "Ruai side poa. Route 120 express iko Railways, fare ni 100 bob. Avoid Jogoo Road - jam mbaya.",
            "translated": "Ruai side is fine. Route 120 express is at Railways, fare is 100 KSh. Avoid Jogoo Road - bad traffic.",
            "topics": ["fare_update", "traffic_alert", "jogoo_road_jam"],
            "confidence": 0.85, "source": "direct_observation"
        },
        {
            "router_id": "R005", "router_name": "Muthoni W.",
            "timestamp": "2026-05-16T08:10:00+03:00",
            "message": "Kawangware to CBD via 46/56 takes 45min now. Heavy traffic Dagoretti Corner. Better use Valley Road matatu.",
            "translated": "Kawangware to CBD via 46/56 takes 45 minutes now. Heavy traffic at Dagoretti Corner.",
            "topics": ["congestion", "time_estimate", "dagoretti_traffic"],
            "confidence": 0.88, "source": "direct_observation"
        },
        {
            "router_id": "R006", "router_name": "Kamau J.",
            "timestamp": "2026-05-16T08:08:00+03:00",
            "message": "Pipeline-Ruai stretch clear. 120 running well, 15 min intervals. Fare steady at 80-100.",
            "translated": "Pipeline to Ruai stretch is clear. Route 120 running well, 15 min intervals.",
            "topics": ["route_clear", "frequency_update", "fare_update"],
            "confidence": 0.92, "source": "direct_observation"
        }
    ],
    "default": [
        {
            "router_id": "R003", "router_name": "Achieng P.",
            "timestamp": "2026-05-16T08:20:00+03:00",
            "message": "CBD area normal traffic flow. Most matatus running on schedule.",
            "translated": "CBD area has normal traffic flow. Most matatus running on schedule.",
            "topics": ["normal_traffic", "on_schedule"],
            "confidence": 0.8, "source": "general_observation"
        },
        {
            "router_id": "R004", "router_name": "Njoroge D.",
            "timestamp": "2026-05-16T08:18:00+03:00",
            "message": "No major incidents reported. Standard rush hour delays on main corridors.",
            "translated": "No major incidents reported. Standard rush hour delays on main corridors.",
            "topics": ["normal_traffic", "rush_hour"],
            "confidence": 0.75, "source": "general_observation"
        }
    ]
}


def get_simulated_responses(task_id: str) -> list:
    """Get simulated crowd responses for a task.

    Args:
        task_id: The broadcast task ID

    Returns:
        List of simulated router responses.
    """
    # For demo, return Kawangware-Ruai responses as they're the most detailed
    # In production, this would fetch from Firestore based on task_id
    return SIMULATED_RESPONSES.get("kawangware_ruai", SIMULATED_RESPONSES["default"])
