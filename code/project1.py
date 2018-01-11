from Tkinter import *
from PIL import ImageTk, Image
import sys
import os

window = Tk()
window.title("EMOTION DETECTOR")
window.geometry("500x500")
window.configure(background='grey')

path = "images.jpeg"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(window, image = img)
panel.pack()

label_1 = Label(window,text="\nThis is where the 'magic' happens\n",bg="blue",fg="white")
label_1.pack()

label_2 = Label(window,text="\n-->Press SPACE to take pictures; press ESC to exit\n")
label_2.pack(side=BOTTOM)

def mainFunction():
	os.system('python main.py')

frame = Frame(window)
frame.pack()

button_1 = Button(window, text="\nStart the Program\n",bg="red",width=17,fg="white",font=("Arial,14"), command=mainFunction)
button_1.pack()

button_2 = Button(window,text="\nQuit\n", bg="red",width=18,fg="white",font=("Arial",14), command=frame.quit)
button_2.pack()

window.mainloop()
