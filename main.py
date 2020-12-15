'''
Created on Jul 24, 2020

@author: gems
'''

import tkinter as tk 
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


# layout = [  [sg.Text('Some text on Row 1')],
#             [sg.Text('Enter something on Row 2'), sg.InputText()],
#             [sg.Text('Enter something on Row 3'), sg.InputText()],
#             [sg.Checkbox('Hello')],
#             [sg.Button('Ok'), sg.Button('Cancel')] ]


tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
              [sg.Button('Read')]]



# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if  values[2] == True:
        print('Checkbox was clicked ')
    else:   
        print('Checkbox was not clicked ')
           
    print('You entered ', values[0],values[1])
    

window.close()