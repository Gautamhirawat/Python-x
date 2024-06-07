from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView

class main(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Label
        label = Label(text='Label', font_size=20, size_hint=(1, None), height=50)
        layout.add_widget(label)

        # TextInput
        text_input = TextInput(hint_text='TextInput', size_hint=(1, None), height=50)
        layout.add_widget(text_input)

        # Button
        button = Button(text='Button', size_hint=(1, None), height=50)
        layout.add_widget(button)

        # ToggleButton
        toggle_button = ToggleButton(text='ToggleButton', size_hint=(1, None), height=50)
        layout.add_widget(toggle_button)

        # Switch
        switch = Switch(active=False, size_hint=(1, None), height=50)
        layout.add_widget(switch)

        # Slider
        slider = Slider(min=0, max=100, value=50, size_hint=(1, None), height=50)
        layout.add_widget(slider)

        # Spinner
        spinner = Spinner(text='Spinner', values=('Option 1', 'Option 2', 'Option 3'), size_hint=(1, None), height=50)
        layout.add_widget(spinner)

        # CheckBox
        checkbox = CheckBox(active=False, size_hint=(1, None), height=50)
        layout.add_widget(checkbox)

        # ProgressBar
        progress_bar = ProgressBar(value=50, size_hint=(1, None), height=50)
        layout.add_widget(progress_bar)

        # ScrollView
        scroll_view = ScrollView(size_hint=(1, None), height=100)
        scroll_content = BoxLayout(orientation='vertical', spacing=50, size_hint_y=None)
        for i in range(5):
            scroll_content.add_widget(Label(text=f'ScrollLabel {i}'))
        scroll_view.add_widget(scroll_content)
        layout.add_widget(scroll_view)

        return layout

if __name__ == '__main__':
    main().run()
