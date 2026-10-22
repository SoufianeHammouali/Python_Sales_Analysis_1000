# Sales Performance Analysis — Python | 2025

## Project Overview

This project analyzes 1,000 sales orders from January to December 2025 using Python to identify revenue trends, profitability drivers, product performance, and business opportunities.

## Tools & Technologies

- Python
- Pandas — data cleaning, validation, and analysis
- Matplotlib — data visualization
- OpenPyXL — Excel data import
- ReportLab — PDF report generation

## Data Cleaning & Validation

- Removed 5 duplicate records from the original 1,005 rows.
- Handled missing customer IDs and city values using `Unknown`.
- Validated quantities, revenue, profit calculations, discounts, dates, and order IDs.
- Prepared a clean dataset containing 1,000 orders.

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Revenue | 7,139,581 MAD |
| Total Profit | 1,900,950.98 MAD |
| Profit Margin | 26.63% |
| Total Orders | 1,000 |

## Key Business Insights

- **Electronics** generated the highest revenue (2.93M MAD).
- **Furniture** achieved the highest profit margin (27.11%).
- **Smartphone** was the top product by revenue (931K MAD).
- **Rabat** generated the highest revenue among cities (1.05M MAD).
- **Marketplace** achieved the highest sales-channel profit margin (27.35%).
- **Corporate** was the most profitable customer segment by margin (27.90%).
- **February** recorded the highest monthly revenue, while September recorded the lowest.

## Project Deliverables

- Python scripts for data preparation, business analysis, visualization, and reporting
- Cleaned sales dataset
- Business insights and recommendations
- Sales performance charts
- Final PDF analysis report

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Python scripts in order:

```bash
python 01_data_exploration.py
python 02_sales_analysis.py
python sales.visualization.py
python 04_final_report.py
```

## Limitations

The dataset covers only 2025. Missing city and customer information was labeled as `Unknown`. Findings describe observed patterns and do not establish causation.