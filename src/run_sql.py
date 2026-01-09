from __future__ import annotations

import os
from sqlalchemy import create_engine, text


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "warehouse.db")


def run_sql_file(path: str) -> None:
    engine = create_engine(f"sqlite:///{DB_PATH}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    statements = [s.strip() for s in content.split(";") if s.strip()]
    print(f"\n=== Running: {os.path.basename(path)} ===")

    with engine.begin() as conn:
        for i, stmt in enumerate(statements, start=1):
            result = conn.execute(text(stmt))
            rows = result.fetchall() if result.returns_rows else []
            if rows:
                print(f"\nQuery {i} returned {len(rows)} row(s):")
                for r in rows[:10]:
                    print(r)
                if len(rows) > 10:
                    print("... (truncated)")
            else:
                print(f"Query {i}: OK (0 rows)")


def main() -> None:
    validation = os.path.join(BASE_DIR, "sql", "02_validation.sql")
    analytics = os.path.join(BASE_DIR, "sql", "03_analytics.sql")
    run_sql_file(validation)
    run_sql_file(analytics)


if __name__ == "__main__":
    main()
