#importa a biblioteca para criar uma janela para a aplicação
import customtkinter as ctk

#deixa a janela no modo dark
ctk.set_appearance_mode('dark')

#variavel para verificar um login
def validação_login():
    #tudo que for colocado em campo_login, senha voltara como usuario e senha
    usuario = campo_login.get()
    senha = campo_senha.get()

    #se o usuario colocado for admin e a senha 12345, colocar como login feito com sucesso em verde
    if usuario == 'admin' and senha == '12345':
        resultado_login.configure(text='Login feito com sucesso!!', text_color='green')
    #senao colocar que nao conseguiu com texto em vermelho
    else:
        resultado_login.configure(text='Login com falha!!', text_color='red')
#variavel para mostrar e esconder senha
def mostrar_senha():
    #se a caixa estiver selecionada mostrar a senha
    if checkbox_mostrar_senha.get():
        campo_senha.configure(show='')
    #senao colocar '*' no lugar das letras
    else:
        campo_senha.configure(show='*')




#criar a pagina (sempre que colocar ctk.CTk(), criar app.mainloop())
app = ctk.CTk()
#nome da janela
app.title('Pagina de login')
#tamanha pré definido da janela
app.geometry('300x300')

#Login!
#criar um texto
label_login = ctk.CTkLabel(app, text='Login')
#aplicar esse texto na janela
label_login.pack(pady=10, padx=10)

#criar um campo para digitarem (input)
campo_login = ctk.CTkEntry(app, placeholder_text='Digite seu login!')
#aplicar esse campo 
campo_login.pack(pady=10, padx=10)

#Senha!
#aplicar esse texto na janela
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10, padx=10)

#criar um campo para digitarem (input)
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha!', show='*')
campo_senha.pack(pady=10, padx=10)

# Adicionar checkbox para mostrar/ocultar senha
checkbox_mostrar_senha = ctk.CTkCheckBox(app, text="Mostrar senha", command=mostrar_senha, width=20)
checkbox_mostrar_senha.pack(pady=5, padx=(85, 0), anchor="w")

#botao para verificar se o login e senha esta correto
botao = ctk.CTkButton(app, text='Submit', command=validação_login, bg_color='blue')
botao.pack(pady=10)

#mostra o resultado se a senha esta correta ou nao
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack()

#manter a pagina sempre aberta até ser fechada
app.mainloop()