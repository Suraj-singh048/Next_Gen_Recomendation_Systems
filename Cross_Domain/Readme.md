

# **Cross-Domain Recommendation System**  

## **Introduction**  
The Cross-Domain Recommendation System is an innovative machine learning application designed to connect two distinct content domains—in this case, books and movies. By utilizing genre-based mapping, natural language processing, and recommendation algorithms, the system enables users to explore items from one domain based on their preferences in the other.  

This project leverages a transformer-based deep learning model (RoBERTa) for genre classification and a K-Nearest Neighbors (KNN) algorithm for cross-domain recommendations. The recommendations are presented through a user-friendly web interface, allowing users to filter, explore, and receive personalized suggestions.  

---

## **Features**  

### 1. **Unified Genre Mapping**  
- The project manually defines 20 major genres (e.g., Action, Drama, Fantasy, etc.) to bridge the genre differences between books and movies.  
- Both datasets are mapped to this unified genre space, enabling cross-domain analysis and recommendations.  

### 2. **Transformer-Based Genre Classifier**  
- **Model**: RoBERTa (a transformer architecture optimized for NLP tasks).  
- **Task**: Predict the major genre(s) of a book based on its description.  
- **Training Data**: Book descriptions and associated genres from the books dataset.  

### 3. **K-Nearest Neighbors (KNN) Recommendation Engine**  
- **Input**: Genre predictions and metadata from the RoBERTa model.  
- **Output**: Movies that align with the book’s major genre(s).  
- **Recommendation Tiers**:  
  - 5 very close matches (high similarity in genre and description).  
  - 3 close matches (moderate similarity).  
  - 2 recommendations based on previous user searches.  

### 4. **Interactive Web Interface**  
- **Filters**: Users can filter books and movies by genres, popularity, or other metadata.  
- **Search**: Allows users to search for a book or movie and receive tailored recommendations.  
- **Dynamic Recommendations**: Clicking on a book suggests 10 movies with varying levels of relevance.  

---

## **System Architecture**  

### **Data Flow**  
1. **Data Preparation**:  
   - Raw datasets of books and movies are preprocessed.  
   - Genres are mapped to the 20 unified categories.  

2. **Model Training**:  
   - RoBERTa is fine-tuned on book descriptions to classify genres.  

3. **Cross-Domain Recommendation**:  
   - KNN recommends movies by calculating similarities between book genres and movie metadata.  

4. **Web Application**:  
   - Flask-based frontend integrates model predictions and user queries for real-time interaction.  

---

## **File Structure**  

### **Key Files**  
1. `classifier.ipynb`:  
   - Contains code for training the RoBERTa model on book descriptions.  
   - Outputs the predicted genres for each book.  

2. `MovieBookGenreClassifier.ipynb`:  
   - Prepares and maps book and movie genres to the 20 major categories.  
   - Includes data exploration and visualization scripts.  

3. `cross-predictor.ipynb`:  
   - Implements the recommendation logic using KNN.  
   - Connects book genres with movie metadata to generate recommendations.  

4. `app.py`:  
   - Hosts the web interface.  
   - Integrates backend model predictions with the frontend.  

5. `data/`:  
   - Directory containing raw and processed datasets for books and movies.  

---

## **Datasets**  

### **Books Dataset**  
- **Fields**:  
  - Title, Author, Description, Genre, Ratings, etc.  
- **Purpose**: Used to train the RoBERTa model and as input for recommendations.  

### **Movies Dataset**  
- **Fields**:  
  - Title, Description, Genre, Director, Release Year, etc.  
- **Purpose**: Used as the recommendation target for the system.  

---

## **How to Run**  

### **Step 1: Install Dependencies**  
Run the following command to install required Python libraries:  
```bash
pip install numpy pandas scikit-learn transformers flask matplotlib
```  

### **Step 2: Prepare the Datasets**  
Ensure the processed book and movie datasets are stored in the `data/` directory.  

### **Step 3: Train the Genre Classifier**  
Open and run the `classifier.ipynb` notebook to fine-tune the RoBERTa model and predict genres for the books dataset.  

### **Step 4: Classify Genres and Train the Recommender**  
Run `MovieBookGenreClassifier.ipynb` to:  
- Map genres to the 20 unified categories.  
- Visualize and validate genre classification.  

Run `cross-predictor.ipynb` to train the KNN recommendation engine and test cross-domain recommendations.  

### **Step 5: Deploy the Web Application**  
Use the Flask app for real-time interaction:  
```bash
python app.py
```  
Access the app at `http://127.0.0.1:5000/`.  

---

## **Example Scenarios**  

### **Scenario 1: Book-to-Movie Recommendations**  
- Search for a book (e.g., *The Hobbit*).  
- The system predicts the genre (e.g., Fantasy) and recommends 10 movies (e.g., *The Lord of the Rings*).  

### **Scenario 2: Filtering Results**  
- Filter movies and books by genres (e.g., Action, Romance).  
- Receive results tailored to the selected genres.  

---

## **Challenges Faced**  
1. **Genre Unification**: Balancing specificity and overlap across genres for two distinct datasets.  
2. **Dataset Limitations**: Ensuring robust model performance on limited data.  
3. **Performance Optimization**: Fine-tuning RoBERTa efficiently to prevent overfitting.  

---

## **Future Scope**  
1. Expand the dataset to include more books and movies for improved accuracy.  
2. Integrate additional domains like music or video games for a comprehensive recommendation system.  
3. Incorporate user feedback into the recommendation pipeline for dynamic personalization.  
4. Use advanced embedding techniques (e.g., Sentence Transformers) for enhanced similarity calculations.  

---

## **Technologies Used**  
- **Languages**: Python  
- **Libraries**: Transformers, Scikit-learn, Flask, Pandas, NumPy  
- **Models**: RoBERTa, KNN  
- **Frontend**: HTML, CSS, JavaScript (via Flask templates)  

---

## **Contributors**  
- **Suraj Singh**  

---
