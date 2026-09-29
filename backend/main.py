from fastapi import FastAPI
from pydantic import BaseModel

from database import create_table, create_product, get_products


app = FastAPI(title="FlyRank 10x Solution")


class ProductCreate(BaseModel):
    name: str
    category: str
    price: float


create_table()


@app.get("/")
def home():
    return {
        "message": "FlyRank 10x Solution API is running"
    }


@app.post("/products")
def add_product(product: ProductCreate):

    product_id = create_product(
        product.name,
        product.category,
        product.price
    )

    return {
        "message": "Product created successfully",
        "product_id": product_id,
        "product": product
    }


@app.get("/products")
def list_products():
    return {
        "products": get_products()
    }