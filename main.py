import fix_qt_import_error

from random import choice
from PyQt5 import QtWidgets
from sys import exit, argv
from design import Ui_Dialog
from string import ascii_lowercase, ascii_uppercase, digits


class Window(QtWidgets.QMainWindow, Ui_Dialog):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.constructor()
		self.show()

	def constructor(self):
		self.generate.clicked.connect(self.generate_)
		self.copy.clicked.connect(self.copy_)
		self.generate.clicked.emit()

	def copy_(self):
		QtWidgets.QApplication.clipboard().setText(self.password.text())

	def generate_(self):
		text = self.gerenate_password()
		self.password.setText(text)

	def gerenate_password(self):
		password = ""
		spec = "{#%$}@*&<?>)(:'`"
		range_ = choice([10, 11, 12])

		for _ in range(range_):
			password += choice(ascii_lowercase + ascii_uppercase + digits + spec)

		return password


if __name__=="__main__":
	app = QtWidgets.QApplication(argv)
	window = Window()
	exit(app.exec_())