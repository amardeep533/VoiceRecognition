#!/usr/bin/python
import speech_recognition as sr
import os #imports operating system module
import re #imports regular expression module

class VoiceCommand:

    def obtainCommandFromMicrophone(self):
        '''This method obtains audio from the microphone and returns the audio file'''
        rec = sr.Recognizer()
        audiotext=""
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = rec.listen(source,10)
                audiotext = rec.recognize_google(audio)
        except sr.UnknownValueError:
            os.system('say '+"could not understand audio")
            print("could not understand audio")
        except sr.RequestError as e:
            os.system('say '+"Could not request results from Google")
            print("Could not request results from Google; {0}".format(e))
        return audiotext

    def openApplication(self,replytext,applicationName):
        '''This method opens the application depending on the name of the application provided'''
        if replytext=="yes":
            os.system('open -a '+ applicationName)
        else:
            os.system('say '+"Do you want to try again")

    def textToSpeech(self,textToBeConverted):
        '''This method converts text to speech'''
        os.system('say '+ textToBeConverted)

    def openWebSite(url):
        '''This method opens a website provided by the user'''
        os.system('open '+ url)

    def findUrl(self,inputText):
        '''This method finds the incomplete url from the text data'''
        incompleteUrl = re.compile('\w+.com').search(inputText)
        return incompleteUrl

    def createUrl(self,incompleteUrl):
        '''This method creates complete url from incomplete url'''
        completeUrl = re.sub('^',"https://www.",incompleteUrl)


v=VoiceCommand()
question1="Which application do you want to open?"
v.textToSpeech(question1)
applicationName = v.obtainCommandFromMicrophone()
print applicationName
question2="do you mean?" + applicationName
v.textToSpeech(question2)
reply = v.obtainCommandFromMicrophone()
print reply
v.openApplication(reply,applicationName)
