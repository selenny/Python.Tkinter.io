#!/user/bin/python
# Python Ver:     3.6.3
#
# Author:	      Terri Hall
#
# Purpose:	     Creating a User Interface which allows users to choose files to be checked for updates and then move them.
#
# Tested OS:         This code was written and tested to work with Windows 10.
 

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class ChooseApp:

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Choose From The Choices Below")
        self.label.grid(row = 0, column = 0, columnspan = 3)
        
        ttk.Button(master, text = "Check Files Daily",
                   command = self.check_files).grid(row = 1, column = 0)

        ttk.Button(master, text = "Receive Copied Files",
                   command = self.copy_files).grid(row = 1, column = 1)

        ttk.Button(master, text = "Check For File Updates",
                   command = self.check_update).grid(row = 1, column = 3)

    def check_files(self):
        self.label.config(command = askDirectory)

    def copy_files(self):
        self.label.config(command = askDirectory)
    def check_files(self):
        self.label.config(command = checkFileMove)


def main():            
    
    root = Tk()
    app = ChooseApp(root)
    root.mainloop()
    
if __name__ == "__main__": main()


        

def askDirectory():
    root = Tk()
    directory = filedialog.askdirectory()
    print(directory)
    
if __name__== "askDirectory__": askDirectory()


def checkFileMove(src, dest):
    currentTime = time.time()
    listFile = os.listdir(src)
    
    for files in listFile:
        if files.endswith(".txt"):
            sourceFile = os.path.join(src + files)
        lastFileUpdate = os.path.getmtime(sourceFile)
        print (lastFileUpdate)
        modTime = currentTime - lastFileUpdate
        if modTime < 86400:
            shutil.move(sourceFile, dest)
            print (sourceFile + 'Was moved to FolderB')
        else:
            print ("No files were updated today")
    
def main():
    src = 'C:\Users\webde\Desktop\FolderA\\'
    dest = 'C:\Users\webde\Desktop\FolderB\\'
    checkFileMove(src, dest)
    
                
if __name__=='__main__':
    main()


            







           

