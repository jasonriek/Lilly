import pyttsx3

engine = pyttsx3.init()

# Set to female voice 
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
# Set voice rate
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.2)
    
def lilly_says(text):
    engine.say(text)
    engine.runAndWait()
