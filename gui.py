import tkinter as tk
from tkinter import Entry, Label

def respond_to_query():
    query = entry.get()
    response = "This is a dummy response for the query: " + query
    label.config(text=response)

root = tk.Tk()
root.title("Google Assistant GUI")

label = Label(root, text="Ask me anything")
label.pack()

entry = Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=respond_to_query)
button.pack()

root.mainloop()
