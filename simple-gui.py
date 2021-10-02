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


def main():
    layout = [
        [sg.Image(key="_IMAGE_")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="_FILE_"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [
            sg.Text("Pick a palette"),
            sg.Listbox(palette_list, size=(20, 4), enable_events=False, key="_LIST_"),
            sg.Button("Show Palette")
        ],
        [sg.Button("Pixelate!"), sg.Button("Cancel")]
    ]

    window = sg.Window("Pixelator App", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "Load Image":
            filename = values["_FILE_"]
            if os.path.exists(filename):
                image = Image.open(values["_FILE_"])
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["_IMAGE_"].update(data=bio.getvalue())

        if event == "Show Palette":
            palette_choice = ' '.join(values["_LIST_"])
            sg.popup(title=f'{palette_choice}', image=f'Large_Palettes/{palette_choice}')

        if event == "Pixelate!":
            filename = values["_FILE_"]
            palette_choice = ' '.join(values["_LIST_"])
            if os.path.exists(filename):
                new_image = pixel_image_creator.main(filename, palette_choice)
                # bio = io.BytesIO()
                # new_image.save(bio, format="PNG")
                # window["_IMAGE_"].update(data=bio.getvalue())

    window.close()


if __name__ == "__main__":
    main()
