import tkinter as tk

def cambiar_texto():
    if label["text"] == "¡Hola, Mundo!":
        label["text"] = "¡Has presionado el botón!"
    else:
        label["text"] = "¡Hola, Mundo!"

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ejemplo Tkinter")

# Etiqueta
label = tk.Label(root, text="¡Hola, Mundo!", font=("Helvetica", 16))
label.pack(pady=20)

# Botón
button = tk.Button(root, text="Presióname", command=cambiar_texto)
button.pack(pady=10)

# Ejecutar el loop de la ventana
root.mainloop()
