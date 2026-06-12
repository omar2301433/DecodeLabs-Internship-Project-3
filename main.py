from fastapi import FastAPI , status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Decodelabs Project 1 API"}

@app.get("/products")
def get_products():
    return {"products": []}


class Product(BaseModel):
    name: str
    price: float

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "product": product
    }