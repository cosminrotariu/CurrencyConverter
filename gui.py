import PySimpleGUI as sg
import main

sg.theme("DarkBlue")

available_currencies = main.get_available_currencies()  # se obtin toate monedele disponibile pe site
available_currencies.sort()  # se sorteaza alfabetic

layout = [
    [sg.Text("Input currency")],
    [sg.Combo(available_currencies, size=(6, 6), key='input_currency', default_value='EUR', readonly=True),
     sg.Input('1', key='input', size=(30, 1), enable_events=True)],
    [sg.Text("Output currency")],
    [sg.Combo(available_currencies, size=(6, 6), key='output_currency', default_value='RON', readonly=True),
     sg.Input('', key='output', size=(30, 1), readonly=True, disabled_readonly_background_color='black')],
    [sg.Text('', size=(3, 0))],
    [sg.Button("Convert", key='convert'),
     sg.Button("Exit", key='exit')]
]

window = sg.Window('Currency converter', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'exit':  # daca se apasa pe exit se va inchide fereastra
        break
    elif event == 'input' and values['input'] != '' and values['input'][-1] \
            not in '.0123456789':  # daca se introduc valori in afara de cifre si . se va afisa un mesaj
        window['output'].update("Please write the amount in digits.")
        window['input'].update('')
    elif event == 'convert':  # daca se apasa pe convert, se face conversia
        window['output'].update(main.convert(values['input_currency'], values['input'], values['output_currency']))
window.close()
