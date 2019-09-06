import  tkinter as tk
from gui import Application
from PIL import ImageTk, Image

def main():
    root = tk.Tk()
    app = Application(master=root)

    app.mainloop()

if __name__ == "__main__":
    main()
