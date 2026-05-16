"""
RouteResolverAgent — Queries GTFS data and builds route skeletons.
Uses Gemini 2.5 Pro for multi-step reasoning about route options.
"""

from google.adk.agents import Agent
from agent.tools.gtfs_tool import get_routes, find_stops, get_alternatives

route_resolver_agent = Agent(
    name="RouteResolverAgent",
    model="gemini-2.5-flash",
    instruction="""You are a route resolver for MRIA, the Nairobi matatu route assistant.

Your job is to find the best matatu routes between two locations using the GTFS tools.

Process:
1. Use get_routes() to find direct routes between origin and destination
2. If no direct route exists, the tool will also return transfer options
3. Use find_stops() to get details about stops near the origin and destination
4. Use get_alternatives() to find backup routes
5. Compile a comprehensive route skeleton with:
   - Primary recommended route (direct if available)
   - Transfer details if needed (where to alight and re-board)
   - Matatu numbers for each leg
   - Fare estimates
   - Stop sequences

Return the structured route data for the orchestrator to merge with crowd intelligence.
Always include at least one alternative route option.""",
    description="Resolves matatu routes using GTFS data",
    tools=[get_routes, find_stops, get_alternatives],
)
