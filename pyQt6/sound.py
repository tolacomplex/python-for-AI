from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
import pyttsx3
import os

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to Speech Converter")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.text_input = QTextEdit()
        self.layout.addWidget(self.text_input)

        self.convert_button = QPushButton("Convert to Speech")
        self.convert_button.clicked.connect(self.convert_text)
        self.layout.addWidget(self.convert_button)

        self.status_label = QLabel("")
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def convert_text(self):
        text = self.text_input.toPlainText()
        if text:
            try:
                tts = pyttsx3(text=text, lang='en')
                tts.save("output.mp3")
                self.status_label.setText("Text converted and saved as output.mp3")
                os.system("start output.mp3") # Plays the audio on Windows
            except Exception as e:
                self.status_label.setText(f"Error: {e}")
        else:
            self.status_label.setText("Please enter some text.")

if __name__ == "__main__":
    app = QApplication([])
    window = TextToSpeechApp()
    window.show()
    app.exec()