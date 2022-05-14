from tkinter import *
from PIL import Image, ImageTk

root = Tk()

frame = Frame(root)
frame.pack(fill=BOTH, expand=1)
root.resizable(width = FALSE, height = FALSE)

mainPanel = Canvas(frame, cursor='tcross')
mainPanel.grid(row = 1, column = 1, sticky = W+N)

img = Image.open('puppy.jpg')
curimg_w, curimg_h = img.size
tkimg = ImageTk.PhotoImage(img)
mainPanel.config(width = max(tkimg.width(), 400), height = max(tkimg.height(), 400))
mainPanel.create_image(0, 0, image = tkimg, anchor=NW)
 
root.resizable(width =  True, height = True)
root.mainloop()
