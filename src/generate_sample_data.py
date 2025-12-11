"""
Generate a realistic sample sales dataset and save it to:
    data/sample_sales.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from pathlib import Path

# -----------------------------
# Output Path Setup
# -----------------------------
BASE = Path(__file__).resolve().parents[1]   # project root
DATA_DIR = BASE / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "sample_sales.csv"

# -----------------------------
# Random Seed for Reproducibility
# -----------------------------
np.random.seed(42)

# -----------------------------
# Dataset Config
# -----------------------------
NUM_ROWS = 500

products = ["Widget A", "Widget B", "Gadget X", "Gadget Y"]
regions = ["North", "South", "East", "West"]

start_date = datetime(2024, 1, 1)

rows = []

# -----------------------------
# Generate data rows
# -----------------------------
for i in range(NUM_ROWS):

    order_date = start_date + timedelta(days=np.random.randint(0, 90))

    product = np.random.choice(products)
    region = np.random.choice(regions)

    # Generate realistic pricing
    if product in ["Widget A", "Widget B"]:
        unit_price = round(np.random.normal(55, 6), 2)
    else:
        unit_price = round(np.random.normal(80, 10), 2)

    quantity = np.random.randint(1, 6)

    # Random missing values
    customer_id = np.random.choice(
        [f"CUST{np.random.randint(1000, 1300)}", None],
        p=[0.95, 0.05]
    )

    discount = np.random.choice(
        [0, 5, 10, 15, None],
        p=[0.60, 0.20, 0.10, 0.05, 0.05]
    )

    rows.append({
        "order_id": f"ORD{i+1:04d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "product": product,
        "region": region,
        "unit_price": unit_price,
        "quantity": quantity,
        "customer_id": customer_id,
        "discount_pct": discount
    })

# -----------------------------
# Convert to CSV
# -----------------------------
df = pd.DataFrame(rows)
df.to_csv(OUT_PATH, index=False)

print("✔ Sample dataset generated successfully!")
print(f"📄 Saved at: {OUT_PATH}")
print(f"📊 Rows generated: {NUM_ROWS}")
