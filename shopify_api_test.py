import os
import shopify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Shopify credentials from environment variables
shop_url = os.getenv('SHOPIFY_SHOP_URL')
api_password = os.getenv('SHOPIFY_API_PASSWORD')
api_version = os.getenv('SHOPIFY_API_VERSION', '2021-07')

# Authenticate with the Shopify store
session = shopify.Session(shop_url=shop_url,
                          version=api_version,
                          token=api_password)

shopify.ShopifyResource.activate_session(session)

# Retrieve orders
orders = shopify.Order.find()

# Iterate through orders and retrieve associated items
for order in orders:
    print(f"Order ID: {order.id}")
    print(f"Created at: {order.created_at}")
    print("Line Items:")
    
    # Retrieve line items for each order
    for line_item in order.line_items:
        print(f"  - Product ID: {line_item.product_id}")
        print(f"    Title: {line_item.title}")
        print(f"    Quantity: {line_item.quantity}")
        print(f"    Price: {line_item.price}")
        print("------------------------")

    print("\n")

# Note: This is a basic example, and you may need to customize it based on your specific requirements.
