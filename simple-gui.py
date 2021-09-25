import PySimpleGUI as sg
import io
import os
from PIL import Image
import pixel_image_creator

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

# sg.theme("DarkBlue3")

# create list of palette choices for Listbox
palette_list = []
dirs = os.listdir("Palettes")
for palette in dirs:
    palette_list.append(palette)
# maybe load palettes the same way you load and image?  But then user would need to have palette on their computer


def main():
    layout = [
        [sg.Image(key="IMAGE")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="FILE"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [sg.Text("Pick a palette"), sg.Listbox(palette_list, size=(20, 4), enable_events=False, key="_LIST_")],
        [sg.Button("Pixelate!"), sg.Button("Cancel")]
    ]

    window = sg.Window("Pixelator App", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Load Image":
            filename = values["FILE"]
            if os.path.exists(filename):
                image = Image.open(values["FILE"])
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["IMAGE"].update(data=bio.getvalue())
        if event == "Pixelate!":
            # figure out how to call pixelate program on image and return pixelated copy
            # need to pass the original image and the palette selection
            new_image = pixel_image_creator.main(image, palette)

    window.close()


if __name__ == "__main__":
    main()
