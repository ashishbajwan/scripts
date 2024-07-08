# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()

# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()

# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()
# Import Module
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    #print(entry.get())
    
    name = print('"Application Name":"' + str(entry.get()) + '",')
    #name.set(str())
    print (name)
    file1 = open('Data1.txt', 'w')
    # Writing multiple strings
    # at a time
    file1.writelines(str(name))
    # Closing file
    file1.close()
    #output_string.set(str())
#Window
window = ttk.Window(themename = 'darkly')
window.title('VTM')
window.geometry('300x250')

#title
title_label = ttk.Label(master = window, text = 'Application List', font = 'Calibri 20 bold')
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = 'Save', command = convert)
entry.pack(side = 'left', padx = 20)
button.pack(side = 'left')
input_frame.pack(pady = 30)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
output_label.pack(pady = 5)

#Run
window.mainloop()


