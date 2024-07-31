# Fixit✨

Fixit is an AI-powered chatbot built using Streamlit, OpenAI API, and Google Gemini API. This project includes user registration, login, and password reset functionalities with a focus on providing helpful responses in multiple languages.

## Features

- User

# Fixit✨

Fixit is an AI-powered chatbot built using Streamlit, OpenAI API, and Google Gemini API. This project includes user registration, login, and password reset functionalities with a focus on providing helpful responses in multiple languages.

## Features

- User registration with security questions for password recovery.
- User login with password validation.
- Password reset functionality using security questions.
- Integration with OpenAI GPT-4 and Google Gemini for chatbot responses.
- Multi-language support for chatbot responses.
- Text-to-speech conversion of chatbot responses.
- File upload and management.
- Reminder setting and notification system.
- Animated loading indicator during chatbot response generation.
- Chat history display.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fixit.git
    cd fixit
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the SQLite database:
    ```sh
    sqlite3 users.db < schema.sql
    ```

5. Add your OpenAI API key to the Streamlit secrets:
    ```sh
    echo "[secrets]" > .streamlit/secrets.toml
    echo "openai_api_key = 'your_openai_api_key'" >> .streamlit/secrets.toml
    ```

6. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

### Registration

1. Open the app in your browser.
2. Navigate to the registration page.
3. Fill in the required fields (username, password, security question, and security answer).
4. Click "Register" to create a new account.

### Login

1. Open the app in your browser.
2. Navigate to the login page.
3. Enter your username and password.
4. Click "Login" to access the chatbot.

### Password Reset

1. Open the app in your browser.
2. Navigate to the forgot password page.
3. Enter your username and answer the security question.
4. Enter a new password and confirm it.
5. Click "Reset Password" to update your password.

### Chatbot Interaction

1. Once logged in, you can interact with the Fixit chatbot.
2. Select the desired API (OpenAI or Google Gemini).
3. Choose the language for responses.
4. Enter your query in the text input field.
5. View the response and listen to the audio if needed.
6. Set reminders and upload files using the sidebar.

## Dependencies

- Streamlit
- OpenAI
- Streamlit-Lottie
- gTTS
- Requests
- SQLite
- bcrypt

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file further based on your project's specific requirements and additional information.
