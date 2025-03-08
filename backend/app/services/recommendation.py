import pandas as pd
import os
import random
from typing import List,Dict,Any


#Path to the netflix csv file
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'netflix_titles.csv')


#loading csv data 
netflix_df = pd.read_csv(
    DATA_PATH,
    header=None,
    names=[
        "id", "type", "title", "director", "cast", "country", 
        "date_added", "release_year", "rating", "duration", 
        "genres", "description"
    ],
    skiprows=1,  # If your CSV has a header row, adjust accordingly
)
netflix_df.fillna("", inplace=True)


def get_recommendations(genre: str = None, rating: str = None, num_recs: int = 5) -> List[Dict[str, Any]]:
    """
    Basic recommendation logic: filter the DataFrame by genre & rating, 
    then randomly sample results.
    """
    filtered_df = netflix_df

    if genre:
        # Check if row's 'genres' column contains the genre string
        filtered_df = filtered_df[filtered_df['genres'].str.contains(genre, case=False, na=False)]
    
    if rating:
        # Check if row's 'rating' column matches
        filtered_df = filtered_df[filtered_df['rating'].str.contains(rating, case=False, na=False)]
    
    if filtered_df.empty:
        return []

    # Randomly sample up to `num_recs` results
    sampled = filtered_df.sample(n=min(num_recs, len(filtered_df)))
    return sampled.to_dict(orient="records")