import os 
import sys 
import json
from datetime import datetime
from typing import List, Dict,Optional, Any
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class TroubleShootingRule:
  """Represents a troubleshooting rule with symptoms and solutions"""
  def __init__(self, rule_id: str , title: str, description: str, symptoms: List[str], solution: str, category: str,priority: int = 1, confidence: float = 0.8 ):
    self.rule_id = rule_id
    self.title = title 
    self.description = description
    self.symptoms = symptoms
    self.solution = solution
    self.priority = priority
    self.category = category
    self.confidence = confidence
    self.created_date = datetime.now().isoformat()
    
  def to_dict(self) -> Dict[str, Any]:
    return {
      'rule_id': self.rule_id,
      'title': self.title,
      'descripton': self.description,
      'symptoms': self.symptoms,
      'solution': self.solution,
      'priority': self.priority,
      'category': self.category,
      'confidence': self.confidence,
      'created_date': self.created_date
    }
    
  @classmethod
  def from_dict(cls, data: Dict[str, Any]):
    rule = cls(
      data['rule_id'], data['title'], data['description'],
      data['symptoms'], data['solution'], data['priority'],
      data.get('category', 1), data.get('confidence', 0.8)
    )
    rule.created_date = data.get('created_date', datetime.now().isoformat())
    return rule
  
class TroubleShootingCase:
  """Represents a troubleshooting case/session """
  def __init__(self, case_id: str, symptoms: List[str], diagnosis: str, solution: List[str] = None):
    self.case_id = case_id
    self.symptoms = symptoms
    self.diagnosis = diagnosis
    self.created_date = datetime.now().isoformat()
  def to_dict(self) -> Dict[str, Any]:
    return {
      'case_id': self.case_id,
      'symptoms': self.symptoms,
      'diagnosis': self.diagnosis,
      'solution': self.solution,
      'created_date': self.created_date
    }
  @classmethod
  def from_dict(cls, data: Dict[str, Any]) -> 'TroubleShootingCase':
    case = cls(data['case_id'], data['symptoms'], data.get('diagnosis', ''), data.get('solution', []))
    case.created_date = data.get('created_date', datetime.now().isoformat())
    return case
  
