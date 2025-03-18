from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import openai

app = Flask(__name__)

# OpenAI API Key (Replace with your actual key)
openai.api_key = "your-api-key"
client = openai.OpenAI()

 # Speech Recognizer
recognizer = sr.Recognizer()

def chat_with_gpt(user_input):
    """Sends user input to OpenAI's GPT-4o and returns a response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/text", methods=["POST"])
def text_chat():
    """Handles text-based chat."""
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"message": "No input received."})

    bot_response = chat_with_gpt(user_message)
    return jsonify({"message": bot_response})

@app.route("/voice", methods=["POST"])
def voice_chat():
    """Handles voice input using Speech Recognition."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        
        try:
            audio = recognizer.listen(source, timeout=5)
            user_message = recognizer.recognize_google(audio)
            print(f"User said: {user_message}")
        except sr.UnknownValueError:
            return jsonify({"message": "Sorry, I couldn't understand that."})
        except sr.RequestError:
            return jsonify({"message": "Speech recognition service error."})

    bot_response = chat_with_gpt(user_message)
    return jsonify({"message": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
