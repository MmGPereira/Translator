import PIL.Image
#from PIL import Image
from pytesseract import pytesseract
import requests
from googletrans import Translator
from tkinter import *
from tkinter import simpledialog
from gtts import gTTS
from playsound import playsound


########### INITIALIZING WINDOW ###########

root = Tk()
root.geometry('1000x300')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('Photo Translation - TEXT TO SPEECH')

#Heading
Label(root, text = 'Photo Translation' , font='arial 15 bold' , bg ='white smoke').pack()

#Text variable
Msg = StringVar()

#Entry
entry_field = Entry(root, textvariable = Msg, width ='150')
entry_field.place(x=20 , y=100)


########### PHOTO TO TEXT ###########

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# URL of chosen photo
get_url = entry_field.get()
url_input = str(get_url)
##url_input=input("Enter the photo URL:")

#Downloads and creates local file
#.content after request.get() saves the image
img_data = requests.get(url_input).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

# Opening the image & storing it in an image object
##img = Image.open('image_name.jpg')
fp = open('image_name.jpg',"rb")
img = PIL.Image.open(fp)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract


########### TRANSLATE TEXT ###########

# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)

#Translates the string from the image
file_translate = Translator()
translated = file_translate.translate(text, dest='fr')
result = translated.text
#print(translated.text)

#Creates a file with te translated sentence
f = open('result', 'w')
f.write(result)


########### TEXT TO SPEECH ###########

def translate():
    speech = gTTS(text = result)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')

def Exit():
    root.destroy()

def next_photo():
    Msg.set("")

#Button
Button(root, text = "Translate" , font = 'arial 15 bold', command = translate, width = 10).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=320,y=140)
Button(root, text = 'Next Photo', font='arial 15 bold', command = next_photo).place(x=175 , y =140)

#infinite loop to run program
root.mainloop()