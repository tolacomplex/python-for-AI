import sys
import sqlite3
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QPushButton, QLineEdit,
    QLabel, QHBoxLayout, QVBoxLayout, QTextEdit, QFileDialog, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class DatabaseManager:
    """ Manages all database operations for the chatbot """
    
    def __init__(self, db_path='chatbot.db'):
        """Initializes the database connection and sets up the table."""
        
        self.db_path = db_path
        self.database_data = {
            "hello": "Hello! 👋 How can I help you today?",
            "hi": "Hello! 👋 How can I help you today?",
            "what is norton university and when was it founded": (
                "Norton University (NU) is a private university in Phnom Penh, Cambodia. "
                "It was established in December 1996 and officially recognized in September 1997."
            ),
            "what is its vision and mission at norton school": (
                "Vision: To become an internationally respected higher education institution.\n"
                "Mission: To develop graduates who are entrepreneurial, professionally competitive, and creative."
            ),
            "who is founder of norton university": (
                "Norton University was founded on December 2, 1996, by Professor Chan Sok Khieng."
            ),
            "what faculties does norton university offer": (
                "Norton University offers various faculties, including:\n"
                "• Faculty of Engineering\n"
                "• Faculty of Information Technology\n"
                "• Faculty of Business and Economics\n"
                "• Faculty of Law and Social Sciences\n"
                "• Graduate School (Master’s programs)"
            ),
            "what programs does norton university provide": (
                "Norton offers Bachelor’s, Master’s, and short-term training programs in fields like "
                "Computer Science, Civil Engineering, Business Administration, and English."
            ),
            "what language is used for teaching": (
                "Courses are taught in both Khmer and English, depending on the program."
            ),
            "how long is a bachelor’s degree at norton university": (
                "Most Bachelor’s degrees at Norton University take 4 years to complete."
            ),
            "what facilities are available at norton university": (
                "The university provides computer and engineering labs, a library, Wi-Fi, a canteen, and a career center."
            ),
            "are there scholarships available at norton university": (
                "Yes, Norton University offers scholarships to outstanding students and those with financial need."
            ),
            "how much is the tuition fee at norton university": (
                "Tuition fees vary by faculty, typically ranging from $400 to $800 per year."
            ),
            "can i study in the evening or on weekends": (
                "Yes, Norton University offers flexible class schedules, including evening and weekend classes."
            ),
            "are there english programs or training at norton university": (
                "Yes, Norton provides English foundation and professional training courses."
            ),
            "can you tell me about norton university": (
                "Norton University (NU) is one of the first private universities in Cambodia, established on December\n 2, 1996 by Professor Chan Sok Khieng, who still serves as its rector."
                "NU offers:\n"
                "• Bachelor’s Degrees (typically 4 years)\n"
                "• Master’s Degrees\n"
                "• Short-term training programs\n"
            )
        }
        self.setup_database()

    def setup_database(self):
        """Creates the database and populates it with initial data."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS database_data (
                        question TEXT PRIMARY KEY,
                        answer TEXT
                    )
                """)
                
                cursor.execute("SELECT COUNT(*) FROM database_data")
                
                if cursor.fetchone()[0] == 0:
                    cursor.executemany("INSERT INTO database_data VALUES (?, ?)", self.database_data.items())
                    conn.commit()

        except sqlite3.Error as e:
            QMessageBox.critical(None, "Database Error", f"Failed to set up database: {str(e)}")


    def get_response(self, message: str) -> str:
        """ Response from the database for a given message."""
        message = message.lower().strip()
        response = "I'm sorry 🙏, I can only answer questions related to Norton University."

        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT answer FROM database_data WHERE question=?", (message,))
                result = cursor.fetchone()

                if result:
                    response = result[0]

        except sqlite3.Error as e:
            QMessageBox.critical(None, "Database Error", f"Failed to retrieve data: {str(e)}")

        return response


class ChatbotApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Norton Mini Chatbot")
        self.setGeometry(100, 100, 500, 700)
        self.setStyleSheet("background-color: black;")
        
        # Instantiate the new DatabaseManager class
        self.db_manager = DatabaseManager()

        page_widget = QWidget()
        page_widget.setStyleSheet("background-color: white")
        self.setCentralWidget(page_widget)
    
        layout = QVBoxLayout(page_widget)

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setFont(QFont("Arial", 12))
        self.output_display.setStyleSheet("""
            QTextEdit {
                border-radius: 4px;
                background-color: white;
                padding: 10px;
            }
        """)
        layout.addWidget(self.output_display)

        self.file_path_label = QLabel("No file selected")
        self.file_path_label.setStyleSheet("color: #888; margin-left: 5px;")
        layout.addWidget(self.file_path_label)

        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 10, 0, 0)

        self.upload_file_button = QPushButton("+")
        self.upload_file_button.setFixedSize(40, 40)
        self.upload_file_button.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.upload_file_button.setStyleSheet("""
            QPushButton {
                border-radius: 20px;
                background-color: #845ec2;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #6b4c9e;
            }
        """)
        self.upload_file_button.clicked.connect(self.open_file_dialog)
        h_layout.addWidget(self.upload_file_button)

        # Input text field
        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Ask a question about Norton University...")
        self.input_text.setStyleSheet("""
            QLineEdit {
                border-radius: 20px;
                padding: 10px;
                background-color: gray;
                border: 1px solid black;
            }
        """)
        self.input_text.setFixedHeight(40)
        self.input_text.textChanged.connect(self.update_send_button_state)
        self.input_text.returnPressed.connect(self.send_message)
        h_layout.addWidget(self.input_text)

        # Send button
        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(40, 40)
        self.send_button.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                border-radius: 20px;
                background-color: #845ec2;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #6b4c9e;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setEnabled(False) 
        h_layout.addWidget(self.send_button)

        layout.addLayout(h_layout)

    def update_send_button_state(self):
        """Enable/disable the send button based on text in the input field."""
        self.send_button.setEnabled(bool(self.input_text.text()))

    def open_file_dialog(self):
        """Open a file dialog and display the selected file path."""
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Select File",
                "",
                "All Files (*);;Text Files (*.txt);;Image Files (*.png *.jpg *.jpeg)"
            )
            if file_name:
                self.file_path_label.setText(f"Selected file: {file_name}")
        except Exception as e:
            QMessageBox.warning(self, "File Error", f"Could not open file: {str(e)}")
            self.file_path_label.setText("No file selected")

    def send_message(self):
        """
        Handle sending the user message and displaying the chatbot response.
        """
        user_message = self.input_text.text()
        if not user_message:
            return

        # Get response from the new DatabaseManager class
        bot_response = self.db_manager.get_response(user_message)

        # Display user message
        self.output_display.append(f"""
            <div style='text-align: left; margin: 5px; color: #845ec2; font-weight: bold;'>
                {user_message}
            </div>
        """)

        # Display bot message
        self.output_display.append(f"""
            <div style='text-align: left; margin: 5px; color: #333; background-color: #e3e8ed; padding: 10px; border-radius: 10px;'>
                {bot_response}
            </div>
        """)
        
        self.input_text.clear()
        self.file_path_label.setText("No file selected")


def main():
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
