import tkinter as tk
from PIL import ImageTk, Image

# application is a frame which 2 stacked frames (bottom and top frame), master is the window for the frames
############################################################################################################################
class WelcomeScreen(tk.Frame):
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
        self.master.resizable(False, False)
        self.pack()


    def create_widgets(self):
        self.quitButton = tk.Button(self.botFrame, text="QUIT", width=25, fg="red", command=self.master.destroy)
        self.launchButton = tk.Button(self.botFrame, text="LAUNCH BREWMASTER", width=25,
                                 command = self.launch_main_menu)
        self.welcomeLabel = tk.Label(self.botFrame, text="Welcome to brewmasters \n v1.0, by Pookie",font ="Times 18" ,height=5)

        self.welcomeLabel.grid(row=0, column=0)
        self.quitButton.grid(row=2, column=0)
        self.launchButton.grid(row=1, column=0)


    # image on welcome screen
    def open_image(self):

        path = "images/brewimage.jpg"
        self.image = Image.open(path)
        self.image = self.image.resize((400, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self.topFrame, image=self.img)
        self.label.image =self.img
        self.label.grid(row=0, column=0)

    def launch_main_menu(self):
        self.topFrame.destroy()
        self.botFrame.destroy()
        menu = MenuScreen(self.master)


#############################################################################################
class MenuScreen(tk.Frame):
    def __init__(self, master=None):

        # setting up the master window
        super().__init__(master)
        self.master = master
        self.masterWindow_setup()

        self.topFrame = tk.Frame(master)
        self.topFrame.pack()

        self.botFrame = tk.Frame(master)
        self.botFrame.pack(side="bottom")

        self.create_widgets()
        self.open_image()


    def masterWindow_setup(self):
        self.master.title("Brew Master 1.0")
        self.master.minsize(500, 500)
        self.master.resizable(False, False)
        self.pack()

    def create_widgets(self):
        self.recipesButton = tk.Button(self.botFrame, text="RECIPES", width=25,
                                      command=self.launch_recipes_menu)
        self.calculationsButton = tk.Button(self.botFrame, text="CALCULATIONS", width=25,
                                      command=self.launch_calculations_menu)

        self.quitButton = tk.Button(self.botFrame, text="QUIT", width=25, fg="red", command=self.master.destroy)
        self.welcomeLabel = tk.Label(self, text="Chose what you wanna do", font="Times 18",
                                     height=5)

        self.recipesButton.grid(row=1, column=0)
        self.quitButton.grid(row=2, column=1)
        self.calculationsButton.grid(row=1, column=1)


    def launch_recipes_menu(self):
        print("next")

    def launch_calculations_menu(self):
        print("next")

        # image on welcome screen

    def open_image(self):
        path = "images/brewimage2.jpg"
        self.image = Image.open(path)
        self.image = self.image.resize((400, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self, image=self.img)
        self.label.image = self.img
        self.label.grid(row=0, column=0)

