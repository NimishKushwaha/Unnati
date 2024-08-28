# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import io
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load model and get responses
text_model = genai.GenerativeModel('gemini-pro')
image_model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input_text, uploaded_image=None):
    if input_text and not uploaded_image:
        return text_model.generate_content(input_text).text
    elif uploaded_image:
        # Convert the uploaded image to bytes
        image_bytes = uploaded_image.read()

        # Convert the bytes to a PIL Image
        pil_image = Image.open(io.BytesIO(image_bytes))

        # Generate content using the image
        return image_model.generate_content([input_text, pil_image]).text
    else:
        return "Please provide a question or an image for Saathi to respond."

# Initialize Streamlit app
st.set_page_config(page_title="Saathi - Your Q&A Chatbot", page_icon="🤖")

# Set app header and background
st.title("Ask Saathi - Your AI Mentor")

# Resize and style the logo
logo_image = Image.open("big.jpg")
small_logo = logo_image.resize((100, 100))  # Adjust the size as needed
st.image(small_logo, use_column_width=False, caption="Saathi Logo")

# User input and interaction
input_question = st.text_input("Ask a question:", key="input_question")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
ask_button = st.button("Ask Saathi")

# If the user asks a question
if ask_button and (input_question.strip() or uploaded_image):
    response = get_gemini_response(input_question, uploaded_image)
    st.markdown("---")
    st.subheader("Saathi's Response:")
    st.write(response)

# Add some style to the app
st.markdown("---")
st.subheader("About Saathi:")
st.write("Saathi is your friendly AI companion at Unnati ready to assist you with any questions.")
st.write("Feel free to ask anything, and Saathi will provide insightful responses.")
