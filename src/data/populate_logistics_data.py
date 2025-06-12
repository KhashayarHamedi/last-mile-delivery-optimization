import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def populate_logistics_data():
    """Populate database with realistic logistics data."""
    
    conn = sqlite3.connect('data/logistics.db')
    np.random.seed(42)
    
    # Generate realistic routes data (like Bettermile would have)
    routes_data = []
    for i in range(500):  # 500 routes over 3 months
        route_date = datetime(2025, 3, 1) + timedelta(days=np.random.randint(0, 90))
        planned_stops = np.random.randint(8, 45)
        
        # Realistic delivery efficiency (some routes have failed stops)
        actual_stops = max(1, planned_stops - np.random.binomial(planned_stops, 0.05))
        
        # Time and cost calculations
        planned_duration = planned_stops * 15 + np.random.randint(60, 180)  # 15min per stop + travel
        actual_duration = planned_duration + np.random.randint(-30, 120)  # delays happen
        distance = planned_stops * 2.5 + np.random.exponential(20)  # km
        
        routes_data.append({
            'route_id': f'R_{i+1:04d}',
            'driver_id': f'DRV_{np.random.randint(1, 50):03d}',
            'vehicle_id': f'VEH_{np.random.randint(1, 25):03d}',
            'route_date': route_date.strftime('%Y-%m-%d'),
            'planned_stops': planned_stops,
            'actual_stops': actual_stops,
            'planned_duration_min': planned_duration,
            'actual_duration_min': max(30, actual_duration),
            'total_distance_km': round(distance, 1),
            'fuel_cost_euros': round(distance * 0.15, 2),  # €0.15 per km
            'driver_cost_euros': round((actual_duration / 60) * 25, 2),  # €25 per hour
            'total_revenue_euros': round(actual_stops * 8.50, 2)  # €8.50 per delivery
        })
    
    # Insert routes
    routes_df = pd.DataFrame(routes_data)
    routes_df.to_sql('routes', conn, if_exists='replace', index=False)
    
    # Generate deliveries for each route
    deliveries_data = []
    delivery_counter = 1
    
    for _, route in routes_df.iterrows():
        for stop in range(1, route['actual_stops'] + 1):
            # Random delivery outcomes
            status = np.random.choice(['delivered', 'failed', 'rescheduled'], 
                                    p=[0.92, 0.05, 0.03])
            
            deliveries_data.append({
                'delivery_id': f'D_{delivery_counter:06d}',
                'route_id': route['route_id'],
                'stop_sequence': stop,
                'customer_id': f'CUST_{np.random.randint(1000, 9999)}',
                'city': np.random.choice(['Berlin', 'Munich', 'Hamburg', 'Cologne', 'Frankfurt']),
                'delivery_time_slot': np.random.choice(['09:00-12:00', '12:00-15:00', '15:00-18:00']),
                'planned_delivery_time': '14:30',  # Simplified
                'actual_delivery_time': '14:45' if status == 'delivered' else None,
                'delivery_status': status,
                'package_weight_kg': round(np.random.exponential(2.5), 1),
                'package_value_euros': round(np.random.exponential(50) + 20, 2),
                'delivery_cost_euros': 8.50 if status == 'delivered' else 12.00  # Failed deliveries cost more
            })
            delivery_counter += 1
    
    # Insert deliveries
    deliveries_df = pd.DataFrame(deliveries_data)
    deliveries_df.to_sql('deliveries', conn, if_exists='replace', index=False)
    
    print(f"✅ Database populated with:")
    print(f"   • {len(routes_df)} routes")
    print(f"   • {len(deliveries_df)} deliveries")
    print(f"   • Success rate: {(deliveries_df['delivery_status'] == 'delivered').mean():.1%}")
    
    conn.close()

if __name__ == "__main__":
    populate_logistics_data()
