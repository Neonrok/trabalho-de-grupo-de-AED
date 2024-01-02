from tkinter import *
from tkinter import messagebox
import os

jan= Tk()

class ordens:
    def saving(self):
        save = self.Nome.get()
        password = self.Pass.get()

        self.escreva(save, password)

    @staticmethod
    def escreva(X, Y):
        ficheiro = "./base/contas/{0}.txt".format(X)
        if os.path.isfile(ficheiro):
            with open(ficheiro, "r") as g:
                ordens.entra(g,Y)
        else:
            with open(ficheiro, "w") as g:
                escrita = Y
                g.write(escrita)

    @staticmethod
    def entra(g,Y):
        pas = g.readline().strip()
        Y = Y.strip()
        if Y == pas:
            messagebox.showinfo(title="^_^" ,message="bem vindo")
        else:
            messagebox.showwarning(title="erro" ,message="esse usuario existe mas a palavra pass está errada")
        print(pas)
        print(Y)



class tela(ordens):
    def __init__(self):
        self.jan = jan
        self.tela()
        self.botões()
        self.prencher()
        jan.mainloop()
    
    def tela(self):
        
        SW=jan.winfo_screenwidth()
        SH=jan.winfo_screenheight()

        AW=400
        AH=450

        x=(SW/2)-(AW/2)
        y=(SH/2)-(AH/2)

        self.jan.geometry(f'{AW}x{AH}+{int(x)}+{int(y)}')

        self.jan.title("criar")

        self.jan.iconbitmap("./cat-_1_.ico")

        self.jan.configure(bg="#636A72")

        self.jan.minsize(width=400, height=450)

        self.jan.maxsize(width=400, height=450)

    def botões(self):
        self.painel=PanedWindow(jan, bg="#636A72", bd=3, relief="sunken")
        self.butão_I=Button(jan, text="SAVE", bg="#636A72", fg="blue", font=("Helvetica 9 bold"), borderwidth="2px", relief="groove", command=self.saving)#buttona é para butão lable é para texto

        self.butão_I.place(relx=0.05,y=160)
        self.painel.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)

    def prencher(self):
        self.textoI=Label(jan, text="Nome", fg="black", bg="#636A72")
        self.Nome=Entry(jan, width=50)
        self.textoII=Label(jan, text="PasseWord", fg="black", bg="#636A72")
        self.Pass=Entry(jan, width=20, show="-")

        self.textoI.place(relx=0.05, y=50)
        self.Nome.place(relx=0.05, y=75)
        self.textoII.place(relx=0.05, y=110)
        self.Pass.place(relx=0.05, y=135)
        



tela()