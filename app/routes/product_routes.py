# from fastapi import APIRouter
# from app.models.product_model import Product
# from app.database.connection import database

# router = APIRouter()

# @router.post("/products")
# async def create_product(product: Product):
#     result = await database["products"].insert_one(product.dict())
#     return {"id": str(result.inserted_id), "message": "Product added successfully"}


from fastapi import APIRouter, HTTPException
from app.models.product_model import Product
from app.database.connection import product_collection
from bson import ObjectId

router = APIRouter()

# 🔽 Convert Mongo _id to string
# def product_serializer(product) -> dict:
#     return {
#         "id": str(product["_id"]),
#         "name": product["name"],
#         "price": product["price"],
#         "description": product.get("description", "")
#     }

def product_serializer(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "image": product.get("image", "")
    }

@router.post("/products")
async def create_product(product: Product):
    result = await product_collection.insert_one(product.dict())
    return { "id": str(result.inserted_id) }

@router.get("/products")
async def get_products():
    products = []
    async for product in product_collection.find():
        products.append(product_serializer(product))
    return products

@router.get("/products/{id}")
async def get_product(id: str):
    product = await product_collection.find_one({"_id": ObjectId(id)})
    if product:
        return product_serializer(product)
    raise HTTPException(status_code=404, detail="Product not found")

@router.put("/products/{id}")
async def update_product(id: str, updated: Product):
    result = await product_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": updated.dict()}
    )
    if result.modified_count == 1:
        return {"msg": "Product updated"}
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/products/{id}")
async def delete_product(id: str):
    result = await product_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"msg": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

@router.get("/products")
async def get_all_products():
    products = []
    async for product in product_collection.find():
        products.append(product_serializer(product))
    return products


