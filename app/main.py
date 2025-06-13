# # from fastapi import FastAPI
# # from app.database.connection import test_connection

# # app = FastAPI()

# # @app.on_event("startup")
# # async def startup_db():
# #     await test_connection()

# # @app.get("/")
# # async def home():
# #     return {"message": "FastAPI + MongoDB Connected!"}

# # 


from fastapi import FastAPI
from app.database.connection import test_connection
from app.routes.product_routes import router as product_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # For development only. Use specific origins in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await test_connection()

@app.get("/")
async def home():
    return {"message": "FastAPI + MongoDB Connected!"}

app.include_router(product_router)


# test_main.py
# from fastapi import FastAPIs

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello FastAPI!"}
