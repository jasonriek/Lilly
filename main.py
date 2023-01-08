import webbrowser
from time import sleep 

from lilly_sr import voice_to_text
from lilly_voice import lilly_says

while True:
    print('Python is listening...')
    inp = voice_to_text().lower()
    print(f'You just said "{inp}."')
    if inp == "stop listening":
        print("Later gator!")
        break
    elif "search" in inp:
        inp = inp.replace("search", "")
        lilly_says(f"Searching for {inp}")
        webbrowser.open(f"https://yandex.com/images/search?from=tabbar&text={inp}")
        continue
    elif "what is" in inp:
        lilly_says(f"Jason, I don't have time for your crap, go talk to Alexa or something you loser!")