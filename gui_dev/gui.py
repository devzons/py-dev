from tkinter import *

root = Tk()
root.title("Dev GUI")

btn1 = Button(root, text="Button 1")
btn1.pack()

btn2 = Button(root, padx=20, pady=10, text="Button 2")
btn2.pack()

btn3 = Button(root, width=10, height=3, text="Button 3")
btn3.pack()

btn4 = Button(root, fg="red", text="Button 4")
btn4.pack() 

# photo = PhotoImage(file="/Users/don/Projects/python/gui_dev/check.jpg")
# btn5 = Button(root, image=photo)
# btn5.pack()

def btncmd():
    print("Button clicked!")

btn6 = Button(root, text="Working Button", command=btncmd)
btn6.pack() 

root.mainloop()