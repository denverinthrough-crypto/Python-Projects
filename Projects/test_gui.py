import PySimpleGUI as sg

layout = [[sg.Text("Hello! This works!")], [sg.Button("OK")]]

window = sg.Window("Test GUI", layout)
window.read()
window.close()
