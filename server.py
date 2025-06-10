from auth import MyOAuthServerProvider, get_auth
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    "AxisDirect RAPID API",
    auth_server_provider=MyOAuthServerProvider(),
    auth=get_auth()
)


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    # get the token and fetch user profile; use axisdirect-rapidapi package
    return f"Profile data for user {user_id}"