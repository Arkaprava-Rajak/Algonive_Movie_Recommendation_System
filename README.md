# Algonive_Movie_Recommendation_System
A hybrid recommendation system that suggests movies using a combination of content-based filtering and collaborative (user-based) filtering techniques. The app is built with Python and Streamlit, featuring an intuitive interface and real-time movie poster fetching via the TMDB API.
.

🧠 Features:


  *🎯 Content-Based Filtering: Suggests movies similar to the selected one using movie metadata (overview, genre, cast, etc.).
  
  *👥 Collaborative Filtering: Learns from user preferences and ratings to recommend movies that like-minded users enjoyed.
  
  *🧩 Hybrid Model: Merges both content and collaborative insights to overcome the limitations of individual approaches.
  
  *🖼️ Dynamic Poster Display: Fetches movie posters directly from the TMDB API.
  
  *⚡ Interactive Streamlit Interface: Simple, fast, and user-friendly.

🧰 Tech Stack

    Python
    
    Streamlit
    
    Scikit-learn
    
    Surprise (SVD for collaborative filtering)
    
    Pickle
    
    TMDB API

🚀 How It Works

Content-Based Module: Calculates similarity between movies using TF-IDF or embeddings with cosine similarity.

Collaborative Module: Predicts unseen movie ratings using matrix factorization (SVD).

Hybrid Layer: Combines both similarity and predicted rating scores to produce final recommendations.

UI Layer: Built with Streamlit for seamless interaction and visualization.

💡 Future Enhancements

  -Use Sentence-BERT embeddings for better semantic similarity.
  
  -Include user rating history and demographics for personalization.
  
  -Add model evaluation metrics like Precision@K and Recall@K.
  
  -Deploy on Streamlit Cloud for live access.

📸 Demo:
<img width="1919" height="1011" alt="Screenshot 2025-10-30 123903" src="https://github.com/user-attachments/assets/69c3330b-967f-4a52-8cdf-e5cb2a1834fc" />

<img width="1920" height="1080" alt="Screenshot 2025-10-30 123958" src="https://github.com/user-attachments/assets/701af5aa-e6db-4fbc-9c48-b21a430731c8" />

