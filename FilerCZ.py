import tkinter as tkin

def readFile():        
                                                                           # tato funkce otevře napsaný soubor, analyzuje ho a napíše, zda se v něm nacházejí, nebo nenacházejí slova ze seznamu
    with open("/home/cathodec/Desktop/file.txt", "r") as fileRead:         # TENTO ŘÁDEK KÓDU MUSÍ BÝT ZMĚNĚN TEBOU, napiš si do uvozovek vlastní cestu k souboru a jeho název ("/cesta/k/souboru/název.txt")
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
            print("Tvůj text obsahuje sprosté výrazy!!!")      
        else:
            print("Tvůj text není vulgární a je rodinně nezávadný, gratuluji!")
                
def makeFile():
    
    cont = str(input("Napiš svůj text: "))                                 # tato funkce vezme tvůj text, udělá a uloží z něj soubor, počemž spustí dialogové okno
    with open("/home/cathodec/Desktop/file.txt", "w") as fileGet:          # TENTO ŘÁDEK KÓDU MUSÍ BÝT ZMĚNĚN TEBOU, napiš si do uvozovek vlastní cestu k souboru a jeho název ("/cesta/k/souboru/název.txt")
        fileGet.write(cont) 
        Win()
    
def Win():    
    root = tkin.Tk()
                                                                           # tato funkce vytváří dialogové okno (GUI)
    root.geometry("300x100")
    root.title("Filer")
    button1 =  tkin.Button(root, text="Analyzuj text!",
                        bd="8", command=readFile)
    button2 = tkin.Button(root, text="Zavřít",
                         bd="10", command=root.destroy)
    button1.pack()
    button2.pack()
    root.mainloop()            

makeFile()