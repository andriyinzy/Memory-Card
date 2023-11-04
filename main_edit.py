from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QTableWidget, QListWidget, QListWidgetItem,
    QLineEdit, QFormLayout,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QButtonGroup, QRadioButton,
    QPushButton, QLabel, QSpinBox)
from main_app import app

txt_question = QLineEdit('')
txt_answer = QLineEdit('')
txt_wrong_answer1 = QLineEdit('')
txt_wrong_answer2 = QLineEdit('')
txt_wrong_answer3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Question:', txt_question)
layout_form.addRow('Answer:', txt_answer)
layout_form.addRow('Wrong answer №1:', txt_wrong_answer1)
layout_form.addRow('Wrong answer №2', txt_wrong_answer2)
layout_form.addRow('Wrong answer №3:', txt_wrong_answer3)
