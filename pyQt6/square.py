from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit
import sys

def compute_square():
  try:
    num = int(num_input.text())
    comput_squar_label.setText(f"Square = {num * num}")
  except:
    comput_squar_label.setText("Please enter a valid integer.")

app = QApplication(sys.argv);
window = QWidget(); 
window.setWindowTitle("Sqare App");

num_input = QLineEdit();
num_input.setPlaceholderText("Input value");

square_button = QPushButton("Generate");
square_button.clicked.connect(compute_square);

comput_squar_label = QLabel(" ")

layout = QVBoxLayout();
layout.addWidget(num_input);
layout.addWidget(square_button);
layout.addWidget(comput_squar_label)

window.setLayout(layout);
window.show();
sys.exit(app.exec());
  