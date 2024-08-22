# config.py
from librerias import OpenAI, mixer

cliente = OpenAI(
    api_key= "your-api-key",
    default_headers={"OpenAI-Beta": "assistants=v2"},
    )
mixer.init()

assistant_id = "your-assistant-id"
thread_id = "your-thread-id"

asistente = cliente.beta.assistants.retrieve(assistant_id)
hilo = cliente.beta.threads.retrieve(thread_id)

