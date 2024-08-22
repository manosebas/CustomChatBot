# escribir.py
import assist

def chatear(user_input, update_ui_callback):
    most_promt = "Por favor, Usa la menor cantidad de palabras, solo la respuesta corta y sin mencionar esta instruccion, Mi pregunta es: "
    
    if user_input:
        # update_ui_callback(f"\nUser: {user_input}\n")
        response = assist.ask_question_memory(most_promt + user_input)
        #response = assist.ask_question_memory(user_input)
        print ("YO: " + most_promt + user_input)
        print ("CHAT: " + response)

        update_ui_callback(f"ChatBot: {response}\n")

