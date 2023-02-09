from tkinter import ttk
import tkinter as tk

from Formularis.form1Protagonist import updateProtagonistScreen

connexio = None


def openLocationsFromMenu():
    frameMenu.pack_forget()
    frameLocations.pack()


def backToMenufromLocations():
    frameLocations.pack_forget()
    frameMenu.pack()

def openRoadsFromMenu():
    frameMenu.pack_forget()
    frameRoads.pack()


def backToMenufromRoads():
    frameRoads.pack_forget()
    frameMenu.pack()

def openObjectsFromMenu():
    frameMenu.pack_forget()
    frameObjects.pack()


def backToMenufromObjects():
    frameObjects.pack_forget()
    frameMenu.pack()

def openProtagonistFromMenu():
    frameMenu.pack_forget()
    frameProtagonist.pack()


def backToMenufromProtagonist():
    frameProtagonist.pack_forget()
    frameMenu.pack()
def updateProtagonist():
    updateProtagonistScreen()


def leaveGame():
    window.destroy()


window = tk.Tk()
frameMenu = tk.Frame(window)
frameMenu.pack()
buttonLocations = tk.Button(frameMenu,
                            text="LOCALITZACIONS",
                            command=openLocationsFromMenu)
buttonRoads = tk.Button(frameMenu,
                        text="CAMINS",
                        command=openRoadsFromMenu)
buttonObjects = tk.Button(frameMenu,
                          text="OBJECTES",
                          command=openObjectsFromMenu)
buttonProtagonist = tk.Button(frameMenu,
                              text="PROTAGONISTA",
                              command=openProtagonistFromMenu)
buttonGetOut = tk.Button(frameMenu,
                         text="SORTIR",
                         command=leaveGame)

buttonLocations.pack()
buttonRoads.pack()
buttonObjects.pack()
buttonProtagonist.pack()
buttonGetOut.pack()

frameProtagonist = tk.Frame(window)


buttonGetOutFromProtagonist = tk.Button(frameProtagonist,
                                        text="SORTIR",
                                        command=backToMenufromProtagonist)
buttonGetOutFromProtagonist.pack()


frameLocations = tk.Frame(window)
buttonGetOutFromLocations = tk.Button(frameLocations,
                                      text="SORTIR",
                                      command=backToMenufromLocations)
buttonGetOutFromLocations.pack()


frameRoads = tk.Frame(window)
buttonGetOutFromRoads = tk.Button(frameRoads,
                                  text="SORTIR",
                                  command=backToMenufromRoads)

buttonGetOutFromRoads.pack()


frameObjects = tk.Frame(window)
buttonGetOutFromObjects = tk.Button(frameObjects,
                                    text="SORTIR",
                                    command=backToMenufromObjects)

buttonGetOutFromObjects.pack()

window.mainloop()
