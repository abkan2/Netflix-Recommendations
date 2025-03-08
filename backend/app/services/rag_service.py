from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAIKEY"))

def generate_dynamic_description(title, director, cast, original_description):
    prompt = f"""
    Title: {title}
    Director: {director}
    Cast: {cast}
    Original description: {original_description}

    Write a single paragraph highlighting what makes this movie appealing in a friendly and concise tone.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Description not available at the moment."


def augment_movie_description(movie: dict) -> dict:
    """
    A function that simulates retrieval-augmented generation.
    - First we gather relevant info from the movie.
    - Then we call generate_dynamic_description for a custom summary.
    """
    title = movie.get("title", "unknown title")
    director = movie.get("director", "No director listed ")
    cast = movie.get("cast", "No cast listed")
    original_description = movie.get("description", "No description listed")

    #Generating GPT description
    gpt_description = generate_dynamic_description(title, director, cast,original_description)

    #storing the augmented description from GPT in the movies dict
    movie["augmented_description"] = gpt_description
    return movie