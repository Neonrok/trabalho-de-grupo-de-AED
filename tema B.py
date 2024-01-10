import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

ADM=[("Cat")]

user="wads"
imagem="./base/imagens/dumy.png"
N_Post="0"

#tela para logar e criar conta
class TelaCriação(Toplevel):
    def __init__(self, master=None, user_var=None):
        super().__init__(master)
        self.user_var = user_var
        self.tela()
        self.utilizador()
        self.social()

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

    def social(self):
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

class postagem(Toplevel):
    def __init__(self, master=None, postagem_var=None):
        super().__init__(master)
        self.postagem_var = postagem_var
        self.tela()
        self.Titulo()
        self.preço()
        self.descrição()
        self.ilustração()
        self.postar()
       

    def tela(self):#defenir limites da tela
        SW = self.winfo_screenwidth()
        SH = self.winfo_screenheight()

        AW = 1050
        AH = 500

        x = (SW/2) - (AW/2)
        y = (SH/2) - (AH/2)

        self.geometry(f'{AW}x{AH}+{int(x)}+{int(y)}')
        self.title("criar")
        self.iconbitmap("./cat-_1_.ico")
        self.configure(bg="#636A72")
        self.minsize(width=AW, height=AH)
        self.maxsize(width=AW, height=AH)

    def Titulo(self):
        self.Tilt=Label(self, text="Título" ,bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px")
        self.Titlo=Entry(self, width=100, relief="groove")
        self.Titlo.place(relx=0.01, y=35)
        self.Tilt.place(relx=0.01, y=10)
    
    def preço(self):
        self.texto_preço=Label(self, text="Preço" ,bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px")
        self.escrever_preço=Entry(self, width=100, relief="ridge")
        self.texto_preço.place(relx=0.01, y=400)
        self.escrever_preço.place(relx=0.01, y=420)

    def descrição(self):
        self.descricao = Text(self, width= 75, height=10)

        self.descricao.place(relx=0.01, y=75)

    def ilustração(self):
        self.escolher_img=Button(self, text="escolher imagem", bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px", command=self.escolher_imagem)

        self.escolher_img.place(relx=0.01, y=350)
    
    def escolher_imagem(self):
        global imagem
        nome_img=filedialog.askopenfilename(title="qual a imagem", initialdir="C:\\Users\\rodri\\OneDrive\\Imagens", filetypes=(("png files","*png"),("gif files", "*gif"),("all files","*.*")))

        imagem=PhotoImage(file=nome_img)

    def postar(self):

        self.but=Button(self, text="Postar", bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px", command=self.salvar)

        self.but.place(relx=0.01, y=450)

    def salvar(self):
        global N_Post, user

        save_titulo = self.Titlo.get()
        save_descrição = self.descricao.get("1.0", tk.END)
        save_imag = str(imagem)  # Converte a imagem para string

        save_preço = self.escrever_preço.get()

        save = save_titulo + "\n\n" + save_descrição + "\n\n" + save_imag + "\n\n" + save_preço

        print(save)

        with open("./base/post_numero.txt", "r") as arquivo:
            N_Post = int(arquivo.read().strip())

        arcname = user + str(N_Post)

        ficheiro = "./base/postagens/{0}.txt".format(arcname)

        with open("./base/post_numero.txt", "w") as arquivo:
            arquivo.write(str(N_Post + 1))

        with open(ficheiro, "w") as g:
            g.write(save)

       

#tela principal
class tela(tk.Tk):
    def __init__(self):#base para executar tudo
        super().__init__()
        self.user_var = tk.StringVar()
        self.postagem_var = tk.StringVar()
        self.tela()
        self.utilizador()
        self.social()
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
        self.butão_I=Button(self, text="criar/logar", bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px", command=self.open_window) 
        self.usuario=Label(self, text=user, fg="black", bg="white", bd=3, relief="ridge", font=("Courier 12"), textvariable=self.user_var)
        
        self.butão_I.place(relx=0.92,rely=0.05)
        self.painel.place(relx=0.001, rely=0.032, relheight=0.95, relwidth=0.998)
        self.usuario.place(relx=0.05,y=50)
        self.user_var.set(f"{user}")

    def open_window(self):
        window_criar = TelaCriação(self, user_var=self.user_var)
        window_criar.grab_set()

    def social(self):
        self.comonicação=Label(self, height=40, width=200)
        self.criar=Button(self, text="postar", bg="#636A72", fg="red", font=("Helvetica 9 bold"), borderwidth="2px", command=self.open_postar_window)
        
        self.comonicação.place(relx=0.04,y=135)
        self.criar.place(relx=0.04,y=105)
    
    def open_postar_window(self):
        if user=="guest":
            messagebox.showwarning(title="Aviso", message="Logue ou crie uma conta primeiro")
        else:
            window_postar = postagem(self, postagem_var=self.postagem_var)
            window_postar.grab_set()

    
tela()