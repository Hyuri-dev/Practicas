import sys
from PySide6 import QtCore , QtWidgets, QtGui


class Login(QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        self.setStyleSheet("background-color: #e8daef") # setStyleSheet nos permite darle estilos a los widgets como color, bg, radius, etc

        #Widgets

        #Textos
        self.title = QtWidgets.QLabel("Login", alignment= QtCore.Qt.AlignCenter)
        self.username = QtWidgets.QLabel("Usuario")
        self.password = QtWidgets.QLabel("Password")

        self.title.setStyleSheet("""font-size: 40px; color: #bb8fce""")

        #Entradas
        self.entry_username = QtWidgets.QLineEdit()
        self.entry_password = QtWidgets.QLineEdit()

        #Buttons
        self.login_button = QtWidgets.QPushButton("Entrar")

        #Ingresamos los widgets al layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.login_button)

        self.login_button.clicked.connect(self.verificacion)

    @QtCore.Slot()
    def verificacion (self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if username == "admin" and password == "admin":
            print("Login exitoso")
        else:
            print("Error al iniciar sesion, verifique los datos ingresados...")



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Login()
    widget.resize(400 , 200)
    widget.show()
    
    sys.exit(app.exec_())