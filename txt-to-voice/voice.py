import tkinter as tk 
from tkinter import *
import speech_recognition as sr

window = tk.Tk()
window.title("Text to Voice")
window.minsize(400,400)
window.maxsize(400,400)

def widgets():
    lbl_start = Label(window, text="please speak!")
    lbl_start.config(font=("Titr", 22, "bold"), bg="blue", fg="white", width=24)
    lbl_start.grid(row=0)

    btn_start = Button(window, text="start", command=get_voice)
    btn_start.config(font=("aviny", 20), bg="lime", width=5)
    btn_start.grid(row=1, pady=10)

r = sr.Recognizer()

def get_voice():
    try:
        with sr.Microphone() as src :
            audio = r.listen(src)
            text = r.recognizer_google(audio)
            text = text.lower()
            print(text)
    except:
        pass



widgets()
window.mainloop()