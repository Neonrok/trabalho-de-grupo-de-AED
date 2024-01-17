import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

user="guest"
imagem="./base/imagens/dumy.png"
N_Post="0"
Titulo=""
Nome=""
emagem=""
preço=""
texto=""
likes=""

class Post(Toplevel):
    def __init__(self, variavel, tela=None, master=None, user_var=None):
        super().__init__(master)
        self.user_var = user_var
        self.variavel = variavel
        self.tela_1 = tela
        self.tela()
        self.separação()
        self.escrita()
        self.liks_cont()
        self.ler_comentar()
    
    def tela(self):
        SW = self.winfo_screenwidth()
        SH = self.winfo_screenheight()

        AW = 1050
        AH = 650

        x = (SW/2) - (AW/2)
        y = (SH/2) - (AH/2)

        self.geometry(f'{AW}x{AH}+{int(x)}+{int(y)}')
        self.title("criar")
        self.iconbitmap("./cat-_1_.ico")
        self.configure(bg="#636A72")
        self.minsize(width=AW, height=AH)
        self.maxsize(width=AW, height=AH)

    def separação(self):
        global Titulo, Nome, emagem, preço, texto

        self.caminho=str(self.variavel)

        with open(self.caminho, 'r', encoding='utf-8') as file:
        # Ler as primeiras cinco linhas em variáveis separadas
            Titulo = file.readline().strip()
            Nome = file.readline().strip()
            emagem = file.readline().strip()
            preço = file.readline().strip()
            texto = file.read()

    def escrita(self):


        self.name=Label(self, text= Titulo, font=("Helvetica 12 bold"), bg="#FFFFFF", fg="red")
        self.name.place(relx=0.01,rely=0.01)

        self.autor=Label(self, text=f"autor: {Nome}", font=("Helvetica 6 bold"), bg="#FFFFFF", fg="black")
        self.autor.place(relx=0.01, rely=0.05)

        try:
            self.img=PhotoImage(file=emagem)
        except Exception as e:
            self.img=imagem

        largura = 200
        altura = 150
        
        self.img_red = self.img.subsample(int(self.img.width() / largura),int(self.img.height() / altura))
        self.img_place=Label(self, image=self.img_red)#ajuda-------------------------------------------------------------------------------
        self.img_place.place(relx=0.5, rely=0.09)

        self.descrição=Label(self, text=texto, font=("Helvetica 7"), bg="#FFFFFF", fg="black")
        self.descrição.place(relx=0.01, rely=0.09)

        self.preso=Label(self, text=f"preço: {preço}", font=("Helvetica 8 bold"), bg="#FFFFFF", fg="black")
        self.preso.place(relx=0.01, rely=0.81)

        self.lick=Button(self, text="like", bg="#636A72", fg="red", font=("Helvetica 9 bold"), borderwidth="2px", command=self.liks)
        self.lick.place(relx=0.01, rely=0.9)
        self.like=Label(self, text=likes, bg="#ffffff")
        self.like.place(relx=0.06, rely=0.9)

        self.delet=Button(self, text="delete", bg="#636A72", fg="red", font=("Helvetica 9 bold"), borderwidth="2px", command=self.delete)
        if user == Nome or user == "Cat":
            self.delet.place(relx=0.12, rely=0.9)

        self.TelComents=Text(self, width=35, height=32)
        self.TelComents.place(relx=0.72, rely=0.05)
        self.coment=Entry(self, width=35)
        self.confirm=Button(self, text="coment", bg="#636C75", fg="blue", font=("Helvetica 9 bold"), borderwidth="2px", relief="groove", command=self.comentar)
        if user!="guest":
            self.coment.place(relx=0.74,rely=0.85)
            self.confirm.place(relx=0.74,rely=0.89)

    def delete(self):
        os.remove(self.variavel)
        self.tela_1.atualizar_postagens()
        self.destroy()

    def liks(self):
        global likes
        if user!="guest":
            if os.path.exists("{0}-likes/{1}".format(self.variavel.rstrip(".txt"),user))==True:
                os.remove("{0}-likes/{1}".format(self.variavel.rstrip(".txt"),user))

            else:
                with open("{0}-likes/{1}".format(self.variavel.rstrip(".txt"),user),"w") as file:
                    file.write("-")

        else:
            messagebox.showwarning("inicie a conta", "entre em uma conta")

        self.liks_cont()
    def liks_cont(self):
        like=os.listdir("{0}-likes".format(self.variavel.rstrip(".txt")))

        likes=str(len(like))
        self.like.config(text=likes)
    
    def comentar(self):
        comentario=str(self.coment.get())
        ordem=len(os.listdir("{0}-respostas".format(self.variavel.rstrip(".txt"))))
        with open("{0}-respostas/{1}".format(self.variavel.rstrip(".txt"),ordem),"w") as file:
            file.write(comentario)
            self.coment.delete(0, 'end')
        self.ler_comentar()

    def ler_comentar(self):

        self.TelComents.config(state="normal")
        self.TelComents.delete("1.0", 'end')
        posts = os.listdir("{0}-respostas".format(self.variavel.rstrip(".txt")))

        for i in range(len(posts)):
            with open("{0}-respostas/{1}".format(self.variavel.rstrip(".txt"),posts[i]),"r") as file:
                coment = file.readline().strip()
                coment=str(coment) + "\n"
                print(coment)
                self.TelComents.insert("1.0", coment)
        self.TelComents.config(state="disabled")



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
#tela para criar post
class postagem(Toplevel):
    def __init__(self, master=None, tela=None, postagem_var=None):
        super().__init__(master)
        self.tela_1 = tela
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
        nome_img=filedialog.askopenfilename(title="qual a imagem", initialdir="./base/imagens", filetypes=(("png files","*png"),("gif files", "*gif"),("all files","*.*")))

        imagem=nome_img

    def postar(self):
        print("postar")
        self.but=Button(self, text="Postar", bg="#636A72", fg="red", font=("Helvetica 12 bold"), borderwidth="2px", command=self.salvar)

        self.but.place(relx=0.01, y=450)

    def salvar(self):
        print("salvar")
        global N_Post, user

        save_titulo = self.Titlo.get()
        save_descrição = self.descricao.get("1.0", tk.END)
        save_imag = str(imagem)  # Converte a imagem para string

        save_preço = self.escrever_preço.get()

        save = save_titulo + "\n" + user + "\n" + save_imag + "\n" + save_preço + "\n" + save_descrição

        print(save)

        with open("./base/post_numero.txt", "r") as arquivo:
            N_Post = int(arquivo.read().strip())

        arcname = str(N_Post) + user

        ficheiro = "./base/postagens/{0}.txt".format(arcname)

        with open("./base/post_numero.txt", "w") as arquivo:
            arquivo.write(str(N_Post + 1))

        with open(ficheiro, "w") as g:
            g.write(save)
            os.makedirs("./base/postagens/{0}-likes".format(arcname))
            os.makedirs("./base/postagens/{0}-respostas".format(arcname))

        self.tela_1.atualizar_postagens()

        self.destroy()
        

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

        # Adicionar uma barra de rolagem vertical
        self.Scrol=Scrollbar(self)
        self.Post=Text(self, bg="#ffffff", yscrollcommand=self.Scrol.set, state='disabled')
        self.Scrol.config(command=self.Post.yview)
        self.Post.place(relx=0.15, rely=0.25, relheight=0.6, relwidth=0.7)
        self.Scrol.place(relheight=0.6, relx=0.85, rely=0.25)

        # Criar um frame para conter os botões
        self.inner_frame = tk.Frame(self.Post, background="#ffffff")

        # Adicionar o frame no Text
        self.Post.window_create("insert", window=self.inner_frame)

        # Configurar o evento de rolagem
        self.inner_frame.bind("<Configure>", self.configure_scroll_region)

        # Listar arquivos na pasta
        arquivos_na_pasta = os.listdir("./base/postagens")
        
        # Obter o número de arquivos
        n_arquivos = len(arquivos_na_pasta)

        self.atualizar_postagens()

        # criar postagem
        self.criar=Button(self, text="postar", bg="#636A72", fg="red", font=("Helvetica 9 bold"), borderwidth="2px", command=self.open_postar_window)
        self.criar.place(relx=0.04,y=105)
    
    def atualizar_postagens(self): #ajuda--------------------------------------------------------------------------------------------------
        #destroir
        for widget in self.inner_frame.winfo_children():
            widget.destroy()
        
        arquivos_na_pasta = os.listdir("./base/postagens")
        # Acessar o conteúdo de cada arquivo
        for arquivo in arquivos_na_pasta:
            caminho_completo = os.path.join("./base/postagens", arquivo)
            #ler a primeira linha e 
            if os.path.isfile(caminho_completo):
                with open(caminho_completo, 'r', encoding='utf-8') as file:

                    variavel = f"{caminho_completo}"

                    primeira_linha = file.readline().strip()
                    new_button = tk.Button(self.inner_frame, text=primeira_linha, command=lambda v=variavel: self.executar_Post(v))
                    new_button.pack(pady=5)
                    self.update_idletasks()  # Atualizar a região de rolagem

    #area de rolagem
    def configure_scroll_region(self, event):
        try:
            self.Post.configure(scrollregion=self.Post.bbox("all"))
        except tk.TclError:
            #caso não tenha items
            pass
    
    def executar_Post(self, variavel):
        # Instanciar a classe e executar com a variável do botão
        Post(variavel, tela=self)


    def open_postar_window(self):
        if user=="guest":
            messagebox.showwarning(title="Aviso", message="Logue ou crie uma conta primeiro")
        else:
            window_postar = postagem(self, tela=self, postagem_var=self.postagem_var)
            window_postar.grab_set()

    
tela()