import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
import math



import numpy as np
import matplotlib.pyplot as plt

def desenhaLinha(x1, y1, x2, y2, **parametros):
    plt.plot([x1, x2], [y1, y2], **parametros)
    
def desenhaCubo2D(pontos2D):
    #p0 liga no p1, p2 e p4
                #    x1               y1               x2                y2
    desenhaLinha(pontos2D[0][0], pontos2D[0][1], pontos2D[1][0], pontos2D[1][1],marker="o", color="blue")
    desenhaLinha(pontos2D[0][0], pontos2D[0][1], pontos2D[2][0], pontos2D[2][1],marker="o", color="blue")
    desenhaLinha(pontos2D[0][0], pontos2D[0][1], pontos2D[4][0], pontos2D[4][1],marker="o", color="blue")

    #p1 liga no p3, p5,
    desenhaLinha(pontos2D[1][0], pontos2D[1][1], pontos2D[3][0], pontos2D[3][1],marker="o", color="blue")
    desenhaLinha(pontos2D[1][0], pontos2D[1][1], pontos2D[5][0], pontos2D[5][1],marker="o", color="blue")

    #p2 liga no p3, p6
    desenhaLinha(pontos2D[2][0], pontos2D[2][1], pontos2D[3][0], pontos2D[3][1],marker="o", color="blue")
    desenhaLinha(pontos2D[2][0], pontos2D[2][1], pontos2D[6][0], pontos2D[6][1],marker="o", color="blue")

    #p3 liga no p7
    desenhaLinha(pontos2D[3][0], pontos2D[3][1], pontos2D[7][0], pontos2D[7][1],marker="o", color="blue")

    #p4 liga no p5, p6
    desenhaLinha(pontos2D[4][0], pontos2D[4][1], pontos2D[5][0], pontos2D[5][1],marker="o", color="blue")
    desenhaLinha(pontos2D[4][0], pontos2D[4][1], pontos2D[6][0], pontos2D[6][1],marker="o", color="blue")

    #p5 liga no p7
    desenhaLinha(pontos2D[5][0], pontos2D[5][1], pontos2D[7][0], pontos2D[7][1],marker="o", color="blue")

    #p6 liga no p7
    desenhaLinha(pontos2D[6][0], pontos2D[6][1], pontos2D[7][0], pontos2D[7][1],marker="o", color="blue")


def geraMatrizTrasnformacao(tx, ty, tz, sx, sy, sz, rx, ry, rz):
    #Matriz de translação
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0, 1]])
    
    #Matriz de escala
    S = np.array([[sx, 0, 0, 0],
                  [0, sy, 0, 0],
                  [0, 0, sz, 0],
                  [0, 0, 0, 1]])
    
    #Converte os angulos de graus pra radianos
    rx = np.radians(rx)
    ry = np.radians(ry)
    rz = np.radians(rz)

    #Matrizes de rotação
    Rx = np.array([ [1,     0,              0,          0],
                    [0,     np.cos(rx),    -np.sin(rx), 0],
                    [0,     np.sin(rx),    np.cos(rx),  0],
                    [0,     0,              0,          1]])
    
    Ry = np.array([ [np.cos(ry),    0, np.sin(ry),      0],
                    [0,             1, 0,               0],
                    [-np.sin(ry),   0, np.cos(ry),      0],
                    [0,             0, 0,               1]])
    
    Rz = np.array([ [np.cos(rz),   -np.sin(rz),     0,  0],
                    [np.sin(rz),    np.cos(rz),     0,  0],
                    [0,             0,              1,  0],
                    [0,             0,              0,  1]])
    
    #Combina todas as transformações em uma única matriz por meio de multiplicação de matrizes
    combinacao = S @ Rz @ Ry @ Rx @ T

    return combinacao

def geraMatrizCamera(camx, camy, camz, camrx, camry, camrz):
    #Matriz de translação da câmera
    T = np.array([[1, 0, 0, -camx],
                  [0, 1, 0, -camy],
                  [0, 0, 1, -camz],
                  [0, 0, 0, 1]])
    
    #Converte os angulos de graus pra radianos
    camrx = np.radians(camrx)
    camry = np.radians(camry)
    camrz = np.radians(camrz)

    #Matrizes de rotação
    Rx = np.array([ [1,     0,                  0,              0],
                    [0,     np.cos(-camrx),    -np.sin(-camrx), 0],
                    [0,     np.sin(-camrx),    np.cos(-camrx),  0],
                    [0,     0,                  0,              1]])
    
    Ry = np.array([ [np.cos(-camry),    0, np.sin(-camry),     0],
                    [0,                 1, 0,                  0],
                    [-np.sin(-camry),   0, np.cos(-camry),     0],
                    [0,                 0, 0,                  1]])
    
    Rz = np.array([ [np.cos(-camrz),   -np.sin(-camrz),     0,  0],
                    [np.sin(-camrz),    np.cos(-camrz),     0,  0],
                    [0,                 0,                  1,  0],
                    [0,                 0,                  0,  1]])
    
    combinacao = T @ Rz @ Ry @ Rx

    return combinacao

