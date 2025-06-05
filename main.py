from tkinter import *
from tkinter import ttk

#Задание №1

#Создание окна
window = Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("Форма регистрации")

#Хранение данных из entry
name = ""
surname = ""
email = ""

#Передача данных
def send_form():
    name = name_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()

    print(f"Пользователь ввел следующие данные:\nИмя - {name}\nФамилия - {surname}\nEmail - {email}")

#Надпись "Форма регистрации"
label_form = ttk.Label(text="Форма регистрации")
label_form.pack(pady=10)

#Контейнер для имени
frame_for_name = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

#Label имени
name_label = ttk.Label(frame_for_name, text="Имя:")
name_label.pack(anchor=NW)

#Entry имени
name_entry = ttk.Entry(frame_for_name)
name_entry.pack(anchor=W)

#Упаковка контейнера
frame_for_name.pack(fill=X, padx=15, pady=5)

#Контейнер для фамилии
frame_for_surname = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

#label фамилии
surname_label = ttk.Label(frame_for_surname, text="Фамилия:")
surname_label.pack(anchor=NW)

#Entry фамилии
surname_entry = ttk.Entry(frame_for_surname)
surname_entry.pack(anchor=W)

#Упаковка контейнера
frame_for_surname.pack(fill=X, padx=15, pady=6)

#Контейнер для почты
frame_for_email = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

#Label почты
email_label = ttk.Label(frame_for_email, text="Email:")
email_label.pack(anchor=NW)

#Entry почты
email_entry = ttk.Entry(frame_for_email)
email_entry.pack(anchor=W)

#Упаковка контейнера
frame_for_email.pack(fill=X, padx=15, pady=7)

#Кнопка "Отправить"
send_button = ttk.Button(text="Отправить", width=25, command=send_form)
send_button.pack()

#Задание №2

#Создание второго окна
root = Tk()
root.title("Кнопки-переключатели")
root.resizable(False, False)
root.geometry("200x200")

#Метка, которая будет меняться
switching_label = ttk.Label(root, text="Выберите кнопку")
switching_label.pack(pady=15)

#Смена текста на "Привет!"
def changing_text_hello():
    switching_label.config(text="Привет!")

#Смена текста на "До свидания!"
def changing_text_goodbye():
    switching_label.config(text="До свидания!")

#Кнопка "Привет"
hello_button = ttk.Button(root, text="Привет", command=changing_text_hello)
hello_button.pack(ipadx=7)

#Кнопка "До свидания"
goodbye_button = ttk.Button(root, text="До свидания", command=changing_text_goodbye)
goodbye_button.pack(ipadx=5, pady=5)

#Активация окон
root.mainloop()
window.mainloop()