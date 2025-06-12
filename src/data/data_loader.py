"""
Data loading utilities for Last-Mile Delivery Optimization.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Class for loading and generating delivery data."""
    
    def __init__(self):
        """Initialize the DataLoader."""
        logger.info("DataLoader initialized")
    
    def create_sample_data(self):
        """Create sample delivery data for testing."""
        logger.info("Creating sample delivery data...")
        
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Create sample data
        n_deliveries = 1000
        
        data = {
            'delivery_id': [f"D_{i:06d}" for i in range(1, n_deliveries + 1)],
            'route_id': [f"R_{np.random.randint(1, 100):03d}" for _ in range(n_deliveries)],
            'city': np.random.choice(['Berlin', 'Munich', 'Hamburg'], n_deliveries),
            'delivery_success': np.random.choice([True, False], n_deliveries, p=[0.95, 0.05]),
            'delivery_time_minutes': np.random.exponential(15, n_deliveries)
        }
        
        df = pd.DataFrame(data)
        logger.info(f"Created {len(df)} sample delivery records")
        
        return df

def main():
    """Test the DataLoader."""
    loader = DataLoader()
    df = loader.create_sample_data()
    
    print(f"Sample data shape: {df.shape}")
    print(f"Success rate: {df['delivery_success'].mean():.2%}")
    print("\nFirst 5 records:")
    print(df.head())

if __name__ == "__main__":
    main()
