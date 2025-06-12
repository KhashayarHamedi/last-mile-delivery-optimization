import sqlite3
import pandas as pd

def run_logistics_analysis():
    """Run the SQL queries that logistics analysts use daily."""
    
    conn = sqlite3.connect('data/logistics.db')
    
    print("🚛 DAILY LOGISTICS ANALYSIS - Real Industry Queries")
    print("=" * 60)
    
    # Query 1: Driver Performance Analysis (Used Daily)
    print("\n📊 1. DRIVER PERFORMANCE RANKING")
    driver_performance = pd.read_sql_query("""
        SELECT 
            r.driver_id,
            COUNT(r.route_id) as total_routes,
            AVG(r.actual_stops) as avg_stops_per_route,
            SUM(d.delivery_status = 'delivered') as successful_deliveries,
            SUM(d.delivery_status = 'failed') as failed_deliveries,
            ROUND(
                SUM(d.delivery_status = 'delivered') * 100.0 / COUNT(d.delivery_id), 1
            ) as success_rate_percent,
            ROUND(SUM(r.total_revenue_euros - r.fuel_cost_euros - r.driver_cost_euros), 2) as profit_generated
        FROM routes r
        LEFT JOIN deliveries d ON r.route_id = d.route_id
        GROUP BY r.driver_id
        HAVING total_routes >= 5
        ORDER BY success_rate_percent DESC, profit_generated DESC
        LIMIT 10
    """, conn)
    print(driver_performance)
    
    # Query 2: Route Efficiency Analysis (Critical for Optimization)
    print("\n🎯 2. ROUTE EFFICIENCY - Cost per Delivery")
    route_efficiency = pd.read_sql_query("""
        SELECT 
            r.route_id,
            r.route_date,
            r.actual_stops,
            ROUND(r.total_distance_km / r.actual_stops, 2) as km_per_delivery,
            ROUND((r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops, 2) as cost_per_delivery,
            ROUND(r.total_revenue_euros / (r.fuel_cost_euros + r.driver_cost_euros), 2) as profit_margin_ratio,
            CASE 
                WHEN (r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops < 6.0 THEN 'Efficient'
                WHEN (r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops < 8.0 THEN 'Average' 
                ELSE 'Needs Optimization'
            END as efficiency_category
        FROM routes r
        WHERE r.actual_stops > 0
        ORDER BY cost_per_delivery ASC
        LIMIT 15
    """, conn)
    print(route_efficiency)
    
    # Query 3: Daily Operations Dashboard (What managers see)
    print("\n📈 3. DAILY OPERATIONS DASHBOARD")
    daily_ops = pd.read_sql_query("""
        SELECT 
            r.route_date,
            COUNT(DISTINCT r.route_id) as routes_completed,
            SUM(r.actual_stops) as total_deliveries,
            SUM(d.delivery_status = 'delivered') as successful_deliveries,
            ROUND(SUM(d.delivery_status = 'delivered') * 100.0 / SUM(r.actual_stops), 1) as daily_success_rate,
            ROUND(SUM(r.total_revenue_euros), 2) as total_revenue,
            ROUND(SUM(r.fuel_cost_euros + r.driver_cost_euros), 2) as total_costs,
            ROUND(SUM(r.total_revenue_euros) - SUM(r.fuel_cost_euros + r.driver_cost_euros), 2) as daily_profit
        FROM routes r
        LEFT JOIN deliveries d ON r.route_id = d.route_id
        GROUP BY r.route_date
        ORDER BY r.route_date DESC
        LIMIT 10
    """, conn)
    print(daily_ops)
    
    print("\n💡 These are the exact queries logistics analysts run daily!")
    conn.close()

if __name__ == "__main__":
    run_logistics_analysis()
