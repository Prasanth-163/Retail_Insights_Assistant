def create_classification_prompt(question):

    prompt = f"""
You are a retail business question classifier.

Your task is to understand the user's question and classify it
into exactly ONE category.

Allowed categories:

- total_sales
- total_quantity
- category
- state
- products
- unknown

Rules:
1. Return ONLY the category name.
2. Do not provide an explanation.
3. Do not calculate any numbers.
4. If the question does not match the available categories,
   return unknown.
5. Understand the meaning of the question, not just exact keywords.

Examples:

"What is the total sales?" -> total_sales
"How much money did we make overall?" -> total_sales
"What was our overall revenue?" -> total_sales

"How many units were sold?" -> total_quantity
"What is the total quantity?" -> total_quantity

"Which category performed best?" -> category
"What is our best-selling category?" -> category

"Which state had the highest sales?" -> state
"Which state performed best?" -> state

"What are the top products?" -> products
"Which products sold the most?" -> products

"Which region performed best in Q3?" -> unknown

User question:
{question}
"""

    return prompt