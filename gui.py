import tkinter as tk

root = tk.Tk()

topframe = tk.Frame(root)
topframe.pack()

bottemframe = tk.Frame(root)
bottemframe.pack(side = tk.BOTTOM)



greenbutton = tk.Button(bottemframe, text="green", fg="green")
greenbutton.pack(side= tk.RIGHT)


redbutton = tk.Button(topframe, text="red", fg="red")
redbutton.pack(side= tk.LEFT)


bluebotton = tk.Button(topframe, text="blue", fg="blue")
bluebotton.pack(side= tk.LEFT)





# main loop
root.mainloop()
