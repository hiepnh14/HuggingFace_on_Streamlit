import streamlit as st
from transformers import pipeline

# Set page title and description
st.set_page_config(
    page_title="Text Generation App", page_icon=":pencil2:", layout="wide"
)
# 
# Set up the Streamlit app layout
st.title('Hugging Face Language Model Chatbot')
user_input = st.text_input("Type your message here:")

# Load the Hugging Face language model
chatbot = pipeline("text-generation", model="gpt2")

if st.button('Send'):
    # Generate a response using the language model
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    st.text_area("Chatbot's response:", value=response[0]['generated_text'], height=200)
