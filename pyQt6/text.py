from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
import sys
def greet():
    name = name_input.text()
    phone = phone_input.text()
    email = email_input.text()
    date = date_input.text()
    greet_first.setText(f"Your Personal Information")
    greet_label_name.setText(f"Hello User, {name}")
    greet_label_phone.setText(f"Your Phone Number: {phone}")
    greet_label_email.setText(f"Your Email: {email}")
    greet_label_date.setText(f"Your Birthday: {date}")
    

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Welcome to System sign in")
# label name input
name_input = QLineEdit()
name_input.setPlaceholderText("Enter Your Name")
# label phone number input
phone_input = QLineEdit()
phone_input.setPlaceholderText("Phone number")
# label email input 
email_input = QLineEdit()
email_input.setPlaceholderText("Email")
# label date of birth input
date_input = QLineEdit()
date_input.setPlaceholderText("Date of Birth")
# Button label click to connect reply
greet_button = QPushButton("Click")
greet_button_reset = QPushButton("Reset")
greet_button.clicked.connect(greet)

# Label response when user input information in label text input 
greet_first = QLabel(" ")
greet_label_name = QLabel(" ")
greet_label_phone = QLabel(" ")
greet_label_email = QLabel(" ")
greet_label_date = QLabel(" ")

# View widget show UI
layout = QVBoxLayout()
layout.addWidget(name_input)
layout.addWidget(phone_input)
layout.addWidget(email_input)
layout.addWidget(date_input)
layout.addWidget(greet_button)
layout.addWidget(greet_first)
layout.addWidget(greet_label_name)
layout.addWidget(greet_label_phone)
layout.addWidget(greet_label_email)
layout.addWidget(greet_label_date)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
