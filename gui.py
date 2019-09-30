import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from itertools import islice
import fnmatch
import os
import pickle

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
        #self.master.maxsize(800, 600)
        self.master.resizable(True, True)
        # setting up the frames


        #self.topRightFrame = tk.Frame(master)
        #self.topRightFrame.pack(side="top")

        self.topLeftFrame = tk.Frame(master)
        self.topLeftFrame.pack(side="top", fill=tk.X, expand=True)




        self.botLeftFrame = tk.Frame(master, bd=2, relief="sunken")
        self.botLeftFrame.pack(side="left", fill=tk.Y, expand=False)



        self.rightBotFrame = tk.Frame(master, bd= 2,relief="sunken")
        self.rightBotFrame.pack(side="left", expand=False)



        # list of all recipes in recipe directory
        self.recipeNames = tk.StringVar(value=self.getRecipeNames())

        # update the dictionary to retrieve listbox index -> file path
        self.boxPathDict = dict()
        self.updateListboxRecipePathDictionary()

        # creating the widgets
        self.create_widgets_right()
        self.create_widgets_left()
        #self.create_widgets_topRight()
        self.makeRecipeInactive()



    # listboxIndex -> Recipe path Dictionary
    def updateListboxRecipePathDictionary(self):
        boxPathDictionary = dict()
        recipeNames = self.getRecipeNames()
        for i in range(0, len(self.getRecipeNames())):
            boxPathDictionary[i] = 'recipes/' + recipeNames[i] + '.txt'
        self.boxPathDict = boxPathDictionary

    # returns list of all the recipes created in recipes directory
    def getRecipeNames(self):
        recipeFullNames =  fnmatch.filter(os.listdir("recipes"), '*.txt')
        recipeNames = []
        for fullname in recipeFullNames:
            base, ext = os.path.splitext(fullname)
            recipeNames.append(base)
        return recipeNames

     # used to update the list of recipes in the listbox, also updates the recipe dictionary
    def updateRecipeListBox(self):
        self.recipeNames = tk.StringVar(value=self.getRecipeNames())
        self.listbox = tk.Listbox(self.topLeftFrame, listvariable=self.recipeNames)
        self.listbox.grid(row=0,column=0,columnspan=6,pady=5)
        self.updateListboxRecipePathDictionary()

    #def create_widgets_topRight(self):
    #    readRecipeButton = tk.Button(self.topLeftFrame, text="READ", command=self.readRecipe)
    #    readRecipeButton.pack()

    # creates the scoll recipe menu on the left side ACTUALLY TOP SIDE NOW
    def create_widgets_left(self):
        self.listbox =tk.Listbox(self.topLeftFrame, listvariable=self.recipeNames)
        self.listbox.grid(row=0,column=0,columnspan=6,pady=5)
        readRecipeButton = tk.Button(self.topLeftFrame, text="READ", command=self.readRecipe)
        readRecipeButton.grid(row=1, column=2,padx=0)
        editRecipeButton = tk.Button(self.topLeftFrame, text="EDIT", command=self.editRecipe)
        editRecipeButton.grid(row=1, column=3)
        editRecipeButton = tk.Button(self.topLeftFrame, text="NEW", command=self.newRecipe)
        editRecipeButton.grid(row=1, column=4)
        deleteRecipeButton = tk.Button(self.topLeftFrame, text="DELETE", command=self.deleteRecipe)
        deleteRecipeButton.grid(row=1, column=5)
        recipeScrollbar = tk.Scrollbar(self.topLeftFrame, orient="vertical")
        recipeScrollbar.grid(row=0,column=6, sticky='ns')
        recipeScrollbar.configure(command= self.listbox.yview)
        self.listbox.configure(yscrollcommand=recipeScrollbar.set)

        self.beerImage = Image.open('images/nobeerimage.jpg')
        self.beerImage = self.beerImage.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.beerImage)

        self.userBeerImage = tk.Label(self.topLeftFrame, image=self.img)
        self.userBeerImage.image = self.img
        self.userBeerImage.grid(row=0, column=10, padx=(450, 0))



    # creates the recipe entry on the right side
    def create_widgets_right(self):
        # creating input for the recipetext




        # naam
        self.beername = tk.StringVar()
        self.beernameEntry = tk.Entry(self.botLeftFrame, textvariable=self.beername)
        self.beernameEntry.grid(row=1,column=1, sticky="W")
        self.beernamelable = tk.Label(self.botLeftFrame, text="Recipe Name")
        self.beernamelable.grid(row=1,column=0)

        # hoeveelheid
        self.brouwhoeveelheid = tk.StringVar()
        self.brouwhoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable= self.brouwhoeveelheid)
        self.brouwhoeveelheidEntry.grid(row=2, column=1, sticky="W")
        self.brouwhoeveelheidlable = tk.Label(self.botLeftFrame, text="Batch size")
        self.brouwhoeveelheidlable.grid(row=2, column=0)

        # calculate

        self.recipeCalculateButton = tk.Button(self.botLeftFrame, text="Calculate", width=25, command=self.calculateNewSizes)
        self.recipeCalculateButton.grid(row=11, column=1)

        # vergisbare ingredienten

        self.moutlijstMetGrammen = []

        aantalMouten = 0

        self.mout1 = tk.StringVar()
        self.mout1Hoeveelheid = tk.StringVar()
        self.mout1paar = (self.mout1, self.mout1Hoeveelheid)
        self.moutlijstMetGrammen.append(self.mout1paar)

        self.mout1Entry = tk.Entry(self.botLeftFrame, textvariable=(self.moutlijstMetGrammen[aantalMouten])[0])
        self.mout1Entry.grid(row=3, column=1, sticky="W")
        self.mout1lable = tk.Label(self.botLeftFrame, text="Mout")
        self.mout1lable.grid(row=3, column=0)

        self.mout1HoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable=(self.moutlijstMetGrammen[aantalMouten])[1])
        self.mout1HoeveelheidEntry.grid(row=3, column=2)
        self.mout1Hoeveelheidlable = tk.Label(self.botLeftFrame, text="gram")
        self.mout1Hoeveelheidlable.grid(row=2, column=2, sticky="W")

        aantalMouten += 1

        self.mout2 = tk.StringVar()
        self.mout2Hoeveelheid = tk.StringVar()
        self.mout2paar = (self.mout2, self.mout2Hoeveelheid)
        self.moutlijstMetGrammen.append(self.mout2paar)

        self.mout2Entry = tk.Entry(self.botLeftFrame, textvariable=(self.moutlijstMetGrammen[aantalMouten])[0])
        self.mout2Entry.grid(row=4, column=1, sticky="W")
        self.mout2lable = tk.Label(self.botLeftFrame, text="Mout 2")
        self.mout2lable.grid(row=4, column=0)

        self.mout2HoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable=(self.moutlijstMetGrammen[aantalMouten])[1])
        self.mout2HoeveelheidEntry.grid(row=4, column=2, sticky="W")

        # gisten
        self.gistlijstMetGrammen = []

        aantalGisten = 0

        self.gist1 = tk.StringVar()
        self.gist1Hoeveelheid = tk.StringVar()
        self.gist1paar = (self.gist1, self.gist1Hoeveelheid)
        self.gistlijstMetGrammen.append(self.gist1paar)

        self.gist1Entry = tk.Entry(self.botLeftFrame, textvariable=(self.gistlijstMetGrammen[aantalGisten])[0])
        self.gist1Entry.grid(row=5, column=1, sticky="W")
        self.gist1lable = tk.Label(self.botLeftFrame, text="Gist")
        self.gist1lable.grid(row=5, column=0)

        self.gist1HoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable=(self.gistlijstMetGrammen[aantalGisten])[1])
        self.gist1HoeveelheidEntry.grid(row=5, column=2, sticky="W")

        # hoppen
        self.hoplijstMetGrammen = []

        # lijst met hop paar, paar = (soort, gewicht)
        aantalHoppen = 0

        self.hop1 = tk.StringVar()
        self.hop1Hoeveelheid = tk.StringVar()
        self.hop1paar = (self.hop1, self.hop1Hoeveelheid)
        self.hoplijstMetGrammen.append(self.hop1paar)

        self.hop1Entry = tk.Entry(self.botLeftFrame, textvariable= (self.hoplijstMetGrammen[aantalHoppen])[0])
        self.hop1Entry.grid(row=6, column=1, sticky="W")
        self.hop1lable = tk.Label(self.botLeftFrame, text="Hop")
        self.hop1lable.grid(row=6, column=0)

        self.hopHoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable= (self.hoplijstMetGrammen[aantalHoppen])[1])
        self.hopHoeveelheidEntry.grid(row=6, column=2, sticky="W")
        aantalHoppen += 1

        self.hop2 = tk.StringVar()
        self.hop2Hoeveelheid = tk.StringVar()
        self.hop2paar = (self.hop2, self.hop2Hoeveelheid)
        self.hoplijstMetGrammen.append(self.hop2paar)

        self.hop2Entry = tk.Entry(self.botLeftFrame, textvariable=(self.hoplijstMetGrammen[aantalHoppen])[0])
        self.hop2Entry.grid(row=7, column=1, sticky="W")
        self.hop2lable = tk.Label(self.botLeftFrame, text="Hop 2")
        self.hop2lable.grid(row=7, column=0)

        self.hop2HoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable=(self.hoplijstMetGrammen[aantalHoppen])[1])
        self.hop2HoeveelheidEntry.grid(row=7, column=2, sticky="W")

        aantalHoppen += 1

        self.hop3 = tk.StringVar()
        self.hop3Hoeveelheid = tk.StringVar()
        self.hop3paar = (self.hop3, self.hop3Hoeveelheid)
        self.hoplijstMetGrammen.append(self.hop3paar)

        self.hop3Entry = tk.Entry(self.botLeftFrame, textvariable=(self.hoplijstMetGrammen[aantalHoppen])[0])
        self.hop3Entry.grid(row=8, column=1, sticky="W")
        self.hop3lable = tk.Label(self.botLeftFrame, text="Hop 3")
        self.hop3lable.grid(row=8, column=0)

        self.hop3HoeveelheidEntry = tk.Entry(self.botLeftFrame, textvariable=(self.hoplijstMetGrammen[aantalHoppen])[1])
        self.hop3HoeveelheidEntry.grid(row=8, column=2, sticky="W")


        # algemene recept info
        self.beerBrewingRecipeInfo = tk.Text(self.rightBotFrame)
        self.beerBrewingRecipeInfo.grid(row=1, column=0)
        self.receptlable = tk.Label(self.rightBotFrame, text="Recept info")
        self.receptlable.grid(row=0, column=0)

        self.recipeSubmitButton = tk.Button(self.botLeftFrame, text="SAVE", width=25, command=self.save_recipe_to_file)
        self.recipeSubmitButton.grid(row=10, column=1)

        self.uploadImageButton = tk.Button(self.botLeftFrame, text="UPLOAD IMAGE", command=self.uploadBeerImage)
        self.uploadImageButton.grid(row=10, column=0)



        self.uploadImageButton.configure(state='disabled')
        self.recipeSubmitButton.configure(state='disabled')




    # returns all text from the user input beerbrew info
    def retrieve_beerBrewingInfo(self):
        inputs = self.beerBrewingRecipeInfo.get('1.0', 'end')
        return inputs

    # creates a new recipe from input in textbox beerBrewingRecipe and beerNameEntry and saves it to textfile in recipes
    # to file with same name is beerName

    def save_recipe_to_file(self):
        pathname = 'recipes/' + self.beername.get() + '.txt'
        if(pathname == 'recipes/.txt'):
            MsgBox = tk.messagebox.showinfo('Recipe name', 'Please fill in recipe name before saving recipe')
            return

        # the text already in the file
        if(os.path.exists(pathname)):
            textFileLines = open(pathname, 'r').readlines()
        else:
            textFileLines = []

        # the new recipe the user has put in
        newRecipe = self.retrieve_beerBrewingInfo()

        # open the file to which we are going to write the new recipe

        file = open(pathname, 'w')
        # find which line the recipe begins in the file, BEFORE FOUND copy old recipe file, AFTER FOUND copy new file
        foundRecipeStartLine = False
        # finds the start of the recipe marked by STARTRECIPE keyword
        for i in range(len(textFileLines)):
            if(textFileLines[i].startswith("STARTRECIPE")):
                foundRecipeStartLine = True
            if(foundRecipeStartLine == False):
                file.write(textFileLines[i])
        # if the start has been found the new recipe is copied
        # als er nog geen recept was start recept op tweede lijn anders start op dezelfd lijn als eerste recept
        if(foundRecipeStartLine == False):
            file.write("\nSTARTRECIPE\n")
        else:
            file.write("STARTRECIPE\n")
        file.write(newRecipe)

        file.close()


        # we store the recipe general info and link to the picture in the txt file with the same name as the recipe
        # we store ingredient info in a pickle file with the same name as the recipe


        ingredientData = dict()


        # create pickle friendly dictionary
        pickleMoutLijst = []
        for moutPaar in self.moutlijstMetGrammen:
            mp = (moutPaar[0].get(), moutPaar[1].get())
            pickleMoutLijst.append(mp)

        pickleGistLijst = []
        for gistPaar in self.gistlijstMetGrammen:
            mp = (gistPaar[0].get(), gistPaar[1].get())
            pickleGistLijst.append(mp)

        pickleHopLijst = []
        for hopPaar in self.hoplijstMetGrammen:
            mp = (hopPaar[0].get(), hopPaar[1].get())
            pickleHopLijst.append(mp)

        ingredientData["mout"] = pickleMoutLijst
        ingredientData["hop"] = pickleHopLijst
        ingredientData["gist"] = pickleGistLijst
        ingredientData["volume"] = self.brouwhoeveelheid.get()

        with open('recipes/' + self.beername.get() +"pickle", 'wb') as handle:
            pickle.dump(ingredientData, handle, protocol=pickle.HIGHEST_PROTOCOL)

       # print(my_data == unserialized_data)

        # update the listbox Options to create new recipe
        #print(moutlijst)
        self.updateRecipeListBox()
        self.beerBrewingRecipeInfo.configure(state='disabled')
        self.beernameEntry.configure(state='disabled')
        self.uploadImageButton.configure(state='disabled')
        self.recipeSubmitButton.configure(state='disabled')

        self.makeRecipeInactive()

    def clearAllRecipeWidgets(self):
        # clear and set recipe field to read only
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.beerBrewingRecipeInfo.delete(1.0, tk.END)
        # clear and set recipe name to read only
        self.beernameEntry.configure(state='normal')
        self.beernameEntry.delete(0, tk.END)

        self.mout1Entry.configure(state='normal')
        self.mout1Entry.delete(0, tk.END)
        self.mout1HoeveelheidEntry.configure(state='normal')
        self.mout1HoeveelheidEntry.delete(0, tk.END)

        self.mout2Entry.configure(state='normal')
        self.mout2Entry.delete(0, tk.END)
        self.mout2HoeveelheidEntry.configure(state='normal')
        self.mout2HoeveelheidEntry.delete(0, tk.END)

        self.hop1Entry.configure(state='normal')
        self.hop1Entry.delete(0, tk.END)

        self.hopHoeveelheidEntry.configure(state='normal')
        self.hopHoeveelheidEntry.delete(0, tk.END)

        self.hop2Entry.configure(state='normal')
        self.hop2Entry.delete(0, tk.END)
        self.hop2HoeveelheidEntry.configure(state='normal')
        self.hop2HoeveelheidEntry.delete(0, tk.END)

        self.hop3Entry.configure(state='normal')
        self.hop3Entry.delete(0, tk.END)
        self.hop3HoeveelheidEntry.configure(state='normal')
        self.hop3HoeveelheidEntry.delete(0, tk.END)

        self.gist1Entry.configure(state='normal')
        self.gist1Entry.delete(0, tk.END)
        self.gist1HoeveelheidEntry.configure(state='normal')
        self.gist1HoeveelheidEntry.delete(0, tk.END)

        self.beernameEntry.configure(state='normal')
        self.beernameEntry.delete(0, tk.END)

        self.beernameEntry.configure(state='normal')
        self.beernameEntry.delete(0, tk.END)

        self.brouwhoeveelheidEntry.configure(state='normal')
        self.brouwhoeveelheidEntry.delete(0, tk.END)

    def makeRecipeInactive(self):
        # clear and set recipe field to read only
        self.beerBrewingRecipeInfo.configure(state='disabled')
        # clear and set recipe name to read only
        self.beernameEntry.configure(state='disabled')
        self.mout1Entry.configure(state='disabled')
        self.mout1HoeveelheidEntry.configure(state='disabled')
        self.mout2Entry.configure(state='disabled')
        self.mout2HoeveelheidEntry.configure(state='disabled')
        self.hop1Entry.configure(state='disabled')
        self.hopHoeveelheidEntry.configure(state='disabled')
        self.hop2Entry.configure(state='disabled')
        self.hop2HoeveelheidEntry.configure(state='disabled')
        self.hop3Entry.configure(state='disabled')
        self.hop3HoeveelheidEntry.configure(state='disabled')
        self.gist1Entry.configure(state='disabled')
        self.gist1HoeveelheidEntry.configure(state='disabled')
        self.beernameEntry.configure(state='disabled')
        self.brouwhoeveelheidEntry.configure(state='disabled')
        self.recipeCalculateButton.configure(state='disabled')
    def makeRecipeActive(self):
        # clear and set recipe field to read only
        self.beerBrewingRecipeInfo.configure(state='normal')
        # clear and set recipe name to read only
        self.beernameEntry.configure(state='normal')
        self.mout1Entry.configure(state='normal')
        self.mout1HoeveelheidEntry.configure(state='normal')
        self.mout2Entry.configure(state='normal')
        self.mout2HoeveelheidEntry.configure(state='normal')
        self.hop1Entry.configure(state='normal')
        self.hopHoeveelheidEntry.configure(state='normal')
        self.hop2Entry.configure(state='normal')
        self.hop2HoeveelheidEntry.configure(state='normal')
        self.hop3Entry.configure(state='normal')
        self.hop3HoeveelheidEntry.configure(state='normal')
        self.gist1Entry.configure(state='normal')
        self.gist1HoeveelheidEntry.configure(state='normal')
        self.beernameEntry.configure(state='normal')
        self.brouwhoeveelheidEntry.configure(state='normal')


    # opens the recipe for reading only
    def readRecipe(self):
        self.clearAllRecipeWidgets()

        with open(self.boxPathDict.get(self.listbox.curselection()[0]), 'r') as f:
            recipeStart = False
            for line in islice(f, 0, None):
                if(str(line).startswith("STARTRECIPE")):
                    recipeStart = True
                    continue;
                if(recipeStart):
                    self.beerBrewingRecipeInfo.insert(tk.INSERT,line)
            self.beernameEntry.insert(0, self.getRecipeNames()[self.listbox.curselection()[0]])
        self.beerBrewingRecipeInfo.configure(state='disabled')
        self.beernameEntry.configure(state='disabled')

        self.open_custom_image()



        # get the pickle recipe info and fill it in
        path  = self.boxPathDict.get(self.listbox.curselection()[0])
        base, ext = os.path.splitext(path)
        with open(base + "pickle", 'rb') as handle:
            recept = pickle.load(handle)

        self.mout1Entry.insert(0,(recept.get("mout")[0])[0])
        self.mout1HoeveelheidEntry.insert(0,(recept.get("mout")[0])[1])

        self.mout2Entry.insert(0,(recept.get("mout")[1])[0])
        self.mout2HoeveelheidEntry.insert(0,(recept.get("mout")[1])[1])

        self.hop1Entry.insert(0,(recept.get("hop")[0])[0])
        self.hopHoeveelheidEntry.insert(0,(recept.get("hop")[0])[1])

        self.hop2Entry.insert(0,(recept.get("hop")[1])[0])
        self.hop2HoeveelheidEntry.insert(0,(recept.get("hop")[1])[1])

        self.hop3Entry.insert(0,(recept.get("hop")[2])[0])
        self.hop3HoeveelheidEntry.insert(0,(recept.get("hop")[2])[1])

        self.gist1Entry.insert(0,(recept.get("gist")[0])[0])
        self.gist1HoeveelheidEntry.insert(0,(recept.get("gist")[0])[1])

        self.brouwhoeveelheidEntry.insert(0,recept.get("volume"))
        self.makeRecipeInactive()
        self.brouwhoeveelheidEntry.configure(state='normal')
        self.recipeCalculateButton.configure(state='normal')
        self.recipeSubmitButton.configure(state='disabled')

    def calculateNewSizes(self):
        self.recipeSubmitButton = tk.Button(self.botLeftFrame, text="SAVE", width=25, command=self.save_recipe_to_file)
        self.recipeSubmitButton.grid(row=10, column=1)

        pathname = 'recipes/' + self.beername.get()

        beernaam = self.beername.get()
        with open(pathname + "pickle", 'rb') as handle:
            recept = pickle.load(handle)

        previous = self.brouwhoeveelheidEntry.get()
        # open the file to which we are going to write the new recipe
        scalar = round(int(self.brouwhoeveelheidEntry.get())/int(recept.get("volume")))
        print(scalar)
        self.makeRecipeActive()

        self.clearAllRecipeWidgets()
        self.mout1Entry.insert(0, (recept.get("mout")[0])[0])
        self.mout1HoeveelheidEntry.insert(0, int((recept.get("mout")[0])[1])*scalar)

        self.mout2Entry.insert(0, (recept.get("mout")[1])[0])
        self.mout2HoeveelheidEntry.insert(0, int((recept.get("mout")[1])[1])*scalar)

        self.hop1Entry.insert(0, (recept.get("hop")[0])[0])
        self.hopHoeveelheidEntry.insert(0, int((recept.get("hop")[0])[1])*scalar)

        self.hop2Entry.insert(0, (recept.get("hop")[1])[0])
        self.hop2HoeveelheidEntry.insert(0, int((recept.get("hop")[1])[1])*scalar)

        self.hop3Entry.insert(0, (recept.get("hop")[2])[0])
        self.hop3HoeveelheidEntry.insert(0, int((recept.get("hop")[2])[1])*scalar)

        self.gist1Entry.insert(0, (recept.get("gist")[0])[0])
        self.gist1HoeveelheidEntry.insert(0, int((recept.get("gist")[0])[1])*scalar)
        self.brouwhoeveelheidEntry.insert(0,previous)
        self.beernameEntry.insert(0,beernaam)
        self.makeRecipeInactive()
        self.recipeSubmitButton.configure(state='disabled')
        self.recipeCalculateButton.configure(state='normal')

        self.brouwhoeveelheidEntry.configure(state='normal')


    # opens the recipe for editing
    def editRecipe(self):
        # clears recipe

        self.beernameEntry.configure(state='normal')
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.uploadImageButton.configure(state='normal')
        self.recipeSubmitButton.configure(state='normal')
        self.recipeCalculateButton.configure(state='disabled')
        self.beerBrewingRecipeInfo.delete('1.0', tk.END)
        self.beernameEntry.delete(0, tk.END)
        self.makeRecipeActive()

        try:
            pathname = self.boxPathDict.get(self.listbox.curselection()[0])
        except:
            return

        with open(self.boxPathDict.get(self.listbox.curselection()[0]), 'r') as f:
            recipeStart = False
            for line in islice(f, 0, None):
                if (str(line).startswith("STARTRECIPE")):
                    recipeStart = True
                    continue;
                if (recipeStart):
                    self.beerBrewingRecipeInfo.insert(tk.INSERT, line)
            self.beernameEntry.insert(0, self.getRecipeNames()[self.listbox.curselection()[0]])

    def newRecipe(self):
        self.clearAllRecipeWidgets()
        self.beernameEntry.configure(state='normal')
        self.beerBrewingRecipeInfo.configure(state='normal')
        self.uploadImageButton.configure(state='normal')
        self.recipeSubmitButton.configure(state='normal')
        self.recipeCalculateButton.configure(state='disabled')
        self.beerBrewingRecipeInfo.delete('1.0', tk.END)
        self.beernameEntry.delete(0, tk.END)

        self.beerImage = Image.open('images/nobeerimage.jpg')
        self.beerImage = self.beerImage.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.beerImage)

        self.userBeerImage = tk.Label(self.topLeftFrame, image=self.img)
        self.userBeerImage.image = self.img
        self.userBeerImage.grid(row=0, column=10, padx=(450, 0))

    # deletes pickle file and the txt file of the recipe
    def deleteRecipe(self):
        MsgBox = tk.messagebox.askquestion('Delete recipe', 'Are you sure you want to delete this recipe', icon='warning')
        if MsgBox == 'yes':
            textFile = self.boxPathDict.get(self.listbox.curselection()[0])
            os.remove(textFile)
            pickleFile = str(textFile).replace('.txt',"")
            pickleFile += "pickle"
            os.remove(pickleFile)
            self.updateRecipeListBox()
            self.beernameEntry.configure(state='normal')
            self.beerBrewingRecipeInfo.configure(state='normal')
            self.beerBrewingRecipeInfo.delete('1.0', tk.END)
            self.beernameEntry.delete(0, tk.END)
            self.beernameEntry.configure(state='disabled')
            self.beerBrewingRecipeInfo.configure(state='disabled')
            self.beerImage = Image.open('images/nobeerimage.jpg')
            self.beerImage = self.beerImage.resize((200, 200), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.beerImage)

            self.userBeerImage = tk.Label(self.topLeftFrame, image=self.img)
            self.userBeerImage.image = self.img
            self.userBeerImage.grid(row=0, column=10, padx=(450, 0))
            self.clearAllRecipeWidgets()
            self.makeRecipeInactive()
        else:
            return

  # image for beerRecipe
    def open_custom_image(self):
        pathname = 'recipes/' + self.beername.get() + '.txt'
        path = self.get_recipefile_subsection(pathname,"FILEIMAGE")
        try:
            self.beerImage = Image.open(path)
        except:
            self.beerImage = Image.open('images/nobeerimage.jpg')
        self.beerImage = self.beerImage.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.beerImage)

        self.userBeerImage = tk.Label(self.topLeftFrame, image=self.img)
        self.userBeerImage.image = self.img
        self.userBeerImage.grid(row=0, column=10, padx=(450, 0))



    # schrijft path van custom beer image voor recept naar eerst lijn recept file, if provideede with currect path also
    # opens that image
    def uploadBeerImage(self):
        if(len(self.beername.get())!=0):
            self.beerImagePath = filedialog.askopenfile(initialdir ="/", title="Select an image", filetypes =[('all files', '.*'),
                                                                                                              ('text files', '.txt'),
                                                                                                              ('image files', ('.png', '.jpg')),
                                                                                                              ])
            pathname = 'recipes/' + self.beername.get() + '.txt'

            # we schrijven path naar de eerste lijn van het recept text document
            if (self.textFileContainsSection(pathname, "BEERIMAGE")):
                self.replace_line_textfile(pathname, 1, str(self.beerImagePath.name) +"\n")
            else:
                self.replace_line_textfile(pathname, 0, "BEERIMAGE" + "\n" + str(self.beerImagePath.name) + "\n")
            self.open_custom_image()

        else:
            MsgBox = tk.messagebox.showinfo('Recipe name', 'Please fill in recipe name before uploading image')
            return


    # method to check if the text file of the recipe contains a keyword,
    def textFileContainsSection(self, pathname, word):
        lines = open(pathname, 'r').readlines()
        found = False
        for line in lines:
            if line.startswith(word):
                found = True
        return found


    # replaces the file with given filename on the given line with the given text
    def replace_line_textfile(self,file_name, line_num, text):
        try:
            lines = open(file_name, 'r').readlines()

        except:
            MsgBox = tk.messagebox.showinfo('No file found', 'Please create file before addinng pictures')
            return
        if (len(lines)!= 0):
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        else:
            out = open(file_name, 'w')
            out.writelines(text)
            out.close()
        lines = open(file_name, 'r').readlines()


    def get_recipefile_subsection(self,file_name,subsection):
        try:
            lines = open(file_name, 'r').readlines()
        except:
            return
        return lines[1].rstrip()