class DataManager:
  """Handles all CRUD operations and JSON persistence"""
  def __init__(self, filename: str = "expert_system_data.json"):
    self.filename = filename
    self.rule: Dict[str, TroubleShootingRule] = {}
    self.cases: Dict[str, TroubleShootingCase] = {}
    self.symptoms_list = set()
    self.load_data()
    
  def load_data(self):
    if os.path.exists(self.filename):
      try:
        with open(self.filename, 'r', encoding = 'urf-8') as f:
          data = json.load()
        # Load rule
        for rule_data in data.get('rules', []):
          rule = TroubleShootingRule.form_dict(rule_data)
          self.rules[rule.rule_id] = rule
          self.symptoms_list.update(rule.symptoms)
        
        # Loao case
        for case_data in data.get("cases", []):
          case = TroubleShootingCase.from_dict(case_data)
          self.cases[case.case_id] = case
      except Exception as e:
        print(f"Error loading data: {e}")
        self.created_sample_data()
    else:
      self.create_sample_data
    
  def save_data(self):
    """Save data to JSON file"""
    data = {
        'rules': [rule.to_dict() for rule in self.rules.values()],
        'cases': [case.to_dict() for case in self.cases.values()],
        'symptoms': list(self.symptoms_list)
    }
    try:
      with open(self.filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
      print(f"Error saving data {e}")
  
  def create_sample_data(self):
    """Create sample data troubleshooting rules and data"""
    sample_rule = [
      TroubleShootingRule(
        "RULE001", "Computer Won't Start",
        "Computer doesn't power on at all",
        ["No power light", "No fan noise", "Screen blank"],
        "1. Check power cable connection\n2. Verify power outlet works\n3. Check power supply switch\n4. Test with different power cable",
        "Hardware", 1,0.9
      ),
      TroubleShootingRule(
        "RULE002", "Blue Screen of Death",
        "Computer crashes with blue screen error",
        ["Blue screen ", "Automatic restart", "Error codes" ],
        "1. Note error code\n2. Check recent software/hardware changes\n3. Run memery diagnostic\n4. Update driver\n5. Check for overheating",
        "Software", 2, 0.85
      ),
      TroubleShootingRule(
        "RULE003", "Slow Performance",
        "Computer run every slowly",
        ["Slow boot time", "Programs lag", "high CPU usage" ],
        "1. Run activirus scan\n2. Check startup program\n3. Clean temperary file\n4. Add more RAM if needed\n5. Defragment hard drive",
        "Performance", 1, 0.8
      ),
      TroubleShootingRule(
        "RULE004", "Internet connect Issue",
        "Can not connect to internet",
        ["No internet access", "Connect timeout", "DNS error" ],
        "1. Check cable connection\n2. Restart router/modem\n3. Run network troubleshooter\n4.  Update network drives\n5. reset network settings",
        "Network", 1, 0.85
      ),
      TroubleShootingRule(
        "RULE005", "Overheating Issue",
        "Computer gets too hot and shuts down",
        ["Computer hot to touch", "Automatic shuts down", "Fan noise loud" ],
        "1. Clean dust from vents and fans\n2. Check thermal paste\n3. Ensure proper ventilation\n4.  Ckeck fan functionality\n5. Reduce CPU load",
        "Hardware", 2, 0.9
      )
    ]  
    
    for rule in sample_rules:
      self.rules[rule.rule_id] = rule
      self.symptoms_list.update(rule.symptoms)
      
    self.save_data()
    
    # CRUD Operations for Rules
  def create_rule(self, rule: TroubleShootingRule) -> bool:
    if rule.rule_id not in self.rules:
      self.rules[rule.rule_id] = rule 
      self.symptoms_list.update(rule.symptoms)
      self.save_data()
    return False
  def read_rule(self, rule_id: str) -> Optional[TroubleShootingRule]:
    return self.rules.get(rule_id)
  
  def read_all_rules(self) -> List[TroubleShootingRule]:
    return list(self.rules.values())
  
  def update_rule(self, rule) -> List[TroubleShootingRule]:
    if rule.rule_id in self.rules:
      old_symptoms = self.rules[rule.rule_id].symptoms
      self.rules[rule.rule_id] = rule
      # Update symptoms list
      for symptom in old_symptoms:
        if not any(symptom in r.symptoms for r in self.rules.values() if r.rule_id != rule.rule_id):
          self.symptoms_list.discard(symptom)
      self.symptoms_list.update(rule.symptoms)
      self.save_data()
      return True
    return False
  
  def delete_rule(self, rule_id: str) -> bool:
    if rule_id in self.rules:
      old_symptoms = self.rules[rule_id].symptoms
      del self.rules[rule_id]
      # clean up symptoms that are not longger used
      for symptom in old_symptoms:
        if not any(symptom in rule.symptoms for rule in self.rules.values()):
          self.symptoms_list.discard(symptom)
      self.save_data()
      return True
    return False
  
  #CRUD Operations for cases
  def create_case(self, case: TroubleShootingCase) -> bool:
    if case.case_id not in self.cases:
      self.cases[case.case_id] = case
      self.save_data()
      return True
    return False 
  def diagnose(self, selected_symptoms: List[str]) -> List[tuple]:
    """Returns list of (rule, confidence_score) tuple"""  
    matches = []
    rules = self.data_manager.read_all_rules()
    
    for rule in rules:
      matches_symptoms = 0
      for symptom in rule.symptoms: 
        if any(s.lower() in symptom.lower() or symptom.lower() in s.lower() for s in selected_symptoms):
          matches_symptoms += 1
          
      if matches_symptoms > 0:
        # Calculate confidence based on symptoms match ratio
        match_ratio = matches_symptoms / len(rule.symptoms)
        confidence = rule.confidence * match_ratio
        matches.append((rule, confidence))
    
    # Sort by confidence and priority
    matches.sort(key=lambda x: (x[1].priority), reverse=True)
    return matches[:5]  # return top 5 matches
  
class RuleDialog(QDialog):
  """Dialog for creating/editing rules"""
  def __init__(self, parent=None, rule: TroubleShootingRule=None, symptoms_list: List[str] = None):
    super().__init__(parent)
    self.rule = rule
    self.symptoms_list = symptoms_list or []
    self.setWindowTitle("Add/Edit Rule")
    self.setModal(True)
    self.resize(500, 500)
    self.setup_ui()
    if rule:
      self.populate_fields()
    
  def setup_ui(self):
    layout = QVBoxLayout()
    
    # Form fields
    form_layout = QFormLayout()
    
    self.rule_id_edit = QLineEdit()
    self.title_edit = QLineEdit()
    self.description_edit = QTextEdit()
    self.description_edit.setMaximumHeight(80)
    
    self.category_combo = QComboBox()
    self.category_combo.addItems(["Hardware", "Software", "Performance", "Security"])
    
    self.priority_spin = QSpinBox()
    self.priority_spin.setRange(1, 5)
    self.priority_spin.setValue(1)
    
    self.confidence_spin = QSpinBox()
    self.confidence_spin.setRange(1, 100)
    self.confidence_spin.setValue(80)
    self.confidence_spin.setSuffix("%")
    
    form_layout.addRow("Rule ID: ", self.rule_id_edit)
    form_layout.addRow("Title: ", self.title_edit)
    form_layout.addRow("Descripton: ", self.description_edit)
    form_layout.addRow("Category: ", self.category_combo)
    form_layout.addRow("Priority: ", self.priority_spin)
    form_layout.addRow("Confidence: ", self.confidence_spin)
    
    layout.addLayout(form_layout)
    
    # Symptoms section
    symptoms_group = QGroupBox("Symptoms (check all that apply)")
    symptoms_layout = QVBoxLayout()
    
    # Add new symptoms
    add_symptom_layout = QHBoxLayout()
    self.new_symptom_edit = QLineEdit()
    self.new_symptom_edit.setPlaceholderText("Enter new symptom...")
    add_symptom_btn = QPushButton("Add Symptom")
    add_symptom_btn.clicked.connect(self.add_new_symptom)
    add_symptom_layout.addWidget(self.new_symptom_edit)
    add_symptom_layout.addWidget(add_symptom_btn)
    symptoms_layout.addLayout(add_symptom_layout)
    
    # symptoms checkboxes
    self.symptoms_area = QScrollArea()
    self.symptoms_widget = QWidget()
    self.symptoms_checkboxes_layout = QVBoxLayout(self.symptoms_widget)
    self.symptoms_area.setWidget(self.symptoms_widget)
    self.symptoms_area.setWidgetResizable(True)
    self.symptoms_area.setMaximumHeight(200)
    
    self.symptom_checkboxes = {}
    self.update_systems_checkboxes()
    
    symptoms_layout.addWidget(self.symptoms_area)
    symptoms_group.setLayout(symptoms_layout)
    layout.addWidget(symptoms_group)
    
    # Solution
    layout.addWidget(QLabel("Solution:"))
    self.solution_edit = QTextEdit()
    self.solution_edit.setMaximumHeight(100)
    
    # Button 
    button_layout = QHBoxLayout()
    save_btn = QPushButton("Save")
    cancel_btn = QPushButton("Cancel")
    save_btn.clicked.connect(self.accept)
    cancel_btn.clicked.connect(self.reject)
    button_layout.addWidget(save_btn)
    button_layout.addWidget(cancel_btn)
    layout.addLayout(button_layout)
    
    self.setLayout(layout)
    
  def add_new_symptom(self) :
    new_symptom = self.new_symptom_edit.text().strip()
    if new_symptom and new_symptom not in self.symptoms_list:
      self.symptoms_list.append(new_symptom)
      self.update_symptoms_checkboxes()
      self.new_symptom_edit.clear()
  
  def update_symptoms_checkboxes(self):
    # clear existing checkboxes
    for checkbox in self.symptom_checkboxes.values():
      checkbox.setParent(None)
    self.symptom_checkboxes.clear()
    
    # Create new checkBoxes
    for symptom in sorted(self.symptoms_list):
      checkbox = QCheckBox(symptom)
      self.symptom_checkboxes[symptom] = checkbox
      self.symptoms_checkboxes_layout.addWidget(checkbox)
      
  def poputate_fields(self):
    self.rule_id_edit.setText(self.rule.rule_id)
    self.rule_id_edit.setReadOnly(True)
    self.title_edit.setText(self.rule.title)
    self.description_edit.setPlainText(self.rule.description)
    self.category_combo.setCurrentText(self.rule.category)
    self.priority_spin.setValue(self.rule.priority)
    self.confidence_spin.setValue(self.rule.confidence * 100)
    self.solution_edit.setPlainText(self.rule.solution)
    
    # Check relevent symptoms
    for symptom in self.rule.symptoms:
      if symptom in self.symptom_checkboxes:
        self.symptom_checkboxes[symptom].setChecked(True)
  
  def get_rule_data(self) -> TroubleShootingRule:
    selected_symptoms = [symptom for symptom, checkbox in self.symptom_checkboxes.items()
                         if checkbox.isChecked()]
    return TroubleShootingRule(
      self.rule_id_edit.text(),
      self.title_edit.text(),
      self.description_edit.toPlainText(),
      selected_symptoms,
      self.solution_edit.toPlainText(),
      self.category_combo.currentText(),
      self.priority_spin.value(),
      self.confidence_spin.value() / 100.0
    )
    
class ExpertSystemApp(QMainWindow):
  """Main application window """
  def __init__(self):
    super().__init__()
    self.data_manager = DataManager()
    self.inference_engine = InferenceEngine(self.data_manager)
    self.setWindowTitle("Computer Troubleshootin Expert System")
    self.setGeometry(100, 100, 1000, 700)
    self.setup_ui()
    self.load_data()
  def setup_ui(self):
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    
    layout = QVBoxLayout()
    central_widget.setLayout(layout)
    
    # Title
    title = QLabel("Computer Troubleshooting Expert System")
    title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    font = QFont()
    font.setPointSize(16)
    font.setBold(True)
    title.setFont(font)
    layout.addWidget(title)
    
    # Tab widget
    self.tab_widget = QTabWidget()
    layout.addWidget(self.tab_widget)
    
    # Create tab
    self.create_dianosis_tab()
    self.create_rule_tab()
    self.create_cases_tab()
  
  def create_diagnosis_tab(self):
    """Create the main diagnosis interface"""
    tab = QWidget()
    layout = QVBoxLayout()
    
    # Instructions
    instructions = QLabel("Select symptoms yout're experiencing")
    instructions.setFont(QFont("Arial", 10 , QFont.Weight.Bold))
    layout.addWidget(instructions)
    
    # Symptoms selection
    self.symptoms_area = QScrollArea()
    self.symptoms_widget = QWidget()
    self.symptoms_layout = QVBoxLayout(self.symptoms_widget)
    self.symptoms_area.setWidget(self.symptoms_widget)
    self.symptoms_area.setWidgetResizable(True)
    self.symptoms_area.setMaximumHeight(200)
    layout.addWidget(self.symptoms_area)
    
    # diagnosis 
    
      
    
    
    
  