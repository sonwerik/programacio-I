import random
import tkinter as tk
from tkinter import messagebox

def empezar_juego():
    root.destroy()

    top = tk.Tk()
    top.title("Juego del Ahorcado")
    top.geometry("500x400")

    puntuacion_letras = {
        "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4,
        "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "Ñ": 8, "O": 1,
        "P": 3, "Q": 5, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4,
        "X": 8, "Y": 4, "Z": 10
    }

    lista_palabras = ["ZAFIRO", "ESMERALDA", "AMATISTA", "AGUAMARINA", "LAPISLAZULI", "TURMALINA", "AGATA",
                      "NITROGENO", "MAGNESIO", "FOSFORO", "AZUFRE", "TITANIO", "MANGANESO", "ESTAÑO", "PRASEODIMIO",
                      "VICTIMOLOGÍA", "IMPUNIDAD", "SECUESTRO", "VICTIMIZACION", "HOMICIDIO", "IMPUTABILIDAD",
                      "CRIMINOLOGIA",
                      "INVESTIGACION", "SENTENCIA", "ELECTROENCEFALOGRAMA", "ONTOLOGIA", "EPISTEMOLOGIA", "METAFISICA",
                      "COSMOLOGIA", "FENOMENOLOGIA", "MATERIALISMO", "EXISTENCIALISMO"]

    palabra = ""
    raya = []
    letras_falladas = set()
    letras_adivinadas = set()
    puntuacion_acumulada = 0
    intentos = 0
    max_intentos = 6

    label_raya = tk.Label(top, text="", font=("Arial", 24))
    label_raya.place(x=250, y=200, anchor="center")

    def mostrar_raya():
        label_raya.config(text=" ".join(raya))

    def reiniciar_juego():
        nonlocal palabra, raya, letras_falladas, letras_adivinadas, puntuacion_acumulada, intentos
        palabra = random.choice(lista_palabras).upper()
        raya = ["_"] * len(palabra)
        letras_falladas = set()
        letras_adivinadas = set()
        puntuacion_acumulada = 0
        intentos = 0

        mostrar_raya()
        label_letras_falladas.config(text="Letras falladas:")
        label_puntuacion.config(text="Puntuación acumulada: {}".format(puntuacion_acumulada))
        label_vidas.config(text="Vidas restantes: {}".format(max_intentos))
        entry_letra.delete(0, "end")

    def comprobar_letra():
        nonlocal intentos, puntuacion_acumulada

        letra = entry_letra.get().upper()
        entry_letra.delete(0, "end")

        if letra.isalpha() and len(letra) == 1 and letra not in letras_adivinadas and letra not in letras_falladas:
            if letra in palabra:
                letras_adivinadas.add(letra)
                puntuacion_acumulada += puntuacion_letras[letra]
                for i in range(len(palabra)):
                    if letra == palabra[i]:
                        raya[i] = letra
                mostrar_raya()  # Actualiza la visualización de la palabra
                label_puntuacion.config(text="Puntuación acumulada: {}".format(puntuacion_acumulada))
                if "_" not in raya:
                    opcion_continuar = messagebox.askquestion(
                        "¡Felicidades!", "¡Has adivinado la palabra!\n¿Deseas continuar?")
                    if opcion_continuar == "yes":
                        reiniciar_juego()
                    else:
                        top.destroy()
            else:
                letras_falladas.add(letra)
                intentos += 1
                label_letras_falladas.config(text="Letras falladas: {}".format(", ".join(letras_falladas)))
                label_vidas.config(text="Vidas restantes: {}".format(max_intentos - intentos))
                if intentos >= max_intentos:
                    opcion_continuar = messagebox.askquestion(
                        "¡Has perdido!", "La palabra era: {}\n¿Quieres continuar?: ".format(palabra))
                    if opcion_continuar == "yes":
                        reiniciar_juego()
                    else:
                        top.destroy()
        else:
            messagebox.showinfo(
                "Error", "Introduce una única letra válida y no repetida.")

    label_vidas = tk.Label(top, text="Vidas restantes: {}".format(max_intentos), font=("Arial", 15))
    label_vidas.place(x=20, y=50)

    label_letras_falladas = tk.Label(top, text="Letras falladas:", font=("Arial", 15))
    label_letras_falladas.place(x=20, y=85)

    label_letra = tk.Label(top, text="Introduce una letra: ", font=("Arial", 15))
    label_letra.place(x=20, y=130)

    entry_letra = tk.Entry(top, width=10, font=("Arial", 14))
    entry_letra.place(x=200, y=130)

    label_puntuacion = tk.Label(top, text="Puntuación acumulada: {}".format(puntuacion_acumulada), font=("Arial", 15))
    label_puntuacion.place(x=250, y=20, anchor="center")

    def enviar_con_enter(event):
        comprobar_letra()

    entry_letra.bind('<Return>', enviar_con_enter)

    reiniciar_juego()

    button_comprobar = tk.Button(top, text="Comprobar", font=("Arial", 14), command=comprobar_letra)
    button_comprobar.place(x=350, y=130)

    button_salir = tk.Button(top, text="Salir", font=("Arial", 14), command=top.destroy)
    button_salir.place(x=400, y=360)

    top.mainloop()


root = tk.Tk()
root.geometry("500x400")
root.title("Inicio Ahorcado")

tk.Label(root, text="Made by Hass & Èrik").place(x=190, y=100)
tk.Label(root, text="¡Bienvenidos al Juego del Ahorcado!",
         font=("Arial", 20)).place(x=250, y=60, anchor="center")

tk.Button(root, text="¡Empezar Juego!", command=empezar_juego).place(x=200, y=250)


root.mainloop()