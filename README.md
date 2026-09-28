# E-commerce Data Visualization with SQL

This project transforms raw e-commerce transaction logs into high-impact visual charts. It includes automated exploratory data analysis (EDA), product performance insights, and marketing attribution.

## Project structure

- `visualize_data.py` — generates the charts from `orders_dataset.csv`
- `orders_dataset.csv` — sample e-commerce transaction data
- `requirements.txt` — Python dependencies
- `README.md` — project overview and usage steps

## Features

- Product revenue analysis by category
- Order fulfillment status distribution
- Referral source attribution

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python visualize_data.py
```

This creates the `visualizations/` folder and saves the generated charts:

- `visualizations/product_revenue.png`
- `visualizations/order_status_distribution.png`
- `visualizations/traffic_acquisition.png`
