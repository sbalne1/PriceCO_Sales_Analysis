import pandas as pd

def compute_avg_ticket(df):
    """Calculating average ticket value"""
    return df['Total_mxp'].mean()

def avg_ticket_by_membership(df):
    """Compute average ticket by membership type"""
    return df.groupby('Membership')['Total_mxp'].mean().reset_index()

def top_selling_products(df):
    """Get top-selling product lines"""
    return df.groupby('Product line')['Total_mxp'].sum().reset_index().sort_values(by="Total_mxp", ascending=False)

if __name__ == "__main__":
    from data_processing import load_data, clean_data
    df = load_data(r"C:\Users\balne\PriceCo_Sales_Analysis\data\PriceCo_sales-2.xlsx")
    df = clean_data(df)
    
    print("Average Ticket Value:", compute_avg_ticket(df))
    print("Average Ticket by Membership Type:\n", avg_ticket_by_membership(df))
    print("Top-Selling Product Categories:\n", top_selling_products(df))
