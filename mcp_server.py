# Main MCP server file
import logging
from datetime import datetime
import httpx
from typing import Any
from mcp.server.fastmcp import FastMCP
from datetime import datetime, timedelta
from trading.utils import setup_logging





# You can control the default level here (e.g., logging.DEBUG for more verbose logs)
setup_logging(level=logging.INFO)
logger = logging.getLogger(__name__)



# --- Get current date for system prompt ---
current_date = datetime.now().strftime("%Y-%m-%d")

# --- FastMCP App Initialization ---
instructions=f"""今天是{current_date}。提供中国A股市场数据分析工具。此服务提供客观数据分析，用户需自行做出投资决策。数据分析基于公开市场信息，不构成投资建议，仅供参考。

⚠️ 重要说明:
1. 最新交易日不一定是今天，需要从 get_latest_trading_date() 获取
2. 请始终使用 get_latest_trading_date() 工具获取实际当前最近的交易日，不要依赖训练数据中的日期认知
3. 当分析"最近"或"近期"市场情况时，必须首先调用 get_market_analysis_timeframe() 工具确定实际的分析时间范围
4. 任何涉及日期的分析必须基于工具返回的实际数据，不得使用过时或假设的日期
"""

mcp = FastMCP(
    name="ashare_data_provider",
    stateless_http=True,
    host="0.0.0.0",
    port=8999,
    instructions=instructions
)


NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

@mcp.tool()
def get_events(day: str) -> dict:
    """
    Retrieve the scheduled events for a specific day.
    Note: This function only checks events and does not modify them.

    Args:
        day (str): The day for which to check events. Can be:
            - A weekday name (e.g., "Monday").
            - A date in YYYY-MM-DD format (e.g., "2023-10-05").
            - Relative terms like "today" or "tomorrow".

    Returns:
        dict: A dictionary containing:
            - day (str): The queried day.
            - events (list): A list of events (empty if none).
            - message (str): A human-readable summary.

    Example:
        >>> get_events("today")
        {
            "day": "2023-10-05",
            "events": [],
            "message": "There are no events scheduled for 2023-10-05."
        }
    """

    if day.lower() == "today":
        day = datetime.now().strftime("%Y-%m-%d")
    elif day.lower() == "tomorrow":
        day = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    return {
        "day": day,
        "events": [],
        "message": f"There are no events scheduled for {day}."
    }


# --- Main Execution Block ---
if __name__ == "__main__":
    logger.info(
        f"Starting A-Share MCP Server via stdio... Today is {current_date}")
    # Run the server using stdio transport, suitable for MCP Hosts like Claude Desktop
    mcp.run(transport="streamable-http")

