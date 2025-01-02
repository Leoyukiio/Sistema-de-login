import customtkinter as ctk

ctk.set_appearance_mode('dark')

def validação_login():
    usuario = campo_login.get()
    senha = campo_senha.get()


    if usuario == 'admin' and senha == '12345':
        resultado_login.configure(text='Login feito com sucesso!!', text_color='green')
    
    else:
        resultado_login.configure(text='Login com falha!!', text_color='red')

def mostrar_senha():
    if checkbox_mostrar_senha.get():
        campo_senha.configure(show='')
    else:
        campo_senha.configure(show='*')





app = ctk.CTk()
app.title('Pagina de login')
app.geometry('300x300')

#Login!
label_login = ctk.CTkLabel(app, text='Login')
label_login.pack(pady=10, padx=10)

campo_login = ctk.CTkEntry(app, placeholder_text='Digite seu login!')
campo_login.pack(pady=10, padx=10)

#Senha!
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10, padx=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha!', show='*')
campo_senha.pack(pady=10, padx=10)

# Adicionar checkbox para mostrar/ocultar senha
checkbox_mostrar_senha = ctk.CTkCheckBox(app, text="Mostrar senha", command=mostrar_senha, width=20)
checkbox_mostrar_senha.pack(pady=5, padx=(85, 0), anchor="w")

botao = ctk.CTkButton(app, text='Submit', command=validação_login, bg_color='blue')
botao.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack()


app.mainloop()