import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API (Replace with your API Key)
genai.configure(api_key="AIzaSyA4fuJD-ltHZFuURPFU7-p9qbsAXQX29nEY")

# Function to review Python code
def review_code(code):
    model = genai.GenerativeModel("gemini-pro")  # Use Gemini-Pro model
    prompt = f"Review the following Python code, find bugs, and suggest fixes:\n\n{code}"
    
    response = model.generate_content(prompt)
    return response.text  # Get AI's response

# Streamlit UI
st.title("AI Code Reviewer 🧑‍💻")
st.write("Paste your Python code below and get AI-generated feedback!")

# User input
user_code = st.text_area("Enter your Python code:", height=250)

# Review Button
if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing code..."):
            result = review_code(user_code)
        st.subheader("AI Review & Suggestions:")
        st.code(result, language="python")
    else:
        st.warning("Please enter some Python code.")
