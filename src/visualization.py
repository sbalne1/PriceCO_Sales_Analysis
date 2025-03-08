import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_by_membership(df):
    """Plot total sales by membership type"""
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Membership", y="Total_mxp", data=df, estimator=sum, ci=None)
    plt.title("Total Sales by Membership Type")
    plt.ylabel("Total Sales_MXP")
    plt.show()

def plot_sales_trends(df):
    """Plot daily sales trend"""
    df_daily_sales = df.groupby("Date")["Total_mxp"].sum().reset_index()

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=df_daily_sales, x="Date", y="Total_mxp")
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Sales_MXP")
    plt.show()

if __name__ == "__main__":
    from data_processing import load_data, clean_data
    df = load_data(r"C:\Users\balne\PriceCo_Sales_Analysis\data\PriceCo_sales-2.xlsx")
    df = clean_data(df)
    
    plot_sales_by_membership(df)
    plot_sales_trends(df)
