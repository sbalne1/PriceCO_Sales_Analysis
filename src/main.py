from data_processing import load_data, clean_data
from eda import compute_avg_ticket, avg_ticket_by_membership, top_selling_products
from visualization import plot_sales_by_membership, plot_sales_trends

# Load and clean data
df = load_data(r"C:\Users\balne\PriceCo_Sales_Analysis\data\PriceCo_sales-2.xlsx")
df = clean_data(df)

# Compute insights
print("Average Ticket Value:", compute_avg_ticket(df))
print("Average Ticket by Membership Type:\n", avg_ticket_by_membership(df))
print("Top-Selling Product Categories:\n", top_selling_products(df))

# Generate visualizations
plot_sales_by_membership(df)
plot_sales_trends(df)
