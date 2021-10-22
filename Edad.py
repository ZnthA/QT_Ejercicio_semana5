#Mostrar la edad de una persona de acuerdo al año que nació. 
import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "Edad.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btnCalculo.clicked.connect(self.fn_calculo)
        self.btnLimpiar.clicked.connect(self.fn_limpiar)
        self.btnSalir.clicked.connect(self.fn_salir)

    def fn_calculo(self):
    	fechaActual = int(self.txtN1.text())
    	fecha = int(self.txtN2.text())
    	edad = fechaActual-fecha
    	self.txtN3.setText(str(edad))


    def fn_limpiar(self):
    	self.txtN1.setText("")
    	self.txtN2.setText("")
    	self.txtN3.setText("")
    	self.txtN1.setFocus()


    def fn_salir(root):
    	root.destroy()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


