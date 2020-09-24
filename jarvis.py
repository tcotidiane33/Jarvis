import os
import platform
import sys
import webbrowser
from datetime import datetime

import pyttsx3 as audio
import speech_recognition as sr

now = datetime.now()
current = now.strftime("%p")
clock = now.strftime("%I")
today = now.strftime("%A")

# TODO: include phone location
# TODO: include face recognition
# TODO: include gmail reader


def initialize():
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rInitialized: I'm listening...")
            listener = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            name = recognizer.recognize_google(listener)

            if 'exit' in name or 'quit' in name:
                sys.stdout.write("\r")
                speaker.say(exit_msg)
                speaker.runAndWait()
                exit()

            if str(os.getenv('key')) in str(name):
                sys.stdout.write("\r")
                if current == 'AM' and int(clock) < 10:
                    speaker.say("Welcome back sire. Good Morning. What can I do for you?")
                elif current == 'AM' and int(clock) >= 10:
                    speaker.say("Welcome back sire. Hope you're having a nice morning. What can I do for you?")
                elif current == 'PM' and (int(clock) == 12 or int(clock) < 4):
                    speaker.say("Welcome back sire. Good Afternoon. What can I do for you?")
                elif current == 'PM' and int(clock) < 7:
                    speaker.say("Welcome back sire. Good Evening. What can I do for you?")
                else:
                    speaker.say("Welcome back sire. Hope you're having a nice night. What can I do for you?")
            else:
                sys.stdout.write("\r")
                if current == 'AM' and int(clock) <= 10:
                    speaker.say(f"Hi {name}. Good Morning. What can I do for you?")
                elif current == 'AM' and int(clock) > 10:
                    speaker.say(f"Hi {name}. Hope you're having a nice morning. What can I do for you?")
                elif current == 'PM' and (int(clock) == 12 or int(clock) < 4):
                    speaker.say(f"Hi {name}. Good Afternoon. What can I do for you?")
                elif current == 'PM' and int(clock) < 7:
                    speaker.say(f"Hi {name}. Good Evening. What can I do for you?")
                else:
                    speaker.say(f"Hi {name}. Hope you're having a nice night. What can I do for you?")
            speaker.runAndWait()
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            speaker.say("Whom am I speaking with?.")
            speaker.runAndWait()
            initialize()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee.")
            speaker.say("Whom am I speaking with?.")
            speaker.runAndWait()
            initialize()

    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rName addressed: I'm listening...")
            listener_new = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            return recognizer.recognize_google(listener_new)
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            dummy.has_been_called = True
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            dummy.has_been_called = True
        renew()


def renew():
    if dummy.has_been_called:
        sys.stdout.write("\r")
        speaker.say("Is there anything I can do for you?. You may simply answer yes or no")
    else:
        sys.stdout.write("\r")
        speaker.say("Is there anything else I can do for you?")
    speaker.runAndWait()
    dummy.has_been_called = False
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rRedo: I'm listening...")
            listener2 = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            recognized_text2 = recognizer.recognize_google(listener2)
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            dummy.has_been_called = True
            renew()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            dummy.has_been_called = True
            renew()
        if 'no' in recognized_text2 or "that's all" in recognized_text2 or 'that is all' in recognized_text2 or \
                "that's it" in recognized_text2 or 'that is it' in recognized_text2 or 'quit' in recognized_text2 \
                or 'exit' in recognized_text2:
            sys.stdout.write("\r")
            speaker.say(exit_msg)
            speaker.runAndWait()
            exit()
        else:
            sys.stdout.write("\r")
            speaker.say("Go ahead, I'm listening")
            speaker.runAndWait()
            try:
                sys.stdout.write("\rContinue: I'm listening...")
                listener_redo_ = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                recognized_redo_ = recognizer.recognize_google(listener_redo_)
                sys.stdout.write("\r")
                conditions(recognized_redo_)
            except (sr.UnknownValueError, sr.RequestError):
                sys.stdout.write("\r")
                speaker.say("I didn't quite get that. Try again.")
                dummy.has_been_called = True
                renew()
            except sr.WaitTimeoutError:
                sys.stdout.write("\r")
                speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
                dummy.has_been_called = True
                renew()


def conditions(recognized_text):
    if "today's date" in recognized_text or 'current date' in recognized_text:
        date()

    elif 'current time' in recognized_text:
        time()

    elif 'weather' in recognized_text or 'temperature' in recognized_text:
        weather()

    elif 'system' in recognized_text or 'configuration' in recognized_text:
        system_info()

    elif 'website' in recognized_text or '.com' in recognized_text or 'webpage' in \
            recognized_text or 'web page' in recognized_text:
        webpage()

    elif 'fact' in recognized_text or 'info' in recognized_text or 'information' in \
            recognized_text or 'wikipedia' in recognized_text or 'facts' in recognized_text or 'Wikipedia' in \
            recognized_text:
        wiki_pedia()

    elif 'news' in recognized_text or 'latest' in recognized_text:
        news()

    elif 'report' in recognized_text or 'good morning' in recognized_text:
        report()

    elif 'investment' in recognized_text or 'stock' in recognized_text or 'share' in recognized_text or 'shares' in \
            recognized_text or 'portfolio' in recognized_text:
        robinhood()

    elif 'launch' in recognized_text:
        apps.has_been_called = False
        apps()

    elif 'repeat' in recognized_text:
        repeater()

    elif 'chat' in recognized_text or 'bot' in recognized_text:
        chatBot()

    elif 'exit' in recognized_text or 'quit' in recognized_text:
        speaker.say(exit_msg)
        speaker.runAndWait()
        exit()

    else:
        sys.stdout.write(f"\r{recognized_text}")
        speaker.say(f"I heard {recognized_text}. Let me look that up.")
        speaker.runAndWait()

        search = str(recognized_text).replace(' ', '+')

        url = f"https://www.google.com/search?q={search}"

        webbrowser.open(url)

        speaker.say("I have opened a google search for your request.")
        renew()


def report():
    sys.stdout.write("\rStarting today's report")
    report.has_been_called = True
    date()
    time()
    weather()
    news()
    renew()


def date():
    today_date = datetime.now()
    dt_string = today_date.strftime("%A, %B %d, %Y")
    sys.stdout.write("\r")
    speaker.say(f'Today is {dt_string}')
    speaker.runAndWait()
    if report.has_been_called:
        pass
    else:
        renew()


def time():
    from datetime import datetime
    current_time = datetime.now()
    dt_string = current_time.strftime("%I:%M %p")
    sys.stdout.write("\r")
    speaker.say(f'The current time is: {dt_string}')
    if report.has_been_called:
        pass
    else:
        renew()


def webpage():
    sys.stdout.write("\r")
    speaker.say("Which website shall I open? Just say the name of the webpage.")
    speaker.runAndWait()
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rWebpage: I'm listening...")
            listener1 = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            recognized_text1 = recognizer.recognize_google(listener1)
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            webpage()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            webpage()

    if 'exit' in recognized_text1 or 'quit' in recognized_text1:
        renew()

    url = f"https://{recognized_text1}.com"

    webbrowser.open(url)
    sys.stdout.write("\r")
    speaker.say(f"I have opened {recognized_text1}")
    renew()


def weather():
    sys.stdout.write('\rGetting your weather info')
    from urllib.request import urlopen
    import pytemperature
    import json
    api_key = os.getenv('api_key')

    url = 'http://ipinfo.io/json'
    resp = urlopen(url)
    data = json.load(resp)
    city, state, country, coordinates = data['city'], data['region'], data['country'], data['loc']
    lat = coordinates.split(',')[0]
    lon = coordinates.split(',')[1]
    api_endpoint = "http://api.openweathermap.org/data/2.5/"
    url = f'{api_endpoint}onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}'
    r = urlopen(url)  # sends request to the url created
    response = json.loads(r.read())  # loads the response in a json

    weather_location = f'{city} {state}'
    temperature = response['current']['temp']
    condition = response['current']['weather'][0]['description']
    feels_like = response['current']['feels_like']
    maxi = response['daily'][0]['temp']['max']
    high = int(round(pytemperature.k2f(maxi), 2))
    mini = response['daily'][0]['temp']['min']
    low = int(round(pytemperature.k2f(mini), 2))
    temp_f = int(round(pytemperature.k2f(temperature), 2))
    temp_feel_f = int(round(pytemperature.k2f(feels_like), 2))
    sunrise = (datetime.fromtimestamp(response['daily'][0]['sunrise']).strftime("%I:%M %p"))
    sunset = (datetime.fromtimestamp(response['daily'][0]['sunset']).strftime("%I:%M %p"))
    output = f'You are currently at {weather_location}. The weather at your location is {temp_f}°F, with a high of ' \
             f'{high}, and a low of {low}. It currenly feels Like {temp_feel_f}°F, and the current ' \
             f'condition is {condition}. Sunrise at {sunrise}. Sunset at {sunset}'
    sys.stdout.write("\r")
    speaker.say(output)
    speaker.runAndWait()
    if report.has_been_called:
        pass
    else:
        renew()


def system_info():
    import shutil
    from psutil import virtual_memory
    import platform

    total, used, free = shutil.disk_usage("/")
    total = f"{(total // (2 ** 30))} GB"
    used = f"{(used // (2 ** 30))} GB"
    free = f"{(free // (2 ** 30))} GB"

    mem = virtual_memory()
    ram = f"{mem.total // (2 ** 30)} GB"

    cpu = str(os.cpu_count())
    release = str(platform.release())
    sys.stdout.write("\r")
    speaker.say(f"You're running {(platform.platform()).split('.')[0]}, with {cpu} cores. "
                f"The release version is {release}. Your physical drive capacity is {total}. "
                f"You have used up {used} of space. Your free space is {free}. Your RAM capacity is {ram}")
    speaker.runAndWait()
    renew()


def wiki_pedia():
    import wikipedia
    sys.stdout.write("\r")
    speaker.say("Please tell the keyword.")
    speaker.runAndWait()
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rWikipedia: I'm listening...")
            listener1 = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            keyword = recognizer.recognize_google(listener1)
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            wiki_pedia()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            wiki_pedia()

        if 'exit' in keyword or 'quit' in keyword:
            renew()

        sys.stdout.write(f'\rGetting your info from Wikipedia API for {keyword}')
        try:
            data = wikipedia.summary(keyword)
        except wikipedia.exceptions.DisambiguationError as e:
            sys.stdout.write(e)
            speaker.say('Your search has multiple results. Pick one displayed on your screen.')
            speaker.runAndWait()
            sys.stdout.write("\rMultiple Search: I'm listening...")
            listener1 = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            keyword1 = recognizer.recognize_google(listener1)
            data = wikipedia.summary(keyword1)
        sys.stdout.write("\r")
        speaker.say(''.join(data.split('.')[0:2]))
        speaker.runAndWait()
        speaker.say("Do you want me to continue?")
        speaker.runAndWait()
        sys.stdout.write("\rContinue Reading: I'm listening...")
        try:
            listener2 = recognizer.listen(source, timeout=3, phrase_time_limit=5)
            response = recognizer.recognize_google(listener2)
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            dummy.has_been_called = True
            renew()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            dummy.has_been_called = True
            renew()
        if 'yes' in response or 'continue' in response or 'proceed' in response or 'yeah' in response:
            sys.stdout.write("\r")
            speaker.say(''.join(data.split('.')[3:-1]))
            speaker.runAndWait()
            renew()
        else:
            renew()


def news():
    source = 'fox'
    sys.stdout.write(f'\rGetting news from {source} news.')
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key=os.getenv('news_api'))
    all_articles = newsapi.get_top_headlines(sources=f'{source}-news')

    for article in all_articles['articles']:
        sys.stdout.write("\r")
        speaker.say(article['title'])
        speaker.runAndWait()

    if report.has_been_called:
        pass
    else:
        renew()


def apps():
    import subprocess
    import re
    global operating_system

    if operating_system == 'Windows':
        if not apps.has_been_called:
            sys.stdout.write("\r")
            speaker.say("Opening third party apps on a Windows machine is complicated. Please tell me a system app "
                        "that I could try opening.")
            speaker.runAndWait()
        apps.has_been_called = True
        with sr.Microphone() as source:
            try:
                sys.stdout.write("\rApps: I'm listening...")
                listener = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                keyword = recognizer.recognize_google(listener)
                sys.stdout.write("\r")
                if 'exit' in keyword or 'quit' in keyword:
                    renew()
                status = os.system(f'start {keyword}')
                if status == 0:
                    speaker.say(f'I have opened {keyword} application')
                    renew()
                else:
                    speaker.say(f"I wasn't able to find the app {keyword}. Try again. Please tell me an app name.")
                    speaker.runAndWait()
                    apps()
            except (sr.UnknownValueError, sr.RequestError):
                sys.stdout.write("\r")
                speaker.say("I didn't quite get that. Try again. Please tell me an app name.")
                speaker.runAndWait()
                apps()
            except sr.WaitTimeoutError:
                sys.stdout.write("\r")
                speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. "
                            "Or, please tell me an app name")
                speaker.runAndWait()
                apps()

    elif operating_system == 'Darwin':
        if apps.has_been_called:
            speaker.say("Please repeat the app name alone.")
        else:
            speaker.say("Which app shall I open? Please say the app name alone.")
        speaker.runAndWait()
        with sr.Microphone() as source:
            try:
                sys.stdout.write("\rApps: I'm listening...")
                listener = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                keyword = recognizer.recognize_google(listener)
                sys.stdout.write("\r")
            except (sr.UnknownValueError, sr.RequestError):
                sys.stdout.write("\r")
                speaker.say("I didn't quite get that. Try again.")
                apps()
            except sr.WaitTimeoutError:
                sys.stdout.write("\r")
                speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
                apps()

        if 'exit' in keyword:
            renew()

        v = (subprocess.check_output("ls /Applications/", shell=True))
        apps_ = (v.decode('utf-8').split('\n'))

        for app in apps_:
            if re.search(keyword, app, flags=re.IGNORECASE) is not None:
                keyword = app

        app_status = os.system(f"open /Applications/'{keyword}'")
        apps.has_been_called = True
        if app_status == 256:
            speaker.say(f"I did not find the app {keyword}.")
            apps()
        else:
            speaker.say(f"I have opened {keyword}")
            renew()


def robinhood():
    sys.stdout.write('\rGetting your investment details.')
    from pyrh import Robinhood
    u = os.getenv('user')
    p = os.getenv('pass')
    q = os.getenv('qr')
    rh = Robinhood()
    rh.login(username=u, password=p, qr_code=q)
    raw_result = rh.positions()
    result = raw_result['results']
    from robinhood import watcher
    stock_value = watcher(rh, result)
    sys.stdout.write("\r")
    speaker.say(stock_value)
    speaker.runAndWait()
    renew()


def repeater():
    speaker.say("Please tell me what to repeat.")
    speaker.runAndWait()
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rRepeater: I'm listening...")
            listener = recognizer.listen(source, timeout=3, phrase_time_limit=15)
            keyword = recognizer.recognize_google(listener)
            sys.stdout.write("\r")
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            repeater()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            repeater()
        if 'exit' in keyword or 'quit' in keyword:
            renew()
        speaker.say(f"I heard {keyword}")
        speaker.runAndWait()
    renew()


def chatBot():
    if operating_system == 'Windows':
        speaker.say('Seems like you are running a Windows operating system. Requirements have version conflicting '
                    'installations. So, currently chat bot is available only for mac OS.')
        renew()

    file1, file2 = 'db.sqlite3', f"/Users/{os.environ.get('USER')}/nltk_data"
    if os.path.isfile(file1) and os.path.isdir(file2):
        from chatterbot import ChatBot
        from chatterbot.trainers import ChatterBotCorpusTrainer
        bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
    else:
        sys.stdout.write("\r")
        speaker.say('Give me a moment while I train the module.')
        speaker.runAndWait()
        from chatterbot import ChatBot
        from chatterbot.trainers import ChatterBotCorpusTrainer
        bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train("chatterbot.corpus.english")
        speaker.say('The chatbot is ready. You may start a conversation now.')
        speaker.runAndWait()
    with sr.Microphone() as source:
        try:
            sys.stdout.write("\rChatBot: I'm listening...")
            listener = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            keyword = recognizer.recognize_google(listener)
            sys.stdout.write("\r")
        except (sr.UnknownValueError, sr.RequestError):
            sys.stdout.write("\r")
            speaker.say("I didn't quite get that. Try again.")
            chatBot()
        except sr.WaitTimeoutError:
            sys.stdout.write("\r")
            speaker.say("You're quite slower than I thought. Make quick responses, or go have a coffee. Or,")
            chatBot()
        if 'exit' in keyword or 'quit' in keyword:
            speaker.say('Let me remove the training modules.')
            os.system('rm db*')
            os.system(f'rm -rf {file2}')
            speaker.runAndWait()
            renew()
        else:
            response = bot.get_response(keyword)
            if response == 'What is AI?':
                speaker.say(f'The chat bot is unable to get a response for the phrase, {keyword}. Try something else.')
                speaker.runAndWait()
            else:
                speaker.say(f'{response}')
                speaker.runAndWait()
            chatBot()


def dummy():
    return None


if __name__ == '__main__':
    speaker = audio.init()
    recognizer = sr.Recognizer()
    report.has_been_called, dummy.has_been_called = False, False
    # noinspection PyTypeChecker
    volume = int(speaker.getProperty("volume")) * 100
    sys.stdout.write(f'\rCurrent volume is: {volume}% Voice ID::Friday: 1/17 Jarvis: 7')

    operating_system = platform.system()

    voices = speaker.getProperty("voices")

    if operating_system == 'Darwin':
        # noinspection PyTypeChecker
        speaker.setProperty("voice", voices[7].id)
        speaker.say("Hi, I'm Jarvis. Vicky's virtual assistant. Whom am I speaking with?")
    elif operating_system == 'Windows':
        # noinspection PyTypeChecker
        speaker.setProperty("voice", voices[1].id)
        speaker.setProperty('rate', 190)
        speaker.say("Hi, I'm Friday. Vicky's virtual assistant. Whom am I speaking with?")
    speaker.runAndWait()

    weekend = ['Friday', 'Saturday']
    if current == 'AM' and int(clock) < 10:
        exit_msg = f"Thank you for using Vicky's virtual assistant. Have a nice day. Happy {today}. Good bye."
    elif current == 'AM' and int(clock) >= 10:
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice rest of your day. Good bye."
    elif current == 'PM' and (int(clock) == 12 or int(clock) < 4):
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice afternoon. Good bye."
    elif current == 'PM' and int(clock) < 7 and today in weekend:
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice evening and enjoy your weekend. " \
                   "Good bye."
    elif current == 'PM' and int(clock) < 7:
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice evening. Good bye."
    elif today in weekend:
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice night and enjoy your weekend. Good bye."
    else:
        exit_msg = "Thank you for using Vicky's virtual assistant. Have a nice night. Good bye."

    conditions(initialize())
