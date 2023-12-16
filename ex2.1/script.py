import os
 
sefras = os.path.join("./ex2.1/sifra.txt")

def escreva():  # write()
    ficheiro = input("qual o ficheiro\n>>")
    if os.path.isfile("./ex2.1/texto/{0}.txt".format(ficheiro)):
        g = open("./ex2.1/texto/{0}.txt".format(ficheiro), "a")
    else:
        g = open("./ex2.1/texto/{0}.txt".format(ficheiro), "w")
 
    escrita = input(">>")
 
    code = script(escrita)
    print(escrita, code)
 
    code = code+"\n"
    g.write(code)
    print("___\n"+code)
    g.close()

def script(X):
    code=""
    with open(sefras, "r") as f:
        base = f.readlines()
 
    for i in range(len(X)):
        nlista = False #nlist 
        for j in range(len(base)):
            MoreX = X[i]
            c1de = base[j].replace("\n", "")
         
            print(MoreX, c1de)
 
            if str(MoreX) == str(c1de):
                if j + 1 < len(base)-1: 
                    print(X[i], c1de, base[j+1])
                    code += base[j+1].replace("\n", "")
                    nlista = True
 
        if MoreX == " ":
            print("else", X[i], c1de)
            code += " "
            nlista = True
        if nlista == False:
            code += X[i]
    return code

def leia(): 
    
    ficheiro = input("qual o ficheiro\n>>")
    
    if os.path.isfile("./ex2.1/texto/{0}.txt".format(ficheiro)):
    
        g = open("./ex2.1/texto/{0}.txt".format(ficheiro), "r")
    
    else:
        print("arquivo não encontrado a redirecionar para 1-escreva")
        escreva()
        return
    fens= decript(g)
    print(fens)

def decript(X):
    X = X.readlines()
    code=""
    with open(sefras, "r") as f:
        base = f.readlines()
    for s in range(len(X)):
        Y=X[s]
        for i in range(len(Y)):
            nlista = False #nlist 
            for j in range(len(base)):
                MoreX = Y[i]
                c1de = base[j].replace("\n", "")
         
                print(MoreX, c1de)
 
                if str(MoreX) == str(c1de):
                    if j - 1 < len(base)-1: 
                        print(Y[i], c1de, base[j+1])
                        code += base[j-1].replace("\n", "")
                        nlista = True
            if MoreX == " ":
                print("else", Y[i], c1de)
                code += " "
                nlista = True
            if nlista == False:
                code += Y[i]
    return code


while True:
    Menu = input("MENU\n1-escreva\n2-leia\n0-fim\n\n\t>>")
    match Menu:
        case "1":
            escreva()  
        case "2":
            print(leia())
        case "0":
            print("fim")  
            exit()
        case _:
            print("erro")
