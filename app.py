import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '7a80344c83b15325f155588d463ec444676cc2f74c436213e7c7725d99f89e60'

# Title and description for the app
st.title("OpenAI Python Code Generator")
st.markdown("Generate Python code based on your description using OpenAI GPT-3!")

# Text area for the user to input the description
description = st.text_area("Enter a description for your code:")

# Button to trigger code generation
if st.button("Generate Code"):
    if description:
        with st.spinner("Generating your Python code..."):
            try:
                # Send the request to OpenAI to generate Python code based on user input
                response = openai.Completion.create(
                    engine="text-davinci-003",  # You can use other models like "gpt-3.5-turbo"
                    prompt=f"Write Python code for the following: {description}",
                    max_tokens=150,
                    temperature=0.7,
                )
                # Display the result in the text area
                result = response.choices[0].text.strip()
                st.code(result, language='python')
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a description before generating code.")

# Sidebar with additional information
st.sidebar.header("About")
st.sidebar.text("This app is a Python Code Generator built using Streamlit and OpenAI.")
