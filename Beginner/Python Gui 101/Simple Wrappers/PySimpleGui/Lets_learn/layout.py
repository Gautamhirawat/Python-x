import PySimpleGUI as p

layout = [
    [p.Text('If you only want to just show text and nothing else : ')],
    [p.Text('Now in this i will add an input box for user by : ') , p.InputText()],
    [p.Button('Ok')],
    [p.Text('Because you haven`t added function or any command  for the button')],
    [p.Text('Now next button would be cancel and we will assign a case/function for cancel in while loop below') , p.Button('Cancel')]

]
window = p.Window('Here is the Title',layout)

while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values[0])
window.close()