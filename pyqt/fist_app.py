import sys
from PySide6 import QtCore , QtWidgets, QtGui


class myApp (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Widgets
        self.sumar = QtWidgets.QPushButton("Sumar") #QPushButton es un boton 
        self.restar = QtWidgets.QPushButton("restar")
        self.multiplicar = QtWidgets.QPushButton("multiplicar")
        self.dividir = QtWidgets.QPushButton("dividir")
        
        
        self.text = QtWidgets.QLabel("0" , alignment= QtCore.Qt.AlignCenter) #Qlabel es un label como tkinter
        self.entry1 = QtWidgets.QLineEdit() #Qline edit crea entradas para el usuario
        self.entry2 = QtWidgets.QLineEdit() #Qline edit crea entradas para el usuario
        
        #Añadir widgets
        self.layout = QtWidgets.QVBoxLayout(self) # Los layout funcionan para añadir los widgets a la aplicacion
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.entry1)
        self.layout.addWidget(self.entry2)
        self.layout.addWidget(self.sumar)
        self.layout.addWidget(self.restar)
        self.layout.addWidget(self.multiplicar)
        self.layout.addWidget(self.dividir)
        
        
        self.sumar.clicked.connect(self.adicion)
        self.restar.clicked.connect(self.resta)
        self.multiplicar.clicked.connect(self.multiplicacion)
        self.dividir.clicked.connect(self.division)
        
#Logica del script, creamos las funciones dentro del slot ya que tienen interaccion con los widgets en este caso los botones
    @QtCore.Slot()
    def adicion (self):
        num1 = int(self.entry1.text())
        num2 = int(self.entry2.text())
        suma = num1 + num2
        self.text.setText(str(suma))
        
    def resta (self):
        num1 = int(self.entry1.text())
        num2 = int(self.entry2.text())
        resta = num1 - num2
        self.text.setText(str(resta))
        
    def multiplicacion(self):
        num1 = int(self.entry1.text())
        num2 = int(self.entry2.text())
        multiplicacion = num1 * num2
        self.text.setText(str(multiplicacion))
        
    def division(self):
        num1 = int(self.entry1.text())
        num2 = int(self.entry2.text())
        division = num1 / num2
        self.text.setText(str(division))


# Inicio de la aplicacion
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = myApp()
    widget.resize(400 , 200)
    widget.show()
    
    sys.exit(app.exec_())