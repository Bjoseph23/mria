"""
GTFS Tool — Provides Nairobi matatu route data from GTFS feed.

Uses a comprehensive dataset of Nairobi's matatu routes including
route numbers, stops, common transfer points, and fare estimates.
"""

import json
from typing import Optional

# Comprehensive Nairobi matatu route knowledge base
# Based on Digital Matatu GTFS data + local knowledge
NAIROBI_ROUTES = {
    "routes": [
        {
            "route_id": "R001",
            "route_number": "46/56",
            "route_name": "Kawangware - CBD",
            "stops": ["Kawangware", "Dagoretti Corner", "Lavington", "Museum Hill", "CBD (Archives)"],
            "fare_range": "50-80",
            "frequency": "5-10 min peak, 15-20 min off-peak",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R002",
            "route_number": "33/34",
            "route_name": "Kawangware - CBD (via Ngong Road)",
            "stops": ["Kawangware", "Uthiru", "Kinoo", "Ngong Road", "CBD (Kencom)"],
            "fare_range": "50-80",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R003",
            "route_number": "120",
            "route_name": "CBD - Ruai (Superhighway)",
            "stops": ["CBD (Railways)", "Muthurwa", "Donholm", "Pipeline", "Embakasi", "Utawala", "Ruai"],
            "fare_range": "50-100",
            "frequency": "10-15 min",
            "operating_hours": "5:00 AM - 9:30 PM"
        },
        {
            "route_id": "R004",
            "route_number": "33",
            "route_name": "CBD - Ruai (via Jogoo Road)",
            "stops": ["CBD (Bus Station)", "Makadara", "Hamza", "Donholm", "Savannah", "Embakasi", "Ruai"],
            "fare_range": "50-100",
            "frequency": "10-15 min",
            "operating_hours": "5:00 AM - 9:00 PM"
        },
        {
            "route_id": "R005",
            "route_number": "58",
            "route_name": "CBD - Eastleigh",
            "stops": ["CBD (OTC)", "Pangani", "Eastleigh Section I", "Eastleigh Section III", "California"],
            "fare_range": "30-50",
            "frequency": "5-10 min",
            "operating_hours": "5:30 AM - 10:00 PM"
        },
        {
            "route_id": "R006",
            "route_number": "23/25",
            "route_name": "CBD - Westlands - Rongai",
            "stops": ["CBD (Kencom)", "University Way", "Westlands", "Kangemi", "Kikuyu", "Rongai"],
            "fare_range": "30-150",
            "frequency": "5-15 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R007",
            "route_number": "44/45",
            "route_name": "CBD - Ngong",
            "stops": ["CBD (Railways)", "Uhuru Highway", "Karen", "Ngong"],
            "fare_range": "80-150",
            "frequency": "15-20 min",
            "operating_hours": "5:30 AM - 8:30 PM"
        },
        {
            "route_id": "R008",
            "route_number": "11/11B",
            "route_name": "CBD - Buruburu",
            "stops": ["CBD (Bus Station)", "Jogoo Road", "Buruburu Phase 1", "Buruburu Phase 5"],
            "fare_range": "30-50",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R009",
            "route_number": "125/126",
            "route_name": "CBD - Kitengela",
            "stops": ["CBD (Railways)", "South B", "South C", "Syokimau", "Mlolongo", "Athi River", "Kitengela"],
            "fare_range": "80-200",
            "frequency": "15-30 min",
            "operating_hours": "5:00 AM - 9:00 PM"
        },
        {
            "route_id": "R010",
            "route_number": "111/112",
            "route_name": "CBD - Thika (Thika Superhighway)",
            "stops": ["CBD (OTC)", "Pangani", "Muthaiga", "Kasarani", "Githurai", "Ruiru", "Juja", "Thika"],
            "fare_range": "50-200",
            "frequency": "5-15 min",
            "operating_hours": "4:30 AM - 10:00 PM"
        },
        {
            "route_id": "R011",
            "route_number": "14/15",
            "route_name": "CBD - Langata - Karen",
            "stops": ["CBD (Railways)", "Uhuru Gardens", "Langata", "Wilson Airport", "Karen"],
            "fare_range": "50-100",
            "frequency": "10-15 min",
            "operating_hours": "5:30 AM - 9:00 PM"
        },
        {
            "route_id": "R012",
            "route_number": "9/9A",
            "route_name": "CBD - South B - South C",
            "stops": ["CBD (Bus Station)", "Nyayo Stadium", "South B", "South C", "Nairobi West"],
            "fare_range": "30-50",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R013",
            "route_number": "100/101",
            "route_name": "CBD - Githurai 45",
            "stops": ["CBD (OTC)", "Pangani", "Roysambu", "Kahawa West", "Githurai 45"],
            "fare_range": "50-80",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R014",
            "route_number": "6/6A",
            "route_name": "CBD - Umoja",
            "stops": ["CBD (Bus Station)", "Jogoo Road", "Donholm", "Umoja I", "Umoja II"],
            "fare_range": "30-60",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 10:00 PM"
        },
        {
            "route_id": "R015",
            "route_number": "17/17B",
            "route_name": "CBD - Dandora",
            "stops": ["CBD (Bus Station)", "Huruma", "Kariobangi", "Dandora Phase 1", "Dandora Phase 4"],
            "fare_range": "30-60",
            "frequency": "5-10 min",
            "operating_hours": "5:00 AM - 9:30 PM"
        }
    ],
    "transfer_points": {
        "CBD (Archives)": ["R001", "R003", "R006"],
        "CBD (Bus Station)": ["R004", "R008", "R012", "R014", "R015"],
        "CBD (Railways)": ["R003", "R007", "R009", "R011"],
        "CBD (OTC)": ["R005", "R010", "R013"],
        "CBD (Kencom)": ["R002", "R006"],
        "Donholm": ["R003", "R004", "R014"],
        "Embakasi": ["R003", "R004"],
        "Pangani": ["R005", "R010", "R013"]
    },
    "areas": {
        "Kawangware": {"zone": "West", "connected_routes": ["R001", "R002"]},
        "Ruai": {"zone": "East", "connected_routes": ["R003", "R004"]},
        "Westlands": {"zone": "West", "connected_routes": ["R006"]},
        "Eastleigh": {"zone": "East-Central", "connected_routes": ["R005"]},
        "Langata": {"zone": "South", "connected_routes": ["R011"]},
        "Karen": {"zone": "South-West", "connected_routes": ["R007", "R011"]},
        "Thika": {"zone": "North-East", "connected_routes": ["R010"]},
        "Kitengela": {"zone": "South", "connected_routes": ["R009"]},
        "Buruburu": {"zone": "East", "connected_routes": ["R008"]},
        "South B": {"zone": "South-Central", "connected_routes": ["R009", "R012"]},
        "South C": {"zone": "South-Central", "connected_routes": ["R009", "R012"]},
        "Githurai": {"zone": "North-East", "connected_routes": ["R010", "R013"]},
        "Dandora": {"zone": "East", "connected_routes": ["R015"]},
        "Umoja": {"zone": "East", "connected_routes": ["R014"]},
        "Rongai": {"zone": "South-West", "connected_routes": ["R006"]},
        "Ngong": {"zone": "South-West", "connected_routes": ["R007"]},
        "Donholm": {"zone": "East", "connected_routes": ["R003", "R004", "R014"]},
        "Embakasi": {"zone": "East", "connected_routes": ["R003", "R004"]},
        "CBD": {"zone": "Central", "connected_routes": ["R001", "R002", "R003", "R004", "R005", "R006", "R007", "R008", "R009", "R010", "R011", "R012", "R013", "R014", "R015"]},
    }
}


