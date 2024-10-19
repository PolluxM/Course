#Добавляем выбор базовой валюты в новом комбобоксе.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


def update_currency_label(event):
    # Получаем полное название валюты из словаря и обновляем метку первой базовой валюты
    code = base_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def update_currency_label_2(event):
    # Получаем полное название валюты из словаря и обновляем метку второбой базовой валюты
    code = base_2_combobox.get()
    name2 = currencies[code]
    currency_label_2.config(text=name2)

def update_currency_label_3(event):
    # Получаем полное название валюты из словаря и обновляем метку целевой валюты
    code = target_combobox.get()
    name3 = currencies[code]
    currency_label_3.config(text=name3)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base_code_2 = base_2_combobox.get()

    if target_code and base_code and base_code_2:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()

            response_2 = requests.get(f'https://open.er-api.com/v6/latest/{base_code_2}')
            response_2.raise_for_status()
            data_2 = response_2.json()

            if target_code in (data['rates'] and data_2['rates']):
                exchange_rate = data['rates'][target_code]
                exchange_rate_2 = data_2['rates'][target_code]
                base = currencies[base_code]
                base_2 = currencies[base_code_2]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate:.2f} {target} за 1 {base}\nКурс {exchange_rate_2:.2f} {target} за 1 {base_2}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x420")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base_2_combobox = ttk.Combobox(values=list(currencies.keys()))
base_2_combobox.pack(padx=10, pady=5)
base_2_combobox.bind("<<ComboboxSelected>>", update_currency_label_2)

currency_label_3 = ttk.Label()
currency_label_3.pack(padx=10, pady=10)


Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label_3)

currency_label_2 = ttk.Label()
currency_label_2.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
