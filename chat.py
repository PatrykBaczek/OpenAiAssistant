import openai
import speech_recognition as sr
from gtts import gTTS
import os

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

def assistant_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def listen_for_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        return None

def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("response.mp3")

def main():
    while True:
        print("Ask me something:")
        user_input = listen_for_audio()
        if user_input:
            print("You:", user_input)
            assistant_prompt = f"You: {user_input}\nAssistant:"
            assistant_output = assistant_response(assistant_prompt)
            print("Assistant:", assistant_output)
            speak(assistant_output)

if __name__ == "__main__":
    main()
