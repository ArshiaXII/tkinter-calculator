import tkinter as tk

def calculate():
    num1 = float(e1.get())
    num2 = float(e2.get())
    if operation.get() == "+":
        result = num1 + num2
    elif operation.get() == "-":
        result = num1 - num2
    elif operation.get() == "*":
        result = num1 * num2
    elif operation.get() == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    elif operation.get() == "%":
        result = num1 % num2
    else:
        result = "Invalid operator."
    e3.delete(0, tk.END)
    e3.insert(0, str(result))

root = tk.Tk()
root.title("Calculator")

e1 = tk.Entry(root)
e1.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

e2 = tk.Entry(root)
e2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

operation = tk.StringVar()

tk.Radiobutton(root, text="+", variable=operation, value="+").grid(row=2, column=0, padx=20, pady=10)
tk.Radiobutton(root, text="-", variable=operation, value="-").grid(row=2, column=1, padx=20, pady=10)
tk.Radiobutton(root, text="*", variable=operation, value="*").grid(row=2, column=2, padx=20, pady=10)
tk.Radiobutton(root, text="/", variable=operation, value="/").grid(row=3, column=0, padx=20, pady=10)
tk.Radiobutton(root, text="%", variable=operation, value="%").grid(row=3, column=1, padx=20, pady=10)

e3 = tk.Entry(root)
e3.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate).grid(row=5, column=0, columnspan=3, padx=30, pady=30)

root.mainloop()