def get_routes(origin: str, destination: str) -> dict:
    """
    Find matatu routes between two locations in Nairobi.

    Args:
        origin: The starting location (e.g., "Kawangware", "CBD")
        destination: The ending location (e.g., "Ruai", "Westlands")

    Returns:
        A dictionary with direct routes and transfer routes between origin and destination.
    """
    origin_lower = origin.lower().strip()
    dest_lower = destination.lower().strip()

    # Normalize area names
    area_map = {k.lower(): k for k in NAIROBI_ROUTES["areas"].keys()}
    origin_key = area_map.get(origin_lower, origin)
    dest_key = area_map.get(dest_lower, destination)

    origin_info = NAIROBI_ROUTES["areas"].get(origin_key)
    dest_info = NAIROBI_ROUTES["areas"].get(dest_key)

    if not origin_info:
        return {"error": f"Unknown location: {origin}. Known areas: {list(NAIROBI_ROUTES['areas'].keys())}"}
    if not dest_info:
        return {"error": f"Unknown location: {destination}. Known areas: {list(NAIROBI_ROUTES['areas'].keys())}"}

    origin_routes = set(origin_info["connected_routes"])
    dest_routes = set(dest_info["connected_routes"])

    # Find direct routes
    direct = origin_routes & dest_routes
    direct_routes = []
    for route_id in direct:
        route = next(r for r in NAIROBI_ROUTES["routes"] if r["route_id"] == route_id)
        direct_routes.append(route)

    # Find transfer routes if no direct route
    transfer_routes = []
    if not direct_routes:
        for transfer_point, transfer_route_ids in NAIROBI_ROUTES["transfer_points"].items():
            transfer_set = set(transfer_route_ids)
            leg1_routes = origin_routes & transfer_set
            leg2_routes = dest_routes & transfer_set
            if leg1_routes and leg2_routes:
                for l1_id in leg1_routes:
                    for l2_id in leg2_routes:
                        if l1_id != l2_id:
                            l1 = next(r for r in NAIROBI_ROUTES["routes"] if r["route_id"] == l1_id)
                            l2 = next(r for r in NAIROBI_ROUTES["routes"] if r["route_id"] == l2_id)
                            transfer_routes.append({
                                "transfer_point": transfer_point,
                                "leg1": l1,
                                "leg2": l2,
                                "total_fare_estimate": f"{int(l1['fare_range'].split('-')[0]) + int(l2['fare_range'].split('-')[0])}-{int(l1['fare_range'].split('-')[1]) + int(l2['fare_range'].split('-')[1])}"
                            })

    return {
        "origin": origin_key,
        "destination": dest_key,
        "direct_routes": direct_routes,
        "transfer_routes": transfer_routes[:5],  # Limit to top 5 transfer options
        "total_options": len(direct_routes) + len(transfer_routes)
    }


