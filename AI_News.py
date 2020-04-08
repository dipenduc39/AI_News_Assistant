# -*- coding: utf-8 -*-

#Import all requied module
from bs4 import BeautifulSoup as bs
import requests
import speech_recognition as sr
import pyttsx3
import time as t
import platform
import socket
import pygame
from pygame.mixer import music

#Initialize the pyttsx3 class
engine = pyttsx3.init()
#Get the Default voices from your computer
voices = engine.getProperty('voices')
#Set the voice using voice id, It may different in your Computer. According to my PC voice id = 0; means female voice. 
engine.setProperty('voice', voices[0].id)
#Set the Speech rate per minute 
engine.setProperty('rate', 130)
#For more Information on pyttsx3 refer to this link - https://pyttsx3.readthedocs.io/en/latest/engine.html

#Get the Computer Name
computer_name = platform.node()

#Create Speech Recognizer Object
#For more Information on Speech Recognizer refer to this link - https://pypi.org/project/SpeechRecognition/
r = sr.Recognizer()

#Mixer Initialize
pygame.mixer.init()
#Load the background Music file
music.load("background_music.mp3")
#Set the Music Volume
music.set_volume(0.1)

#Create a speak function 
def speak(text):
    engine.say(text)
    #Run the speech and wait 
    engine.runAndWait()

def popular_ai_news():
    #While Loop for continue check the Internet Connection
    while True:
        try:
            #Check the Internet Connection
            socket.create_connection(("Google.com",80))
            #Send the request to the News website
            base_page = requests.get("https://artificialintelligence-news.com/news/")
            #Extract all page text
            bp_text = bs(base_page.text)
            ####Play Background News Music
            music.play()
            speak("Hey {} Here is the top headline for today".format(computer_name))
            #Create empty list to store news headlines for later use
            saved_headline = []
            #Search all link which under class "widget techforge-post-types"
            for base_links in bp_text.find("div", {"class": "widget techforge-post-types"}).findAll("a", href = True):
                  #Find the top headlines
                  headlines = base_links.find("h3")
                  if headlines is not None:
                    print(headlines.text)
                    #Call the speak function
                    speak(headlines.text)
                    #Store the headlines for later use
                    saved_headline.append(headlines.text)
                  else:
                    continue
                  t.sleep(2)
            music.stop()
        except OSError:
            print("No Internet Connection Found")
            t.sleep(5)
            continue
            
        return saved_headline
        break
    
#Call the Function 1st time
saved_headline = popular_ai_news()
while True: 
    try:
        speak("Do you want to listen again")
        with sr.Microphone() as source:
            #Listen the audio through Microphone
            audio = r.listen(source,phrase_time_limit=2)
        if "yes" in r.recognize_google(audio):
            ##Play Background News Music
            music.play()
            speak("Oky, Here is the top headline for today")
            for headline in saved_headline:
                print(headline)
                speak(headline)
                t.sleep(2)
            ##Stop Background Music
            music.stop()
        else:
            speak("Oky, Have a good day")
            break
    except:
         speak("Sorry I can't listen properly")
