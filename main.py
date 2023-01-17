import pyttsx3
import openai
import mic



openai.api_key = ""

def chat(question, personality):
    prompt = (f"personality: {personality}\n"
              f"The current question is: {question}")

    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)

    return response.choices[0].text


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # selecciona la voz de Sabina
engine.setProperty('rate', 150) # velocidad de la voz


while True:
    audio = mic.record_audio()
    text = mic.transcribe_forever(audio)
    print("Yo said:" + text)
    final = result = chat(text, "Please generate an answer as a helper and assistant for someone who wants to learn English:")
    print(final)
    engine.say(final)
    engine.runAndWait()