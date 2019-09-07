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

        # setting up the frames

        self.topFrame =tk.Frame(master)
        self.topFrame.pack()

        self.botFrame = tk.Frame(master)
        self.botFrame.pack(side="bottom")

        # creating the widgets

        self.create_widgets()
        self.open_image()


    def create_widgets(self):
        self.recipesButton = tk.Button(self.botFrame, text="RECIPES", width=25,
                                      command=self.launch_recipes_menu)
        self.calculationsButton = tk.Button(self.botFrame, text="CALCULATIONS", width=25,
                                      command=self.launch_calculations_menu)

        self.quitButton = tk.Button(self.botFrame, text="QUIT", width=25, fg="red", command=self.master.destroy)
        self.welcomeLabel = tk.Label(self.topFrame, text="Choose what you wanna do", font="Times 16",
                                     height=5)

        self.recipesButton.grid(row=1, column=0)
        self.quitButton.grid(row=2, column=2)
        self.calculationsButton.grid(row=1, column=2)
        self.welcomeLabel.grid(row=1,column=0)


        # image on welcome screen

    def open_image(self):
        path = "images/brewimage2.jpg"
        self.image = Image.open(path)
        self.image = self.image.resize((400, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(self.topFrame, image=self.img)
        self.label.image = self.img
        self.label.grid(row=0, column=0)


    def launch_recipes_menu(self):
        self.topFrame.destroy()
        self.botFrame.destroy()
        recipes = RecipesMenu(self.master)

    def launch_calculations_menu(self):
        print("next")


##########################################################################################################
class RecipesMenu(tk.Frame):
    def __init__(self, master=None):

        # setting up the master window
        super().__init__(master)
        self.master = master
        self.master.minsize(1500, 950)
        # setting up the frames

        self.leftFrame = tk.Frame(master)
        self.leftFrame.pack()

        self.rightFrame = tk.Frame(master, bd=2 ,relief="sunken")
        self.rightFrame.pack(side="right")

        self.create_widgets_right()

        # creating the widgets

        self.create_widgets_left()

    def create_widgets_left(self):
        self.recipesButton = tk.Button(self.leftFrame, text="RECIPES", width=25)

    def create_widgets_right(self):
        # creating input for the recipetext

        self.beername = tk.StringVar()
        self.beernameEntry = tk.Entry(self.rightFrame, textvariable=self.beername)
        self.beernameEntry.grid(row=0,column=0)

        self.beerBrewingRecipeInfo = tk.Text(self.rightFrame)
        self.beerBrewingRecipeInfo.grid(row=1, column=0)

        recipeSubmitButton = tk.Button(self.rightFrame, text="SUBMT", width=25, command=self.create_new_recipe_to_file)
        recipeSubmitButton.grid(row=2, column=0)

    def retrieve_beerBrewingInfo(self):
        inputs = self.beerBrewingRecipeInfo.get('1.0', 'end')
        return inputs

    # creates a new recipe from beerBrewingRecipe and beerNameEntry and saves it to textfile in recipes

    def create_new_recipe_to_file(self):
        pathname = 'recipes/' + self.beername.get() + '.txt'
        print(pathname)
        file = file=open(pathname, 'w')
        file.write(self.retrieve_beerBrewingInfo())
        file.close()
