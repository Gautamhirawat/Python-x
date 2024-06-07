import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide2.QtGui import QFont

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SignUp')
        self.setStyleSheet("background-color: #808080; color: white;")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('SignUp', font=QFont("Arial", 24)))
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.layout.addWidget(self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText('Email')
        self.layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.signup_button = QPushButton('SignUp')
        self.signup_button.clicked.connect(self.signup)
        self.layout.addWidget(self.signup_button)

        self.login_button = QPushButton('Already have an account')
        self.login_button.clicked.connect(self.switch_to_login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def signup(self):
        QMessageBox.information(self, 'SignUp', 'SignUp completed successfully!')

    def switch_to_login(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setStyleSheet("background-color: #808080; color: white;")
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Login', font=QFont("Arial", 24)))
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login(self):
        QMessageBox.information(self, 'Login', 'Login completed successfully!')

class MyApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.sign_up_window = SignUpWindow()
        self.sign_up_window.show()

if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())
