def mainmenu():
    options = int(input("Câmera Virtual - Pipeline de Visualização 3D\n  1- Manipular o objeto\n  2- Manipular a câmera\n  3- Modificar projeção\n  4- Modificar mapeamento\n  5- Visualizar objeto\n"))


    match options:
        case 1:
            manipularobj()
        case 2:
            manipularcam()
        case 3:
            modproj()
        case 4:
            modmap()
        case 5:
            visualizarobj()

            

def manipularobj():
    #● O usuário deve informar os valores de cada transformação.
    #● Todas as transformações devem ser acumuladas em uma matriz do modelo.
    #● Essa matriz começa como matriz identidade.
    options = int(input("Manipular o objeto\n  1- Translação\n  2- Escala\n  3- Rotação em X\n  4- Rotação em Y\n  5- Rotação em Z\n"))
    match options:
        case 1:
            #Função da Translação
            pass
        case 2:
            #Função da escala
            pass
        case 3:
            #Função da rotação em X
            pass
        case 4:
            #Função da rotação em Y
            pass
        case 5:
            #Função da rotação em Z
            pass

def manipularcam():
    options = int(input("Manipular a câmera\n  1- Translação\n  2- Rotação em X\n  3- Rotação em Y\n  4- Rotação em Z\n"))
    match options:
        case 1:
            #Função da Translação
            pass
        case 2:
            #Função da rotação em X
            pass
        case 3:
            #Função da rotação em Y
            pass
        case 4:
            #Função da rotação em Z
            pass

def modproj():
    options = int(input("Modificar Projeção\n  1- Projeção Perspectiva\n  2- Projeção Paralela"))
    match options:
        case 1:
            #Função da Projeção Perspectiva
            pass

        case 2:
            #Função da Projeção paralela
            pass

def modmap():
    options = int(input("Modificar Mapeamento\n  1- Window\n  2- Viewport"))
    match options:
        case 1:
            #Função da window
            pass

        case 2:
            #Função do viewport
            pass

def visualizarobj():
    #Ao escolher essa opção, o sistema deve aplicar, na ordem, as etapas do pipeline:
    #1. Matriz do modelo
    #2. Matriz de visualização
    #3. Matriz de projeção (converter de 3D para 2D)
    #4. Mapeamento (window → viewport)
    pass

mainmenu()



