from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, 
                             QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, QFileDialog
                             )
import sys 
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from datetime import time

class ChatbotApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Chatbot App Assistant")
    self.setGeometry(100, 100, 700, 700)
    page_widget = QWidget()
    self.setCentralWidget(page_widget)
    layout = QVBoxLayout(page_widget)
    
    self.output_display = QTextEdit()
    self.output_display.setReadOnly(True)
    layout.addWidget(self.output_display)
    
    self.file_path_label = QLabel("No file selected")
    self.file_path_label.setStyleSheet("color: gray;")
    layout.addWidget(self.file_path_label)
    
    # Button open file and folder
    self.upload_file_button = QPushButton("+")
    self.upload_file_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: blue; color: white;}")
    self.upload_file_button.setFixedSize(32, 32)
    self.upload_file_button.setFont(QFont("Arial", 40))
    self.upload_file_button.clicked.connect(self.open_file_dialog)
    
    # Button Input text
    self.input_text = QLineEdit()
    self.input_text.setFixedSize(500, 40)
    self.input_text.setPlaceholderText("Type something…")
    self.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.input_text.setStyleSheet("QLineEdit {border-radius: 20px; color: black; background: white}")
    
    # Button send text to chatbot
    self.send_button = QPushButton("Send")
    self.send_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: blue; color: white;}")
    self.send_button.setFixedSize(70, 30)
    self.send_button.setFixedHeight(32)
    self.send_button.clicked.connect(self.send_message)
    
    h_layout = QHBoxLayout()
    h_layout.addWidget(self.upload_file_button)
    h_layout.addWidget(self.input_text)
    h_layout.addWidget(self.send_button)
    
    layout.addLayout(h_layout)
    
    
  # Upload file from computer 
  def open_file_dialog(self):
    file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select File",
            "",
            "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg)"
        )
    if file_name:
        self.file_path_label.setText(f"Selected file: {file_name}")

        
  # Response model chatBot
  def response_chatbot(self, message) -> str:
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "hello 👋 user. How can I help you?"
    elif "what is norton university and when was it founded" in message:
        return "Norton University (NU) is a private university located in Phnom Penh, Cambodia.\n It was established in December 1996 by Professor Chan Sok Khieng and officially recognized as a university in September 19."
    elif "weather" in message:
        return "I cannot provide real-time weather information."
    else:
        return "I'm not sure how to respond to that."
  
  def send_message(self):
    user_message = self.input_text.text()
    self.output_display.append(f"You: {user_message}")
    
    bot_response = self.response_chatbot(user_message)
    self.output_display.append(f"Bot: {bot_response}")
    self.input_text.clear()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = ChatbotApp()
  window.show()
  sys.exit(app.exec())