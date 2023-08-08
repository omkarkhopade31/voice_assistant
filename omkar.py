import wolframalpha

client = wolframalpha.Client("Enter Your own Wolfram API")  
import wikipedia                                   
import PySimpleGUI as sg                           
import speech_recognition as sr                    
import pyttsx3                                 

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume',1.0)
engine.say("Hey Brother")
print("Hey Brother")
engine.say("What is your question")
print("What is your question")
engine.runAndWait()

g = sr.Recognizer() 
def SpeakText(command):

    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    engine.say(command)
    engine.runAndWait()


with sr.Microphone() as source2:
    g.adjust_for_ambient_noise(source2,duration=0.1)  
    audio2 = g.listen(source2)

MyText = g.recognize_google(audio2)                   
MyText = MyText.lower()                                
query = "Your Question is"
SpeakText(query)
SpeakText(MyText)
waitMessage = "Please wait Boss i am searching for you."
print("Searching for your question about " + MyText)
SpeakText(waitMessage)


sg.theme('Reddit')
window = sg.Window('Beast : Your Personal Assistance')


SearchEngine = pyttsx3.init()  
SearchEngine .setProperty('rate', 180)
SearchEngine.setProperty('volume',1.0)


try:
    wiki_res = wikipedia.summary(MyText, sentences=2)
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res, "Wikipedia Result :" + wiki_res)
    SearchEngine.say(wolfram_res)
    SearchEngine.say(wiki_res)

except wikipedia.exceptions.DisambiguationError:
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res)
    SearchEngine.say(wolfram_res)

except wikipedia.exceptions.PageError:
    res = client.query(MyText)
    wolfram_res = next(res.results).text
    sg.PopupNonBlocking("Wolfram Result : " + wolfram_res)
    SearchEngine.say(wolfram_res)

except:
    wiki_res = wikipedia.summary(MyText, sentences=2)
    sg.PopupNonBlocking("Wikipedia Result : " + wiki_res)
    SearchEngine.say(wiki_res)

SearchEngine.runAndWait()

window.close()
