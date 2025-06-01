from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My first App')
window.resize(800, 500)

button = QPushButton("Button")

layout = QVBoxLayout()
layout.addWidget(button)
window.setLayout(layout)

window.show()

app.exec()
