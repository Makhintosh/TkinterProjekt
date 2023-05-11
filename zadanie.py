import tkinter as tk

okno = tk.Tk()
okno.title("Zakład pogrzebowy")

firma_label = tk.Label(okno, text="Zakład pogrzebowy 'Żyć nie umierać'", font=("Arial", 16, "bold"))
firma_label.pack(pady=10)

imie_entry = tk.Entry(okno, width=30)
imie_entry.pack(pady=5)

miasta = ["Warszawa", "Kraków", "Gdańsk", "Olsztyn", "Poznać", "Wrocław"]
miasta_var = tk.StringVar(value=miasta[0])
miasta_dropdown = tk.OptionMenu(okno, miasta_var, *miasta)
miasta_dropdown.pack(pady=5)

wiek_entry = tk.Entry(okno, width=10)
wiek_entry.pack(pady=5)