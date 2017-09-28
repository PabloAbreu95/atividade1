#Exercício 1
#Tomar uma matriz qualquer 3x3 com a matriz dos coeficientes não-singular
#de forma a obter-se x1,x2,x3 pelo algorítmo de retro-substituição
from tkinter import *
from tkinter import messagebox
import funcoes
class main:
    def __init__(self,master):
        #Variaveis
        self.matriz = []
        self.chamado = False
        self.aux1 = []
        self.aux2 = []
        self.aux3 = []
        self.aux4 = []

        #Primeira linha
        self.lb1 = Label(master, text="Linha 1")
        self.lb1.grid(row=1,column=0)
        self.ed1 = Entry(master)
        self.ed1.grid(row=1,column=1)
        self.ed2 = Entry(master)
        self.ed2.grid(row=1,column=2)
        self.ed3 = Entry(master)
        self.ed3.grid(row=1,column=3)
        self.ed0 = Entry(master)
        self.ed0.grid(row=1, column=4)


        #Segunda linha
        self.lb2 = Label(master, text="Linha 2")
        self.lb2.grid(row=2,column=0)
        self.ed4 = Entry(master)
        self.ed4.grid(row=2, column=1)
        self.ed5 = Entry(master)
        self.ed5.grid(row=2, column=2)
        self.ed6 = Entry(master)
        self.ed6.grid(row=2, column=3)
        self.ed01 = Entry(master)
        self.ed01.grid(row=2, column=4)


        #Terceira linha
        self.lb3 = Label(master, text="Linha 3")
        self.lb3.grid(row=3, column=0)
        self.ed7 = Entry(master)
        self.ed7.grid(row=3, column=1)
        self.ed8 = Entry(master)
        self.ed8.grid(row=3, column=2)
        self.ed9 = Entry(master)
        self.ed9.grid(row=3, column=3)
        self.ed02 = Entry(master)
        self.ed02.grid(row=3, column=4)




        #Botão
        self.btn1 = Button(master, text="Confirmar", command=self.resolver)
        self.btn1.grid(row=6,column=2)



    def resolver(self): #Função para resolver matriz
        if self.ed1.get() != "" and self.ed2.get() != "" and self.ed3.get() != "" and self.ed4.get() != ""\
                and self.ed5.get() != "" and self.ed6.get() != ""\
                and self.chamado == False:

            a1 = self.ed1.get()
            a2 = self.ed2.get()
            a3 = self.ed3.get()
            a4 = self.ed0.get()
            b1 = self.ed4.get()
            b2 = self.ed5.get()
            b3 = self.ed6.get()
            b4 = self.ed01.get()
            c1 = self.ed7.get()
            c2 = self.ed8.get()
            c3 = self.ed9.get()
            c4 = self.ed02.get()
            #Adicionando os elementos na matriz
            self.matriz.append([int(a1),int(a2),int(a3),int(a4)])
            self.matriz.append([int(b1),int(b2),int(b3),int(b4)])
            self.matriz.append([int(c1),int(c2),int(c3),int(c4)])
            self.chamado = True
            print('Matriz inicial')
            print(self.matriz[0])
            print(self.matriz[1])
            print(self.matriz[2])
            funcoes.triangularizar(self.matriz,self.aux1,self.aux2,self.aux3)

        elif(self.chamado==True):
            messagebox.showinfo("Log", "O programa já foi executado")
        else:
            messagebox.showinfo("Log", "Preencha a matriz corretamente")


root = Tk()
root.wm_title("Exercício 1")
main(root)
root.mainloop()
