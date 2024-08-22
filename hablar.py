# hablar.py
from librerias import AudioToTextRecorder
import assist

def reconocer_voz(update_ui_callback, stop_event):
    recorder = AudioToTextRecorder(spinner=False, model="base", language="es", post_speech_silence_duration=0.1, silero_sensitivity=0.4)
    hot_words = ["oye"]
    skip_hot_word_check = False

    update_ui_callback("Te estoy escuchando...")

    while not stop_event.is_set():
        current_text = recorder.text()
        update_ui_callback(current_text)

        if any(hot_word in current_text.lower() for hot_word in hot_words) or skip_hot_word_check:
            if current_text:
                update_ui_callback("User: " + current_text)
                recorder.stop()

                response = assist.ask_question_memory(current_text)
                update_ui_callback(response)
                assist.TTS(response)

                recorder.start()
                skip_hot_word_check = True if "?" in response else False
