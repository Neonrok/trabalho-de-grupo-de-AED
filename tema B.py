from tkinter import *

jan= Tk()

class tela:
    def __init__(self):
        self.jan = jan
        self.tela()
        self.botões()
        self.prencher()
        jan.mainloop()
    
    def tela(self):
        
        self.jan.geometry("1000x650+25+25")

        self.jan.title("catacumba")

        self.jan.iconbitmap("./cat-_1_.ico")

        self.jan.configure(bg="#636A72")

        self.jan.minsize(width=500, height=325)

        self.jan.maxsize(width=1650, height=950)

    def botões(self):
        self.painel=PanedWindow(jan, bg="#636A72", bd=3, relief="sunken")
        self.butão_I=Button(jan, text="butão", bg="#636A72", fg="blue", font=("Helvetica 9 bold"), borderwidth="2px")#buttona é para butão lable é para texto
        
        self.butão_I.place(relx=0.05,y=75)
        self.painel.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)

    def prencher(self):
        self.textoI=Label(jan, text="IOUAE", fg="red", bg="blue")
        self.escI=Entry(jan, width=20, show="-")
        self.escIT=Text(jan , height=4, width=45)
        
        self.textoI.place(relx=0.05,y=50)
        self.escI.place(relx=0.05,y=110)
        self.escIT.place(relx=0.05,y=135)

tela()