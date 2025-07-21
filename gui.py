import tkinter as tk
from tkinter import filedialog, messagebox
from highlighter import highlight

def gerar_html():
    codigo = entrada_text.get("1.0", tk.END)
    saida_html = highlight(codigo)

    caminho = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if caminho:
        with open(caminho, "w") as f:
            f.write(saida_html)
        messagebox.showinfo("Sucesso", f"Arquivo salvo como {caminho}")

janela = tk.Tk()
janela.title("Colorizador de Código")

entrada_text = tk.Text(janela, height=20, width=80, font=("Courier", 10))
entrada_text.pack(padx=10, pady=10)

botao_gerar = tk.Button(janela, text="Gerar HTML Colorido", command=gerar_html)
botao_gerar.pack(pady=10)

janela.mainloop()
