"""
API router module for the  movie recommnedation system .

This module aggregates and organizes any route modules into a single APIRouter instance, 
making it easy to manage and include routes for various features.
"""

from fastapi import APIRouter
from .recommend_routes import router as reccomendation_router

router = APIRouter()

router.include_router(reccomendation_router, prefix="/api", tags=["Recommendations"])
