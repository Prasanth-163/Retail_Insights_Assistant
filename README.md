# 🛍️ Retail Insights Assistant

Retail Insights Assistant is a simple GenAI chatbot that helps answer questions about sales data.

## What does it do?

You can ask questions like:

- What is the total sales?
- Which category performed best?
- Which state had the highest sales?
- What are the top products?

The chatbot uses **Gemini API** to understand the question and **Python + Pandas** to get the answer from the sales dataset.

## Technologies Used

- Python
- Pandas
- Gemini API
- Streamlit

## How it works

User asks a question  
↓  
Gemini understands the question  
↓  
Python analyzes the sales data  
↓  
The chatbot shows the answer

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
