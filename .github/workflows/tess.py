import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.widget import Widget
import speech_recognition as sr
import PIL
import io
import pytesseract as t
import gtts
from gtts import gTTS
import os
import cv2 as cv
import matplotlib.pyplot as plt
import pyttsx3 as pt
import translate
from translate import Translator
t.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract'
from PIL import Image
#class ScreenOne(Screen):
 #   img=Image(source='C:/Users/Shai/Pictures/new4.png')
  #  img.allow_stretch=True
   # img.keep_ratio=False
    #img.opacity=1
    #s=Widget()
    #a.add_widget(img)
    
#class Button1App(App):
 #   def build(self):
        
  #      return btn1
   # def btn_clk(self,event):
       
#class SecondScreen(Screen):
spin=Spinner(text='Tamil',values=('Hindi','Telugu','Kannada','Gujarati','Punjabi'),size_hint=(None,None),size=(100,44),pos=(300,280),background_color=(0.784,0.443,0.216,1))
        #runTouchApp(spin)

class OzhiApp(App):
    def build(self):
        Fc=BoxLayout(orientation='vertical')
        Fb=BoxLayout(orientation='horizontal')
        Fl=BoxLayout(orientation='vertical')
        #spin=Spinner(text='Tamil',values=('Hindi','Telugu','Kannada','Gujarati','Punjabi'),size_hint=(None,None),size=(100,44),pos=(300,280),background_color=(0.784,0.443,0.216,1))
        #runTouchApp(spin)
        btn=Button(text="Image to text",font_size='20sp',size=(32,32),size_hint=(0.2,0.2),pos=(300,250))
        btn.bind(on_press=self.btn_clk)
        btn1=Button(text='speak',font_size='20sp',background_color=(0.5,0.765,0.8,1),color=(47,82,88,.67),size=(32,32),size_hint=(.2,.2 ),pos=(350,250))
        btn1.bind(on_press=self.callback)
        Fb.add_widget(btn)
        Fb.add_widget(btn1)
        Fl.add_widget(spin)
        Fc.add_widget(Fl)
        Fc.add_widget(Fb)
        return Fc
    def show(spin,text):
        global la
        la=text
    #spin.bind(text=show)
    #runTouchApp(spin)
    def btn_clk(self,event):
        global la
        cap=cv.VideoCapture(0)
        ret,frame=cap.read()
        image=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        cv.imwrite('frame.jpg',image)
        k=cv.waitKey(0)
        if k==32:
            cv.destroyWindow()
        cap.release()
        image1=cv.imread('frame.jpg')
        cv.namedWindow('img')
        cv.imshow('img',image1)
        img=Image.open('frame.jpg')
        mytext=t.image_to_string(img,lang='eng')
        trans=Translator(to_lang=spin.text)
        transl=trans.translate(mytext)
        #fp=io.open("speech.txt",mode='w',encoding="utf-8")
        #fp.write(mytext)
        #fp.write(c)
        #f=open("speech.txt","r")
        #for lines in f:
            #print(lines)
        print(mytext)
        print(transl)
        #my=gTTS(text=mytext,lang="en",slow=False)
        #my.save("first.mp3")
        #os.system("mpg321 first.mp3")
        engine=pt.init()
        #engine.setProperty('voice','HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN_GB_HAZEL_11.0')  
        engine.say(transl)
        engine.runAndWait()

    def callback(slef,event):
            r=sr.Recognizer()
            while(1):
             
                try:
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source,duration=0.2)
                        audio2=r.listen(source)
                        txt=r.recognize_google(audio2)
                        print(txt)
                        trans1=Translator(to_lang=spin.text)
                        transl1=trans1.translate(txt)
                        print(transl1)
                        eng=pt.init()
                        eng.say(transl1)
                        eng.runAndWait()
                except sr.RequstError as e:
                    print('hi')
                except sr.UnknownValueError:
                    print('hi+++')

#sm=ScreenManager()
#sm.add_widget(ScreenOne(name="HI"))
#sm.add_widget(ScreenTwo(name="Hello"))
    
    #return F1
#voice=engine.getProperty('voices')
#for voi in voice:
    #print("VOICES:%s"%voi.name)
#engine.setProperty('voice','Zira')    
#class ActionApp(App):
 #   def build(self):
  #      bt
   #     return RootWidget()

if __name__=="__main__":
    #runTouchApp(spin)
    myApp=OzhiApp()
    myApp.run()
