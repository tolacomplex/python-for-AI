import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextEdit

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Chatbot")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(self.output_display)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

    def chatbot_response(self, message):
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
        user_message = self.input_field.text()
        self.output_display.append(f"You: {user_message}")
        
        bot_response = self.chatbot_response(user_message)
        self.output_display.append(f"Bot: {bot_response}")
        
        self.input_field.clear() # Clear input field after sending

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec())