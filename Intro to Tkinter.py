import tkinter as tk
from tkinter import *

root = tk.Tk()

# def changeText():
#     myName
#
#     labelVariable = tk.Label(root, fg="#06a099", text=myName)
#     labelVariable.config(font=("Sylfaen", 30))
#     labelVariable.pack()
#     # print("Hello World")
#
# root.title("Hello World Sample")
# # labelVariable = tk.Label(root, text="Hello Tkinter!")
# myName = "Hello Gurjas"
#
# buttonVariable = tk.Button(root, text="Ok Button", command=changeText)
# buttonVariable.pack()
# root.mainloop()


nameLabel = tk.Label(root, text="Enter your name", width=30, anchor='w')\
    .grid(row=0, column=0, padx=(30,0))
collegeLabel = tk.Label(root, text="Enter your college", width=30, anchor='w')\
    .grid(row=1, column=0, padx=(30,0))

nameEntry = Entry(root)
collegeEntry = Entry(root)

nameEntry.grid(row=0, column=1, padx=(0,50))
collegeEntry.grid(row=1, column=1, padx=(0,50), pady = 20)
username = ""
collegeName = ""

def takeNameInput():
    global nameEntry, collegeEntry
    global username, collegeName
    username = nameEntry.get()
    nameEntry.delete(0, END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, END)

def printDetails():
    print("Username is: %s and college name is: %s" % (username, collegeName))

button = tk.Button(root, text="Take input", command=takeNameInput)
button.grid(row=2, column=0)

displayButton = tk.Button(root, text="Display result", command=printDetails)
displayButton.grid(row=2, column=1)

root.mainloop()