import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

user="guest"

#tela para logar e criar conta
class TelaCriação(Toplevel):
    def __init__(self, master=None, user_var=None):
        super().__init__(master)
        self.user_var = user_var
        self.tela()
        self.utilizador()
        self.prencher()

    def tela(self):
        SW = self.winfo_screenwidth()
        SH = self.winfo_screenheight()

        AW = 400
        AH = 450

        x = (SW/2) - (AW/2)
        y = (SH/2) - (AH/2)

        self.geometry(f'{AW}x{AH}+{int(x)}+{int(y)}')
        self.title("criar")
        self.iconbitmap("./cat-_1_.ico")
        self.configure(bg="#636A72")
        self.minsize(width=400, height=450)
        self.maxsize(width=400, height=450)

    def utilizador(self):
        self.painel = PanedWindow(self, bg="#636A72", bd=3, relief="sunken")
        self.butão_I = Button(self, text="SAVE", bg="#636A72", fg="blue", font=("Helvetica 9 bold"), borderwidth="2px", relief="groove", command=self.saving)

        self.butão_I.place(relx=0.05, y=160)
        self.painel.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)

    def prencher(self):
        self.textoI = Label(self, text="Nome", fg="black", bg="#636A72")
        self.Nome = Entry(self, width=50)
        self.textoII = Label(self, text="PasseWord", fg="black", bg="#636A72")
        self.Pass = Entry(self, width=20, show="-")

        self.textoI.place(relx=0.05, y=50)
        self.Nome.place(relx=0.05, y=75)
        self.textoII.place(relx=0.05, y=110)
        self.Pass.place(relx=0.05, y=135)

    def saving(self):
        save = self.Nome.get()
        password = self.Pass.get()

        self.escreva(save, password)


    def escreva(self, X, Y):
        global user

        ficheiro = "./base/contas/{0}.txt".format(X)
        if os.path.isfile(ficheiro):
            with open(ficheiro, "r") as g:
                self.entra(g, Y, X)
        else:
            with open(ficheiro, "w") as g:
                escrita = Y
                g.write(escrita)
            user=X
            self.user_var.set(f"usuario: {user}")
            self.destroy()


    def entra(self, g, Y, X):
        pas = g.readline().strip()
        Y = Y.strip()
        if Y == pas:
            global user
            messagebox.showinfo(title="^_^", message="bem-vindo")
            user=X
            self.user_var.set(f"usuario: {user}")
            self.destroy()
        else:
            messagebox.showwarning(title="erro", message="esse usuário existe, mas a palavra-passe está errada")

#tela principal
class tela(tk.Tk):
    def __init__(self):#base para executar tudo
        super().__init__()
        self.user_var = tk.StringVar()

        self.tela()
        self.utilizador()
        self.prencher()
        self.mainloop()
    
    def tela(self):#configotações basicas da tela

        self.state("zoomed")

        self.title("catacumba")

        self.iconbitmap("./cat-_1_.ico")

        self.configure(bg="#636A72")

        SW=self.winfo_screenwidth()
        SH=self.winfo_screenheight()

        self.minsize(width=SW, height=SH)

    def utilizador(self):#aparecer o usuario logado
        self.painel=PanedWindow(self, bg="#636A72", bd=3, relief="sunken")#tenho que mover isto para uma nova def que irá ter toda a aparencia da pagina
        self.butão_I=Button(self, text="criar/logar", bg="#636A72", fg="red", font=("Helvetica 10 bold"), borderwidth="2px", command=self.open_window) 
        self.usuario=Label(self, text=user, fg="black", bg="white", bd=3, relief="ridge", textvariable=self.user_var)
        
        self.butão_I.place(relx=0.925,rely=0.05)
        self.painel.place(relx=0.001, rely=0.032, relheight=0.95, relwidth=0.998)
        self.usuario.place(relx=0.05,y=50)
        self.user_var.set(f"{user}")

    def open_window(self):
        window = TelaCriação(self, user_var=self.user_var)
        window.grab_set()

    def prencher(self):
        
        self.escI=Entry(self, width=20, show="-")
        self.escIT=Text(self, height=4, width=45)
        
        self.escI.place(relx=0.05,y=110)
        self.escIT.place(relx=0.05,y=135)

tela()