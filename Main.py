import tkinter as tk
import os
from dotenv import load_dotenv


load_dotenv()


user_env = os.getenv("APP_USER")
pass_env = os.getenv("APP_PASSWORD")


def tomar_datos():
    usuario = entrada_user.get()
    clave = entrada_pass.get()
    comprobar(usuario, clave)


def comprobar(usuario, clave):
    if usuario == user_env and clave == pass_env:
        mostrar_resultado(True)
    else:
        mostrar_resultado(False)


def mostrar_resultado(correcto):
    if correcto:
        mensaje.config(text="Acceso correcto", fg="green")
    else:
        mensaje.config(text="Usuario o contraseña incorrectos", fg="red")


ventana = tk.Tk()
ventana.title("Login")

tk.Label(ventana, text="Usuario").pack()
entrada_user = tk.Entry(ventana)
entrada_user.pack()

tk.Label(ventana, text="Contraseña").pack()
entrada_pass = tk.Entry(ventana, show="*")
entrada_pass.pack()

tk.Button(ventana, text="Entrar", command=tomar_datos).pack()

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()