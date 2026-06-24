import os
import importlib


if __name__ == "__main__":
    data_dir = "/workspaces/databricks-e2e-project/data"
    os.makedirs(data_dir, exist_ok=True)

    sql_db = importlib.import_module("00_sql_db")
    sql_db.generate_data_for_sql_db()

    historical_orders = importlib.import_module("01_historical_orders")
    historical_orders.generate_historical_orders()

    reviews = importlib.import_module("02_reviews")
    reviews.generate_customer_reviews(review_percentage=0.01)