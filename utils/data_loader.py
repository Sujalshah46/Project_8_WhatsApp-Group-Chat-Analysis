import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_dataset(file_path):
    """Load a CSV dataset from the local directory with safety checks."""
    if not os.path.exists(file_path):
        logger.error(f"Dataset path does not exist: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    logger.info(f"Loading dataset from {file_path}")
    return pd.read_csv(file_path)
