import tkinter as tk
import os
from dotenv import load_dotenv 


load_dotenv(dotenv_path=".env")
user_env = os.getenv("APP_USER")
pass_env = os.getenv("APP_PASSWORD")
print(user_env, pass_env)

def tomar_datos():
    usuario = entrada_user.get()
    clave = entrada_pass.get()

    if usuario == user_env and clave == pass_env:
        mensaje.config(text="Acceso correcto")
    else:
        mensaje.config(text="Datos incorrectos")

ventana = tk.Tk()
ventana.title("Login")

# Usuario
tk.Label(ventana, text="Usuario").grid(row=0, column=0)
entrada_user = tk.Entry(ventana)
entrada_user.grid(row=0, column=1)

# Password
tk.Label(ventana, text="Password").grid(row=1, column=0)
entrada_pass = tk.Entry(ventana, show="*")
entrada_pass.grid(row=1, column=1)

# Botón
tk.Button(ventana, text="Entrar", command=tomar_datos).grid(row=2, column=0, columnspan=2)
mensaje = tk.Label(ventana, text="")
mensaje.grid(row=3, column=0, columnspan=2)
# Mensaje
mensaje = tk.Label(ventana, text="")
mensaje.grid(row=3, column=0, columnspan=2)

ventana.mainloop()