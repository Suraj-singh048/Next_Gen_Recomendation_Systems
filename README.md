# Next Gen Recommendation Systems

Welcome to the **Next Gen Recommendation Systems** project! In this repository, we developed three distinct recommendation systems, each exploring a different approach and catering to unique use cases. Here’s a brief overview of the project structure, methods, and goals.

---

## Project Overview

1. **Cross-Domain Recommendation System (Movies & Books)**
2. **Generative AI-Based Personalized Recommendation System**
3. **Session-Based Recommendation System**

Each system serves a unique purpose and is built with different data-processing pipelines, machine learning models, and evaluation metrics. Additionally, we provide a responsive web application, **FlexRead**, for user interaction with these recommendations.

---

### 1. Cross-Domain Recommendation System (Movies & Books)

This system aims to bridge recommendations across two domains—books and movies—by creating a genre-based "bridge" that allows us to recommend items in one domain (e.g., movies) based on items from another (e.g., books).

- **Custom Genre Mapping**: To connect books and movies, we categorized both into custom genre types that capture similar thematic elements across domains.
- **Modeling Approach**: We used a **RoBERTa model** for text-based embedding of content and a **K-Nearest Neighbors (KNN)** approach to recommend items within these custom genres.
- **FlexRead**: Users can view, filter, and interact with recommendations through the **FlexRead** webpage, which is designed to be responsive and user-friendly.
- ![FlixRead]("C:\Users\suraj\Pictures\Screenshots\FlixRead.png")

### 2. Generative AI-Based Personalized Recommendation System

With the rise of Generative AI, we implemented a recommendation system focused on personalized recommendations, such as daily meal suggestions based on user preferences and needs.

- **Personalization Factors**: Recommendations consider user **location, cuisine preferences, lifestyle, and health requirements** to deliver highly personalized suggestions.
- **Model Evaluation**: We aim to assess the accuracy and relevancy of AI models like **Gemini** and **Ollama** by comparing generated recommendations with real-life user data.
- **Future Directions**: Ongoing research includes measuring the accuracy and personalization of these AI models and enhancing our models’ responsiveness to user-specific needs.

### 3. Session-Based Recommendation System

The goal of this recommendation system is to suggest the next item based on a user’s current session and past activities, such as clicks, cart additions, or purchases.

- **Modeling Approach**: Built using **SR-GNN** (Session-Based Graph Neural Network) and **PyGeometry**, we designed a data pipeline to preprocess session data and train a model for next-item recommendations.
- **Performance Metrics**: Currently, the system achieves a **hit rate of 4 out of 10** and an accuracy rate of **20-30%** in predicting relevant items.
- **Applications**: This system is valuable for e-commerce, where real-time session data can drive personalized recommendations.

---

## Directory Structure

```plaintext
.
├── cross_domain_recommendation/
│   ├── genre_mapping/
│   ├── models/
│   └── roberta_knn.py
├── gen_ai_recommendation/
│   ├── gemini_eval/
│   ├── ollama_eval/
│   └── personalized_meal_recommender.py
├── session_based_recommendation/
│   ├── data_pipeline/
│   ├── sr_gnn_model/
│   └── session_recommender.py
├── flexread/
│   ├── static/
│   ├── templates/
│   └── app.py
└── README.md
```

---

## Future Enhancements

- **Cross-Domain System**: Expand to additional content domains (e.g., music, podcasts).
- **Generative AI System**: Extend AI-based recommendations to broader lifestyle suggestions (e.g., workout plans).
- **Session-Based System**: Improve accuracy and explore real-time feedback integration for instant recommendations.



Thank you for exploring our **Next Gen Recommendation Systems**!
