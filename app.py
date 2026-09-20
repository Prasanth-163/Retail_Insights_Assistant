import streamlit as st

from question_handler import answer_question


# Page configuration
st.set_page_config(
    page_title="Retail Insights Assistant",
    page_icon="🛍️"
)


# Application title
st.title("🛍️ Retail Insights Assistant")

st.write(
    "Ask questions about the Amazon sales data."
)


# User question
question = st.text_input(
    "Ask your question:",
    placeholder="Example: Which category performed best?"
)


# Get answer
if st.button("Get Insights"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Analyzing..."):

            answer = answer_question(question)

        st.subheader("📊 Business Insight")

        st.write(answer)