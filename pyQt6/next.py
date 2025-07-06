from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flex Bar Example")

        layout = QHBoxLayout()

        # Button with no stretch (will maintain its preferred size)
        button1 = QPushButton("Button 1")
        layout.addWidget(button1)

        # Button with a stretch factor of 1 (will expand proportionally)
        button2 = QPushButton("Button 2")
        layout.addWidget(button2, 1)

        # Button with a stretch factor of 2 (will expand twice as much as Button 2)
        button3 = QPushButton("Button 3")
        layout.addWidget(button3, 2)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()