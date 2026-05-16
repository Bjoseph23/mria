"""
Cache Tool — Route caching for faster repeat queries.
"""

import time
import json

# In-memory cache (would be Firestore/Redis in production)
_route_cache = {}


def check_cache(origin: str, destination: str) -> dict:
    """Check if a cached route exists for this origin-destination pair.

    Args:
        origin: Starting location
        destination: Ending location

    Returns:
        Cached route data or indication that no cache exists.
    """
    key = f"{origin.lower().strip()}→{destination.lower().strip()}"
    cached = _route_cache.get(key)
    if cached and (time.time() - cached["timestamp"]) < 900:  # 15 min TTL
        return {"cached": True, "route": cached["route"],
                "age_seconds": int(time.time() - cached["timestamp"])}
    return {"cached": False, "message": "No cached route found or cache expired."}


def write_cache(origin: str, destination: str, route: dict, ttl: int = 900) -> dict:
    """Write a route to the cache.

    Args:
        origin: Starting location
        destination: Ending location
        route: The route data to cache
        ttl: Time to live in seconds (default 15 min)

    Returns:
        Confirmation of cache write.
    """
    key = f"{origin.lower().strip()}→{destination.lower().strip()}"
    _route_cache[key] = {"route": route, "timestamp": time.time(), "ttl": ttl}
    return {"cached": True, "key": key, "ttl": ttl}
