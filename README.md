# AI-agent

**An AI dashboard for automatically classifying customer support queries using Flask and Streamlit.**

---

## Project Description

This project is an AI-powered customer support system that helps automatically understand and classify user queries.

### Features:
- **Flask Backend**: Handles receiving customer queries and predicting their intent using a pre-trained machine learning model.
- **Streamlit Frontend**: Provides a user-friendly dashboard for users to enter queries and view predicted intents and confidence scores.

---

## How it Works:
1. **Select a Query**: Users can select a predefined query from a list.
2. **Type a Query**: Alternatively, users can type in their own custom query.
3. **Submit**: Upon submission, the model predicts the intent of the query and returns the predicted intent with a confidence score.
4. **History**: The dashboard keeps a record of past queries, intents, and confidence scores.

---

## Technologies Used:
- **Backend**: Flask, Python
- **Frontend**: Streamlit
- **Machine Learning Model**: BART model for text classification
- **Database**: SQLite (for storing query history)

---

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/teja2704/AI-agent.git
