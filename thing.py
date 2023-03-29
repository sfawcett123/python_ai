import os
import speech_recognition as sr
import transformers 
import torch
import numpy as np
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

class ChatBot():
    def __init__( self , name ):
        print( "Starting up ", name  )
        self.name = name 
        self.nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
        os.environ["TOKENIZERS_PARALLELISM"] = "true"

    def respond(self , text ):
        chat = self.nlp(transformers.Conversation(ai.text), pad_token_id=50256)
        res = str(chat)
        res = res[res.find("bot >> ")+6:].strip()
        return res

    def text_to_speech( self, text ):
        speaker = gTTS( text , lang='en' )
        speaker.save("res.mp3")
        sound = AudioSegment.from_file( "res.mp3" )
        play( sound )

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("listening...")
             audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            return( self.text)
        except:
            return("I didn't understand that")

if __name__ == "__main__":
     ai = ChatBot(name="Dev")
     while True:
         text = ai.speech_to_text()
         res = ai.respond( text )
         print( "-->" , res )
         ai.text_to_speech( res )
