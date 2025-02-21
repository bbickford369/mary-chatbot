import streamlit as st
import openai

# Set up Streamlit app
st.title("Mary: Your AI Companion")

# User input
user_input = st.text_input("Talk to Mary:")

# AI response logic (replace 'your-api-key' with your OpenAI key)
if user_input:
    openai.api_key = "your-api-key"  # Replace with actual key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write("Mary:", response["choices"][0]["message"]["content"])
