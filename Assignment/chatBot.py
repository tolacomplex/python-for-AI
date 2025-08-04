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
    self.setWindowTitle("Norton Chatbot App Assistant")
    self.setGeometry(100, 100, 500, 700)
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
    self.upload_file_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: gray; color: white;}")
    self.upload_file_button.setFixedSize(32, 32)
    self.upload_file_button.setFont(QFont("Arial", 40))
    self.upload_file_button.clicked.connect(self.open_file_dialog)
    
    # Button Input text
    self.input_text = QLineEdit()
    self.input_text.setFixedSize(500, 40)
    self.input_text.setPlaceholderText("Text something relate NU…")
    self.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.input_text.setStyleSheet("QLineEdit {border-radius: 20px; color: black; background: white}")
    
    # Button send text to chatbot
    self.send_button = QPushButton("➤")
    self.send_button.setStyleSheet("QPushButton {border-radius: 10px; background-color: gray; color: white;}")
    self.send_button.setFixedSize(50, 40)
    self.send_button.setFont(QFont("Arial", 20))
    self.send_button.setFixedHeight(32)
    self.send_button.clicked.connect(self.send_message)
    
    h_layout = QHBoxLayout()
    h_layout.addWidget(self.upload_file_button)
    h_layout.addWidget(self.input_text)
    h_layout.addWidget(self.send_button)
    
    layout.addLayout(h_layout)
    
    
  # Upload file from computer 
  def open_file_dialog(self):
    """Open File path from computer device"""
    try:
      file_name, _ = QFileDialog.getOpenFileName(
              self,
              "Select File",
              "",
              "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg)"
          )
      if file_name:
          self.file_path_label.setText(f"Selected file: {file_name}")
          self.send_message()
    
    except FileNotFoundError as e:
      print(f"Error file unknown {str(e)}")
      
  # Response model chatBot
  def response_chatbot(self, message) -> str:
    
    try:
      message == message.lower()
      
      if "hello" in message or "hi" in message:
          return "hello 👋 user. How can I help you?"
      elif "what is norton university and when was it founded" in message:
          return '''
              Norton University (NU) is a private university located in Phnom Penh, Cambodia.\n
              It was established in December 1996 by Professor Chan Sok Khieng and officially recognized as a university in September 19.
          '''
      elif "what is its vision and mission at norton school" in message:
          return '''
              Answer:\n
              Vision: To become an internationally respected higher education institution, producing\n
              competitive professionals who contribute to Cambodia’s social and economic development and the international community ().\n
              Mission: Norton aims to develop graduates who are entrepreneurial, professionally competitive, creative thinkers, value higher\n
              learning, and promote peace, justice, and development ().
          '''
      
      elif "who is founder of norton university" in message:
        return '''Norton University is the first private university in Cambodia, established on December 2, 1996 by Professor Chan.'''
      
      elif "what faculties does Norton University offer" in message:
        return '''
        Norton University offers various faculties, including:\n
        • Faculty of Engineering\n
        • Faculty of Information Technology\n
        • Faculty of Business and Economics\n
        • Faculty of Law and Social Sciences
        • Graduate School (Master’s programs)\n
      '''
      
      elif "what programs does Norton University provide" in message:
        return '''
        Norton offers Bachelor’s, Master’s, and short-term training programs in areas such as Computer Science, Civil Engineering,\n Architecture, Business Administration, Finance, and English.
      '''
      
      elif "what language is used for teaching" in message:
        return '''
        Courses are taught in both Khmer and English, depending on the program and faculty.
      '''
      
      elif "how long is a Bachelor’s degree at Norton University" in message:
        return '''
        Most Bachelor’s degrees take 4 years to complete.
      '''
      
      elif "what facilities are available at Norton University" in message:
        return '''
        The university provides:\n
        • Computer labs\n
        • Engineering labs\n
        • Library\n
        • Wi-Fi access\n
        • Canteen\n
        • Sports area\n
        • Career center\n
      '''
      
      elif "are there scholarships available at Norton University" in message:
        return '''
        Yes, Norton University offers scholarships to outstanding students and those in financial need, depending on their academic\n
        performance and entrance exam results.
      '''
      
      elif "how much is the tuition fee at Norton University" in message:
        return '''
        Tuition fees vary by faculty. On average, it ranges from $400 to $800 per year depending on the major and study mode\n (morning/evening).
      '''
      
      elif "can I study in the evening or on weekends" in message:
        return '''
        Yes, Norton University offers flexible class schedules including evening and weekend classes, suitable for working students.
      '''
      
      elif "are there English programs or training at Norton University" in message:
        return '''
        Yes, Norton has English foundation programs and professional English training courses for students who want to improve their language skills.
      '''
      else:
          return '''Sorry 🙏 you can ask anything related Norton University.'''
        
    except Exception as e:
      print(f"Error occure {str(e)}")
    
  def send_message(self):
    user_message = self.input_text.text()
    if not user_message:
      return
    
    else: 
      self.send_button.setEnabled(True)
      
      bot_response = self.response_chatbot(user_message)
      self.output_display.append(f"<div align='left';><b>{user_message}</b></div>")
      self.output_display.append(f"<div align='left'; style='color: blue';><b>Bot: {bot_response}</b></div>")
      self.input_text.clear()
  
# Main function     
def main():
  app = QApplication(sys.argv)
  window = ChatbotApp()
  window.show()
  sys.exit(app.exec())

if __name__ == "__main__":
  main()