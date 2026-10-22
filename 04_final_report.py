from pathlib import Path

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
from reportlab.lib.units import inch

# --------------------------------------------------
# 1. FILE PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "Data" / "clean_sales_data.csv"
OUTPUT_FILE = BASE_DIR / "Sales_Analysis_Report_2025.pdf"

df = pd.read_csv(DATA_FILE)

# --------------------------------------------------
# 2. CALCULATE KPIs FROM DATA
# --------------------------------------------------

total_revenue = df["Net_Revenue_MAD"].sum()
total_profit = df["Profit_MAD"].sum()
total_orders = df["Order_ID"].nunique()
profit_margin = total_profit / total_revenue * 100

# --------------------------------------------------
# 3. PDF SETUP
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

styles.add(
    ParagraphStyle(
        name="ReportTitle",
        parent=styles["Title"],
        fontSize=20,
        leading=26,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=20,
        alignment=TA_CENTER,
    )
)

styles.add(
    ParagraphStyle(
        name="ReportBody",
        parent=styles["BodyText"],
        fontSize=10,
        leading=16,
        spaceAfter=10,
    )
)

content = []

# --------------------------------------------------
# 4. COVER & INTRODUCTION
# --------------------------------------------------

content.append(
    Paragraph(
        "Sales Performance Analysis - 2025",
        styles["ReportTitle"]
    )
)

content.append(
    Paragraph(
        "Python Data Analysis Project | January - December 2025",
        styles["Normal"]
    )
)

content.append(Spacer(1, 25))

content.append(
    Paragraph("Executive Summary", styles["Heading2"])
)

content.append(
    Paragraph(
        "This report analyzes 1,000 sales orders from 2025 "
        "to evaluate revenue, profitability, product performance, "
        "sales channels, customer segments, and geographic trends.",
        styles["ReportBody"]
    )
)

# --------------------------------------------------
# 5. KEY PERFORMANCE INDICATORS
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph("Key Performance Indicators", styles["Heading2"])
)

kpi_data = [
    ["Metric", "Value"],
    ["Total Revenue", f"{total_revenue:,.2f} MAD"],
    ["Total Profit", f"{total_profit:,.2f} MAD"],
    ["Profit Margin", f"{profit_margin:.2f}%"],
    ["Total Orders", f"{total_orders:,}"],
]

kpi_table = Table(kpi_data, colWidths=[230, 230])

kpi_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, colors.HexColor("#F1F5F9")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

content.append(kpi_table)

# --------------------------------------------------
# 6. DATA PREPARATION
# --------------------------------------------------

content.append(Spacer(1, 25))

content.append(
    Paragraph("Data Preparation", styles["Heading2"])
)

content.append(
    Paragraph(
        "The original dataset contained 1,005 rows. "
        "Five duplicate orders were removed, resulting in "
        "1,000 unique orders. Missing Customer_ID and City values "
        "were labeled as Unknown. Data quality checks covered "
        "quantities, revenue, profit calculations, discounts, "
        "dates, and duplicate order IDs.",
        styles["ReportBody"]
    )
)

# --------------------------------------------------
# 7. VISUALIZATIONS
# --------------------------------------------------

charts = [
    (
        "Revenue by Product Category",
        "revenue_by_category.png"
    ),
    (
        "Profit by Product Category",
        "profit_by_category.png"
    ),
    (
        "Monthly Revenue Trend",
        "monthly_revenue_trend.png"
    ),
    (
        "Revenue by Sales Channel",
        "revenue_by_channel.png"
    ),
    (
        "Revenue by Customer Segment",
        "revenue_by_customer_segment.png"
    ),
    (
        "Top 10 Products by Revenue",
        "top_10_products_revenue.png"
    ),
    (
        "Profit Margin by Category",
        "profit_margin_by_category.png"
    ),
    (
        "Top 8 Cities by Revenue",
        "revenue_by_city.png"
    ),
]

content.append(PageBreak())

content.append(
    Paragraph("Sales Performance Visualizations", styles["Heading1"])
)

content.append(Spacer(1, 15))

for chart_title, chart_filename in charts:

    chart_path = BASE_DIR / "Charts" / chart_filename

    if chart_path.exists():

        content.append(
            KeepTogether([
                Paragraph(chart_title, styles["Heading2"]),
                Spacer(1, 10),
                Image(str(chart_path), width=450, height=270),
                Spacer(1, 20),
            ])
        )

    else:
        print(f"Warning: Chart not found: {chart_filename}")

# --------------------------------------------------
# 8. BUSINESS INSIGHTS
# --------------------------------------------------

content.append(PageBreak())

content.append(
    Paragraph("Key Business Insights", styles["Heading1"])
)

insights = [
    (
        "Category Performance",
        "Electronics generated the highest revenue "
        "(2.93M MAD) and profit (789K MAD). "
        "Furniture achieved the highest profit margin (27.11%)."
    ),
    (
        "Product Performance",
        "Smartphone was the leading product by revenue "
        "(931K MAD), followed by Air Conditioner (890K MAD) "
        "and Laptop (858K MAD)."
    ),
    (
        "Geographic Performance",
        "Rabat generated the highest city revenue "
        "(1.05M MAD), followed by Fes and Marrakech."
    ),
    (
        "Sales Channel Performance",
        "Online generated the highest revenue (2.59M MAD), "
        "while Marketplace achieved the highest profit margin "
        "(27.35%)."
    ),
    (
        "Customer Segment Performance",
        "Corporate generated the highest revenue "
        "(2.70M MAD) and profit margin (27.90%)."
    ),
    (
        "Monthly Performance",
        "February recorded the highest monthly revenue "
        "(792K MAD), while September recorded the lowest "
        "(388K MAD)."
    ),
]

for title, description in insights:

    content.append(
        Paragraph(title, styles["Heading2"])
    )

    content.append(
        Paragraph(description, styles["ReportBody"])
    )

# --------------------------------------------------
# 9. BUSINESS RECOMMENDATIONS
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph("Business Recommendations", styles["Heading1"])
)

recommendations = [
    "Review inventory and demand for top-selling products.",
    "Investigate cost and discount differences across categories.",
    "Analyze Marketplace profitability before expanding investment.",
    "Evaluate targeted opportunities for Corporate customers.",
    "Investigate the September revenue decline and October recovery.",
]

for i, recommendation in enumerate(recommendations, start=1):

    content.append(
        Paragraph(
            f"{i}. {recommendation}",
            styles["ReportBody"]
        )
    )

# --------------------------------------------------
# 10. LIMITATIONS
# --------------------------------------------------

content.append(Spacer(1, 15))

content.append(
    Paragraph("Analysis Limitations", styles["Heading1"])
)

limitations = [
    "The dataset covers only 2025.",
    "Five orders have unknown city information.",
    "The findings do not establish causation.",
    "Business recommendations require further validation.",
]

for limitation in limitations:
    content.append(
        Paragraph(
            f"- {limitation}",
            styles["ReportBody"]
        )
    )

# --------------------------------------------------
# 11. GENERATE PDF
# --------------------------------------------------

pdf.build(content)

print("PDF report created successfully!")
print("File:", OUTPUT_FILE)
print("Total Orders:", total_orders)
print("Total Revenue:", round(total_revenue, 2))
print("Total Profit:", round(total_profit, 2))
print("Profit Margin:", round(profit_margin, 2))