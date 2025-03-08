# app/endpoints/recommend_routes.py

from fastapi import APIRouter, HTTPException
from app.models.pydantic_models import RecommendationRequest
from app.services.recommendation import get_recommendations
from app.models.pydantic_models import RecommendationRequest, RecommendationResponse, Movie
from app.services.rag_service import augment_movie_description
router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
def recommend_movies(request: RecommendationRequest):
    # Get basic recommendations
    recs = get_recommendations(genre=request.genre, 
                               rating=request.rating, 
                               num_recs=5)
    
    if not recs:
        raise HTTPException(status_code=404, detail="No recommendations found for the given preferences.")
    
    # Augment each recommended movie with RAG
    augmented_recs = [augment_movie_description(movie) for movie in recs]
    
    # Convert dicts to Pydantic model `Movie`
    movies = [Movie(**movie) for movie in augmented_recs]
    return RecommendationResponse(recommendations=movies)

