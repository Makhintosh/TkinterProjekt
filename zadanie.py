from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk


def submit_form():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_spin.get()
    city = city_dropdown.get()
    height = height_slider.get()

    if not first_name or not last_name or not age or not city:
        result_label.config(text="Uzupełnij brakujące pola")
        return

    result_label.config(
        text=f"Zarejestrowano {first_name} {last_name}, {age} lat, z {city}, wzrost: {height}cm")


def reset_form():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_spin.delete(0, tk.END)
    age_spin.insert(13, 13)
    city_dropdown.set(cities[0])
    height_slider.set(100)
    result_label.config(text="")


okno = tk.Tk()
okno.title("Zakład pogrzebowy")
okno.geometry("700x450")

# bg = ImageTk.PhotoImage(file="nagrobek.jpg")

# # Create a Canvas
# canvas = Canvas(okno, width=700, height=3500)
# canvas.pack(fill=BOTH, expand=True)

# # Add Image inside the Canvas
# canvas.create_image(0, 0, image=bg, anchor='nw')

# # Function to resize the window
# def resize_image(e):
#    global image, resized, image2
#    # open image to resize it
#    image = Image.open("nagrobek.jpg")
#    # resize the image with width and height of root
#    resized = image.resize((e.width, e.height), Image.ANTIALIAS)

#    image2 = ImageTk.PhotoImage(resized)
#    canvas.create_image(0, 0, image=image2, anchor='nw')

# # Bind the function to configure the parent window
# okno.bind("<Configure>", resize_image)

bg = PhotoImage(file = "nagrobek.png")

label1 = Label( okno, image = bg)
label1.place(x = 0, y = 0)

company_label = tk.Label(
    okno, text="Zakład pogrzebowy żyć nie umierać", font=("", 20, "bold"))
company_label.pack(pady=20)

form_frame = tk.Frame(okno)

first_name_label = tk.Label(form_frame, text="Imię:")
first_name_label.grid(row=0, column=0, padx=10, pady=5)
first_name_entry = tk.Entry(form_frame)
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = tk.Label(form_frame, text="Nazwisko:")
last_name_label.grid(row=1, column=0, padx=10, pady=5)
last_name_entry = tk.Entry(form_frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = tk.Label(form_frame, text="Wiek:")
age_label.grid(row=2, column=0, padx=10, pady=5)
age_spin = tk.Spinbox(form_frame, from_=13, to=120)
age_spin.grid(row=2, column=1, padx=10, pady=5)

city_label = tk.Label(form_frame, text="Miasta")
city_label.grid(row=3, column=0, padx=10, pady=5)
cities = ["Warszawa", "Kraków", "Poznań",
          "Olsztyn", "Gdańsk", "Szczytno", "Wrocław"]
city_dropdown = tk.StringVar(value=cities[0])
city_dropdown_menu = tk.OptionMenu(form_frame, city_dropdown, *cities)
city_dropdown_menu.grid(row=3, column=1, padx=10, pady=5)

height_label = tk.Label(form_frame, text="Wzrost:")
height_label.grid(row=4, column=0, padx=10, pady=5)
height_slider = tk.Scale(form_frame, from_=100, to=220, orient=tk.HORIZONTAL)
height_slider.grid(row=4, column=1, padx=10, pady=5)

submit_button = tk.Button(form_frame, text="Zatwierdź", command=submit_form)
submit_button.grid(row=5, column=0, padx=10, pady=20)

reset_button = tk.Button(form_frame, text="Reset", command=reset_form)
reset_button.grid(row=5, column=1, padx=10, pady=20)

result_label = tk.Label(form_frame, text="")
result_label.grid(row=6, column=0, columnspan=2)

form_frame.pack(pady=20)

okno.mainloop()
