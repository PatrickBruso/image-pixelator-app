import pixel_image_creator
import tkinter as tk
from tkinter import *


def main():
    # Setup window
    gui = Tk()  # figure out why some tutorials use Tk() and some tk.Tk()
    gui.title("Pixelator App")
    gui.geometry("1200x800")
    window = gui

    # Create label widget to display text
    heading = tk.Label(
        text="Pixelator App",
        fg="black",
        bg="white",
        width=10,
        height=1
    )
    heading.pack()

    # Create button to load image
    button = tk.Button(
        text="Load Image",
        width=25,
        height=5,
        bg="white",
        fg="black"
    )
    button.pack()

    # Call mainloop
    window.mainloop()


if __name__ == '__main__':
    main()
