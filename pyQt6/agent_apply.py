from PyQt6.QtWidgets import *
import sys
from PyQt6.QtCore import *
# Agent layered Architecture layer middle
class SimpleAgent:
    """A very basic rule-based AI agent"""
    def decide(self, environment):
        price = environment['price']
        if price < 30:
            return "buy"
        elif price > 70:
            return "sell"
        else:
            return "wait"

class AIagentSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Agent Simulator")
        self.setGeometry(0, 0, 800, 500)

        self.environment = {"price": 0}
        self.agent = SimpleAgent()

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.price_label = QLabel(f"Price: {self.environment['price']}")
        self.price_slider = QSlider(Qt.Orientation.Horizontal)
        self.price_slider.setRange(0, 100)
        self.price_slider.setValue(self.environment['price'])
        self.price_slider.valueChanged.connect(self.update_price)

        self.action_group = QGroupBox("Trigger Agent Action")
        self.buy_button = QPushButton("Buy")
        self.sell_button = QPushButton("Sell")
        self.wait_button = QPushButton("Wait")

        self.buy_button.clicked.connect(lambda: self.manual_action("Buy"))
        self.sell_button.clicked.connect(lambda: self.manual_action("Sell"))
        self.wait_button.clicked.connect(lambda: self.manual_action("Wait"))

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)

        self.auto_decide_button = QPushButton("Auto Decide")
        self.auto_decide_button.clicked.connect(self.agent_decision)

    def layout_widgets(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Environment Control"))
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_slider)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.buy_button)
        h_layout.addWidget(self.sell_button)
        h_layout.addWidget(self.wait_button)
        self.action_group.setLayout(h_layout)
        layout.addWidget(self.action_group);
        
        layout.addWidget(self.auto_decide_button)
        layout.addWidget(QLabel("Agent Output"))
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def update_price(self, value):
        self.environment['price'] = value
        self.price_label.setText(f"Price: {value}")

    def manual_action(self, action):
        self.result_box.append(f"Manual action triggered: {action}")

    def agent_decision(self):
        decision = self.agent.decide(self.environment)
        self.result_box.append(f"Agent decision based on price {self.environment['price']}: {decision}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulator = AIagentSimulator()
    simulator.show()
    sys.exit(app.exec())
