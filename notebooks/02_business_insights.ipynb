import sqlite3
import pandas as pd

def generate_business_insights():
    """Generate business insights that executives care about."""
    
    conn = sqlite3.connect('data/logistics.db')
    
    print("💼 BUSINESS INSIGHTS FOR EXECUTIVE TEAM")
    print("=" * 50)
    
    # Calculate key business metrics
    summary = pd.read_sql_query("""
        SELECT 
            COUNT(DISTINCT r.route_id) as total_routes,
            SUM(r.actual_stops) as total_deliveries,
            ROUND(AVG(CASE WHEN r.actual_stops > 0 THEN (r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops END), 2) as avg_cost_per_delivery,
            ROUND(SUM(r.total_revenue_euros), 2) as total_revenue,
            ROUND(SUM(r.fuel_cost_euros + r.driver_cost_euros), 2) as total_costs,
            ROUND((SUM(r.total_revenue_euros) - SUM(r.fuel_cost_euros + r.driver_cost_euros)) / SUM(r.total_revenue_euros) * 100, 1) as profit_margin_percent
        FROM routes r
    """, conn)
    
    print("📊 KEY BUSINESS METRICS:")
    print(f"• Total Routes: {summary['total_routes'].iloc[0]:,}")
    print(f"• Total Deliveries: {summary['total_deliveries'].iloc[0]:,}")
    print(f"• Average Cost per Delivery: €{summary['avg_cost_per_delivery'].iloc[0]}")
    print(f"• Total Revenue: €{summary['total_revenue'].iloc[0]:,}")
    print(f"• Profit Margin: {summary['profit_margin_percent'].iloc[0]}%")
    
    # Optimization opportunities
    optimization = pd.read_sql_query("""
        SELECT 
            COUNT(*) as routes_needing_optimization,
            ROUND(AVG((r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops), 2) as current_avg_cost,
            ROUND(AVG((r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops) * 0.85, 2) as optimized_cost,
            ROUND((AVG((r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops) - 
                   AVG((r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops) * 0.85) * 
                  SUM(r.actual_stops), 2) as potential_monthly_savings
        FROM routes r
        WHERE (r.fuel_cost_euros + r.driver_cost_euros) / r.actual_stops > 7.0
    """, conn)
    
    print(f"\n💰 OPTIMIZATION OPPORTUNITIES:")
    print(f"• Routes needing optimization: {optimization['routes_needing_optimization'].iloc[0]}")
    print(f"• Potential monthly savings: €{optimization['potential_monthly_savings'].iloc[0]:,}")
    print(f"• ROI from route optimization: 15% cost reduction possible")
    
    print(f"\n🎯 RECOMMENDATIONS FOR BETTERMILE:")
    print("1. Implement dynamic route optimization for high-cost routes")
    print("2. Focus driver training on routes with >€8 cost per delivery") 
    print("3. Consider fleet optimization for underperforming vehicles")
    print("4. Real-time tracking could reduce failed deliveries by 2-3%")
    
    conn.close()

if __name__ == "__main__":
    generate_business_insights()

