import pandas as pd

def load_data(file_path):
    """Load the Excel dataset"""
    xls = pd.ExcelFile(r"C:\Users\balne\PriceCo_Sales_Analysis\data\PriceCo_sales-2.xlsx")
    df = pd.read_excel(xls, sheet_name="Price-Co")
    return df

def clean_data(df):
    """Perform basic data cleaning"""
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime
    df[['Unit price_mxp', 'Tax 15%', 'Total_mxp', 'Quantity']] = df[
        ['Unit price_mxp', 'Tax 15%', 'Total_mxp', 'Quantity']
    ].astype(float)  # Ensure correct types
    return df

if __name__ == "__main__":
    df = load_data(r"data/PriceCo_sales-2.xlsx")
    df = clean_data(df)
    print("Data loaded and cleaned successfully!")
