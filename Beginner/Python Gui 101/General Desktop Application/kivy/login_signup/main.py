from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window

class SignUpWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 0]
        self.spacing = 10
        Window.clearcolor = (0.5, 0.5, 0.5, 1)  # Grey background color

        # Spacer to center content vertically
        self.add_widget(Label())

        # Main heading
        main_heading = Label(text='SignUp', font_size=24, halign='center', color=(1, 1, 1, 1))  # White text color
        self.add_widget(main_heading)

        # Username input
        username_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=30)  # One line only
        username_label = Label(text='Username:', size_hint=(0.3, 1), color=(1, 1, 1, 1))  # White text color
        self.username_input = TextInput(size_hint=(0.7, 1), background_color=(1, 1, 1, 1))  # White background color
        username_layout.add_widget(username_label)
        username_layout.add_widget(self.username_input)
        self.add_widget(username_layout)

        # Email input
        email_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=30)  # One line only
        email_label = Label(text='Email:', size_hint=(0.3, 1), color=(1, 1, 1, 1))  # White text color
        self.email_input = TextInput(size_hint=(0.7, 1), background_color=(1, 1, 1, 1))  # White background color
        email_layout.add_widget(email_label)
        email_layout.add_widget(self.email_input)
        self.add_widget(email_layout)

        # Password input
        password_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=30)  # One line only
        password_label = Label(text='Password:', size_hint=(0.3, 1), color=(1, 1, 1, 1))  # White text color
        self.password_input = TextInput(size_hint=(0.7, 1), password=True, background_color=(1, 1, 1, 1))  # White background color
        password_layout.add_widget(password_label)
        password_layout.add_widget(self.password_input)
        self.add_widget(password_layout)

        # Spacer to center content vertically
        self.add_widget(Label())

        # Signup button
        signup_button = Button(text='SignUp', size_hint=(1, None), height=30, background_color=(1, 1, 1, 1))  # White background color
        signup_button.bind(on_press=self.signup)
        self.add_widget(signup_button)

        # Already have an account button
        login_button = Button(text='Already have an account', size_hint=(1, None), height=30, background_color=(1, 1, 1, 1))  # White background color
        login_button.bind(on_press=self.switch_to_login)
        self.add_widget(login_button)

    def signup(self, instance):
        popup = Popup(title='SignUp', content=Label(text='SignUp completed successfully!'), size_hint=(None, None), size=(400, 200))
        popup.open()

    def switch_to_login(self, instance):
        self.clear_widgets()
        self.add_widget(LoginWindow())

class LoginWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 0]
        self.spacing = 10
        Window.clearcolor = (0.5, 0.5, 0.5, 1)  # Grey background color

        # Spacer to center content vertically
        self.add_widget(Label())

        # Main heading
        main_heading = Label(text='Login', font_size=24, halign='center', color=(1, 1, 1, 1))  # White text color
        self.add_widget(main_heading)

        # Username input
        username_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=30)  # One line only
        username_label = Label(text='Username:', size_hint=(0.3, 1), color=(1, 1, 1, 1))  # White text color
        self.username_input = TextInput(size_hint=(0.7, 1), background_color=(1, 1, 1, 1))  # White background color
        username_layout.add_widget(username_label)
        username_layout.add_widget(self.username_input)
        self.add_widget(username_layout)

        # Password input
        password_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=30)  # One line only
        password_label = Label(text='Password:', size_hint=(0.3, 1), color=(1, 1, 1, 1))  # White text color
        self.password_input = TextInput(size_hint=(0.7, 1), password=True, background_color=(1, 1, 1, 1))  # White background color
        password_layout.add_widget(password_label)
        password_layout.add_widget(self.password_input)
        self.add_widget(password_layout)

        # Spacer to center content vertically
        self.add_widget(Label())

        # Login button
        login_button = Button(text='Login', size_hint=(1, None), height=30, background_color=(1, 1, 1, 1))  # White background color
        login_button.bind(on_press=self.login)
        self.add_widget(login_button)

    def login(self, instance):
        popup = Popup(title='Login', content=Label(text='Login completed successfully!'), size_hint=(None, None), size=(400, 200))
        popup.open()

class MyApp(App):
    def build(self):
        return SignUpWindow()

if __name__ == '__main__':
    MyApp().run()
