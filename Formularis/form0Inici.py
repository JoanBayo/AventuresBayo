from tkinter import ttk
import tkinter as tk

from Formularis.form1Protagonist import updateProtagonistScreen

connexio = None


def openToProtagonistMenu():

    frameMenu.pack_forget()
    frameProtagonist.pack()
    pass


def openToObjectsMenu():
    pass


def openToRoadsMenu():
    pass


def openToLocationsMenu():
    pass


def updateProtagonist():
    updateProtagonistScreen()


def leaveGame():
    window.destroy()


window = tk.Tk()
frameMenu = tk.Frame(window)
frameMenu.pack()
buttonLocations = tk.Button(frameMenu,
                            text="LOCALITZACIONS",
                            command=openToLocationsMenu)
buttonRoads = tk.Button(frameMenu,
                        text="CAMINS",
                        command=openToRoadsMenu)
buttonObjects = tk.Button(frameMenu,
                          text="OBJECTES",
                          command=openToLocationsMenu)
buttonProtagonist = tk.Button(frameMenu,
                              text="PROTAGONISTA",
                              command=openToProtagonistMenu)
buttonGetOut = tk.Button(frameMenu,
                              text="SORTIR",
                              command=leaveGame)


buttonLocations.pack()
buttonRoads.pack()
buttonObjects.pack()
buttonProtagonist.pack()
buttonGetOut.pack()

frameProtagonist = tk.Frame(window)

buttonGetOut = tk.Button(frameProtagonist,
                              text="SORTIR",
                              command=leaveGame)

buttonGetOut.pack()


window.mainloop()
