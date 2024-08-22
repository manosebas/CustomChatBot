# ui.py
from librerias import tkinter as tk
from librerias import scrolledtext
from librerias import Tk, Toplevel, Text, Button, Label, END
from librerias import threading
import hablar
import escribir


# ui.py
def start_chat_interface():
    chat_window = Toplevel(root)
    chat_window.title("Chat Interface")

    text_input = Text(chat_window, height=3, width=50, font=("Arial", 14))
    text_input.pack(pady=10)

    text_output = scrolledtext.ScrolledText(chat_window, height=15, width=50, font=("Arial", 14))
    text_output.pack(pady=10)

    def on_send_button():
        user_input = text_input.get("1.0", END).strip()
        text_input.delete("1.0", END)
        if user_input:
            text_output.insert(END, f"\nUser: {user_input}\n", "user")
            escribir.chatear(user_input, lambda response: text_output.insert(END, response + "\n", "bot"))

    send_button = Button(chat_window, text="Enviar", command=on_send_button, font=("Arial", 14), bg="#2196F3", fg="white")
    send_button.pack(pady=5)

    text_output.tag_config("user", justify="right", foreground="blue")
    text_output.tag_config("bot", justify="left", foreground="black")

#En desarrollo todavia ------------------------> 
# def start_voice_interface():
#     voice_window = Toplevel(root)
#     voice_window.title("Voice Interface")

#     text_output = scrolledtext.ScrolledText(voice_window, height=15, width=50, font=("Arial", 14))
#     text_output.pack(pady=10)

#     stop_event = threading.Event()

#     def update_ui_callback(text):
#         text_output.insert(END, text + "\n")
#         text_output.see(END)

#     def on_close():
#         stop_event.set()
#         voice_window.destroy()

#     voice_window.protocol("WM_DELETE_WINDOW", on_close)
#     threading.Thread(target=hablar.reconocer_voz, args=(update_ui_callback, stop_event)).start()

root = Tk()
root.title("Chatbot - Español")
root.geometry("400x200")

title_label = Label(root, text="Chatbot Interface", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

chat_button = Button(root, text="Escribir", command=start_chat_interface, font=("Arial", 16), width=15, bg="#2196F3", fg="white")
chat_button.pack(pady=10)

#En desarrollo todavia ------------------------> 
# speak_button = Button(root, text="Hablar", command=start_voice_interface, font=("Arial", 16), width=15, bg="#FF5722", fg="white")
# speak_button.pack(pady=10)

root.mainloop()