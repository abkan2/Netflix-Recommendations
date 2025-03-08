# app/main.py
"""
Entry point for service
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.routes import router
import httpx
# from app.endpoints import recommend_routes, product_routes

app = FastAPI(title="Netflix Movie Recommendation Service")

# Allow cross-origin requests for development purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

if __name__ == "__main__":

    print("httpx version:", httpx.__version__)
    uvicorn.run("main:app", reload=True)
