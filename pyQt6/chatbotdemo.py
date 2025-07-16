import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class ChatBotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI ChatBot")
        self.setGeometry(100, 100, 400, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", 12))
        self.chat_display.setStyleSheet("background-color: white;")

        # Initial messages
        bot_msg = "<span style='color:blue;'><b>Hi 👋 user. Do you have<br>anything ask me.</b></span>"
        user_msg = "<div align='right'><span style='color:white; background-color:black; padding:2px 6px; border-radius:5px;'><b>Hello</b></span></div>"
        self.chat_display.append(bot_msg)
        self.chat_display.append(user_msg)

        # Input and send button
        bottom_layout = QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Hello ChatBot.")
        self.text_input.setStyleSheet("padding: 8px; font-size: 14px;")
        self.text_input.textChanged.connect(self.toggle_send_button)

        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(40, 40)
        self.send_button.setStyleSheet("font-size: 18px;")
        self.send_button.setEnabled(False)
        self.send_button.clicked.connect(self.send_message)

        bottom_layout.addWidget(self.text_input)
        bottom_layout.addWidget(self.send_button)

        main_layout.addWidget(self.chat_display)
        main_layout.addLayout(bottom_layout)

    def toggle_send_button(self):
        self.send_button.setEnabled(bool(self.text_input.text().strip()))

    def send_message(self):
        user_text = self.text_input.text().strip()
        if user_text:
            user_html = f"<div align='right'><span style='color:white; background-color:black; padding:2px 6px; border-radius:5px;'><b>{user_text}</b></span></div>"
            self.chat_display.append(user_html)
            self.text_input.clear()
            self.send_button.setEnabled(False)

            # Simulated bot reply
            bot_reply = "<span style='color:blue;'><b>I'm here to help you.</b></span>"
            self.chat_display.append(bot_reply)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotUI()
    window.show()
    sys.exit(app.exec())
