import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[sg.Text("Load image to pixelate")],
          [sg.Text("Pick a palette"), sg.InputText()],
          [sg.Button("Pixelate!"), sg.Button("Cancel")]]

window = sg.Window("Pixelator App", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    print("You entered ", values[0])

window.close()
