import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [12000, 15000, 13500, 18000, 21000, 19500,
              23000, 25000, 22000, 28000, 32000, 35000],
    "Profit": [2500, 3200, 2800, 4100, 4800, 4300,
               5500, 6200, 5100, 6800, 8200, 9000],
    "Orders": [120, 145, 130, 170, 190, 180,
               210, 230, 200, 250, 290, 310],
    "Customers": [95, 110, 105, 135, 150, 140,
                  165, 180, 155, 195, 220, 240],
    "Category": ["Electronics", "Fashion", "Electronics", "Home",
                 "Fashion", "Home", "Electronics", "Fashion",
                 "Home", "Electronics", "Fashion", "Home"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Seaborn style
sns.set_theme(style="whitegrid")


plt.figure(figsize=(10, 6))

sns.lineplot(data=df, x="Month", y="Sales",
             marker="o", label="Sales")

sns.lineplot(data=df, x="Month", y="Profit",
             marker="o", label="Profit")

plt.title("Monthly Sales and Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.tight_layout()
plt.show()


category_orders = df.groupby("Category", as_index=False)["Orders"].sum()

plt.figure(figsize=(8, 6))

sns.barplot(
    data=category_orders,
    x="Category",
    y="Orders",
    hue="Category",
    legend=False
)

plt.title("Total Orders by Category")
plt.xlabel("Category")
plt.ylabel("Total Orders")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    size="Orders",
    hue="Category",
    sizes=(50, 300),
    alpha=0.8
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()


# Select numerical columns
corr = df[["Sales", "Profit", "Orders", "Customers"]].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))

sns.boxplot(
    data=df,
    x="Category",
    y="Sales",
    hue="Category",
    legend=False
)

plt.title("Sales Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()