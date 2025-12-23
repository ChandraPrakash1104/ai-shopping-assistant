import pandas as pd

data = [
    {"id": 1, "title": "Red Running Shoe", "description": "Lightweight running shoe with cushioned sole", "price": 3499, "brand": "Nike", "image_url": "https://example.com/img1.jpg"},
    {"id": 2, "title": "Black Formal Shoe", "description": "Genuine leather formal shoes", "price": 4599, "brand": "Clarks", "image_url": "https://example.com/img2.jpg"},
    {"id": 3, "title": "Blue Sports T-shirt", "description": "Moisture-wicking sports t-shirt", "price": 899, "brand": "Adidas", "image_url": "https://example.com/img3.jpg"},
    {"id": 4, "title": "Wireless Headphones", "description": "Noise-cancelling over-ear headphones", "price": 6999, "brand": "Sony", "image_url": "https://example.com/img4.jpg"},
    {"id": 5, "title": "Smartwatch X", "description": "Basic smartwatch with heart-rate monitor", "price": 2999, "brand": "Xiaomi", "image_url": "https://example.com/img5.jpg"},
    {"id": 6, "title": "Trail Running Shoe", "description": "Rugged outsole for trail runs", "price": 4999, "brand": "Asics", "image_url": "https://example.com/img6.jpg"},
    {"id": 7, "title": "White Sneakers", "description": "Classic casual sneakers", "price": 1999, "brand": "Converse", "image_url": "https://example.com/img7.jpg"},
    {"id": 8, "title": "Black Hoodie", "description": "Comfortable cotton hoodie", "price": 1299, "brand": "H&M", "image_url": "https://example.com/img8.jpg"}
]

df = pd.DataFrame(data)
df.to_csv('products_sample.csv', index=False)