
import os
import sys
import logging



# --- Logging Setup ---
def setup_logging(level=logging.INFO):
    """Configures basic logging for the application."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # Optionally silence logs from dependencies if they are too verbose
    # logging.getLogger("mcp").setLevel(logging.WARNING)

# Get a logger instance for this module (optional, but good practice)
logger = logging.getLogger(__name__)

