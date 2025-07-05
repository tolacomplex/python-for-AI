from PyQt6.QtWidgets import QApplication, QWidget
import sys 

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Welcome to game")
window.show()
app.exec()