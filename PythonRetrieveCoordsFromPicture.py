from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

if __name__ == "__main__":
    root = Tk()

    # setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    x_scroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E + W)
    y_scroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N + S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N + S + E + W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH, expand=1)

    # adding the image
    File = askopenfilename(parent=root, initialdir="C:/", title='Choose an image.')
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    print("[", end='')

    # function to be called when mouse is clicked
    def print_coordinates(event):
        # outputting x and y coordinates to console
        print(f"[{event.x}, {event.y}],", end=' ')


    # mouseclick event
    canvas.bind("<Button 1>", printcoords)
    print("]", end='')
    root.mainloop()
