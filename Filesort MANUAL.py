import os, shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import *

def organize(userInput):
    userInput += "/"
    filelist = os.listdir(userInput) #Puts all of the Files from the given Directory into a list.
    extensions = {} #Dictionary for all different Extensions. Key: Extension; Value: Foldername
    while len(filelist) > 1:
        for x in range(len(filelist)):
            filename, file_extension = os.path.splitext(filelist[x]) #Splits the filename and the extension
            if (file_extension not in extensions) and (not file_extension == ""): #Only when new entry needs to be created
                extensions[file_extension] = file_extension + " Folder"
                print(extensions)
            newpath = userInput + extensions[file_extension] #creates the new Path of the new Folder if it's not yet created
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(str(userInput + filelist[x]), str(newpath + "/" + str(filelist[x]))) #moves the File in the Downloads folder in the coresponding sub-Folder


def select_directory():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, selected_dir)
        process_button.config(state="active")  # Aktiviere den "Verarbeiten"-Button

def process_input():
    selected_dir = directory_entry.get()  # Das ausgewählte Verzeichnis holen
    # Hier kannst du deine Verarbeitungslogik für das ausgewählte Verzeichnis implementieren
    organize(selected_dir)
    # Zum Beispiel: result = "Verzeichnis erfolgreich ausgewählt: " + selected_dir
    result_label.config(text=f"Aktion erfolgreich: Verzeichnis ausgewählt: {selected_dir}")

# GUI erstellen
root = tk.Tk()
root.title("Verzeichnisauswahl und Verarbeitung")
root.geometry("400x200")

# Verzeichnisauswahl-Button erstellen
select_dir_button = tk.Button(root, text="Verzeichnis auswählen", command=select_directory)
select_dir_button.pack()

# Eingabefeld für ausgewähltes Verzeichnis erstellen
directory_entry = tk.Entry(root)
directory_entry.pack()

# Verarbeitungsbutton erstellen (zunächst deaktiviert)
process_button = tk.Button(root, text="Verarbeiten", command=process_input, state="disabled")
process_button.pack()

# Label für Erfolgsmeldung erstellen
result_label = tk.Label(root, text="")
result_label.pack()

# GUI starten
root.mainloop()
