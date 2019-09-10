import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from itertools import islice
import os

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
        self.master.minsize(800, 600)
        # setting up the frames

        self.leftFrame = tk.Frame(master)
        self.leftFrame.pack(side="left")

        self.rightFrame = tk.Frame(master, bd=2 ,relief="sunken")
        self.rightFrame.pack(side="right")


        # list of all recipes in recipe directory
        self.recipeNames = tk.StringVar(value=self.getRecipeNames())

        # update the dictionary to retrieve listbox index -> file path
        self.boxPathDict = dict()
        self.updateListboxRecipePathDictionary()

        # creating the widgets
        self.create_widgets_right()
        self.create_widgets_left()



    # listboxIndex -> Recipe path Dictionary
    def updateListboxRecipePathDictionary(self):
        boxPathDictionary = dict()
        recipeNames = self.getRecipeNames()
        for i in range(0, len(self.getRecipeNames())):
            boxPathDictionary[i] = 'recipes/' + recipeNames[i] + '.txt'
        self.boxPathDict = boxPathDictionary

    # returns list of all the recipes created in recipes directory
    def getRecipeNames(self):
        recipeFullNames = os.listdir("recipes")
        recipeNames = []
        for fullname in recipeFullNames:
            base, ext = os.path.splitext(fullname)
            recipeNames.append(base)
        return recipeNames

     # used to update the list of recipes in the listbox, also updates the recipe dictionary
    def updateRecipeListBox(self):
        self.recipeNames = tk.StringVar(value=self.getRecipeNames())
        self.listbox = tk.Listbox(self.leftFrame, listvariable=self.recipeNames)
        self.listbox.grid(row=0, column=0)
        self.updateListboxRecipePathDictionary()

    # creates the scoll recipe menu on the left side
    def create_widgets_left(self):
        self.listbox =tk.Listbox(self.leftFrame, listvariable=self.recipeNames)
        self.listbox.grid(row=0,column=0)
        readRecipeButton = tk.Button(self.leftFrame, text="READ", command=self.readRecipe)
        readRecipeButton.grid(row=1, column=1)
        editRecipeButton = tk.Button(self.leftFrame, text="EDIT", command=self.editRecipe)
        editRecipeButton.grid(row=1, column=2)
        editRecipeButton = tk.Button(self.leftFrame, text="NEW", command=self.newRecipe)
        editRecipeButton.grid(row=1, column=3)
        deleteRecipeButton = tk.Button(self.leftFrame, text="DELETE", command=self.deleteRecipe)
        deleteRecipeButton.grid(row=1, column=4)
        recipeScrollbar = tk.Scrollbar(self.leftFrame, orient="vertical")
        recipeScrollbar.grid(row=0,column=1,sticky='ns')
        recipeScrollbar.configure(command= self.listbox.yview)
        self.listbox.configure(yscrollcommand=recipeScrollbar.set)


    # creates the recipe entry on the right side
    def create_widgets_right(self):
        # creating input for the recipetext

        self.beername = tk.StringVar()
        self.beernameEntry = tk.Entry(self.rightFrame, textvariable=self.beername)
        self.beernameEntry.grid(row=1,column=0)

        self.beerBrewingRecipeInfo = tk.Text(self.rightFrame)
        self.beerBrewingRecipeInfo.grid(row=2, column=0)

        recipeSubmitButton = tk.Button(self.rightFrame, text="SAVE", width=25, command=self.save_recipe_to_file)
        recipeSubmitButton.grid(row=3, column=0)

        recipeSubmitButton = tk.Button(self.rightFrame, text="UPLOAD IMAGE", command=self.uploadBeerImage)
        recipeSubmitButton.grid(row=0, column=1)

        self.open_image()


    # returns all text from the user input beerbrew info
    def retrieve_beerBrewingInfo(self):
        inputs = self.beerBrewingRecipeInfo.get('1.0', 'end')
        return inputs

    # creates a new recipe from input in textbox beerBrewingRecipe and beerNameEntry and saves it to textfile in recipes
    # to file with same name is beerName

    def save_recipe_to_file(self):
        pathname = 'recipes/' + self.beername.get() + '.txt'
        file=open(pathname, 'w')

        textFileLines = open(pathname, 'r').readlines()
        if (len(textFileLines)!=0):
            if(textFileLines[0].startswith("beerimage")):
                newTextFile= [textFileLines[0]]
                newTextFile.append("recipe ")
                for line in islice(self.retrieve_beerBrewingInfo(), 0, None):
                    newTextFile.append(line)
                for string in newTextFile:
                    file.write(string)
                file.close()
            else:
                newTextFile = []
                newTextFile.append("recipe ")
                for line in islice(self.retrieve_beerBrewingInfo(), 0, None):
                    newTextFile.append(line)
                for string in newTextFile:
                    file.write(string)
                file.close()
        else:
            newTextFile = []
            newTextFile.append("recipe ")
            for line in islice(self.retrieve_beerBrewingInfo(), 0, None):
                newTextFile.append(line)
            for string in newTextFile:
                file.write(string)
            file.close()



        # update the listbox Options to create new recipe
        self.updateRecipeListBox()
        self.beerBrewingRecipeInfo.configure(state='disabled')
        self.beernameEntry.configure(state='disabled')


    # opens the recipe for reading only
    def readRecipe(self):
        # clear and set recipe field to read only
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.beerBrewingRecipeInfo.delete(1.0, tk.END)
        # clear and set recipe name to read only
        self.beernameEntry.configure(state='normal')
        self.beernameEntry.delete(0, tk.END)


        with open(self.boxPathDict.get(self.listbox.curselection()[0]), 'r') as f:
            recipeStart = False
            for line in islice(f, 0, None):
                if(str(line).startswith("recipe")):
                    recipeStart = True
                if(recipeStart):
                    self.beerBrewingRecipeInfo.insert(1.0,line)
            self.beernameEntry.insert(0, self.getRecipeNames()[self.listbox.curselection()[0]])
        self.beerBrewingRecipeInfo.configure(state='disabled')
        self.beernameEntry.configure(state='disabled')

    # opens the recipe for editing
    def editRecipe(self):
        # clears recipe

        self.beernameEntry.configure(state='normal')
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.beerBrewingRecipeInfo.delete('1.0', tk.END)
        self.beernameEntry.delete(0, tk.END)

        try:
            pathname = self.boxPathDict.get(self.listbox.curselection()[0])
        except:
            return

        with open(self.boxPathDict.get(self.listbox.curselection()[0]), 'r') as f:
            recipeStart = False
            for line in islice(f, 0, None):
                if (str(line).startswith("recipe")):
                    recipeStart = True
                if (recipeStart):
                    self.beerBrewingRecipeInfo.insert(1.0, line)
            self.beernameEntry.insert(0, self.getRecipeNames()[self.listbox.curselection()[0]])

    def newRecipe(self):
        self.beernameEntry.configure(state='normal')
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.beerBrewingRecipeInfo.delete('1.0', tk.END)
        self.beernameEntry.delete(0, tk.END)

    def deleteRecipe(self):
        MsgBox = tk.messagebox.askquestion('Delete recipe', 'Are you sure you want to delete this recipe', icon='warning')
        if MsgBox == 'yes':
            os.remove(self.boxPathDict.get(self.listbox.curselection()[0]))
            self.updateRecipeListBox()
        else:
            return

  # image for beerRecipe
    def open_image(self):
        path = "images/brewimage.jpg"
        self.beerImage = Image.open(path)
        self.beerImage = self.beerImage.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.beerImage)

        self.userBeerImage = tk.Label(self.rightFrame, image=self.img)
        self.userBeerImage.image =self.img
        self.userBeerImage.grid(row=0, column=0)
    # TODO schrijf image path als eerst line in recept als recept bestaat anders vraag om eerst recept aan te maken
    def uploadBeerImage(self):
        if(len(self.beername.get())!=0):
            self.beerImagePath = filedialog.askopenfile(initialdir ="/", title="Select an image", filetypes =[('all files', '.*'),
                                                                                                              ('text files', '.txt'),
                                                                                                              ('image files', ('.png', '.jpg')),
                                                                                                              ])
            pathname = 'recipes/' + self.beername.get() + '.txt'
            self.replace_line_textfile(pathname, 0, "beerimage" + " " +str(self.beerImagePath.name))

        else:
            MsgBox = tk.messagebox.showinfo('Recipe name', 'Please fill in recipe name before uploading image')
            return


    def replace_line_textfile(self,file_name, line_num, text):
        lines = open(file_name, 'r').readlines()
        if (len(lines)!= 0):
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        else:
            out = open(file_name, 'w')
            out.writelines(text)
            out.close()
