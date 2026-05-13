# Este exemplo apresenta uma aplicação completa de OpenGL, que renderiza um quadrado e um triângulo na tela, cada um com um shader diferente.
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np

Window = None
Shader_programm_quadrado = None
Shader_programm_triangulo = None
Vao_quadrado = None
Vao_triangulo = None
WIDTH = 800
HEIGHT = 600

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))

def inicializaCasa():
    global Vao_casa
    # Vao do quadrado
    Vao_casa = glGenVertexArrays(1)
    glBindVertexArray(Vao_casa)

    # VBO dos vértices da casa
    points = [
        # triângulo 1
		0.5, 0.5, 0.0, #vertice superior direito
		0.5, -0.5, 0.0, #vertice inferior direito
		-0.5, -0.5, 0.0, #vertice inferior esquerdo

		#triângulo 2
		-0.5, 0.5, 0.0, #vertice superior esquerdo
		0.5, 0.5, 0.0, #vertice superior direito
		-0.5, -0.5, 0.0, #vertice inferior esquerdo
        
        #triângulo 3
		0.0, 1, 0.0, #cima
		0.7, 0.3, 0.0, #direita
		-0.7, 0.3, 0.0 #esquerda 
        ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.93, 1.0, 0.34, #vertice superior direito
		0.93, 1.0, 0.34, #vertice inferior direito
		0.93, 1.0, 0.34, #vertice inferior esquerdo
		#triângulo 2
		0.93, 1.0, 0.34, #vertice superior direito
		0.93, 1.0, 0.34, #vertice inferior direito
		0.93, 1.0, 0.34, #vertice inferior esquerdo
        #triângulo 3
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaSol():
    global Vao_sol
    # Vao do quadrado
    Vao_sol = glGenVertexArrays(1)
    glBindVertexArray(Vao_sol)

    # VBO dos vértices da sol
    points = [
        # triângulo 1
		0.5, 0.5, 0.0, #vertice superior direito
		0.5, -0.5, 0.0, #vertice inferior direito
		-0.5, -0.5, 0.0, #vertice inferior esquerdo


        ]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    cores = [
		#triângulo 1
		0.93, 1.0, 0.34, #vertice superior direito
		0.93, 1.0, 0.34, #vertice inferior direito
		0.93, 1.0, 0.34, #vertice inferior esquerdo
		#triângulo 2
		0.93, 1.0, 0.34, #vertice superior direito
		0.93, 1.0, 0.34, #vertice inferior direito
		0.93, 1.0, 0.34, #vertice inferior esquerdo
        #triângulo 3
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
	]
    cores = np.array(cores, dtype=np.float32)
    cvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, cvbo)
    glBufferData(GL_ARRAY_BUFFER, cores, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShaderCasa():
    global Shader_programm_casa
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao;
        layout(location = 1) in vec3 vertex_cores;
        out vec3 cores;
        void main () {
            cores = vertex_cores;
            gl_Position = vec4 (vertex_posicao*0.5, 1.0);
        }
    """

    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
        in vec3 cores;
		out vec4 frag_colour;
		void main () {
		    frag_colour = vec4 (cores, 1.0);
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm_casa = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm_casa, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm_casa, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT

    while not glfw.window_should_close(Window):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glViewport(0, 0, WIDTH, HEIGHT)

        #desenha o quadrado
        glUseProgram(Shader_programm_casa) #ativa o shader do quadrado
        glBindVertexArray(Vao_casa) #ativa o VAO do quadrado
        glDrawArrays(GL_TRIANGLES, 0, 9) #renderiza o quadrado


        
        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaCasa()
    inicializaShaderCasa()

    inicializaRenderizacao()

if __name__ == "__main__":
    main()