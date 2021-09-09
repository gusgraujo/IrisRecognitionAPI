from tkinter import *
from tkinter import Menu
from functools import partial
from PIL import Image,ImageTk
from fnc.Iris import Olho
import fnc.Iris
import tkinter.messagebox

olho1 = Olho(r"E:\TCC\image_iris\Amostra5.1.jpg",1)

olho2 = Olho(r"E:\TCC\image_iris\Amostra5.jpg",2)

def compararHd(info1,info2):

    hd = fnc.matching.calHammingDist(info1[0],info1[1],info2[0],info2[1])
        
    print(hd)



def onClick():
    tkinter.messagebox.showinfo("hd")

def montar_inicio():

    #Cria Plat grafica

    root = Tk()
 
    root.title("Protótipo Íris")
    root.configure(background = "Gray")
    
    menu = Menu(root)

    
    
    labelA = Label(root,text = "Imagem Referencia 1 :")
    labelA.grid(column = 0 , row = 3,pady = 3)
    
    image = Image.open(olho1.caminho)
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 0 , row = 6,pady = 3)


    
    labelA = Label(root,text = "Imagem Referencia 2 :")
    labelA.grid(column = 4 , row = 3,pady = 3)

    image = Image.open(olho2.caminho)
    image = image.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    w = Label(image=photo)
    w.image = photo
    w.grid(column = 4 , row = 6,pady = 3)


    buttonC = Button(root,width = 30 , text = "Trocar Referencia 1")
    buttonC.grid(column = 0 , row = 7,pady = 3)

    
    buttonA = Button(root,width = 30 , text = "Trocar Referencia 2")
    buttonA.grid(column = 4 , row = 7,pady = 3)
    

        
    f1 = olho1.extrairCodigo()
    f2 = olho2.extrairCodigo()

    
    
    labelB1 = Label(root,text ="Binarios : ")
    labelB1.grid(column = 0 , row = 8,pady = 3)

    
    labelF1 = Label(root,text = f1)
    labelF1.grid(column = 0 , row = 9,pady = 3)
    
    
    labelB2 = Label(root,text ="Binarios : ")
    labelB2.grid(column = 4 , row = 8,pady = 3)

    
    labelF2 = Label(root,text = f2)
    labelF2.grid(column = 4 , row = 9,pady = 3)

    hd = fnc.Iris.compararHd(f1,f2)
    
    buttonExtract = Button(root,width = 30 , text = "Calcular HD",command = onClick)
    buttonExtract.grid(column = 3 , row = 9)
    
    
   

    item = Menu(menu)
    
    item.add_command(label = 'ADD REF')
    item.add_command(label = 'Exit')


    
    root.config(menu=item)
    #define tamanho da tela
    root.geometry("800x600")

    root.mainloop()



montar_inicio()




