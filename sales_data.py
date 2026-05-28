import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel("C:/Users/Vinícius/Documents/GitHub/sales_data/sales.xlsx")
df["Total"]=df["Quantity"]*df["Price"]
total_revenue=df["Total"].sum(numeric_only=True)
print(f"Your total revenue is: {total_revenue:,.2f}")
Quantity=df["Quantity"].sum()
df_product=df[["Product","Quantity"]].groupby("Product").sum()
rank_products=df_product.sort_values(by="Quantity",ascending=False)
print(f"You sold a total of {Quantity} products and the rank of your products is: {rank_products}")
average_revenue=df["Total"].mean()
highest_sale=df["Total"].max()
print(f"The mean of your revenue is {average_revenue:,.2f} and the most expensive sale was {highest_sale:,.2f}")
df_sellers=df[["Seller","Total"]].groupby("Seller").sum()
df_sellers.plot(kind="bar",color="skyblue")
plt.title("Sellers rank")
plt.xticks(rotation=45)
plt.ylabel("Revenue")
plt.xlabel("Seller")
plt.tight_layout()
plt.savefig("C:/Users/Vinícius/Documents/GitHub/sales_data/sellers_rank.png")
plt.show()

