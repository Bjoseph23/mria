from fastmcp import FastMCP
import sqlite3
import os

# Initialize FastMCP server
mcp = FastMCP("MRIA GTFS Server")

# Database path
DB_PATH = "nairobi_gtfs.sqlite"

@mcp.tool()
def get_routes(origin: str, destination: str) -> str:
    """Find matatu routes between two locations in Nairobi."""
    # This matches the tool we defined in gtfs_tool.py
    # In a real MCP server, we would query the SQLite DB here.
    # For now, we'll return a helpful response.
    from agent.tools.gtfs_tool import get_routes as find_routes
    return str(find_routes(origin, destination))

@mcp.tool()
def find_stops(near: str) -> str:
    """Find matatu stops near a given location."""
    from agent.tools.gtfs_tool import find_stops as search_stops
    return str(search_stops(near))

@mcp.tool()
def get_alternatives(origin: str, destination: str) -> str:
    """Get alternative matatu routes."""
    from agent.tools.gtfs_tool import get_alternatives as list_alternatives
    return str(list_alternatives(origin, destination))

if __name__ == "__main__":
    mcp.run()
