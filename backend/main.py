from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

from database import (
    create_table,
    create_product,
    get_products,
    get_product,
    get_products_by_category
)

from auth import login_user, get_current_user

class LoginRequest(BaseModel):
    email: str
    password: str

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
def add_product(
    product: ProductCreate,
    authorization: str = Header(None)
):

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    token = authorization.replace("Bearer ", "", 1)

    try:
        get_current_user(token)
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

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

@app.get("/products/{product_id}")
def get_single_product(product_id: int):

    product = get_product(product_id)

    if product is None:
        return {
            "message": "Product not found"
        }

    return {
        "product": product
    }

@app.get("/products/category/{category}")
def products_by_category(category: str):

    products = get_products_by_category(category)

    return {
        "category": category,
        "products": products
    }

@app.post("/auth/login")
def login(request: LoginRequest):

    try:
        return login_user(request.email, request.password)

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
@app.get("/auth/me")
def current_user(authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Authorization header required"
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Use Bearer token"
        )

    token = authorization.replace("Bearer ", "", 1)

    try:
        user = get_current_user(token)

        return {
            "user_id": user.id,
            "email": user.email
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )