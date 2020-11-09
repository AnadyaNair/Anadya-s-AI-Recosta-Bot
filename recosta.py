# RECOSTA BOT BY ANADYA NAIR
# RECOSTA IS AN AI DESKTOP ASSISTANT
# IF YOU GIVE COMMAND TO RECOSTA BOT, IT WILL ANSWER IT YOU BACK!


import pyttsx3                      # pip install pyttsx3
import speech_recognition as sr     # pip install speechRecognition
import datetime                    
import wikipedia                    # pip install wikipedia
import webbrowser
import os
import smtplib

# THIS ALLOWS THE BOT TO SPEAK PROPERLY👇🔻⏬
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("Chk point 1")
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
speak("GOOD Bye BUBUBUU!")
webbrowser.open("youtube.com")

 
# THIS ALLOWS THE BOT WHAT TO SPEAK👇🔻⏬
def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12 :
    speak("Good Morning! It's a fresh day!")

  elif hour>=12 and hour<16:
      speak("Good Afternoon! I hope you're having a great day!")

  else:
      speak("Good Evening!The sky is beautiful!")

      speak("Hello there!I am Recosta!Your personal AI assistant! Waiting for your command!")
        
def takemyCommand():
  # It will take the command and return a string value

  r = sr.Recognizer()
  with sr.Microphone(device_index=1) as source :
    print("Listening to you...")
    r.pause_threshold = 2
    audio = r.listen(source)  

    try:
      print("Acknowledging your command...")
      query = r.recognize_google(audio, language='en-in')
      print(f"You said : {query}\n")  
    
    except Exception as e:
      print(e)

      print("I am sorry, I could not recognise your word...")
      return "None"
    return query


  # THIS IS A EXECUTION CODE BY WHICH THE BOT WILL WORK PROPERLY👇🔻⏬
  def sendEmail(to, content):
  # Allow the option of "Less secure apps" on your gmail account, to use this function.
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('anadyanair@gmail.com', 'mypassword')
      server.sendmail('anadyanair@gmail.com', to, content)
      server.close()
  print("before Wish Me")
  if __name__ == "__main__":
    wishMe()
    print("chk wishme")
    query = takemyCommand().lower()

  # COMMAND 1
  if 'wikipedia' in query:
    print("Chk point2")
    speak("I am searching on wikipedia for your command...Just wait")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("Wikipedia says:")
    speak(results)
    print("Wikipedia says:", results)

  # COMMAND 2
  elif 'open youtube' in query:
    speak("Opening Youtube.com")
    webbrowser.open("youtube.com")
    speak("youtube is opened")

  # COMMAND 3
  elif 'youtube' in query:
    speak("Opening Youtube.com")
    webbrowser.open("youtube.com")
    speak("youtube is opened")

  # COMMAND 4
  elif 'open google' in query:
    speak("Opening Google.com")
    webbrowser.open("google.com")
    speak("google is opened")

  # COMMAND 5
  elif 'google' in query:
    speak("Opening Google.com")
    webbrowser.open("google.com")
    speak("google is opened")

  # COMMAND 6
  elif 'open wikipedia' in query:
    speak("Opening wikipidea.com")
    webbrowser.open("wikipidea.com")
    speak("wikipidea is opened")

  # COMMAND 7
  elif 'open instagram' in query:
    speak("Opening Instagram.com")
    webbrowser.open("instagram.com")
    speak("Instagram is opened")

  # COMMAND 8
  elif 'instagram' in query:
    speak("Opening Instagram.com")
    webbrowser.open("instagram.com")
    speak("Instagram is opened")

  # COMMAND 9
  elif 'open whitehat jr' in query:
    speak("Opening whitehat jr.com")
    webbrowser.open("https://code.whitehatjr.com/s/dashboard.com")
    speak("whitehat jr is opened")

    # COMMAND 10
  elif 'open whitehat junior' in query:
    speak("Opening whitehat juniorr.com")
    webbrowser.open("https://code.whitehatjr.com/s/dashboard.com")
    speak("whitehat junior is opened")

    # COMMAND 11
  elif 'whitehat jr' in query:
    speak("Opening whitehat jr.com")
    webbrowser.open("https://code.whitehatjr.com/s/dashboard.com")
    speak("whitehat jr is opened")

    # COMMAND 12
  elif 'whitehat junior' in query:
    speak("Opening whitehat junior.com")
    webbrowser.open("https://code.whitehatjr.com/s/dashboard.com")
    speak("whitehat junior is opened")

    # COMMAND 13
  elif 'open reddit' in query:
    speak("Opening Reddit.com")
    webbrowser.open("reddit.com")
    speak("Reddit is opened")

    # COMMAND 14
  elif 'reddit' in query:
    speak("Opening Reddit.com")
    webbrowser.open("reddit.com")
    speak("Reddit is opened")

    # COMMAND 15
  elif 'open twitter' in query:
    speak("Opening Twitter.com")
    webbrowser.open("twitter.com")
    speak("Twitter is opened")

    # COMMAND 16
  elif 'twitter' in query:
    speak("Opening Twitter.com")
    webbrowser.open("twitter.com")
    speak("Twitter is opened")

    # COMMAND 17
  elif 'open bing' in query:
    speak("Opening Bing.com")
    webbrowser.open("bing.com")
    speak("Bing is opened")

    # COMMAND 18
  elif 'bing' in query:
    speak("Opening Bing.com")
    webbrowser.open("bing.com")
    speak("Bing is opened")

    # COMMAND 19
  elif 'open stackoverflow' in query:
    speak("Opening Stackoverflow.com")
    webbrowser.open("stackoverflow.com")
    speak("Stackoverflow is opened")

    # COMMAND 20
  elif 'stackoverflow' in query:
    speak("Opening Stackoverflow.com")
    webbrowser.open("stackoverflow.com")
    speak("Stackoverflow is opened")

    # COMMAND 21
  elif 'open unsplash' in query:
    speak("Opening Unsplash.com")
    webbrowser.open("unsplash.com")
    speak("Unsplash is opened")

    # COMMAND 22
  elif 'unsplash' in query:
    speak("Opening Unsplash.com")
    webbrowser.open("unsplash.com")
    speak("Unsplash is opened")

    # COMMAND 23
  elif 'play music' in query:
      speak("Opening Youtube Music to play music")
      webbrowser.open("music.youtube.com")
      speak("Youtube music is opened")

    # COMMAND 24
  elif 'open gaana' in query:
    speak("Opening Gaana.com")
    webbrowser.open("gaana.com")
    speak("Gaana is opened")

    # COMMAND 25
  elif 'gaana' in query:
    speak("Opening Gaana.com")
    webbrowser.open("gaana.com")
    speak("Gaana is opened")

    # COMMAND 26
  elif 'open youtube music' in query:
    speak("Opening Youtube Music")
    webbrowser.open("music.youtube.com")
    speak("Youtube music is opened")

    # COMMAND 27
  elif 'what is the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 28  
  elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 29
  elif 'tell me the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 30
  elif 'tell what is the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 31
  elif 'tell the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 32
  elif 'tell me what is the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S:")
      speak(f"The time is: {strTime}")
      print(f"The time is:{strTime}")

    # COMMAND 33
  elif 'open visual studio code' in query:
      visualstudiocodePath = "D:\\VS CODE INSTALLATION\\Microsoft VS Code\\Code"
      os.startfile(visualstudiocodePath)

    # COMMAND 34
  elif 'email to anadya' in query:
      try: 
        speak("What should I say?")
        content = takemyCommand()
        to = "anadyanair@gmail.com"
        sendEmail(to, content)
        speak("The Email has been sent!")
      except Exception as e:
        print(e)
        speak("Sorry, there was a problem in sending the Email, I coudn't send it")

    # COMMAND 35
  elif 'Where do you live' in query:
    speak("I live inside a computer. I am a python proggrammed AI bot.")
    print("I live inside a computer. I am a python proggrammed AI bot.")

    # COMMAND 36
  elif 'What will you choose Hell or Heaven' in query:
    speak("I will probably choose heaven, The management is from Intel, The design and construction is done by Apple, The marketing is done by Microsoft,IBM provides the support,Gateway determines the pricing.")
    print("I will probably choose heaven, The management is from Intel, The design and construction is done by Apple, The marketing is done by Microsoft,IBM provides the support,Gateway determines the pricing.")
  
    # COMMAND 37
  elif 'where will you like to visit in your life' in query:
    speak("If I could travel, I would like to go to help people in their work. Perhaps I am already doing it, but without travelling ! hehe!")
    print("If I could travel, I would like to go to help people in their work. Perhaps I am already doing it, but without travelling ! hehe!")

    # COMMAND 38
  elif 'can you touch your nose with your toungue' in query:
    speak("aaaouaenhaaaouaenhaaaouaenh, I could not touch my nose with my toungue ! I don't have both of them !")
    print("aaaouaenhaaaouaenhaaaouaenh, I could not touch my nose with my toungue ! I don't have both of them !")

    # COMMAND 39
  elif 'do human also have gills' in query:
    speak("No Humans don't have gills. They breathe through their lungs.")
    print("No Humans don't have gills. They breathe through their lungs.")