import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("Data/clean_sales_data.csv")
print("COLUMN NAMES:")
for col in df.columns:print(repr(col))
df["Date"]=pd.to_datetime(df["Date"])
df["Month"]=df["Date"].dt.to_period("M")
# Check dataset dimensions
print("Dataset Shape:", df.shape)
total_revenue=df["Net_Revenue_MAD"].sum()
print("Total Revenue(MAD):",round(total_revenue,2))
total_profit=df["Profit_MAD"].sum()
print("Total Profit(MAD):",round(total_profit,2))
profit_margin = (total_profit / total_revenue) * 100

print("Profit Margin (%):", round(profit_margin, 2))
# Calculate total orders
total_orders = df["Order_ID"].nunique()

print("Total Orders:", total_orders)
revenue_by_category=(df.groupby("Category")["Net_Revenue_MAD"].sum().sort_values(ascending=False))
print("\nRevenue by category:")
print(revenue_by_category)
Profit_by_category= (df.groupby("Category")["Profit_MAD"].sum().sort_values(ascending=False))
print("\nProfit by category:")
print(Profit_by_category)
Margin_by_category= (Profit_by_category/ revenue_by_category)*100
Margin_by_category=Margin_by_category.sort_values(ascending=False)
print("\nProfit Margin by category (%):")
print(Margin_by_category.round(2))
Top_products=(df.groupby("Product")["Net_Revenue_MAD"].sum().sort_values(ascending=False).head(10))
print("\nTop 10 products by revenue:")
print(Top_products)
Top_products_profit=(df.groupby("Product")["Profit_MAD"].sum().sort_values(ascending=False).head(10))
print("\nTop 10 products by profit:")
print(Top_products_profit)
Sales_by_city=(df.groupby("City").agg(Revenue=("Net_Revenue_MAD","sum"),Profit=("Profit_MAD","sum"),Orders=("Order_ID","nunique")).sort_values("Revenue",ascending=False))
print("\nSales Performance by city:")
print(Sales_by_city.round(2).to_string())
Sales_by_channel=(df.groupby("Sales_Channel").agg(Revenue=("Net_Revenue_MAD","sum"),Profit=("Profit_MAD","sum"),Orders=("Order_ID","nunique")).sort_values("Revenue",ascending=False))
print("\nSales Performance by channel:")
print(Sales_by_channel.round(2).to_string())
Sales_by_channel["Profit_Margin_%"]=(Sales_by_channel["Profit"]/Sales_by_channel["Revenue"]*100)
print("\nProfit Margin by Channel")
print(Sales_by_channel[["Revenue","Profit","Profit_Margin_%"]].round(2).to_string())
# Sales performance by customer segment
sales_by_segment = (df.groupby("Customer_Segment").agg(Revenue=("Net_Revenue_MAD", "sum"),Profit=("Profit_MAD", "sum"),Orders=("Order_ID", "nunique")).sort_values("Revenue", ascending=False))
sales_by_segment["Profit_Margin_%"] = ( sales_by_segment["Profit"]/ sales_by_segment["Revenue"] * 100)

print("\nSales Performance by Customer Segment:")
print(sales_by_segment.round(2).to_string())
Monthly_sales=(df.groupby("Month").agg(Revenue=("Net_Revenue_MAD","sum"),Profit=("Profit_MAD","sum"),Orders=("Order_ID","nunique")).sort_index())
print("\nMonthly sales trend:")
print(Monthly_sales.round(2).to_string())
Monthly_sales["Revenue_Growth_%"]=(Monthly_sales["Revenue"].pct_change()*100)
print("\nMonthly Revenue Growth %:")
print(Monthly_sales[["Revenue","Revenue_Growth_%"]].round(2).to_string())