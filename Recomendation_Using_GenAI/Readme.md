# Next Gen Recommendation Systems (Personalized Recommendation System using Gen AI)

## Overview
This project focuses on building a **Next-Gen Personalized Recommendation System** using **Generative AI** for meal planning. It considers individual preferences, dietary requirements, and location to create tailored meal plans. Leveraging cutting-edge machine learning models, the system generates weekly plans, suggests alternatives, and ensures nutritional balance.

### Key Features
- **AI-Powered Meal Planning:** Personalized weekly meal plans based on location, cuisine, and dietary needs.
- **Detailed Nutritional Info:** Each meal includes calories, protein, carbs, fats, fiber, and sugar per 100 grams.
- **Alternative Suggestions:** Provides meal alternatives for variety while maintaining nutritional standards.
- **No Repeats:** Ensures no meal is repeated in the same week.
- **Customizable Parameters:** Configure temperature, top_k, and top_p for tailored outputs.
- **Real-World Data Evaluation:** Validates the system's outputs against real-world data for continuous improvement.

---

## New Addition: Real-World Data Evaluation
The project now includes real-world data analysis to evaluate system performance without prompt optimization. The **`Calculating_metrics.ipynb`** notebook provides insights into the system's accuracy and identifies areas for refinement.

### Key Insights
- **Performance Metrics:** Measures accuracy of generated meal plans compared to real-world data.
- **Nutritional Validation:** Verifies the balance and adequacy of suggested meals.
- **Gap Analysis:** Highlights discrepancies for targeted system enhancements.
- **Benchmarking:** Tracks improvements over time.

### Usage
1. Open the `Calculating_metrics.ipynb` file.
2. Run the notebook to evaluate system performance.
3. Analyze the output for actionable insights.

---

## Requirements
- Python 3.7+
- **Gradio**: For the user interface.
- **Google Generative AI**: Powered by `google.generativeai`.
- **Pandas**: For data handling.
- **Jupyter Notebook**: For running metrics evaluations.

### Install Dependencies
```bash
pip install gradio google-generativeai pandas notebook
genai.configure(api_key="YOUR_API_KEY")

generation_config = {
    "max_output_tokens": 2048,
    "temperature": 0.4,
    "top_k": 40,
    "top_p": 1,
}
response = generate_response(location="New York", cuisine="Italian", dietary_requirements="Diabetic Type 2")

├── app.py                  # Gradio interface and integration logic
├── meal_plan.py            # Core functions for meal generation
├── Calculating_metrics.ipynb # Notebook for real-world data evaluation
├── requirements.txt        # Project dependencies
├── sample_responses.json   # Example outputs from the system
├── README.md               # This file

python app.py

{
  "location": "New York",
  "cuisine": "Italian",
  "dietary_requirements": "Diabetic Type 2"
}

{
  "weekly_meal_plan": {
    "Monday": {
      "breakfast": {
        "name": "Oatmeal with Berries and Nuts",
        "nutrient_content_per_100g": {
          "calories": 150,
          "protein": 5,
          "carbs": 25,
          "fiber": 5,
          "fat": 5
        }
      }
    }
  }
}

