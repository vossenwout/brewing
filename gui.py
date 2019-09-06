import tkinter as tk
from PIL import ImageTk, Image
import os


# application is a frame which 2 stacked frames (bottom and top frame), master is the window for the frames
class Application(tk.Frame):
    def __init__(self, master=None):

        # setting up the master window
        super().__init__(master)
        self.master = master
        self.masterWindow_setup()

        # creating frames on top of master window
        self.topFrame = tk.Frame(master)
        self.topFrame.pack()

        self.botFrame = tk.Frame(master)
        self.botFrame.pack(side="bottom")

        # creating the widgets
        self.create_widgets()

        # loading images
        self.open_image()


    def masterWindow_setup(self):
        self.master.title("Brew Master 1.0")
        self.master.minsize(500, 500)
        self.pack()


    def create_widgets(self):
        quitButton = tk.Button(self.botFrame, text="QUIT", width=25, fg="red", command=self.master.destroy)
        launchButton = tk.Button(self.botFrame, text="LAUNCH BREWMASTER", width=25,command = self.launch_main_menu)
        welcomeLabel = tk.Label(self.botFrame, text="Welcome to brewmasters \n v1.0, by Pookie",font ="Times 18" ,height=5)

        welcomeLabel.grid(row=0, column=0)
        quitButton.grid(row=2, column=0)
        launchButton.grid(row=1, column=0)


    def open_image(self):

        path = "images/brewimage.jpg"
        image = Image.open(path)
        image = image.resize((400, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)

        label = tk.Label(self.topFrame, image=img)
        label.image = img
        label.grid(row=0, column=0)

    def launch_main_menu(self):
        print("next windnppow")