def find_stops(near: str) -> dict:
    """
    Find matatu stops near a given location in Nairobi.

    Args:
        near: The location to search near (e.g., "Kawangware", "CBD")

    Returns:
        A dictionary with nearby stops and available routes.
    """
    near_lower = near.lower().strip()
    area_map = {k.lower(): k for k in NAIROBI_ROUTES["areas"].keys()}
    area_key = area_map.get(near_lower)

    if not area_key:
        # Search in route stops
        matching_routes = []
        for route in NAIROBI_ROUTES["routes"]:
            for stop in route["stops"]:
                if near_lower in stop.lower():
                    matching_routes.append({
                        "stop_name": stop,
                        "route": route
                    })
        if matching_routes:
            return {"location": near, "nearby_stops": matching_routes}
        return {"error": f"No stops found near '{near}'. Try: {list(NAIROBI_ROUTES['areas'].keys())}"}

    area_info = NAIROBI_ROUTES["areas"][area_key]
    routes = []
    for route_id in area_info["connected_routes"]:
        route = next(r for r in NAIROBI_ROUTES["routes"] if r["route_id"] == route_id)
        routes.append(route)

    return {
        "location": area_key,
        "zone": area_info["zone"],
        "available_routes": routes,
        "total_routes": len(routes)
    }


def get_alternatives(origin: str, destination: str) -> dict:
    """
    Get alternative matatu routes between two locations, considering transfers.

    Args:
        origin: The starting location
        destination: The ending location

    Returns:
        A dictionary with alternative routes ranked by preference.
    """
    primary = get_routes(origin, destination)
    if "error" in primary:
        return primary

    alternatives = []

    # Add direct routes as top alternatives
    for route in primary.get("direct_routes", []):
        alternatives.append({
            "type": "direct",
            "route": route,
            "estimated_time": "30-60 min",
            "comfort": "standard",
            "recommendation": "Best option - direct route"
        })

    # Add transfer routes as secondary alternatives
    for transfer in primary.get("transfer_routes", []):
        alternatives.append({
            "type": "transfer",
            "leg1_route": transfer["leg1"],
            "transfer_point": transfer["transfer_point"],
            "leg2_route": transfer["leg2"],
            "total_fare": transfer["total_fare_estimate"],
            "estimated_time": "60-90 min",
            "comfort": "requires walking between stages",
            "recommendation": "Alternative option - requires transfer"
        })

    return {
        "origin": primary["origin"],
        "destination": primary["destination"],
        "alternatives": alternatives,
        "total_alternatives": len(alternatives)
    }
