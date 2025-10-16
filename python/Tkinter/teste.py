import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Minha Primeira Janela com Tkinter")
janela.geometry("800x600")
label = tk.Label(janela, text="Olá, Mundo!")
label.configure(
    fg="#000000",
    font=("Times New Roman", 24, "bold")
)
label.pack(pady=20)
button = tk.Button(
janela,
text = "Enviar",
command = lambda: messagebox.showinfo("Aviso","Informação enviada!"),
bg="#3498db",
fg= "white",
font= ("Times New Roman", 12, "bold"),
bd=1.5
)

entry = tk.Entry(
janela,
width= 50,
font=("Times New Roman",15),
bg= "white",
fg= "#2C3E50",
relief= "solid",
bd=1.5
)
label_entry = tk.Label(
janela,
text= "Informe seu nome:",
font=("Times New Roman", 10, "bold"),
fg="#2C3E50"
)
label_entry.pack(pady=(5, 0))

entry.insert(0, "Meu nome é")
entry.pack(pady=15)
button.pack(pady=20)
janela.mainloop()