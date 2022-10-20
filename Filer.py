import tkinter as tkin

def readFile():        
                                                                           # This function opens the created file, reads it and analyzes if there's any of the database words present
    with open("/home/cathodec/Desktop/file.txt", "r") as fileRead:         # THIS LINE OF CODE HAS TO BE EDITED BY YOU, copypaste your own path here into the quotations
        fContent = fileRead.read()
        badWords = ["píča", "piča", "pičo", 
                    "píčo", "čurák", "čůrák", 
                    "čůráku", "kokot", "kokote", 
                    "debil", "debile", "mrdka", 
                    "mrdko", "mrdat", "kurva", 
                    "děvka", "do piče", "zmrd", 
                    "hajzl", "kunda", "kundo"
                    "mrdal", "mrdala", "mrdali"
                    "kokoti", "kokotům", "kundám",
                    "kundě", "kundu", "debila",
                    "děvku", "piču", "píču",
                    "kurvu", "čuráka", "čůráka",
                    "debila", "mrdku", "mrdky",
                    "mrdal", "mrdala", "mrdali",
                    "ty píčo", "ty pičo", "ty kundo",
                    "do prdele", "ty vole", "do kundy",
                    "ty čůráku", "ty čuráku", "ty zmrde",
                    "ty kokote", "ty debile", "ty magore",
                    "magor"]
        if any(badWord in fContent for badWord in badWords):
            print("Your text contains bad words!!!")       
        else:
            print("Your text doesn't contain bad words and it's family friendly, congrats!")
                
def makeFile():
    
    cont = str(input("Write the file: "))                                  # this function gives you an input entry, makes the file from the input and calls the GUI
    with open("/home/cathodec/Desktop/file.txt", "w") as fileGet:          # THIS LINE OF CODE HAS TO BE EDITED BY YOU, copypaste your own path here into the quotations
        fileGet.write(cont) 
        Win()
    
def Win():    
    root = tkin.Tk()
                                                                               # this function has works with the graphic control
    root.geometry("300x100")
    root.title("Filer")
    button1 =  tkin.Button(root, text="Analyze the file!",
                    bd="8", command=readFile)
    button2 = tkin.Button(root, text="Exit",
                    bd="10", command=root.destroy)
    button1.pack()
    button2.pack()
    root.mainloop()            

makeFile()
