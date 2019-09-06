import tkinter as tk

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

    def masterWindow_setup(self):
        self.master.title("Brew Master 1.0")
        self.master.minsize(500, 500)
        self.pack()


    def create_widgets(self):
        self.launchButton = tk.Button(self.botFrame, text="LAUNCH BREWMASTER", width=25,
                                      command = self.launch_main_menu)

        self.launchButton.pack(side="top")
        self.quitButton = tk.Button(self.botFrame, text="QUIT", width=25, fg="red"
                                                    ,command=self.master.destroy)
        self.quitButton.pack(side="bottom")

    def launch_main_menu(self):
        print("next windnow")


