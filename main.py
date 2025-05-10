from tkinter import *
from tkinter import messagebox
from PIL import image, imageTK

# Setting Up Main Window
root = TK()
root.title('Denomination Counter')
root.configure(bg = 'light blue')
root.geometry('650x400')

# Adding Image and Labels To the Window
upload = Image.open('download.jpg')
#Resizethe image using resize() method
upload = upload.resize(300,300)
image = imageTK.photoImage(upload)
label = label(root, image=image, bg='light blue')
label.place(x=180 , y = 20)
