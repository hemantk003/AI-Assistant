import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
a = pyttsx3.init('sapi5')
voices = a.getProperty('voices')
# print(voices[0].id)
a.setProperty('voice', voices[0].id)


def wakeup():
    
    speak("I AM HERE")


def speak(audio):
    a.say(audio)
    print(f": {audio}")
    a.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("GOOD MORNING SIR!")
    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON SIR!")
    else:
        speak("GOOD EVENING SIR!")
    speak("I AM JARVIS . HOW MAY I HELP YOU")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


def yt():

    speak("tell me what to search!")
    searchname = takecommand()
    searchname = searchname.replace("play", "")

    if 'arcade,' in searchname:
        os.startfile('Music')

    else:
        pywhatkit.playonyt(searchname)

    speak("done sir!")


if __name__ == "__main__":
    # wishme()
    while True:
        query = takecommand().lower()
        if 'wake up' in query:
            wakeup()
            wishme()
            while True:
                query = takecommand().lower()

                if 'how are you' in query:
                    speak("i am fine sir!")
                    speak("how about you?")

                elif 'take rest' in query:
                    speak("OK Sir! YOU CAN CALL ME ANYTIME")
                    break

                elif 'open movie downloader' in query:
                    speak("OK sir! this is what i found")
                    query = query.replace("jarvis", "")
                    #query = query.replace("","")
                    web = 'https://moviesnation.uk/'
                    webbrowser.open(web)
                    speak('done sir!')

                elif 'youtube search' in query:
                    speak("OK sir! this is what i found")
                    query = query.replace("jarvis", "")
                    query = query.replace("youtube search", "")
                    web = 'https://www.youtube.com/results?search_query=' + query
                    webbrowser.open(web)
                    speak('done sir!')

                elif 'google search' in query:
                    speak("OK sir! this is what i found")
                    query = query.replace("jarvis", "")
                    query = query.replace("google search", "")
                    pywhatkit.search(query)
                    speak('done sir!')

                elif 'launch' in query:
                    speak("what's the name of the website?")
                    name = takecommand()
                    query = query.replace("open", "")
                    query = query.replace("launch", "")
                    query = query.replace("website", "")
                    query = query.replace("jarvis", "")
                    web1 = 'https://www.' + name + '.com'
                    webbrowser.open(web1)

                elif 'wikipedia' in query:
                    speak("Searching wikipedia...")
                    query = query.replace("wikipedia", "")
                    query = query.replace("jarvis", "")
                    query = query.replace("open", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'youtube searchbar' in query:
                    query = query.replace("jarvis", "")
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    query = query.replace("jarvis", "")
                    webbrowser.open("google.com")

                elif 'open stack overflow' in query:
                    query = query.replace("jarvis", "")
                    webbrowser.open("stackoverflow.com")

                elif 'play music' in query:
                    music_dir = "C:\\Users\\LENOVO\\Music"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(F"Sir the time is {strTime}")
                    print(strTime)

                elif 'open code' in query:
                    codePath = "C:\\Users\\LENOVO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
                    os.startfile(codePath)

                elif 'open game' in query:
                    codepath1 = "C:\\game prjt\\clgprjt001.exe"
                    query = query.replace("jarvis", "")
                    os.startfile(codepath1)

                elif 'open youtube' in query:
                    yt()

        if 'stop' in query:
            break