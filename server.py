from auth import MyOAuthServerProvider, get_auth
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from rapidapi_axisdirect import AxisAPIClient

# Create an MCP server
mcp = FastMCP(
    "AxisDirect RAPID API",
    auth_server_provider=MyOAuthServerProvider(),
    auth=get_auth()
)

load_dotenv()


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


def initialize_api(client_id, authorization_key):
    """Initialize the AxisDirect RAPID API connection with the API key"""
    return AxisAPIClient(client_id, authorization_key)

@mcp.tool()
def get_portfolio():
    """
    Get portfolio data from the Axis Direct Rapid API.

    Returns:
        Portfolio data as a dictionary or None if an error occurs.
    """
    try:
        return axis_client.holdings()
    except Exception as e:
        logger.exception(f"Holdings Api failed: {e}")
        return None

def main():
    """Main function to demonstrate API workflow"""
    # Get credentials from environment variables
    client_id = os.environ.get('CLIENT_ID')
    auth_key = os.environ.get('AUTH_KEY')
    
    # Initialize API
    global axis_client
    axis_client = initialize_api(client_id, auth_key)
