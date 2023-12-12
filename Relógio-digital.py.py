import tkinter as tk
from time import strftime, localtime
import locale

# Define o local para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR')

def time():
    # Obtém a hora atual formatada como string no formato desejado
    time_string = strftime('%H:%M:%S %p')

    # Obtém o dia da semana e a data atual formatada como string no formato desejado
    date_string = strftime('%A, %d de %B de %Y', localtime())

    # Atualiza o texto do rótulo para incluir a hora e a data
    lbl.config(text=f"{time_string}\n{date_string}")

    # Agenda a função time para ser chamada novamente após 1000 milissegundos (1 segundo)
    lbl.after(1000, time)

root = tk.Tk()
root.title("Relógio Digital")

lbl = tk.Label(root, font=('calibri', 20, 'bold'), background='white', foreground='Teal')
lbl.pack(anchor='center')

time()
root.mainloop()
