
from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --------------------------------------------------
# 1. CHEMINS DES FICHIERS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "Data" / "clean_sales_data.csv"
OUTPUT_FILE = BASE_DIR / "Sales_Analysis_Report_2025.pdf"
CHARTS_DIR = BASE_DIR / "Charts"

df = pd.read_csv(DATA_FILE)

# --------------------------------------------------
# 2. CALCUL DES INDICATEURS
# --------------------------------------------------

total_revenue = df["Net_Revenue_MAD"].sum()
total_profit = df["Profit_MAD"].sum()
total_orders = df["Order_ID"].nunique()
profit_margin = total_profit / total_revenue * 100

def format_nombre(value, decimals=2):
    return f"{value:,.{decimals}f}".replace(",", " ").replace(".", ",")

# --------------------------------------------------
# 3. CONFIGURATION DES POLICES
# --------------------------------------------------

# Polices Windows compatibles avec les accents français
font_dir = Path("C:/Windows/Fonts")
font_regular = font_dir / "arial.ttf"
font_bold = font_dir / "arialbd.ttf"

if font_regular.exists() and font_bold.exists():
    pdfmetrics.registerFont(TTFont("ArialFR", str(font_regular)))
    pdfmetrics.registerFont(TTFont("ArialFR-Bold", str(font_bold)))
    FONT = "ArialFR"
    FONT_BOLD = "ArialFR-Bold"
else:
    # Helvetica prend en charge les accents français courants
    FONT = "Helvetica"
    FONT_BOLD = "Helvetica-Bold"

# --------------------------------------------------
# 4. CONFIGURATION DU PDF
# --------------------------------------------------

pdf = SimpleDocTemplate(
    str(OUTPUT_FILE),
    pagesize=(595.28, 841.89),
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45,
)

styles = getSampleStyleSheet()

styles["Normal"].fontName = FONT
styles["Title"].fontName = FONT_BOLD
styles["Heading1"].fontName = FONT_BOLD
styles["Heading2"].fontName = FONT_BOLD

styles.add(
    ParagraphStyle(
        name="TitreRapport",
        parent=styles["Title"],
        fontName=FONT_BOLD,
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=20,
        alignment=TA_CENTER,
    )
)

styles.add(
    ParagraphStyle(
        name="TexteRapport",
        parent=styles["BodyText"],
        fontName=FONT,
        fontSize=10,
        leading=16,
        spaceAfter=10,
    )
)

content = []

# --------------------------------------------------
# 5. PAGE DE PRÉSENTATION
# --------------------------------------------------

content.append(
    Paragraph(
        "Analyse des performances commerciales — 2025",
        styles["TitreRapport"]
    )
)

content.append(
    Paragraph(
        "Projet d'analyse de données avec Python | "
        "Janvier - Décembre 2025",
        styles["Normal"]
    )
)

content.append(Spacer(1, 25))

content.append(
    Paragraph("Synthèse générale", styles["Heading2"])
)

content.append(
    Paragraph(
        "Ce rapport présente une analyse de 1 000 commandes "
        "commerciales réalisées en 2025. L'objectif est "
        "d'évaluer le chiffre d'affaires, la rentabilité, "
        "les performances des produits, les canaux de vente, "
        "les segments de clientèle et les tendances géographiques.",
        styles["TexteRapport"]
    )
)

# --------------------------------------------------
# 6. INDICATEURS CLÉS DE PERFORMANCE
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph(
        "Indicateurs clés de performance (KPI)",
        styles["Heading2"]
    )
)

kpi_data = [
    ["Indicateur", "Valeur"],
    ["Chiffre d'affaires total", f"{format_nombre(total_revenue)} MAD"],
    ["Bénéfice total", f"{format_nombre(total_profit)} MAD"],
    ["Marge bénéficiaire", f"{format_nombre(profit_margin)} %"],
    ["Nombre total de commandes", format_nombre(total_orders, 0)],
]

kpi_table = Table(kpi_data, colWidths=[230, 230])

