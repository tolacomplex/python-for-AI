from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QPushButton,
    QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit,
    QFileDialog, QLabel
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys


class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbot App Assistant")
        self.resize(800, 600)

        # ---------- Central widget & layouts ----------
        page_widget = QWidget()
        self.setCentralWidget(page_widget)
        v_layout = QVBoxLayout(page_widget)

        # ---------- Chat transcript ----------
        self.output_display = QTextEdit(readOnly=True)
        v_layout.addWidget(self.output_display)

        # ---------- Label for selected file ----------
        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setStyleSheet("color: gray;")
        v_layout.addWidget(self.file_path_label)

        # ---------- Bottom input row ----------
        self.upload_file_button = QPushButton("+")
        self.upload_file_button.setFixedSize(32, 32)
        self.upload_file_button.setFont(QFont("Arial", 18))
        self.upload_file_button.setStyleSheet(
            "QPushButton { border-radius: 16px; background: #1976d2; color: white; }"
            "QPushButton:hover { background: #0d47a1; }"
        )
        self.upload_file_button.clicked.connect(self.open_file_dialog)

        self.input_text = QLineEdit(placeholderText="Type something…")
        self.input_text.setMinimumHeight(36)
        self.input_text.setStyleSheet(
            "QLineEdit { border-radius: 18px; padding: 0 12px; background: white; color: black; }"
        )
        self.input_text.returnPressed.connect(self.send_message)  # hit Enter to send

        self.send_button = QPushButton("Send")
        self.send_button.setFixedHeight(32)
        self.send_button.setStyleSheet(
            "QPushButton { border-radius: 6px; background: #1976d2; color: white; }"
            "QPushButton:hover { background: #0d47a1; }"
        )
        self.send_button.clicked.connect(self.send_message)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.upload_file_button)
        h_layout.addWidget(self.input_text, stretch=1)
        h_layout.addWidget(self.send_button)
        v_layout.addLayout(h_layout)

    # ---------- Slots ----------
    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg)"
        )
        if file_name:
            self.file_path_label.setText(f"Selected file: {file_name}")

    def response_chatbot(self, message: str) -> str:
        message = message.lower()
        if "hello" in message or "hi" in message:
            return "Hello 👋 user. How can I help you?"
        elif "what is norton" in message:
            return "I'm a computer program, so I don't have feelings, but thanks for asking!"
        elif "weather" in message:
            return "I cannot provide real-time weather information."
        else:
            return "I'm not sure how to respond to that."

    def send_message(self):
        user_message = self.input_text.text().strip()
        if not user_message:                      # guard clause
            return

        self.output_display.append(f"<b>You:</b> {user_message}")
        bot_response = self.response_chatbot(user_message)
        self.output_display.append(f"<b>Bot:</b> {bot_response}\n")
        self.input_text.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec())
