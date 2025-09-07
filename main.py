from dotenv import load_dotenv
import openai
import streamlit as st

@st.cache_data
def get_response(user_prompt, temperature):
    return client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        max_output_tokens=100
    )

load_dotenv()

client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first streamlit app.")

user_prompt = st.text_input("Enter your prompt:", "Explain generative AI in one sentence.")

temperature = st.slider(
    "Model temperature:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.01,
    help="Controls randomness: 0 = deterministic, 1 = very creative"
)

with st.spinner("AI is working..."):
    response = get_response(user_prompt, temperature)

    st.write(response.output[0].content[0].text)