import pandas as pd
import random
from datetime import datetime, timedelta

products = [
    "Bed",
    "Dining Table",
    "Office Chair",
    "Wardrobe",
    "Study Table",
    "Sofa",
    "Bookshelf",
    "Coffee Table"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

categories = {
    "Bed":"Furniture",
    "Dining Table":"Furniture",
    "Office Chair":"Furniture",
    "Wardrobe":"Furniture",
    "Study Table":"Furniture",
    "Sofa":"Furniture",
    "Bookshelf":"Furniture",
    "Coffee Table":"Furniture"
}

rows = []

start_date = datetime(2022,1,1)

for i in range(10000):

    product = random.choice(products)

    quantity = random.randint(1,20)

    unit_price = random.randint(2000,50000)

    discount = random.randint(0,20)

    inventory = random.randint(50,500)

    marketing = random.randint(1000,10000)

    order_date = start_date + timedelta(
        days=random.randint(0,1460)
    )

    revenue = quantity * unit_price

    rows.append([
        i+1,
        order_date,
        product,
        categories[product],
        random.choice(regions),
        quantity,
        unit_price,
        discount,
        inventory,
        marketing,
        revenue
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Order_ID",
        "Order_Date",
        "Product_Name",
        "Category",
        "Region",
        "Quantity",
        "Unit_Price",
        "Discount",
        "Inventory_Available",
        "Marketing_Spend",
        "Revenue"
    ]
)

df.to_csv(
    "default_dataset.csv",
    index=False
)

print("Dataset Generated")