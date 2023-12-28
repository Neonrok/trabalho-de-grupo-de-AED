from tkinter import *

from CriarConta import criacao


jan= Tk()

class Ordens:
    def criar(self):
        criar_janela = criacao()
        criar_janela.criar()
        
class tela(Ordens):
    def __init__(self):
        self.jan = jan
        self.tela()
        self.botões()
        self.prencher()
        jan.mainloop()
    
    def tela(self):

        self.jan.state("zoomed")

        self.jan.title("catacumba")

        self.jan.iconbitmap("./cat-_1_.ico")

        self.jan.configure(bg="#636A72")

        SW=jan.winfo_screenwidth()
        SH=jan.winfo_screenheight()

        self.jan.minsize(width=SW, height=SH)

    def botões(self):
        self.painel=PanedWindow(jan, bg="#636A72", bd=3, relief="sunken")
        self.butão_I=Button(jan, text="EXIT", bg="#636A72", fg="red", font=("Helvetica 10 bold"), borderwidth="2px", command=self.criar) 
        
        self.butão_I.place(relx=0.972,rely=0.02)
        self.painel.place(relx=0.001, rely=0.032, relheight=0.95, relwidth=0.998)

    def prencher(self):
        self.textoI=Label(jan, text="IOUAE", fg="red", bg="blue")
        self.escI=Entry(jan, width=20, show="-")
        self.escIT=Text(jan , height=4, width=45)
        
        self.textoI.place(relx=0.05,y=50)
        self.escI.place(relx=0.05,y=110)
        self.escIT.place(relx=0.05,y=135)

tela()