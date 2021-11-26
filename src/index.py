from tkinter import Tk
from ui.gui import GUI

window = Tk()
window.resizable(0,0)
window.title("Dummy Calculator")
gui = GUI(window)
gui.start()
window.mainloop()
