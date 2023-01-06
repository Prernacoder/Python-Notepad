from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox
root = Tk()


root.minsize(650,650)
root.maxsize(650,650)

open_image = ImageTk.PhotoImage(Image.open("open.png"))
save_image = ImageTk.PhotoImage(Image.open("save.png"))

exit_image = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text = "file space name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name=name.split('.')[0]
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    text_file = open(name,'r')
    paragraph = text_file.read()
    my_text.insert(END,paragraph)
    textfile.close()

def saveFile():
    input_name = input_file_name.get()
    file = open(input_name + ".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update", "success")
    
def closewindow():
    root.destroy()

open_button = Button(root, image = open_image, text = "openfile", command = openFile)
open_button.place(relx = 0.05, rely = 0.03, anchor = CENTER)
save_button = Button(root, image = save_image, text = "savefile", command = saveFile)
save_button.place(relx = 0.11, rely = 0.03, anchor = CENTER)
exit_button = Button(root, image = exit_image, text = "exitfile", command = closewindow)
exit_button.place(relx = 0.17, rely = 0.03, anchor = CENTER)


root.mainloop()