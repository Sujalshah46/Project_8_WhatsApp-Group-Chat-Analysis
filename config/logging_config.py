import logging
import os

def setup_logging(default_level=logging.INFO):
    """Configure local application logging"""
    logging.basicConfig(
        level=default_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log", mode='a')
        ]
    )
