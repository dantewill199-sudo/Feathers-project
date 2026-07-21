import os
import tkinter as tk
from tkinter import messagebox

PASTA_TEMP = os.path.join(os.environ["SystemDrive"], "temp")

def abrir_temp():
    if os.path.exists(temp):
        os.startfile(temp)
        messagebox.showinfo(
            "Sucesso",
            "A pasta Temp foi aberta com sucesso."
        )
    else:
        messagebox.showerror(
            "Erro",
            "A pasta Temp não foi encontrada."
        )

def colocar_senha():
    messagebox.showinfo(
        "Em desenvolvimento",
        "Esta função será adicionada futuramente."
    )

root = tk.Tk()
root.title("Feathers Systeams")
root.geometry("350x220")
root.resizable(False, False)

titulo = tk.Label(
    root,
    text="Feathers Systeams",
    font=("Segoe UI", 16, "bold")
)
titulo.pack(pady=15)

tk.Button(
    root,
    text="Abrir a pasta Temp",
    width=25,
    command=abrir_temp
).pack(pady=5)

tk.Button(
    root,
    text="Colocar senha",
    width=25,
    command=colocar_senha
).pack(pady=5)

tk.Button(
    root,
    text="Sair",
    width=25,
    command=root.destroy
).pack(pady=15)

root.mainloop()