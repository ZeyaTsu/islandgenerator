from 'islandgenerator-algo' import generate as generate
from tkinter import *
window=Tk()
# Add widgets here

btn=Button(window, text="Generate")
btn.place(x=80, y=100)

class importgenerator:
    btn.bind('<Button-1>', generate)


# Set Window
window.title('Island Generator')
window.geometry("300x200+10+20")
window.mainloop()