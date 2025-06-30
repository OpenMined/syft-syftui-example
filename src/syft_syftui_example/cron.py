"""
Simple cron job component for SyftUI Example
"""

import time
from datetime import datetime
from loguru import logger


class SimpleCron:
    """Simple cron job that logs periodically."""
    
    def __init__(self, interval: int = 10):
        """
        Initialize the cron job.
        
        Args:
            interval: Seconds between executions
        """
        self.interval = interval
        self.running = False
    
    def start(self):
        """Start the cron job."""
        logger.info(f"🔄 Starting SyftUI Example cron job (every {self.interval} seconds)")
        self.running = True
        
        try:
            while self.running:
                self._execute_task()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logger.info("👋 Stopping cron job...")
            self.running = False
    
    def stop(self):
        """Stop the cron job."""
        self.running = False
    
    def _execute_task(self):
        """Execute the periodic task."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"⏰ SyftUI Example cron task executed at {timestamp}")
        
        # Simulate some work
        time.sleep(0.1)
        
        logger.info("✅ Cron task completed")


def main():
    """Run the cron job."""
    cron = SimpleCron(interval=10)
    cron.start()


if __name__ == "__main__":
    main() 