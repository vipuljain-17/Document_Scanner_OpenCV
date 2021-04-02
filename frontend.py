#!/usr/bin/python
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Button, Label,messagebox
from PIL import ImageTk, Image
import cv2
from Document_scanner import scanner

root = tkinter.Tk()


def open_file():
    file_path = askopenfilename(title = "Select File", filetypes =[('Image File', '*.jpeg *.jpg *.png')])
    if file_path is not None:
        return file_path
    else:
        pass

def open_img():
    global panelA, panelB

    file_path = open_file()

    image = cv2.imread(file_path)
    scanned = scanner(file_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (600,600), interpolation=cv2.INTER_NEAREST)

    #return scanned_image
    global return_file
    return_file = scanned

    image = Image.fromarray(image)
    scanned = Image.fromarray(scanned)

    image = ImageTk.PhotoImage(image)
    scanned = ImageTk.PhotoImage(scanned)

    if panelA is None or panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side="left",padx=10, pady=10)

        panelB = Label(image=scanned)
        panelB.image = scanned
        panelB.pack(side="right",padx=10, pady=10)
    
    else:
        panelA.configure(image=image)
        panelB.configure(image=scanned)
        panelA.image = image
        panelB.image = scanned
    
def save_img(image_file):
    if image_file is not None:
        save_path = asksaveasfilename(title = "Give Title", filetypes =[('Image File', '*.jpg')])
        #print(save_path)
        #print(image_file.shape)
        cv2.imwrite(save_path, image_file)
    else:
        messagebox.showerror("Show error", "No Input image was selected")

panelA = None
panelB = None
return_file = None

btn2 = Button(root, text ='Save the scanned Image', command = lambda: save_img(return_file))
btn2.pack(side="bottom", fill="both",expand = 'yes', padx="10", pady="10")

btn = Button(root, text ='Select an Image', command = lambda: open_img())
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

root.title("Document Scanner Using OpenCV") 
#root.geometry("700x700")
root.mainloop()