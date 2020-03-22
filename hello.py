import sys

#import QApplications and the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

#create an istance of QApplication
app = QApplication(sys.argv)

#creae an instance of my app's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100,100,280,80)
window.move(60,15)
helloMsg = QLabel('<h1> Hello Vichon </h1>', parent=window)
helloMsg.move(60,15)

# show the GUI
window.show()

#Run my app's event loop (or main loop)
sys.exit(app.exec_())
