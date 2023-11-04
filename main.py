from PyQt5.QtWidgets import QWidget
from random import shuffle
from main_app import app

from main_window import *
from main_data import *
from main_edit import *

from PyQt5.QtCore import QTimer

main_width, main_height = 1000, 450
card_width, card_height = 600,500
time_unit = 1000

window.resize(card_width, card_height)
window.move(300,300)
window.setWindowTitle('Memory card')
text_wrong = 'Wrong'
text_correct = 'Well done !'

frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'pear'
frm_wrong3 = 'grape'

radio_list = [rbtn_ans1, rbtn_ans2, rbtn_ans3, rbtn_ans4]
shuffle(radio_list)

answer = radio_list[0]
wrong_answer1 = radio_list[1]
wrong_answer2 = radio_list[2]
wrong_answer3 = radio_list[3]

question_listmodel = QuestionListModel()
frm_edit = QuestionEdit(0, txt_question, txt_answer, txt_wrong_answer1, txt_wrong_answer2, txt_wrong_answer3)
radio_list = [rbtn_ans1, rbtn_ans2, rbtn_ans3, rbtn_ans4]
frm_card = 0
timer = QTimer()
win_edit = QWidget()
win_main = QWidget()

def test_list():
    frm = Question('Яблуко', 'apple', 'apply', 'pinaple', 'pear')
    question_listmodel.from_list.append(frm)

window.show()
app.exec_()

