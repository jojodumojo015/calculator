import tkinter as tk
from decimal import Decimal


def tekan(tombol):
    if tombol == "=":
        try:
            
            hasil = Decimal(eval(entry.get()))
            entry.delete(0, tk.END)
            if hasil == hasil.to_integral_value():  
                hasil = int(hasil)
            else:
                hasil = round(hasil, 10)  
            entry.insert(tk.END, hasil)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif tombol == "C":
        entry.delete(0, tk.END)  
    elif tombol == "⌫":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])  
    else:
        entry.insert(tk.END, tombol)  


root = tk.Tk()
root.title("Kalkulator")


entry = tk.Entry(root, width=25, font=("Arial", 16), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)


tombol_list = [
    "7", "8", "9", "/", 
    "4", "5", "6", "*", 
    "1", "2", "3", "-", 
    "C", "0", "=", "+", 
    "⌫"  
]


row_val = 1
col_val = 0
for tombol in tombol_list:
    tk.Button(root, text=tombol, width=5, height=2, font=("Arial", 14),
              command=lambda t=tombol: tekan(t)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:  
        col_val = 0
        row_val += 1


root.mainloop()