def projecaoPerspectiva(fovy, aspect, znear, zfar):
    fovy = np.radians(fovy)

    a = 1/(np.tan(fovy/2)*aspect)
    b = 1/np.tan(fovy/2)
    c = (zfar+znear)/(znear-zfar)
    d = (2*zfar*znear)/(znear-zfar)

    p = np.array([[a, 0, 0,  0],
                  [0, b, 0,  0],
                  [0, 0, c,  d],
                  [0, 0, -1, 0]])
    
    return p


#1. Modelagem do objeto
                     #x     y     z   w
pontos = np.array([[-0.5, -0.5, -0.5, 1],   #p1
                   [-0.5, -0.5, 0.5, 1],    #p2
                   [-0.5, 0.5, -0.5, 1],    #p3
                   [-0.5, 0.5, 0.5, 1],     #p4
                   [0.5, -0.5, -0.5, 1],    #p5
                   [0.5, -0.5, 0.5, 1],     #p6
                   [0.5, 0.5, -0.5, 1],     #p7
                   [0.5, 0.5, 0.5, 1]])     #p8
#transpõe os pontos para podermos multiplicar as matrizes por ele
pontos = np.transpose(pontos)

print("Modelagem do objeto:")
print(np.transpose(pontos))

#2. Coordenadas do mundo
#aplica uma trasformação que só rotaciona o objeto em torno de y por 30 graus
model = geraMatrizTrasnformacao(1,1,0,1,1,1,0,0,0)

pontos = model @ pontos

print("Coordenadas do mundo:")
print(np.transpose(pontos))

#3. Coordenadas de visualização
#Queremos colocar uma câmera posicionada em z = 2
view = geraMatrizCamera(0, 0, 4, 0, -120, 0)

pontos = view @ pontos

print("Coordenadas de visualização:")
print(np.transpose(pontos))

#4. Coordenadas de projeção
proj = projecaoPerspectiva(70, 1.0, 0.1, 100)

pontos = proj @ pontos

print("Coordenadas de projeção:")
print(np.transpose(pontos))

#4.1. Divide o x, y, z e w de cada ponto por w, para que o w volte a ser 1

pontos = np.transpose(pontos)
i = 0
while i<=7:
                #x,y,z,w /  w
    pontos[i] = pontos[i]/pontos[i][3]
    i+=1

print("Coordenadas de projeção corrigidas pelo w:")
print(pontos)

plt.xlim(-1, 1)          # limite eixo X
plt.ylim(-1, 1)          # limite eixo Y

#função para renderizar o cubo
#desenhaCubo2D(pontos)
#plt.show()



# This defines the Python GUI backend to use for matplotlib
matplotlib.use('TkAgg')

# Initialize an instance of Tk
root = tk.Tk()

# Initialize matplotlib figure for graphing purposes
fig = plt.figure(1)

# Special type of "canvas" to allow for matplotlib graphing
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()



desenhaCubo2D(pontos)

# Add the plot to the tkinter widget
plot_widget.grid(row=0, column=0)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)
frame5 = tk.Frame(root)
frame6 = tk.Frame(root)
frame7 = tk.Frame(root)

def mostra_menu_principal(self):
    self.grid_remove()
    frame1.grid()

def mostra_menu_objeto(self):
    self.grid_remove()
    frame2.grid()

def mostra_menu_camera(self):
    self.grid_remove()
    frame3.grid()

def mostra_menu_projecao(self):
    self.grid_remove()
    frame4.grid()

def mostra_menu_mapeamento(self):
    self.grid_remove()
    frame5.grid()

def visualizarobjeto(self):
    self.grid_remove()
    frame6.grid()

def transformarobj(self):
    self.grid_remove()
    frame7.grid()


    