kpi_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
        ("FONTNAME", (0, 1), (-1, -1), FONT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#F1F5F9")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

content.append(kpi_table)

# --------------------------------------------------
# 7. PRÉPARATION ET NETTOYAGE DES DONNÉES
# --------------------------------------------------

content.append(Spacer(1, 25))

content.append(
    Paragraph(
        "Préparation et nettoyage des données",
        styles["Heading2"]
    )
)

content.append(
    Paragraph(
        "Le jeu de données initial contenait 1 005 lignes. "
        "Après la suppression de 5 doublons, le jeu de données "
        "nettoyé comprend 1 000 commandes uniques. "
        "Les valeurs manquantes des champs Customer_ID et City "
        "ont été remplacées par la valeur Unknown. "
        "Les contrôles de qualité ont porté sur les quantités, "
        "le chiffre d'affaires, les bénéfices, les remises, "
        "les dates et les identifiants de commande.",
        styles["TexteRapport"]
    )
)

# --------------------------------------------------
# 8. VISUALISATIONS COMMERCIALES
# --------------------------------------------------

charts = [
    ("Chiffre d'affaires par catégorie", "revenue_by_category.png"),
    ("Bénéfice par catégorie", "profit_by_category.png"),
    ("Évolution mensuelle du chiffre d'affaires", "monthly_revenue_trend.png"),
    ("Chiffre d'affaires par canal de vente", "revenue_by_channel.png"),
    ("Chiffre d'affaires par segment de clientèle", "revenue_by_customer_segment.png"),
    ("Top 10 des produits par chiffre d'affaires", "top_10_products_revenue.png"),
    ("Marge bénéficiaire par catégorie", "profit_margin_by_category.png"),
    ("Top 8 des villes par chiffre d'affaires", "revenue_by_city.png"),
]

content.append(PageBreak())

content.append(
    Paragraph(
        "Visualisations des performances commerciales",
        styles["Heading1"]
    )
)

content.append(Spacer(1, 15))

for chart_title, chart_filename in charts:

    chart_path = CHARTS_DIR / chart_filename

    if chart_path.exists():
        content.append(
            KeepTogether([
                Paragraph(escape(chart_title), styles["Heading2"]),
                Spacer(1, 10),
                Image(str(chart_path), width=450, height=270),
                Spacer(1, 20),
            ])
        )
    else:
        print(f"Attention : graphique introuvable : {chart_filename}")

# --------------------------------------------------
# 9. PRINCIPAUX RÉSULTATS
# --------------------------------------------------

content.append(PageBreak())

content.append(
    Paragraph(
        "Principaux résultats de l'analyse",
        styles["Heading1"]
    )
)

insights = [
    (
        "Performance par catégorie",
        "La catégorie Électronique génère le chiffre d'affaires "
        "le plus élevé (2,93 millions MAD) ainsi que le bénéfice "
        "total le plus important (789 000 MAD). "
        "Le Mobilier présente la meilleure marge (27,11 %)."
    ),
    (
        "Performance par produit",
        "Le Smartphone arrive en tête avec environ 931 000 MAD, "
        "suivi du Climatiseur (890 000 MAD) et de "
        "l'Ordinateur portable (858 000 MAD)."
    ),
    (
        "Performance géographique",
        "Rabat génère le chiffre d'affaires le plus élevé "
        "(1,05 million MAD), suivie de Fès et Marrakech."
    ),
    (
        "Performance par canal de vente",
        "La vente en ligne génère le chiffre d'affaires "
        "le plus élevé (2,59 millions MAD), tandis que "
        "la place de marché présente la meilleure marge "
        "bénéficiaire (27,35 %)."
    ),
    (
        "Performance par segment de clientèle",
        "Le segment Entreprises génère le chiffre d'affaires "
        "le plus élevé (2,70 millions MAD) et affiche "
        "une marge bénéficiaire de 27,90 %."
    ),
    (
        "Évolution mensuelle",
        "Février enregistre le chiffre d'affaires le plus élevé "
        "(792 000 MAD), tandis que septembre présente "
        "le niveau le plus faible (388 000 MAD)."
    ),
]

for title, description in insights:
    content.append(Paragraph(escape(title), styles["Heading2"]))
    content.append(Paragraph(escape(description), styles["TexteRapport"]))

# --------------------------------------------------
# 10. RECOMMANDATIONS COMMERCIALES
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph("Recommandations commerciales", styles["Heading1"])
)

recommendations = [
    "Suivre les stocks et la demande des produits les plus performants.",
    "Analyser les différences de coûts et de remises entre les catégories.",
    "Étudier la rentabilité de la place de marché avant d'augmenter les investissements.",
    "Évaluer des offres ciblées pour le segment Entreprises.",
    "Examiner les facteurs expliquant la baisse de septembre et la reprise d'octobre.",
]

for i, recommendation in enumerate(recommendations, start=1):
    content.append(
        Paragraph(
            f"{i}. {escape(recommendation)}",
            styles["TexteRapport"]
        )
    )

# --------------------------------------------------
# 11. LIMITES DE L'ANALYSE
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph("Limites de l'analyse", styles["Heading1"])
)

limitations = [
    "Les données couvrent uniquement l'année 2025.",
    "Cinq commandes présentent une ville non renseignée.",
    "Les résultats ne permettent pas d'établir de causalité.",
    "Les recommandations nécessitent une validation complémentaire.",
]

for limitation in limitations:
    content.append(
        Paragraph(
            "- " + escape(limitation),
            styles["TexteRapport"]
        )
    )

# --------------------------------------------------
# 12. GÉNÉRATION DU RAPPORT PDF
# --------------------------------------------------

pdf.build(content)

print("Rapport PDF généré avec succès !")
print("Fichier :", OUTPUT_FILE)
print("Nombre de commandes :", total_orders)
print("Chiffre d'affaires total :", round(total_revenue, 2))
print("Bénéfice total :", round(total_profit, 2))
print("Marge bénéficiaire (%) :", round(profit_margin, 2))
