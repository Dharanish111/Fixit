import streamlit as st
import openai
from streamlit_lottie import st_lottie
import json
from datetime import datetime, timedelta
import time
import os
import requests
def ai_page():

 # Load Lottie animation from a JSON file
 def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

 lottie_animation = load_lottiefile("https://raw.githubusercontent.com/Dharanish111/FixitAI/main/animation.json")


 openai_api_key = st.secrets[("openai_api_key")]

 # Initialize session state attributes
 if 'selected_api' not in st.session_state:
    st.session_state.selected_api = 'OpenAI'
 if 'files' not in st.session_state:
    st.session_state.files = []
 if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

 # OpenAI function
 def get_response_chatgpt(prompt):
    openai.api_key = openai_api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Ensure this is a valid chat model, such as "gpt-4.0-chat"
            messages=[{"role": "system", "content": f"You are a helpful assistant, You need to give the output in the selected language: {selected_language}"},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

 # Google Gen AI function
 def get_response_gemini(prompt):  # Corrected parameter name
    palm.configure(api_key=google_gemini_key)
    
    try:
        response = palm.generate_text(
            model='models/text-bison-001',  # Update with the appropriate model ID
            prompt= f"you are a helpful assistant and need to give the response in the language: {selected_language}.{prompt}",  # Corrected variable usage
            temperature=0.9,  # You can adjust the temperature for response variability
            max_output_tokens=200  # Adjust the number of tokens as needed
            )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

 # API selection with pills
 st.header("API Selection")
 st.session_state.selected_api = st.radio("Select API", ('OpenAI', 'Google Gemini'))

 # Display selected API
 st.write(f"Selected API: {st.session_state.selected_api}")

 # File upload area
 st.sidebar.header("File Upload")
 uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "pdf", "docx"])  

 if uploaded_file is not None:
    st.session_state.files.append(uploaded_file)
    st.sidebar.success("File uploaded successfully!")

 st.sidebar.subheader("Uploaded Files")
 for file in st.session_state.files:
    st.sidebar.write(file.name)

 # Initialize session state for reminders
 if 'reminders' not in st.session_state:
    st.session_state.reminders = []

 # Function to check reminders
 def check_reminders():
    current_time = datetime.now()
    for reminder in st.session_state.reminders:
        if reminder['time'] <= current_time:
            st.sidebar.success(f"Reminder: {reminder['message']}")
            # Optionally, remove the reminder after showing it
            st.session_state.reminders.remove(reminder)

 # Input fields for setting a reminder
 st.sidebar.header("Set a Reminder")
 message = st.sidebar.text_input("Reminder Message")
 reminder_time = st.sidebar.time_input("Reminder Time", value=datetime.now().time())

 if st.sidebar.button("Set Reminder"):
    reminder_datetime = datetime.combine(datetime.now().date(), reminder_time)
    if reminder_datetime < datetime.now():
        reminder_datetime += timedelta(days=1)  # Set for the next day if time is in the past
    st.session_state.reminders.append({'message': message, 'time': reminder_datetime})
    st.sidebar.success(f"Reminder set for {reminder_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

 # Periodically check for reminders
 check_reminders()

 # Display all reminders
 st.sidebar.header("All Reminders") 
 for reminder in st.session_state.reminders:
    st.sidebar.write(f"{reminder['message']} at {reminder['time'].strftime('%Y-%m-%d %H:%M:%S')}")

 Languages = ['English', 'Telugu', 'Hindi', 'Tamil', 'Marathi', 'Sanskrit','Bengali','Malayalam','Kannada','Punjabi','Urdu','Manipuri','Kashmiri','Assamese','Bengali','Bodo','Dogri','Konkani','Maithili','Mizo','Manipuri','Odia','Nepali','Santali','Sindhi','Urdu','']
 selected_language = st.selectbox("Select a language", Languages)

 # Main chatbot area
 st.title("Fixit✨")
 user_input = st.text_input("Search here...")

 # Placeholder for the response and loading animation
 response_placeholder = st.empty()
 animation_placeholder = st.empty()

 if user_input:
    # Display loading animation
    with animation_placeholder:
        st_lottie(lottie_animation, height=70, key="loading_animation")
    
    # Get response based on the selected API
    if st.session_state.selected_api == 'OpenAI':
        response = get_response_chatgpt(user_input)
    else:
        response = get_response_gemini(user_input)
    
    # Clear the loading animation
    animation_placeholder.empty()
    
    # Display the response
    response_placeholder.text_area(f"Response ({selected_language}):", value=response, height=200, disabled=True)
    
    st.session_state.chat_history.append({"user_input": user_input, "response": response})

 st.subheader("Chat History")
 for chat in st.session_state.chat_history:
    st.write(f"**You:** {chat['user_input']}")
    st.write(f"**Fixit✨:** {chat['response']}")
