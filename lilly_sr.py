import speech_recognition as sr

speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio) 
        except sr.UnknownValueError as unk_error:
            print(f"Unknown Error: {str(unk_error)}")
        except sr.RequestError as rq_error:
            print(f"Request Error: {str(rq_error)}")
        except sr.WaitTimeoutError as wto_error: 
            print(f"Timeout Error {str(wto_error)}")
    return voice_input