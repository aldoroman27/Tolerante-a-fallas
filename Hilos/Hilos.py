import tkinter as tk
from tkinter import messagebox
import threading

def suma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 + num2)
    except ValueError:
        messagebox.showerror("Error", "Dato no valido.")

def resta():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 - num2)
    except ValueError:
        messagebox.showerror("Error", "Dato no valido.")

def multiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado.set(num1 * num2)
    except ValueError:
        messagebox.showerror("Error", "Dato no valido.")

def division(): 
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir por cero")
        else:
            resultado.set(num1 / num2)
    except ValueError:
        messagebox.showerror("Error", "Dato no valido.")

def realizar_operacion(operacion):
    threading.Thread(target=operacion).start()

app = tk.Tk()
app.title("Calculadora")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

resultado = tk.StringVar()
resultado_label = tk.Label(frame, textvariable=resultado)
resultado_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

suma_button = tk.Button(frame, text="Suma", command=lambda: realizar_operacion(suma))
suma_button.grid(row=2, column=0, padx=5, pady=5)

resta_button = tk.Button(frame, text="Resta", command=lambda: realizar_operacion(resta))
resta_button.grid(row=2, column=1, padx=5, pady=5)

multiplicacion_button = tk.Button(frame, text="Multiplicación", command=lambda: realizar_operacion(multiplicacion))
multiplicacion_button.grid(row=3, column=0, padx=5, pady=5)

division_button = tk.Button(frame, text="División", command=lambda: realizar_operacion(division))
division_button.grid(row=3, column=1, padx=5, pady=5)

app.mainloop()