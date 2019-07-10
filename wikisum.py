import wikipedia
import pyfiglet

result = pyfiglet.figlet_format("Wikisum", font = "slant")
print(result)
print("Author:An-Source                                    Version:1.0.0")

value = input("What do you want to Know about: ")
lang = input("Select your language: ")
num = input("How long should be the summery: ")

print("                      ")
wikipedia.set_lang(lang)
print(wikipedia.summary(value,sentences=num)) 

print("                      ")


   


