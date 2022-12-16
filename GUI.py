import tkinter as tk
from tkinter import filedialog

from wordProcessor import *
from teleprompter import *
import sys

class Window(object):
    def __init__(self, title, size):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size)

        self.fileLabel = tk.Label(self.root, font=("Arial", 15), text="Enter the file name for the script (include the file extentsion '.docx') and then press the button to continue.")
        self.fileEntry = tk.Entry(self.root, font=("Arial", 15), width=50, justify="center")
        self.startWordProcessorButton = tk.Button(self.root, font=("Arial", 15), text="Process File", command=self.run_button)
        self.fileExplorerButton = tk.Button(self.root, font=("Arial", 15), text="Browse Files", command=self.browse_files)
        
        self.fileLabel.place(relx=0.5, y=25, anchor="center")
        self.fileEntry.place(relx=0.5, y=70, anchor="center")
        self.fileExplorerButton.place(relx=0.5, y=120, anchor="center")
        self.startWordProcessorButton.place(relx=0.5,y=170, anchor="center")

        self.quitting = False

    def browse_files(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Word files",".docx"), ("All Files", "*.*")))
        self.fileEntry.insert(0, self.filename)

    def run_button(self):
        parse_script(self.fileEntry.get())
        result = run_teleprompter()
        # print(result)
        # if result == "quitted":
            # self.quitting = True

    def update(self):
        self.root.update()


window1 = Window("Teleprompter", "1000x300")
while window1.quitting == False:
    window1.update()
