# Flask Voice and Text Chatbot with OpenAI GPT-4o

This is a Flask-based chatbot application that supports both text and voice input. It utilizes OpenAI's GPT-4o for generating responses and SpeechRecognition for handling voice input.

## Features
- Chat with the bot using text messages.
- Speak to the bot and receive responses.
- Uses OpenAI's GPT-4o for generating intelligent replies.
- Uses SpeechRecognition for voice input processing.
- Simple Flask web interface.

## Requirements
Make sure you have the following installed:
- Python 3.9+
- Flask
- SpeechRecognition
- OpenAI Python client
- A working microphone for voice input

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up OpenAI API Key:**
   - Replace `openai.api_key = ""` with your actual OpenAI API key in `app.py`.

## Usage
1. **Run the Flask App:**
   ```bash
   python app.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000/`.

## API Endpoints
- `POST /text` → Send a JSON payload `{ "message": "Your text here" }` to chat with GPT-4o.
- `POST /voice` → Uses a microphone to capture voice input, convert it to text, and respond.

## File Structure
```
.
├── app.py          # Main Flask application
├── templates/
│   ├── index.html  # Frontend template
├── static/
│   ├── styles.css  # Optional CSS file
├── requirements.txt # List of dependencies
└── README.md        # Project documentation
```

## Notes
- Ensure your microphone is working for voice input.
- This project is for educational purposes; do not expose your API key in production.

---

Enjoy your chatbot! 🚀

