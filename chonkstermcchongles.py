#    Implemente as classes mat2, mat3 e mat4, destinadas à representação de matrizes quadradas de dimensões 2x2, 3x3 e 4x4, respectivamente.
#    A classe mat2 deverá possuir:


#    
#    Um método para multiplicação da matriz por outra matriz mat2, recebida como parâmetro, cujo retorno deve ser uma nova instância de mat2 contendo o resultado do produto matricial.
#    Um método que realize a transposição da matriz, trocando as posições das linhas pelas colunas.
#    Um método que retorne uma matriz bidimensional do tipo float, de dimensões 2x2, contendo exatamente os valores armazenados nos atributos da classe.

#    As classes mat3 e mat4 deverão possuir exatamente a mesma estrutura e os mesmos métodos descritos para a classe mat2, adaptando apenas a quantidade de atributos e as dimensões da matriz para 3x3 e 4x4, respectivamente. Na classe mat3, os métodos que utilizarem vetores deverão trabalhar com objetos do tipo vet3. Na classe mat4, os métodos que utilizarem vetores deverão trabalhar com objetos do tipo vet4. Todas as operações devem seguir corretamente as regras da álgebra matricial conforme a dimensão da matriz.

class mat2:
    
# Quatro atributos do tipo float, correspondentes às posições da matriz, nomeados como: m00, m01, m10 e m11 (onde o primeiro índice representa a linha e o segundo a coluna).
# Um construtor padrão, sem parâmetros, que obrigatoriamente chame o método toIdentity, garantindo que toda nova instância seja criada como matriz identidade.
    def __init__(self, m00, m01, m10, m11):
        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        m00 = float
        m01 = float
        m10 = float
        m11 = float

        self.toIdentity()





    def toIdentity(self):
        # Um método chamado toIdentity, que não recebe parâmetros e não retorna valor,
        # e que deve definir os valores dos atributos m00, m01, m10 e m11 como uma matriz identidade 2x2 (valor 1 na diagonal principal e valor 0 nas demais posições).
        self.m00 = 1
        self.m01 = 0
        self.m10 = 0
        self.m11 = 1

        matrix = [self.m00,self.m01,self.m10,self.m11]
        print("Matriz Identidade:\n","[", matrix[0], matrix[1],"\n  ",matrix[2],matrix[3],"]")


    # Um método para adição de outra matriz mat2, que receba uma instância de mat2 como parâmetro e realize a soma com a matriz atual.

    def addmatrix(self, othermat):

        if type(othermat) == mat2:
            print("Soma das duas matrizes:\n","[",self.m00 + othermat.m00,self.m01 + othermat.m01,"\n  ", self.m10 + othermat.m10,self.m11 + othermat.m11,"]")


        else:
            print("O segundo parâmetro recebido não é uma matriz.")

            pass

    # Um método para subtração de outra matriz mat2, que receba uma instância de mat2 como parâmetro e realize a subtração em relação à matriz atual.

    def submatrix(self, othermat):
        if type(othermat) == mat2:
            print("Subtração das duas matrizes:\n","[",self.m00 - othermat.m00,self.m01 - othermat.m01,"\n  ", self.m10 - othermat.m10,self.m11 - othermat.m11,"]")



        else:
            print("O segundo parâmetro recebido não é uma matriz.")

            pass

#    Um método que receba um escalar do tipo float, chamado x, e multiplique todos os elementos da matriz (m00, m01, m10 e m11) por esse valor.

    def multmatrix(self):
        escalar = float(input("Insira o valor do escalar: "))
        print("Multiplicação da matriz pelo escalar:\n","[",self.m00 * escalar ,self.m01 * escalar ,"\n  ", self.m10 * escalar ,self.m11 * escalar,"]")

#    Um método que receba um escalar do tipo float, chamado x, e divida todos os elementos da matriz (m00, m01, m10 e m11) por esse valor.

    def divmatrix(self):
        escalar = float(input("Insira o valor do escalar: "))
        print("Divisão da matriz pelo escalar:\n","[",self.m00 / escalar ,self.m01 / escalar ,"\n  ", self.m10 / escalar ,self.m11 / escalar,"]")

    def multmatvet(self, vector):
        if type(vector) == vet2: 
            print("Multiplicação do vetor com a matriz:\n","[",self.m00 + .m00,self.m01 + othermat.m01,"\n  ", self.m10 + othermat.m10,self.m11 + othermat.m11,"]")

            pass
            
    

            


class vet2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        x = float
        y = float


a = [1, 2    
     3, 4]   = "2x2"

v = [1, 
     2]   = "2x1"

a + v = [1, 4
         ]

        








ping = mat2(0, 0, 0, 0)
pong = mat2(0, 0, 0, 0)
chonk = vet2(5, 5)

ping.divmatrix()

