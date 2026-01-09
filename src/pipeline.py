from __future__ import annotations

import os
import pandas as pd
from sqlalchemy import create_engine, text


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_CSV = os.path.join(BASE_DIR, "data", "raw", "orders.csv")
DB_PATH = os.path.join(BASE_DIR, "data", "warehouse.db")
SCHEMA_SQL = os.path.join(BASE_DIR, "sql", "01_schema.sql")


def extract(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing raw CSV: {path}")
    return pd.read_csv(path)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Trim text fields
    text_cols = ["order_id", "customer_id", "order_date", "product_name", "product_category", "city", "channel"]
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # Fix numeric types
    for col in ["quantity", "unit_price", "amount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Parse date, keep as YYYY-MM-DD string for SQLite
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.strftime("%Y-%m-%d")

    # Handle missing category
    df["product_category"] = df["product_category"].replace({"": None})
    df["product_category"] = df["product_category"].fillna("Unknown")

    # Drop rows missing key required fields
    df = df.dropna(subset=["order_id", "customer_id", "order_date", "product_name", "quantity", "unit_price", "amount", "city", "channel"])

    # Drop duplicates by order_id (keep first)
    df = df.drop_duplicates(subset=["order_id"], keep="first")

    # Remove invalid numbers
    df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0) & (df["amount"] >= 0)]

    # Make amount consistent with quantity * unit_price
    df["amount"] = (df["quantity"] * df["unit_price"]).round(2)

    # Keep clean column order
    return df[
        ["order_id", "customer_id", "order_date", "product_name", "product_category",
         "quantity", "unit_price", "amount", "city", "channel"]
    ].copy()


def load(df: pd.DataFrame, db_path: str) -> None:
    engine = create_engine(f"sqlite:///{db_path}")

    # Create schema
    with open(SCHEMA_SQL, "r", encoding="utf-8") as f:
        schema = f.read()

    with engine.begin() as conn:
        for stmt in schema.split(";"):
            s = stmt.strip()
            if s:
                conn.execute(text(s))

        # Make pipeline re-runnable (idempotent): clear table before insert
        conn.execute(text("DELETE FROM orders;"))

    df.to_sql("orders", engine, if_exists="append", index=False)


def main() -> None:
    raw = extract(RAW_CSV)
    clean = transform(raw)

    print(f"Raw rows: {len(raw)} | Clean rows: {len(clean)}")
    load(clean, DB_PATH)
    print(f"Loaded into DB: {DB_PATH}")


if __name__ == "__main__":
    main()
