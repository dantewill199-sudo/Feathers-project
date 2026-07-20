import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# Área de Trabalho
DESKTOP = Path.home() / "Desktop"

def criar_feather():
    codigo = editor.get("1.0", tk.END).rstrip()

    if not codigo:
        messagebox.showwarning(
            "Aviso",
            "Escreva algum código primeiro."
        )
        return

    arquivo = DESKTOP / "Feather projeto.py"

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(codigo)

    messagebox.showinfo(
        "Feathers",
        f"Projeto criado com sucesso!\n\n{arquivo}"
    )

# -------------------------
# Janela
# -------------------------

janela = tk.Tk()
janela.title("Feathers Creator")
janela.geometry("800x600")

titulo = tk.Label(
    janela,
    text="Feathers Creator",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

editor = tk.Text(
    janela,
    font=("Consolas", 11),
    undo=True
)
editor.pack(fill="both", expand=True, padx=10, pady=10)

editor.insert(
    "1.0",
    '# Escreva seu código Python aqui\n\nprint("Olá, Feathers!")'
)

frame = tk.Frame(janela)
frame.pack(pady=10)

tk.Button(
    frame,
    text="Criar Feather",
    width=18,
    command=criar_feather
).pack(side="left", padx=5)

tk.Button(
    frame,
    text="Sair",
    width=18,
    command=janela.destroy
).pack(side="left", padx=5)

janela.mainloop()