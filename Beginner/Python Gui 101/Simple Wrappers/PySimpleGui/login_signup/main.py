import PySimpleGUI as p

def main():
    layout = [
        [p.Text('Sign Up', size=(20,1), justification='center', font=("Helvetica", 20), key='-TITLE-')],
        [p.Column([[p.Text('Username:'), p.InputText()],
                    [p.Text('Email:'), p.InputText()],
                    [p.Text('Password:'), p.InputText(password_char='*')],
                    [p.Button('Sign In')],
                    [p.Button('Already have a account')]], 
                    element_justification='center', vertical_alignment='center', justification='center', key='-CONTENT-')],

    ]
    layout2 = [
        [p.Text('Login', size=(20,1), justification='center', font=("Helvetica", 20), key='-TITLE-')],
        [p.Column([[p.Text('Username:'), p.InputText()],
                    [p.Text('Password:'), p.InputText(password_char='*')],
                    [p.Button('Sign Up'), p.Button('Login')]], 
                    element_justification='center', vertical_alignment='center', justification='center', key='-CONTENT-')],

    ]

    # Create the main and secondary window
    window = p.Window('Sign Up', layout, size=(400, 400), element_justification='center')
    window2 = p.Window('Login Page', layout2, size=(400, 400), element_justification='center')

    # loop to just run the window by read()
    while True:
        event, values = window.read()
        if event == p.WINDOW_CLOSED:
            break
        if event == 'Sign In':
            p.popup('Sign Up !')
        elif event == 'Already have a account':
            while True:
                event, values = window2.read()
                if event == p.WINDOW_CLOSED:
                    break           
            window2.close(),window.close()
        window.close()




if __name__ == "__main__":
    main()
