
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
#import datetime
import os
from pydub import AudioSegment
from pydub.playback import play
#import pyautogui



wel = pyttsx3.init()#تجهيز المكتبة للاستخدام باسم المتحول 
voices = wel.getProperty('voices')#للحصول من المكتبة على خصائص الصوت
wel.setProperty('voice', voices[0].id)#لاننا نستخدم ميك اللابتوب نستخدم 0 ولو خارجي 1 
#دالة التكلم 
def Speak(audio):#دالة تكلم الصوت
     wel.say(audio)#نطق الملف الصوتي 
     wel.runAndWait()#تحدث وانتظر الامر 

def Take_coummand():#دالة اغطاء الاوامر
    command = sr.Recognizer()# مكتبة التعرف على الصوت 
    with sr.Microphone() as mic: #انشاء اختصار لكلمة ميكرفون عند استدعاء خاصية الميكرفون
        print("say command ......")
        command.phrase_threshold = 0.4#دقة الاستماع للصوت كلما كانت اقل كانت الدقة اعلى واخترنا الدقة متوسطة نظرا للضجيج
        audio = command.listen(mic) #عرفتو انو الصوت الي بدةو يسمعو هو المتحول audio
        try:
            print("recording....")
            query = command.recognize_google(audio , language='en')#باستخدام المتعرف المقدم من غوغل تعرف على الصوت ماذا يقول 
            print(f'you sad :  {query}')#هنا سوف يطبع لقد قولت (الاوامر الي بقولها)
        except Exception as Error:#هنا في حالة حدوث خطاء لا يعيد شيئ 
            return None
        return query.lower()



while True:
    query = Take_coummand()
    if 'good morning' in query:
        b = AudioSegment.from_mp3('C:\\Users\\Jouna\\OneDrive\\سطح المكتب\\python\\مشاريع AI\\sound command using python and AI of google\\sounds\\welcome.mp3')
        play(b)
    elif 'good evening' in query:
        b = AudioSegment.from_mp3('C:\\Users\\Jouna\\OneDrive\\سطح المكتب\\python\\مشاريع AI\\sound command using python and AI of google\\sounds\\goodevining.mp3')
        play(b)

    elif 'open new tab in google' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://www.google.com/')

    elif 'open my page in facebook' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://m.facebook.com/people/Jounait-Boshi/100009700692639/')
        
    elif 'open my instagram page' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://www.instagram.com/jounaitbochi/')

    elif 'open my twitter page' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://twitter.com/Jounait2000')

    elif 'open my courses' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://www.coursera.org/')

    elif 'open youtube page' in query:
        time.sleep(2)
        webbrowser.open_new_tab('https://www.youtube.com/')

    elif 'shutdown pc' in query:
        time.sleep(2)
        print("work right now ")
        time.sleep(10)
        #مشان الوقت الحالي ما يطفي الكومبيتر 
        os.system("shutdown /s /t 1")

    elif 'open vs' in query:
        time.sleep(2)
        vs_code_path = "C:\\Users\\Jouna\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vs_code_path)
    

    elif 'open get hub' in query:
        time.sleep(2)
        vs_code_path = "C:\\Users\\Jouna\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
        os.startfile(vs_code_path)

    ''' هذه الوظيفة لكتبة البوستات مازلت قيد التطوير
    elif 'write post in facebook' in query:
        time.sleep(2)
        post = input("enter your post: ")
        webbrowser.register('chrome',None,
        webbrowser.BackgroundBrowser("C:\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        )
        link_write_post_in_facebook = 'رابط الصفحة الخاص بك'
        time.sleep(5)
        webbrowser.get('chrome').open_new(link_write_post_in_facebook)
        time.sleep(10)
        pyautogui.hotkey('ctrl','f')
        pyautogui.typewrite("بم تفكر؟")
        pyautogui.press('enter')
        pyautogui.press('escape')
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.typewrite(post)
        #pyautogui.click(690,590)
        #search google or type a url
    '''



    
    

    
    
    

    






