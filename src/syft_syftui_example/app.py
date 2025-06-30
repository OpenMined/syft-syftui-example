"""
Main application entry point for SyftUI Example
"""

import sys
from loguru import logger
from .cron import SimpleCron


def main():
    """Main application entry point."""
    logger.info("🚀 Starting SyftUI Example application")
    
    if len(sys.argv) > 1 and sys.argv[1] == "cron":
        # Run cron job
        cron = SimpleCron(interval=10)
        cron.start()
    else:
        # Default: show help
        print("SyftUI Example - Minimal SyftUI application")
        print()
        print("Usage:")
        print("  syft-syftui-example cron    - Run the cron job component")
        print("  just dev                     - Run full development server")
        print("  just backend                 - Run backend only")
        print("  just frontend                - Run frontend only")
        print()
        print("Visit: http://localhost:3000")


if __name__ == "__main__":
    main() 