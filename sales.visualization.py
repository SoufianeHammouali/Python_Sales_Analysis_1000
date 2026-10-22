
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("Data/clean_sales_data.csv")
print("Dimensions du jeu de données :", df.shape)

# Traduction des catégories pour les graphiques
traduction_categories = {
    "Electronics": "Électronique",
    "Furniture": "Mobilier",
    "Home Appliances": "Électroménager",
}

# 1. Chiffre d'affaires par catégorie
revenue_by_category = (
    df.groupby("Category")["Net_Revenue_MAD"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(10, 6))
plt.barh(
    [traduction_categories.get(c, c) for c in revenue_by_category.index],
    revenue_by_category.values,
    color="#16A34A"
)
plt.title("Chiffre d'affaires par catégorie — 2025", fontsize=15)
plt.xlabel("Chiffre d'affaires net (MAD)")
plt.ylabel("Catégorie de produits")
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("Charts/revenue_by_category.png", dpi=300)
plt.show()

# 2. Bénéfice par catégorie
profit_by_category = (
    df.groupby("Category")["Profit_MAD"]
    .sum()
    .sort_values(ascending=True)
)
plt.figure(figsize=(10, 6))
plt.barh(
    [traduction_categories.get(c, c) for c in profit_by_category.index],
    profit_by_category.values,
    color="#16A34A"
)
plt.title("Bénéfice total par catégorie — 2025", fontsize=15)
plt.xlabel("Bénéfice total (MAD)")
plt.ylabel("Catégorie de produits")
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("Charts/profit_by_category.png", dpi=300)
plt.show()

# 3. Évolution mensuelle du chiffre d'affaires
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

monthly_revenue = (
    df.groupby("Month")["Net_Revenue_MAD"]
    .sum()
    .sort_index()
)
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o",
    linewidth=2.5,
    color="#2563EB"
)
plt.title("Évolution mensuelle du chiffre d'affaires — 2025", fontsize=15)
plt.xlabel("Mois")
plt.ylabel("Chiffre d'affaires net (MAD)")
plt.xticks(rotation=45)
plt.grid(linestyle="--", alpha=0.3)
plt.tight_layout()
plt.savefig("Charts/monthly_revenue_trend.png", dpi=300)
plt.show()

# 4. Chiffre d'affaires par canal de vente
revenue_by_channel = (
    df.groupby("Sales_Channel")["Net_Revenue_MAD"]
    .sum()
    .sort_values(ascending=False)
)
traduction_canaux = {
    "Online": "En ligne",
    "Marketplace": "Place de marché",
    "Store": "Magasin"
}
plt.figure(figsize=(9, 6))
bars = plt.bar(
    [traduction_canaux.get(c, c) for c in revenue_by_channel.index],
    revenue_by_channel.values,
    color=["#2563EB", "#0D9488", "#F59E0B"]
)
plt.title("Chiffre d'affaires par canal de vente — 2025", fontsize=15)
plt.xlabel("Canal de vente")
plt.ylabel("Chiffre d'affaires net (MAD)")
plt.bar_label(
    bars,
    labels=[f"{v / 1_000_000:.2f} M" for v in revenue_by_channel.values],
    padding=4
)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.savefig("Charts/revenue_by_channel.png", dpi=300)
plt.show()

# 5. Chiffre d'affaires par segment de clientèle
revenue_by_segment = (
    df.groupby("Customer_Segment")["Net_Revenue_MAD"]
    .sum()
    .sort_values(ascending=False)
)
traduction_segments = {
    "Corporate": "Entreprises",
    "Consumer": "Particuliers",
    "Small Business": "Petites entreprises"
}
plt.figure(figsize=(9, 6))
bars = plt.bar(
    [traduction_segments.get(s, s) for s in revenue_by_segment.index],
    revenue_by_segment.values,
    color=["#2563EB", "#0D9488", "#F59E0B"]
)
plt.title("Chiffre d'affaires par segment de clientèle — 2025", fontsize=15)
plt.xlabel("Segment de clientèle")
plt.ylabel("Chiffre d'affaires net (MAD)")
plt.bar_label(
    bars,
    labels=[f"{v / 1_000_000:.2f} M" for v in revenue_by_segment.values],
    padding=4
)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.savefig("Charts/revenue_by_customer_segment.png", dpi=300)
plt.show()

# 6. Top 10 des produits par chiffre d'affaires
top_products = (
    df.groupby("Product")["Net_Revenue_MAD"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values(ascending=True)
)
traduction_produits = {
    "Smartphone": "Smartphone",
    "Air Conditioner": "Climatiseur",
    "Laptop": "Ordinateur portable",
    "Refrigerator": "Réfrigérateur",
    "Washing Machine": "Machine à laver",
    "Television": "Télévision",
    "Sofa": "Canapé",
    "Desk": "Bureau",
    "Chair": "Chaise",
    "Tablet": "Tablette"
}
plt.figure(figsize=(11, 7))
bars = plt.barh(
    [traduction_produits.get(p, p) for p in top_products.index],
    top_products.values,
    color="#2563EB"
)
plt.title("Top 10 des produits par chiffre d'affaires — 2025", fontsize=15)
plt.xlabel("Chiffre d'affaires net (MAD)")
plt.ylabel("Produit")
plt.bar_label(
    bars,
    labels=[f"{v / 1000:.0f} k" for v in top_products.values],
    padding=4
)
plt.xlim(0, top_products.max() * 1.15)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.savefig("Charts/top_10_products_revenue.png", dpi=300)
plt.show()

# 7. Marge bénéficiaire par catégorie
category_profitability = (
    df.groupby("Category")
    .agg(
        Revenue=("Net_Revenue_MAD", "sum"),
        Profit=("Profit_MAD", "sum")
    )
)
category_profitability["Profit_Margin"] = (
    category_profitability["Profit"]
    / category_profitability["Revenue"] * 100
)
margin_by_category = (
    category_profitability["Profit_Margin"]
    .sort_values(ascending=True)
)
plt.figure(figsize=(10, 6))
bars = plt.barh(
    [traduction_categories.get(c, c) for c in margin_by_category.index],
    margin_by_category.values,
    color="#0D9488"
)
plt.title("Marge bénéficiaire par catégorie — 2025", fontsize=15)
plt.xlabel("Marge bénéficiaire (%)")
plt.ylabel("Catégorie de produits")
plt.bar_label(
    bars,
    labels=[f"{v:.2f} %" for v in margin_by_category.values],
    padding=4
)
plt.xlim(0, margin_by_category.max() * 1.15)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.savefig("Charts/profit_margin_by_category.png", dpi=300)
plt.show()

# 8. Top 8 des villes par chiffre d'affaires
revenue_by_city = (
    df[df["City"] != "Unknown"]
    .groupby("City")["Net_Revenue_MAD"]
    .sum()
    .sort_values(ascending=False)
    .head(8)
    .sort_values(ascending=True)
)
plt.figure(figsize=(11, 7))
bars = plt.barh(
    revenue_by_city.index,
    revenue_by_city.values,
    color="#2563EB"
)
plt.title("Top 8 des villes par chiffre d'affaires — 2025", fontsize=15)
plt.xlabel("Chiffre d'affaires net (MAD)")
plt.ylabel("Ville")
plt.bar_label(
    bars,
    labels=[f"{v / 1_000_000:.2f} M" for v in revenue_by_city.values],
    padding=4
)
plt.xlim(0, revenue_by_city.max() * 1.15)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.savefig("Charts/revenue_by_city.png", dpi=300)
plt.show()

print("Les 8 graphiques ont été générés avec succès.")
