# server.py
from fastmcp import FastMCP
import httpx

mcp = FastMCP("revparts")  # server name shown to clients

@mcp.tool
def lookup_part(sku: str) -> dict:
    """Return basic details for a SKU."""
    # demo logic — replace with your real source
    return {"sku": sku, "name": f"Demo Part {sku}", "price_usd": 42.00}

if __name__ == "__main__":
    # expose an SSE server so remote clients can connect over HTTP
    # (stdio is also supported; SSE is convenient for ACA)
    mcp.run_sse(host="0.0.0.0", port=8080)
