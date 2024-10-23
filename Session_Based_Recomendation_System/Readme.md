# Session-Based Recommendation System

## Overview

This repository contains a project focused on implementing a **Session-Based Recommendation System** using **Session-based Graph Neural Networks (SR-GNN)**. The model is designed to recommend the next item a user is likely to interact with based on their session history. It is built using the **PyTorch Geometric (PyG)** library on top of **PyTorch** and utilizes real-world **Retail Rocket E-commerce Dataset**.

### Key Features:
- **Session-Based Recommendations**: Predicts the next item a user is likely to view based on their current session.
- **Graph Neural Networks (GNN)**: Utilizes SR-GNN to learn item embeddings and session representations.
- **Dynamic Sessions**: Session data is dynamically grouped by user interaction timeframes.
- **Performance**: Provides competitive results compared to traditional models such as GRU4Rec or NARM.

## Requirements

To run the project, ensure you have the following dependencies installed:

- **Python 3.7+**
- **PyTorch**
- **PyTorch Geometric**
- **Pandas** and **Matplotlib** for data manipulation and visualization.

### Install Dependencies
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
pip install torch-scatter torch-sparse -f https://data.pyg.org/whl/torch-2.3.0+cu118.html
pip install torch-geometric
pip install matplotlib pandas
```

## Project Structure

1. **Data Preprocessing**:
   - Preprocesses the **Retail Rocket dataset** to generate sessions by grouping interactions within a one-hour window.
   - Filters out "view" events and users with single interactions.
   
2. **Session Graph Construction**:
   - Converts user interactions within a session into graph structures.
   - Each session is treated as a directed graph where nodes represent items and edges represent the sequence of item interactions.

3. **Graph Neural Network Model**:
   - Implements **Gated Graph Neural Networks (GG-NN)** for item and session embedding learning.
   - A **Gated Recurrent Unit (GRU)** refines session representations by applying a soft attention mechanism.
   
4. **Training and Evaluation**:
   - The model is trained to predict the next item in a session based on the learned session embeddings.
   - Evaluation includes **Hit@10** and **Next Item Prediction Accuracy**.

## Dataset

The **Retail Rocket Dataset** is used for this project. It consists of 2.75M interactions (view, add-to-cart, transaction) from 1.4M users. The dataset includes item properties describing over 417,000 unique items.

- You can download the dataset from [Kaggle](https://www.kaggle.com/retailrocket/ecommerce-dataset).

## How to Run

### 1. Data Preprocessing
Load the dataset, filter the relevant events, and split it into sessions:
```python
events_df = pd.read_csv('path_to/events.csv')
# Preprocess data
```

### 2. Train the SR-GNN Model
Train the session-based recommendation model with the following command:
```python
python train.py
```
This script handles model training, validation, and evaluation using the SR-GNN architecture.

### 3. Evaluate the Model
Once the model is trained, you can evaluate its performance on test data using:
```python
python evaluate.py
```
The evaluation will output **Hit@10** and **Next Item Prediction Accuracy**.

## Example Usage

```python
from model import SRGNN
model = SRGNN(hidden_size=64, n_items=466868)
```

## Results
- **Hit@10 Accuracy**: 44%
- **Next Item Prediction Accuracy**: ~20%

These results demonstrate the model's effectiveness in predicting the next item a user might interact with in a session-based environment.

## References
- [SR-GNN Paper](https://arxiv.org/abs/1811.00855)
- [PyTorch Geometric Documentation](https://pytorch-geometric.readthedocs.io/en/latest/)

---
