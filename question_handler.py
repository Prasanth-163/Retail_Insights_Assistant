from analysis import (
    get_total_sales,
    get_total_quantity,
    get_sales_by_category,
    get_sales_by_state,
    get_top_products
)

from gemini_helper import generate_answer
from prompt_handler import create_classification_prompt


def understand_question(question):

    # Create the engineered prompt
    prompt = create_classification_prompt(question)

    # Gemini understands the user's natural-language question
    result = generate_answer(prompt).strip().lower()

    valid_types = [
        "total_sales",
        "total_quantity",
        "category",
        "state",
        "products",
        "unknown"
    ]

    # Keep only the expected category
    for question_type in valid_types:
        if question_type in result:
            return question_type

    return "unknown"


def answer_question(question):

    question_type = understand_question(question)

    # Total sales
    if question_type == "total_sales":

        total_sales = get_total_sales()

        return (
            f"Total sales are ₹{total_sales:,.2f}."
        )

    # Total quantity
    elif question_type == "total_quantity":

        total_quantity = get_total_quantity()

        return (
            f"Total quantity sold is "
            f"{total_quantity:,} units."
        )

    # Best category
    elif question_type == "category":

        data = get_sales_by_category()

        top_category = data.index[0]
        top_sales = data.iloc[0]

        return (
            f"The top-performing category is "
            f"{top_category}, with sales of "
            f"₹{top_sales:,.2f}."
        )

    # Best state
    elif question_type == "state":

        data = get_sales_by_state()

        top_state = data.index[0]
        top_sales = data.iloc[0]

        return (
            f"The state with the highest sales is "
            f"{top_state}, with sales of "
            f"₹{top_sales:,.2f}."
        )

    # Top products
    elif question_type == "products":

        data = get_top_products()

        result = "Top 5 products by sales:\n\n"

        for product, sales in data.items():

            result += (
                f"- {product}: ₹{sales:,.2f}\n"
            )

        return result

    # Unsupported question
    else:

        return (
            "Sorry, I don't have enough information to answer "
            "that question from the available sales data."
        )