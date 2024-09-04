import customtkinter as ctk
from database import *

def init_gui():
    root = ctk.CTk()
    root.geometry('400x200')
    root.title('Login')

    def new_register():
        new_user = user_entry.get()
        new_password = password_entry.get()
        conexao = create_connection()
        cursor = define_cursor(conexao)
        
        user_created = create_new_user(conexao, cursor, new_user, new_password)

        if user_created:
            message.configure(text='User created', text_color='green')
        else:
            message.configure(text='User already exists', text_color='red')

    def user_login():
        user = user_entry.get()
        password = password_entry.get()
        conexao = create_connection()
        cursor = define_cursor(conexao)

        login_successfull = login(conexao, cursor, user, password)

        if login_successfull:
            message.configure(text='Login successfull', text_color='green')
        else:
            message.configure(text='Wrong username or password', text_color='red')

    user_entry = ctk.CTkEntry(root, placeholder_text='Username')
    user_entry.pack(pady=5)

    password_entry = ctk.CTkEntry(root,
        placeholder_text='Password'
        )
    password_entry.pack(pady=5)

    register_button = ctk.CTkButton(root,
        text='Register',
        command=new_register
        )
    register_button.pack(pady=5)

    login_button = ctk.CTkButton(root,
        text='Login',
        command=user_login
        )
    login_button.pack(pady=5)

    message = ctk.CTkLabel(root, text='')
    message.pack(pady=5)

    root.mainloop()
