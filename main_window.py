from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QSpinBox, QRadioButton, QGroupBox, 
                             QButtonGroup, QHBoxLayout, QVBoxLayout)
from main_app import app

window = QWidget()

btn_menu = QPushButton("Menu")
btn_rest = QPushButton("Rest")
btn_next = QPushButton("Submit")
btn_edit = QPushButton("Edit")
sp_rest = QSpinBox()

#ANSWER BOX
radio_group_box = QGroupBox("Ansverrs")
radio_group = QButtonGroup()


rbtn_ans1 = QRadioButton("1")
rbtn_ans2 = QRadioButton("2")
rbtn_ans3 = QRadioButton("3")
rbtn_ans4 = QRadioButton("4")

radio_group.addButton(rbtn_ans1)
radio_group.addButton(rbtn_ans2)
radio_group.addButton(rbtn_ans3)
radio_group.addButton(rbtn_ans4)

#RESULT BOX
ans_group_box = QGroupBox('Result')
lb_result = QLabel('')
lb_correct = QLabel('')
layout_res =QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=(Qt.AlignHCenter | stretch = 2))
ans_group_box.setLayout(layout_res)
ans_group_box.hide()


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_ans1)
layout_ans2.addWidget(rbtn_ans2)
layout_ans3.addWidget(rbtn_ans3)
layout_ans3.addWidget(rbtn_ans4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
radio_group_box.setLayout(layout_ans1)

menu_line = QHBoxLayout()
main_line = QVBoxLayout()

time_lbl = QLabel("minuts")
question_lbl = QLabel("Question")

menu_line.addWidget(btn_menu)
menu_line.addWidget(btn_rest)
menu_line.addWidget(sp_rest)
menu_line.addWidget(time_lbl)

main_line.addLayout(menu_line)
main_line.addWidget(question_lbl)
main_line.addWidget(radio_group_box)
main_line.addWidget(btn_next)

#window.setLayout(main_line)

def show_result():
    radio_group_box.hide()
    ans_group_box.show()
    btn_next.setText('Next question')

def show_question():
    radio_group_box.hide()
    ans_group_box.show()
    btn_next.setText('Submit')
    radio_group_box.setExclusive(False)
    rbtn_ans1.setChecked(False)
    rbtn_ans2.setChecked(False)
    rbtn_ans3.setChecked(False)
    rbtn_ans4.setChecked(False)
    radio_group_box.setExclusive(True)