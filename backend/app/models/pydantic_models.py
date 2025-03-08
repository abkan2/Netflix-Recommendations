# backend/app/models/recommendation_model.py
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class RecommendationRequest(BaseModel):
    genre: Optional[str] = None
    rating: Optional[str] = None

class Movie(BaseModel):
    id: str
    type: str
    title: str
    director: Optional[str]
    cast: Optional[str]
    country: Optional[str]
    date_added: Optional[str]
    release_year: int
    rating: Optional[str]
    duration: Optional[str]
    genres: Optional[str]
    description: Optional[str]
    augmented_description: Optional[str]

class RecommendationResponse(BaseModel):
    recommendations: List[Movie]
