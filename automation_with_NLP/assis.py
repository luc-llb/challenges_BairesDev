import os
from edge_tts import Communicate
import speech_recognition as sr
import webbrowser
import requests
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime
import asyncio

async def __speak__(text, voice):
    filename = "voice.mp3"
    tts = Communicate(text, voice=voice)
    await tts.save(filename)
    audio = AudioSegment.from_mp3(filename)
    audio = audio.speedup(playback_speed=1.1)
    play(audio)
    os.remove(filename)

def speak(text):
    asyncio.run(__speak__(text, 'pt-BR-AntonioNeural'))

def get_order():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ouvindo...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")
            # print("Você disse:", said)
        except sr.UnknownValueError:
            said = "Desculpe, não entendi."
        except sr.RequestError:
            said = "Erro ao acessar o serviço de reconhecimento de voz."
    return said.lower()

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?lang=pt"  # API with jokes in Portuguese
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        if joke_data["type"] == "twopart":
            return f"{joke_data['setup']} - {joke_data['delivery']}"
        else:
            return joke_data["joke"]
    else:
        return "Não foi possível obter uma piada no momento."

# Set the browser to be used
BROWERS = 'opera'

# Commands that the assistant can respond to
COMMANDS = """Estes são os comandos que você pode usar:
        - Ao dizer 'pesquisar', você pode pesquisar no Google.
        - Ao dizer 'youtube', você pode pesquisar no Youtube.
        - Falando a palavra 'piada', eu conto uma piada.
        - Perguntar as horas dizendo a palavra 'horas'.
        - dizer 'fechar' fara com que eu feche o navegador.
        - Ao dizer 'sair', eu encerro a execução.
    """
def respond(text):
    print("Texto do audio: " + text)
    if 'youtube' in text:
        speak("O que você quer pesquisar no youtube?")
        keyword = get_order()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Isso é o que encontrei pesquisando por {keyword} no youtube")
    elif 'pesquisar' in text:
        speak("O que você quer pesquisar no google?")
        query = get_order()
        if query !='':
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.get().open(url)
            speak(f"Isso é o que encontrei pesquisando por {query} no google")
    elif 'fechar' in text:
        os.system(f"taskkill /f /im {BROWERS}.exe")
        speak("Fechando o navegador")
    elif 'piada' in text:
        speak(get_joke())
    elif 'horas' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'comando' in text or 'comandos' in text:
        print(COMMANDS)
        speak(COMMANDS)
    elif 'sair' in text:
        speak("Até logo!")
        exit()
    else:
        speak("Não posso te ajudar com isso. Tente outra coisa.")

def main():
    speak("Olá, eu sou Assis, seu assistente virtual. Chame por 'Assis' quando precisar de mim. Ao dizer 'comandos', eu mostro o que posso fazer por você.")
    while True:
        text = ""
        print("Chame por 'Assis' para ativar o assistente")
        while get_order() != 'assis':
            continue
        speak("Como posso ajudar?")
        text = get_order()
        respond(text)

if __name__ == "__main__":
    main()