import PySimpleGUI as sg
import io
import os
from PIL import Image
import pixel_image_creator

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

# sg.theme("DarkBlue3")


def main():
    layout = [
        [sg.Image(key="IMAGE")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="FILE"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [sg.Text("Pick a palette"), sg.InputText()],
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
                image.thumbnail((500, 500))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["IMAGE"].update(data=bio.getvalue())

    window.close()


if __name__ == "__main__":
    main()
