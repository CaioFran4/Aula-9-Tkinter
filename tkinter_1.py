import tkinter as tk

janela = tk.Tk()
janela.title("Minha Janela")
janela.state("zoomed")
janela.configure(bg="#DCDCDC")  # Fundo cinza externo igual ao Figma

# Painel central branco (simulando a tela do protótipo)
painel_central = tk.Frame(janela, bg="white")
painel_central.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.75, relheight=0.85)

# Tenta carregar a imagem da logo
try:
    imagem = tk.PhotoImage(file="amais.png")
    label_imagem = tk.Label(painel_central, image=imagem, bg="white")
except Exception:
    label_imagem = tk.Label(painel_central, text="[Logo amais.png]", bg="white", fg="#3498DB", font=("Roboto", 20, "bold"))

# Posicionamento da logo no topo do painel
label_imagem.place(relx=0.5, rely=0.32, anchor="center")

def placeholder(entry, texto, senha=False):
    if senha:
        entry.config(show="")
        
    entry.insert(0, texto)
    entry.config(fg="#8D8585")

    def entrar(event):
        if entry.get() == texto:
            entry.delete(0, tk.END)
            entry.config(fg="black")
            if senha:
                entry.config(show="*")

    def sair(event):
        if entry.get() == "":
            if senha:
                entry.config(show="")
            entry.insert(0, texto)
            entry.config(fg="#8D8585")

    entry.bind("<FocusIn>", entrar)
    entry.bind("<FocusOut>", sair)

# --- E-MAIL (Com a bordinha/sombra cinza clara exatamente como no Figma) ---
sombra_email = tk.Frame(
    painel_central,
    bg="#E5D9D9",  # Tom exato de cinza/bege leve da borda da foto
    bd=1
)
sombra_email.place(relx=0.5, rely=0.51, anchor="center", width=340, height=48)

email = tk.Entry(
    sombra_email,
    bg="#F5ECEC",  # Tom interno levemente rosado/acinzentado igual ao protótipo
    fg="#8D8585",
    font=("Roboto", 14),
    bd=0,
    relief="flat"
)
placeholder(email, "e-mail")
email.place(relx=0.03, rely=0.15, relwidth=0.94, relheight=0.7)


# --- SENHA ---
sombra_senha = tk.Frame(
    painel_central,
    bg="#E5D9D9",
    bd=1
)
sombra_senha.place(relx=0.5, rely=0.58, anchor="center", width=340, height=48)

senha = tk.Entry(
    sombra_senha,
    bg="#F5ECEC",
    fg="#8D8585",
    font=("Roboto", 14),
    bd=0,
    relief="flat"
)
placeholder(senha, "senha", senha=True)
senha.place(relx=0.03, rely=0.15, relwidth=0.94, relheight=0.7)


# --- BOTÃO ACESSAR (Azul sólido do Figma) ---
botao = tk.Button(
    painel_central,
    text="ACESSAR",
    bg="#2B8CC4",  # Tom de azul idêntico ao protótipo
    fg="white",
    activebackground="#206B97",
    activeforeground="white",
    font=("Roboto", 13, "bold"),
    bd=0,
    relief="flat",
    cursor="hand2"
)
botao.place(relx=0.5, rely=0.66, anchor="center", width=340, height=48)


# --- PRIMEIRO ACESSO ---
primeiro_acesso = tk.Label(
    painel_central,
    text="PRIMEIRO ACESSO",
    bg="white",
    fg="#2B8CC4",
    font=("Roboto", 11, "bold"),
    cursor="hand2"
)
primeiro_acesso.place(relx=0.5, rely=0.75, anchor="center")

janela.mainloop()