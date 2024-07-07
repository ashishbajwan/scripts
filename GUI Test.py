# Import Module
import tkinter as tk
from tkinter import filedialog
from tkinter import *


def save_as_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Text files", "*.json"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file_content = text_widget.get('1.0', tk.END)
                file.write(file_content)
                status_label.config(text=f"File saved as: {file_path}")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")
# create root window
root = tk.Tk()
# root window title and dimension
root.title("Export")
# Set geometry(widthxheight)
root.geometry('500x500')
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar 
menu = Menu(root)
item = Menu(menu)
item1 = Menu(menu)
item2 = Menu(menu)
menu.add_cascade(label='File', menu=item)
item.add_command(label='About')
menu.add_cascade(label='File1', menu=item1)
item1.add_command(label='Settings')
menu.add_cascade(label='File', menu=item2)
item2.add_command(label='New')
root.config(menu=menu)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)

txt = Entry(root, width=10)
txt.grid(column =3, row =0)


text_widget = tk.Text(root, wrap=tk.WORD, height=1, width=35)
text_widget.pack(padx=20, pady=20)

text_widget = tk.Text(root, wrap=tk.WORD, height=1, width=35)
text_widget.pack(padx=20, pady=20)


save_button = tk.Button(root, text="Save As", command=save_as_text_file)
save_button.pack(padx=20, pady=10)

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

root.mainloop()
