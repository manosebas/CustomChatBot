# assist.py
from config import cliente, asistente, hilo
from librerias import mixer, time, os

# Pregunta
def ask_question_memory(question):
    global hilo
    cliente.beta.threads.messages.create(hilo.id, role="user", content=question)
    run = cliente.beta.threads.runs.create(thread_id=hilo.id, assistant_id=asistente.id)
    
    
    while (run_status := cliente.beta.threads.runs.retrieve(thread_id=hilo.id, run_id=run.id)).status != 'completed':
        if run_status.status == 'failed':
            return "The run failed."
        time.sleep(1)
    
    messages = cliente.beta.threads.messages.list(thread_id=hilo.id)
    return messages.data[0].content[0].text.value

# Generade texto a voz
def generate_tts(sentence, speech_file_path):
    response = cliente.audio.speech.create(model="tts-1", voice="echo", input=sentence)
    response.stream_to_file(speech_file_path)
    return str(speech_file_path)

# Reproduce el sonido
def play_sound(file_path):
    mixer.music.load(file_path)
    mixer.music.play()

# Reproduce respuesta en audio
def TTS(text):
    speech_file_path = generate_tts(text, "speech.mp3")
    play_sound(speech_file_path)
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.music.unload()
    os.remove(speech_file_path)
    return "done"
