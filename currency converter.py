import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch exchange rates
def get_exchange_rate(from_currency, to_currency):
    base_url = "https://open.er-api.com/v6/latest/"
    
    response = requests.get(base_url + from_currency)
    data = response.json()

    if response.status_code != 200 or data['result'] != 'success':
        raise Exception(f"Error fetching data: {data.get('error-type', 'Unknown error')}")

    rate = data['rates'].get(to_currency)
    if rate is None:
        raise Exception(f"Conversion rate not found for {to_currency}")
    
    return rate

# Function to perform the currency conversion
def convert_currency():
    from_currency = from_currency_var.get().upper()
    to_currency = to_currency_var.get().upper()
    try:
        amount = float(amount_entry.get())
        converted_amount = get_exchange_rate(from_currency, to_currency) * amount
        result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Tkinter window
root = tk.Tk()
root.title("Currency Converter")

# GUI elements
tk.Label(root, text="Base Currency (e.g., USD):").grid(row=0, column=0, padx=10, pady=10)
from_currency_var = tk.StringVar()
from_currency_entry = tk.Entry(root, textvariable=from_currency_var)
from_currency_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Target Currency (e.g., EUR):").grid(row=1, column=0, padx=10, pady=10)
to_currency_var = tk.StringVar()
to_currency_entry = tk.Entry(root, textvariable=to_currency_var)
to_currency_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Amount to Convert:").grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

input("Press Enter to exit...")
