import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "calculadora.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Aqui van los botones
        self.btnSuma.clicked.connect(self.fn_suma)
        self.btnResta.clicked.connect(self.fn_resta)
        self.btnMultiplicar.clicked.connect(self.fn_multiplicar)
        self.btnDividir.clicked.connect(self.fn_dividir)
        self.btnLimpiar.clicked.connect(self.fn_limpiar)
        self.btnSalir.clicked.connect(self.fn_salir)


    #Aqui las funciones
    def fn_suma(self):
    	numero1 = int(self.txtN1.text())
    	numero2 = int(self.txtN2.text())
    	s = numero1 + numero2
    	self.txtRes.setText(str(s))#mostrar text

    def fn_resta(self):
    	numero1 = int(self.txtN1.text())
    	numero2 = int(self.txtN2.text())
    	r = numero1 - numero2
    	self.txtRes.setText(str(r))

    def fn_multiplicar(self):
    	numero1 = int(self.txtN1.text())
    	numero2 = int(self.txtN2.text())
    	m = numero1 * numero2
    	self.txtRes.setText(str(m))

    def fn_dividir(self):
    	numero1 = int(self.txtN1.text())
    	numero2 = int(self.txtN2.text())
    	d = round(numero1 / numero2, 2)
    	self.txtRes.setText(str(d))


    def fn_limpiar(self):
    	self.txtN1.setText("")
    	self.txtN2.setText("")
    	self.txtRes.setText("")
    	self.txtN1.setFocus()


    def fn_salir(root):
    	root.destroy()
    	
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())