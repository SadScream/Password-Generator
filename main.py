import fix_qt_import_error

from random import choice
from PyQt5 import QtWidgets, QtGui
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

		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":/icons/assets/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.tray_icon = QtWidgets.QSystemTrayIcon(self)
		self.tray_icon.setIcon(QtGui.QIcon(icon))

		show_action = QtWidgets.QAction("Показать", self)
		hide_action = QtWidgets.QAction("Скрыть", self)
		quit_action = QtWidgets.QAction("Закрыть", self)

		show_action.triggered.connect(self.show)
		hide_action.triggered.connect(self.hide)
		quit_action.triggered.connect(self.closeEvent)

		tray_menu = QtWidgets.QMenu()
		tray_menu.addAction(show_action)
		tray_menu.addAction(hide_action)
		tray_menu.addAction(quit_action)

		self.tray_icon.setContextMenu(tray_menu)
		self.tray_icon.show()

	def closeEvent(self, e):
		try:
			self.tray_icon.hide()
			e.accept()
		except:
			e.accept()

	def showEvent(self, e):
		self.showNormal()

	def hideEvent(self, e):
		self.hide()

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