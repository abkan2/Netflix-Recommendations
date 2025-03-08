// RecommendationsPage.jsx
import React, { useState } from "react";
import axios from "axios";
import "./index.css";

function RecommendationsPage() {
  const [genre, setGenre] = useState("");
  const [rating, setRating] = useState("");
  const [releaseYear, setReleaseYear] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setLoading(true);
    setError("");
    try {
      // Prepare the payload. Adjust keys as needed to match backend expectations.
      const payload = { genre, rating};
      const response = await axios.post("http://localhost:8000/api/recommend", payload);
      setRecommendations(response.data.recommendations);
      setSelectedMovie(null); // Reset selected movie on new fetch
    } catch (err) {
      setError("Error fetching recommendations. Please try again.");
      console.error(err);
    }
    setLoading(false);
  };

  const handleSelectMovie = (movie) => {
    setSelectedMovie(movie);
  };

  return (
    <div className="page-container">
      <h1 className="page-title">Netflix Recommendations</h1>
      <p className="instructions">Make your selections below</p>
      
      <div className="input-container">
        <div className="input-field">
          <label htmlFor="genre">Genre</label>
          <select
            id="genre"
            value={genre}
            onChange={(e) => setGenre(e.target.value)}
          >
            <option value="">--Select Genre--</option>
            <option value="Adventure">Adventure</option>
            <option value="Action">Action</option>
            <option value="Comedy">Comedy</option>
            <option value="Mystery">Mystery</option>
            <option value="Horror">Horror</option>
          </select>
        </div>
        
        <div className="input-field">
          <label htmlFor="rating">Rating</label>
          <select
            id="rating"
            value={rating}
            onChange={(e) => setRating(e.target.value)}
          >
            <option value="">--Select Rating--</option>
            <option value="pg-13">PG-13</option>
            <option value="TV-MA">TV-MA</option>
            <option value="R">R</option>
            <option value="tv-14">TV-14</option>
            <option value="tv-pg">TV-PG</option>
          </select>
        </div>
        
      </div>

      <button
        className="recommendations-button"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Loading..." : "Get Recommendations"}
      </button>

      {error && <div className="error-message">{error}</div>}

      <div className="recommendations-list">

        {recommendations.length > 0 ? (
          <ul>
            {recommendations.map((movie) => (
              <li
                key={movie.id}
                onClick={() => handleSelectMovie(movie)}
                className="recommendation-item"
              >
                {movie.title} - {movie.rating}
              </li>
            ))}
          </ul>
        ) : (
          <p>No recommendations yet. Try adjusting your selections and click "Get Recommendations".</p>
        )}
      </div>

      {selectedMovie && (
        <div className="movie-card">
          <h2>{selectedMovie.title}</h2>
          <p><strong>Type:</strong> {selectedMovie.type}</p>
          <p><strong>Rating:</strong> {selectedMovie.rating}</p>
          <p>{selectedMovie.augmented_description}</p>
          
        </div>
      )}
    </div>
  );
}

export default RecommendationsPage;
