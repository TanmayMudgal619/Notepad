import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowIcon(QIcon('img/logo.ico'))
		self.Home()
		self.e=0
		titlebar=QToolBar()

		spacer = QLabel('<h3>Notepad</h3>',self)
		spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		self.minimize=QAction(QIcon('img/minimize.png'),'Minimize',self)
		self.minimize.triggered.connect(self.mini)
		self.maximize=QAction(QIcon('img/maximize.png'),'Maximize',self)
		self.maximize.triggered.connect(self.maxi)
		self.close=QAction(QIcon('img/close.png'),'Close',self)
		self.close.triggered.connect(self.Exit)

		titlebar.setIconSize(QSize(15,15))
		titlebar.addWidget(spacer)
		titlebar.addActions([self.minimize,self.maximize,self.close])
		titlebar.setMovable(False)

		toolbar=QToolBar()
		toolbar.setIconSize(QSize(25,25))
		
		self.toolbarbtn0=QAction(QIcon('img/open.png'),'Open',self)
		self.toolbarbtn0.triggered.connect(self.Open)
		self.toolbarbtn0.setToolTip('Open')
		
		self.toolbarbtn1=QAction(QIcon('img/add.png'),'Add',self)
		self.toolbarbtn1.triggered.connect(self.Add)
		self.toolbarbtn1.setToolTip('Add')

		self.toolbarbtn2=QAction(QIcon('img/save.png'),'Save',self)
		self.toolbarbtn2.triggered.connect(self.Save)
		self.toolbarbtn2.setDisabled(True)
		self.toolbarbtn2.setToolTip('Save')

		toolbar.addActions([self.toolbarbtn0,self.toolbarbtn1,self.toolbarbtn2])

		self.addToolBar(Qt.LeftToolBarArea,toolbar)
		self.addToolBar(titlebar)
		self.setGeometry(100,100,500,500)
		self.setWindowTitle('Notepad')
		toolbar.setStyleSheet('background-color:white;')
		toolbar.setMovable(False)

	def Add(self):
		self.toolbarbtn2.setDisabled(False)
		def deleteDocument():
			self.Home()
		add=QWidget()
		form=QFormLayout()
		try:
			if self.ofilename:
				self.filename=QLineEdit(self.ofilename.text())
				fl=open(self.ofilename.text()+'.txt','r')
				self.container=QPlainTextEdit(str(fl.read()))
			else:
				self.filename=QLineEdit()
				self.container=QPlainTextEdit()
		except:
			self.filename=QLineEdit()
			self.container=QPlainTextEdit()
		self.filename.setPlaceholderText('File Name')
		self.filename.setStyleSheet('''
			width: 100%;
			background-color:white;
			border: 1px solid #ccc;
			margin:0px;''')
		form.addRow(self.filename)
		form.addRow(self.container)
		add.setLayout(form)
		self.container.setStyleSheet('''QScrollBar {width:15px;background-color:white;},
			width: 100%;
			color: cornflowerblue;
			background-color:white;
			border: 0px solid transparent;
			margin:0px;''')
		add.setStyleSheet('background-color:white;')
		self.setCentralWidget(add)

	def Save(self):
		f=self.filename.text()
		data=self.container.toPlainText()
		if f=='':
			self.filename.setStyleSheet('''
			width: 100%;
			background-color:white;
			border: 1px solid #ff6666;
			margin:0px;''')
		else:
			if os.path.exists(f+'.txt'):
				file=open(f+'.txt','w')
				file.write(data)
			else:
				file=open(f+'.txt','x')
				file.write(data)

	def Open(self):
		self.toolbarbtn2.setDisabled(True)
		opn=QWidget()
		form=QFormLayout()
		self.ofilename=QLineEdit()
		self.ofilename.setPlaceholderText('Filename You Want to Open')
		obtn=QPushButton(QIcon('img/open.png'),'Open')
		obtn.clicked.connect(self.Add)
		form.addRow(self.ofilename)
		form.addRow(obtn)
		opn.setLayout(form)
		self.setCentralWidget(opn)

	def Home(self):
		home=QWidget()
		self.setCentralWidget(home)

	def Exit(self):
		self.destroy()
		sys.exit()

	def mini(self):
		self.showMinimized()

	def maxi(self):
		if (self.e)%2==0:
			self.showMaximized()
			self.e+=1
		else:
			self.showNormal()
			self.e+=1

app=QApplication(sys.argv)
app.setStyle('Fusion')
window=mainWindow()
window.setWindowFlags(Qt.FramelessWindowHint)
window.show()
sys.exit(app.exec_())
