from ihsa_oop import Problem
from PyQt4 import QtGui
import sys
import ihsagui


class IHSAApp(QtGui.QMainWindow, ihsagui.Ui_MainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		self.Oblicz.clicked.connect(self.oblicz())
		self.Zamknij.clicked.connect(self.zamknij())
	def oblicz(self):
		ranges = []
		ranges.append(float(self.dg1.value()))
		ranges.append(float(self.gg1.value()))
		ranges.append(float(self.dg2.value()))
		ranges.append(float(self.gg2.value()))
		if self.chooseCamelFunction.isChecked():
			function = '(4-2.1*x1^2+(x1^4)/3)*x1^2+x1*x2+(-4+4*x2^2)*x2^2'
		elif self.insertOwnFunction.isChecked():
			function = self.ownFunction.text()
		if function: 
			if 'x3' in function:
    				dimensions = 3
    				ranges.append(float(self.dg3.value()))
    				ranges.append(float(self.gg3.value()))
			else:
    				dimensions = 2
		prob = Problem(function, dimensions, ranges)
		prob.draw_contour(ranges)
		prob.solve()
	def zamknij(self):
		sys.exit()

def main():
	app = QtGui.QApplication(sys.argv)
	form = IHSAApp()
	form.show()
	app.exec_()
	

if __name__ == '__main__':
	main()
