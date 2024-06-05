import PySimpleGUI as p


use_custom_titlebar = True if p.running_trinket() else False

def make_window(theme=None):

    NAME_SIZE = 23


    def name(name):
        dots = NAME_SIZE-len(name)-2
        return p.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    p.theme(theme)

    # NOTE that we're using our own LOCAL Menu element. It can be the standard Menubar or the PySimpleGUI MenubarCustom
    if use_custom_titlebar:
        Menu = p.MenubarCustom
    else:
        Menu = p.Menu

    treedata = p.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [[name('Text'), p.Text('Text')],
                [name('Input'), p.Input(s=15)],
                [name('Multiline'), p.Multiline(s=(15,2))],
                [name('Output'), p.Output(s=(15,2))],
                [name('Combo'), p.Combo(p.theme_list(), default_value=p.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                [name('OptionMenu'), p.OptionMenu(['OptionMenu',],s=(15,2))],
                [name('Checkbox'), p.Checkbox('Checkbox')],
                [name('Radio'), p.Radio('Radio', 1)],
                [name('Spin'), p.Spin(['Spin',], s=(15,2))],
                [name('Button'), p.Button('Button')],
                [name('ButtonMenu'), p.ButtonMenu('ButtonMenu', p.MENU_RIGHT_CLICK_EDITME_EXIT)],
                [name('Slider'), p.Slider((0,10), orientation='h', s=(10,15))],
                [name('Listbox'), p.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
                [name('Image'), p.Image(p.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), p.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

    layout_r  = [[name('Canvas'), p.Canvas(background_color=p.theme_button_color()[1], size=(125,40))],
                [name('ProgressBar'), p.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
                [name('Table'), p.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
                [name('Tree'), p.Tree(treedata, ['Heading',], num_rows=3)],
                [name('Horizontal Separator'), p.HSep()],
                [name('Vertical Separator'), p.VSep()],
                [name('Frame'), p.Frame('Frame', [[p.T(s=15)]])],
                [name('Column'), p.Column([[p.T(s=15)]])],
                [name('Tab, TabGroup'), p.TabGroup([[p.Tab('Tab1',[[p.T(s=(15,2))]]), p.Tab('Tab2', [[]])]])],
                [name('Pane'), p.Pane([p.Col([[p.T('Pane 1')]]), p.Col([[p.T('Pane 2')]])])],
                [name('Push'), p.Push(), p.T('Pushed over')],
                [name('VPush'), p.VPush()],
                [name('Sizer'), p.Sizer(1,1)],
                [name('StatusBar'), p.StatusBar('StatusBar')],
                [name('Sizegrip'), p.Sizegrip()]  ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [p.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 14', justification='c', expand_x=True)],
              [p.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-', p=0)],
              [p.Col(layout_l, p=0), p.Col(layout_r, p=0)]]

    window = p.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=p.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=p.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window


window = make_window()

while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == 'Exit':
        break

    if values['-COMBO-'] != p.theme():
        p.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        p.set_options(use_custom_titlebar=use_custom_titlebar)
        window.close()
        window = make_window()
    if event == 'Edit Me':
        p.execute_editor(__file__)
    elif event == 'Version':
        p.popup_scrolled(__file__, p.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
window.close()
