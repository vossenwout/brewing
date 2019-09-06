import  tkinter as tk
from gui import WelcomeScreen


def main():
    root = tk.Tk()
    app = WelcomeScreen(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
