# Language Translator
from translate import Translator
translator= Translator(From_lang="English",to_lang="Hindi")
username=input("Enter your name : ")
translation = translator.translate(username)
print (translation)