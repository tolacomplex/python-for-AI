from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QTextEdit, QFileDialog 
import sys 
from PyQt6.QtGui import QFont

class ChatbotApp(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Chatbot App Assistant")
    self.setGeometry(100, 100, 800, 700)
    
    page_widget = QWidget()
    self.setCentralWidget(page_widget)
    layout = QVBoxLayout(page_widget)
    
    self.output_display = QTextEdit()
    self.output_display.setReadOnly(True)
    layout.addWidget(self.output_display)
    
    # Button open file and folder
    self.upload_file_button = QPushButton("+")
    self.upload_file_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: blue; color: white;}")
    self.upload_file_button.setFixedSize(100, 40)
    self.upload_file_button.setFont(QFont("Arial", 40))
    self.upload_file_button.clicked.connect(self.open_file_dialog)
    
    self.input_text = QLineEdit()
    self.input_text.setFixedSize(300, 40)
    self.input_text.setStyleSheet("QLineEdit {border-radius: 10px; color: white;}")
    
    # Button send text to chatbot
    self.send_button = QPushButton("Send")
    self.send_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: blue; color: white;}")
    self.send_button.setFixedSize(100, 40)
    self.send_button.clicked.connect(self.send_message)
    
    layout.addWidget(self.upload_file_button)
    layout.addWidget(self.input_text)
    layout.addWidget(self.send_button)
    
    
  # Upload file in computer 
  def open_file_dialog(self):
    file_name, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg)')
    if file_name:
        self.file_path_label.setText(f'Selected file: {file_name}')
  
  # Response model chatBot
  def response_chatbot(self, message):
    message = message.lower()
    if "hello" in message:
        return "Hi there!"
    elif "how are you" in message:
        return "I'm a computer program, so I don't have feelings, but thanks for asking!"
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