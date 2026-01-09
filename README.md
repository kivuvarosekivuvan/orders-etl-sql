# Orders ETL + SQL Checks (Mini Project) 🧪🧩

This repo is a small, working ETL-style pipeline:

- 🧾 Take raw data from a CSV file (an **orders** dataset)
- 🧽 Clean it (fix formats, remove duplicates, handle missing values)
- 🗃️ Load it into a relational database
- 🧿 Run SQL checks to confirm the data is correct
- 📈 Run SQL queries to get simple insights (totals, trends, top items)

This project focuses on solid data habits: clean inputs, clean outputs, and clear checks.

---

## What’s inside 🗂️

- `data/raw/` → raw CSV data (example: `orders.csv`)
- `data/processed/` → cleaned output (optional)
- `sql/`
  - `01_schema.sql` → table setup
  - `02_validation.sql` → data quality checks (duplicates, missing fields, invalid numbers)
  - `03_analytics.sql` → simple insight queries (totals, trends, top products)
- `src/` → pipeline scripts (extract → transform → load)

---

## Pipeline flow (simple) 🧵

1. **Extract** 🧾: Read the raw CSV file  
2. **Transform** 🧽: Clean and standardize the data  
3. **Load** 🗃️: Insert clean data into a relational database  
4. **Validate** 🧿: Run SQL checks to confirm data quality  
5. **Analyze** 📈: Run SQL queries to get insights  

---

## How to run 🛠️

1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2) Install dependencies 🧰

```bash
pip install -r requirements.txt
```

## 3) Run the pipeline (CSV → clean → database) 🧾➡️🗃️

```bash
python src/pipeline.py
```

## 4) Run SQL validation + analytics queries 🧿📈

```bash
python src/run_sql.py
```





## Example output ✅🧾

This is a real run result from this repo:

- **Raw rows:** 15  
- **Clean rows:** 12  
- **Validation checks:** all OK (0 bad rows)

Sample analytics results:
- **Total orders:** 12  
- **Total revenue:** 339.50  
- **Top products by revenue:**
  - Wireless Earbuds: 90.00
  - Running Shoes: 60.00
  - Bluetooth Speaker: 55.00
- **Orders by channel:**
  - web: 6
  - mobile: 4
  - partner: 2

What this proves (simple English):
- The pipeline removed or handled bad records (duplicates, missing date, negative amount, missing required fields)
- SQL data checks pass cleanly (0 errors)
- The SQL insights make sense and are useful for business

---

## Data quality checks (SQL) 🧿

Validation checks for common problems like:

- **Duplicate order IDs** (example: the same `order_id` appears twice)  
- **Missing required fields** (example: missing `order_date` or `amount`)  
- **Invalid numbers** (example: negative `amount` or `quantity = 0`)  
- **Sanity checks** (example: `amount` should match `quantity × unit_price`)  

---

## Analytics queries (SQL) 📈

The analytics step answers questions like:

- **Total orders and total revenue** (example: “How much did we make?”)  
- **Revenue trend over time** (example: “Which days/months were strongest?”)  
- **Top products by revenue** (example: “Which items earn the most?”)  
- **Revenue by city** (example: “Which city buys the most?”)  
- **Average order value** (example: “What’s the usual spend per order?”)  
- **Orders by channel** (example: “Web vs mobile vs partner — what wins?”)  

---

## Why I built this 🧠

I’m building practical skills for data & AI-focused software work:

- Working with structured data  
- SQL validation and analytics  
- Building reliable ETL-style workflows  
- Writing clear, repeatable documentation  

---

## Status 🧷

Working ✅  
Next updates:
- Add a slightly bigger dataset
- Add screenshots of the outputs in the README
