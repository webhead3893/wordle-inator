from json import load
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("wordle-inator")
root.geometry("500x500")

with open('wordle.json') as file:
    data = load(file)
    edictionary = list(data.keys())

global alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz")

matchList = tk.Text(
    root,
    height = 8,
    width = 70,
)
matchList.place(relx=0.5, rely=0.82, anchor="center")
matchList.insert(tk.END, "- matches")

def wordExists(word):
    if word in edictionary:
        return(True)
    else:
        return(False)

def findWords(wordle, yellows, greys):
    indices = [i for i, char in enumerate(wordle) if char in alphabet]
    wordList = []
    
    for word in edictionary:
        valid = True
        for index in indices:
            if word[index] != wordle[index]:
                valid = False
        for char in yellows:
            if char not in word:
                valid = False
        for char in greys:
            if char in word:
                valid = False
        
        if valid:
            wordList.append(word)

    outputList = str(len(wordList)) + " matches\n" + ", ".join(wordList)
    matchList.delete("0.0", tk.END)
    matchList.insert(tk.END, outputList)

top = tk.Label(
    text = "wordle-inator"
)
top.pack(anchor=tk.CENTER)

lentry1 = tk.Entry(width=1, justify='center')
lentry1.insert(0,"-")
lentry1.place(relx=0.415, rely=0.1, anchor="center")

lentry2 = tk.Entry(width=1, justify='center')
lentry2.insert(0,"-")
lentry2.place(relx=0.455, rely=0.1, anchor="center")

lentry3 = tk.Entry(width=1, justify='center')
lentry3.insert(0,"-")
lentry3.place(relx=0.495, rely=0.1, anchor="center")

lentry4 = tk.Entry(width=1, justify='center')
lentry4.insert(0,"-")
lentry4.place(relx=0.535, rely=0.1, anchor="center")

lentry5 = tk.Entry(width=1, justify='center')
lentry5.insert(0,"-")
lentry5.place(relx=0.575, rely=0.1, anchor="center")

def resetWordle():
    lentry1.delete(0, tk.END)
    lentry1.insert(0,"-")

    lentry2.delete(0, tk.END)
    lentry2.insert(0,"-")

    lentry3.delete(0, tk.END)
    lentry3.insert(0,"-")

    lentry4.delete(0, tk.END)
    lentry4.insert(0,"-")

    lentry5.delete(0, tk.END)
    lentry5.insert(0,"-")

reset = tk.Button(
    text = "reset wordle",
    width = 10,
    activeforeground="white",
    command = resetWordle
).place(relx=0.495, rely=0.17, anchor="center")

yellows = []
yellowi = tk.Label(text="type in yellow letters here").place(relx=0.35, rely=0.2, anchor="e")

yentry = tk.Entry(width=18, justify="left")
yentry.insert(0, "-")
yentry.place(relx=0.35, rely=0.25, anchor="e")

ylist = tk.Label(text="list of entries").place(relx=0.19, rely=0.3, anchor="e")
ybox = tk.Text(
    root,
    height = 7,
    width = 23
)
ybox.place(relx=0.345, rely=0.44, anchor="e")
ybox.insert(tk.END, "-")

def yellowsAdd(self):
    value = yentry.get().lower()
    if(value in alphabet and value not in yellows):
        yellows.append(value)
    elif (value in yellows):
        tk.messagebox.showinfo("yellows", "value already in list.")
    else:
        tk.messagebox.showinfo("yellows", "enter a single *alphabet* at a time.")
    
    yentry.delete(0, tk.END)
    ybox.delete("0.0", tk.END)
    ybox.insert(tk.END, ", ".join(yellows))

yentry.bind("<Return>", yellowsAdd)

def clearYellows():
    yellows.clear()
    ybox.delete("0.0", tk.END)

yclear = tk.Button(
    text = "clear list",
    width = 8,
    activeforeground = "white",
    command = clearYellows
).place(relx=0.19, rely=0.3, anchor="w")


yremovei = tk.Label(text="enter here to remove from list").place(relx=0.4, rely=0.58, anchor="e")
yremove = tk.Entry(width=18, justify="left")
yremove.insert(0, "-")
yremove.place(relx=0.35, rely=0.62, anchor="e")

def yellowsRemove(self):
    value = yremove.get().lower()
    if(value in yellows):
        yellows.remove(value)
    elif (value not in alphabet):
        tk.messagebox.showinfo("yellows", "enter a single *alphabet* at a time.")
    else:
        tk.messagebox.showinfo("yellows", "value not in list.")

    yremove.delete(0, tk.END)
    ybox.delete("0.0", tk.END)
    ybox.insert(tk.END, ", ".join(yellows))

yremove.bind("<Return>", yellowsRemove)

greys = []
greyi = tk.Label(text="type in grey letters here").place(relx=0.675, rely=0.2, anchor="w")

gentry = tk.Entry(width=18, justify='right')
gentry.insert(0, "-")
gentry.place(relx=0.65, rely=0.25, anchor="w")

glist = tk.Label(text="list of entries").place(relx=0.814, rely=0.3, anchor="w")
gbox = tk.Text(
    root,
    height = 7,
    width = 23,
)
gbox.place(relx=0.655, rely=0.44, anchor="w")
gbox.insert(tk.END, "-")

def greysAdd(self):
    value = gentry.get().lower()
    if(value in alphabet and value not in greys):
        greys.append(value)
    elif(value in greys):
        tk.messagebox.showinfo("greys", "value already in list.")
    else:
        tk.messagebox.showinfo("greys", "enter a single *alphabet* at a time.")
    
    gentry.delete(0, tk.END)
    gbox.delete("0.0", tk.END)
    gbox.insert(tk.END, ", ".join(greys))

gentry.bind("<Return>", greysAdd)

def clearGreys():
    greys.clear()
    gbox.delete("0.0", tk.END)

gclear = tk.Button(
    text = "clear list",
    width = 8,
    activeforeground = "white",
    command = clearGreys
).place(relx=0.81, rely=0.3, anchor="e")

gremovei = tk.Label(text="enter here to remove from list").place(relx=0.6, rely=0.58, anchor="w")
gremove = tk.Entry(width=18, justify="right")
gremove.insert(0, "-")
gremove.place(relx=0.65, rely=0.62, anchor="w")

def greysRemove(self):
    value = gremove.get().lower()
    if(value in greys):
        greys.remove(value)
    elif (value not in alphabet):
        tk.messagebox.showinfo("greys", "enter a single *alphabet* at a time.")
    else:
        tk.messagebox.showinfo("greys", "value not in list.")

    gremove.delete(0, tk.END)
    gbox.delete("0.0", tk.END)
    gbox.insert(tk.END, ", ".join(greys))

gremove.bind("<Return>", greysRemove)

analyse = tk.Button(
    text = "analyse",
    width = 10,
    activeforeground = "white",
    command = lambda: findWords([lentry1.get().lower(), lentry2.get().lower(), lentry3.get().lower(), lentry4.get().lower(), lentry5.get().lower()], yellows, greys)
).place(relx=0.5, rely=0.66, anchor="center")



q = tk.Button(
    text = "quit",
    width = 20,
    activeforeground = "white",
    command = root.destroy
).place(relx=0.5, rely=0.97, anchor="center")

root.mainloop()