#Frame1 (Menu Principal)
tk.Label(frame1, text="Menu Principal").grid(row=1,column=1)
manip_obj_btn = tk.Button(frame1, text="Manipular Objeto", command= lambda: mostra_menu_objeto(frame1)).grid(row=2, column=1)
manip_cam_btn = tk.Button(frame1, text="Manipular a câmera", command=lambda: mostra_menu_camera(frame1)).grid(row=3, column=1)
manip_proj_btn = tk.Button(frame1, text="Modificar Projeção", command=lambda: mostra_menu_projecao(frame1)).grid(row=4, column=1)
mod_map__btn = tk.Button(frame1, text="Modificar Mapeamento", command=lambda: mostra_menu_mapeamento(frame1)).grid(row=5, column=1)
visual_obj_btn = tk.Button(frame1, text="Visualizar Objeto", command=lambda: visualizarobjeto(frame1)).grid(row=6, column=1)
frame1.grid()

#Frame2 (Menu Objeto)
tk.Label(frame2, text="Manipular Objeto").grid(row=1,column=1)
voltar_btn = tk.Button(frame2, text="Voltar", command= lambda: mostra_menu_principal(frame2)).grid(row=2,column=1)
trans_btn = tk.Button(frame2, text="Translação", command= lambda: transformarobj(frame2)).grid(row=3,column=1)
scale_btn = tk.Button(frame2, text="Escala").grid(row=4,column=1)
rot_x_btn = tk.Button(frame2, text="Rotação em X").grid(row=5,column=1)
rot_y_btn = tk.Button(frame2, text="Rotação em Y").grid(row=6,column=1)
rot_z_btn = tk.Button(frame2, text="Rotação em Z").grid(row=7,column=1)

#Frame3 (Menu Câmera)
tk.Label(frame3, text="Manipular Câmera").grid(row=1,column=1)
voltar_btn = tk.Button(frame3, text="Voltar", command= lambda: mostra_menu_principal(frame3)).grid(row=2,column=1)
trans_btn = tk.Button(frame3, text="Translação").grid(row=3,column=1)
scale_btn = tk.Button(frame3, text="Escala").grid(row=4,column=1)
rot_x_btn = tk.Button(frame3, text="Rotação em X").grid(row=5,column=1)
rot_y_btn = tk.Button(frame3, text="Rotação em Y").grid(row=6,column=1)
rot_z_btn = tk.Button(frame3, text="Rotação em Z").grid(row=7,column=1)


#Frame4 (Menu Projeção)
tk.Label(frame4, text="Modificar Projeção").grid(row=1,column=1)
voltar_btn = tk.Button(frame4, text="Voltar", command= lambda: mostra_menu_principal(frame4)).grid(row=2,column=1)
proj_persp_btn = tk.Button(frame4, text="Projeção Perspectiva").grid(row=3,column=1)
proj_par_btn = tk.Button(frame4, text="Projeção Paralela").grid(row=4,column=1)

#Frame5 (Menu Mapeamento)
tk.Label(frame5, text="Modificar Mapeamento").grid(row=1,column=1)
voltar_btn = tk.Button(frame5, text="Voltar", command= lambda: mostra_menu_principal(frame5)).grid(row=2,column=1)
window_btn = tk.Button(frame5, text="Window").grid(row=3,column=1)
viewport_btn = tk.Button(frame5, text="Viewport").grid(row=4,column=1)

#Frame6 (Visualizar Objeto [Provavelmente não será usado])
tk.Label(frame6, text="Visualizar Objeto").grid(row=1,column=1)
voltar_btn = tk.Button(frame6, text="Voltar", command= lambda: mostra_menu_principal(frame6)).grid(row=2,column=1)
tk.Button(frame6,text="Esse botão terá uma função em algum momento no futuro.... ou não.").grid(row=3,column=1)

#Frame7 (Transformações do Objeto [teste])
tk.Label(frame7,text="Transformações do Objeto").grid(row=1,column=1)
voltar_btn = tk.Button(frame7, text="Voltar", command= lambda: mostra_menu_principal(frame7)).grid(row=2,column=1)
transformação = tk.Entry(frame7).grid(row=3,column=1)


# Dropdown options  
transforms = ["Translação", "Escala", "Rotação em X", "Rotação em Y", "Rotação em Z"]
from tkinter import ttk
# Combobox  
transformoptions = ttk.Combobox(frame7, values=transforms)
transformoptions.set(transforms[0])
transformoptions.grid(row=3,column=1)

tk.Entry(frame7).grid(row=4,column=1)
tk.Button(frame7,text="Aplicar").grid(row=5,column=1) #Função da transformação vai aqui


root.mainloop()


