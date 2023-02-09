from tkinter import Pack

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window("THE TO-DO APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()