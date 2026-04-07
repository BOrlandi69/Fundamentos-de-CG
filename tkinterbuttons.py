from tkinter import *
from tkinter.ttk import *

# Create the main window
master = Tk()
master.geometry("300x350")  # Set window size
master.title("Main Window")

# Function to open a new window
def open_new_window():
    new_window = Toplevel(master)  # Create a new window
    new_window.title("New Window")
    new_window.geometry("250x150")  
    

    Label(new_window, text="This is a new window").pack(pady=20)


def window2():
    master.destroy()
    window2_main = Tk()
    Label(window2_main, text="test").pack()
    window2_main.title("Test window")
    window2_main.geometry("300x350")
    window2_main.mainloop()


# Create a label and a button to open the new window
Label(master, text="This is the main window").pack(pady=10)
Button(master, text="Manipular Objeto", command=window2).pack(pady=10)
Button(master, text="Manipular a câmera", command=open_new_window).pack(pady=10)
Button(master, text="Modificar Projeção", command=open_new_window).pack(pady=10)
Button(master, text="Modificar Mapeamento", command=open_new_window).pack(pady=10)
Button(master, text="Visualizar Objeto", command=open_new_window).pack(pady=10)




#"Câmera Virtual - Pipeline de Visualização 3D\n  1- Manipular o objeto\n 
#2- Manipular a câmera\n  3- Modificar projeção\n  4- Modificar mapeamento\n  5- Visualizar objeto\n"))

# Run the Tkinter event loop
master.mainloop()