import Tkinter as tk

window = tk.Tk() # Class constructor for window object
text_box = tk.Entry(window)
def saveText():
    str1 = text_box.get()
    fx = open("file1","w")
    fx.write(str1)
    fx.close()
btn1 = tk.Button(window, text = "Save", command = saveText)

text_box.pack()
btn1.pack()

window.mainloop()
