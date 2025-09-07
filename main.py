from dotenv import load_dotenv
import openai
import string
import streamlit as st
import pandas as pd

def clean_text(text: str) -> str:
    """Cleans text by removing punctuation, lowercasing, and stripping whitespace."""
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Lowercase
    text = text.lower()
    # Strip leading/trailing whitespace and normalize internal whitespace
    text = " ".join(text.split())
    return text

load_dotenv()

client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your GenAI-powered data processing app.")

col1, col2 = st.columns(2)

with col1:
    if st.button("Ingest Dataset"):
        try:
            csv_path = "data/customer_reviews.csv"
            st.session_state['df'] = pd.read_csv(csv_path)
            st.success("Dataset loaded successfully!")
        except FileNotFoundError:
            st.error("Dataset not found. Please check the file path.")

with col2:
    if st.button("Parse Reviews"):
        if 'df' in st.session_state:
            st.session_state['df']['CLEANED_SUMMARY'] = st.session_state['df']['SUMMARY'].apply(clean_text)
            st.success("Reviews parsed and cleaned!")
        else:
            st.warning("Please ingest the dataset first.")

if 'df' in st.session_state:
    st.subheader("Filter by Product")
    product = st.selectbox("Choose Product", ["All Products"] + list(st.session_state['df']['PRODUCT'].unique()))

    st.subheader("Dataset Preview")

    if product != "All Products":
        filtered_df = st.session_state['df'][st.session_state['df']['PRODUCT'] == product]
    else:
        filtered_df = st.session_state['df']

    st.dataframe(filtered_df)