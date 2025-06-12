import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_logistics_database():
    """Create a realistic logistics database like Bettermile uses."""
    
    # Connect to database
    conn = sqlite3.connect('data/logistics.db')
    
    # Create routes table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS routes (
            route_id TEXT PRIMARY KEY,
            driver_id TEXT,
            vehicle_id TEXT,
            route_date DATE,
            planned_stops INTEGER,
            actual_stops INTEGER,
            planned_duration_min INTEGER,
            actual_duration_min INTEGER,
            total_distance_km REAL,
            fuel_cost_euros REAL,
            driver_cost_euros REAL,
            total_revenue_euros REAL
        )
    ''')
    
    # Create deliveries table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS deliveries (
            delivery_id TEXT PRIMARY KEY,
            route_id TEXT,
            stop_sequence INTEGER,
            customer_id TEXT,
            city TEXT,
            delivery_time_slot TEXT,
            planned_delivery_time TEXT,
            actual_delivery_time TEXT,
            delivery_status TEXT,
            package_weight_kg REAL,
            package_value_euros REAL,
            delivery_cost_euros REAL,
            FOREIGN KEY (route_id) REFERENCES routes (route_id)
        )
    ''')
    
    print("✅ Logistics database created!")
    conn.close()

if __name__ == "__main__":
    create_logistics_database()

